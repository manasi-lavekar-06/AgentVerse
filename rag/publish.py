"""publish.py — standalone (no-agent) port of the Publishing Agent.

Renders enriched Knowledge Objects into docs/*.md, docs/practice/*-quiz.md, and
docs/visual/index.md, updates mkdocs.yml nav and pipeline/registry.json, and advances
KO status to "published" — the same contract publishing.agent.md follows by hand, so
`python -m rag.pipeline <file> --publish` can go transcript-to-live-site with no
VS Code/Copilot agent involved. Markup patterns must stay in sync with the Mind Map
Rendering Skill and Content Rendering Skill.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

from rag.categorize import flat_pages, require_categories

_REPO_ROOT = Path(__file__).resolve().parent.parent
KO_DIR = _REPO_ROOT / "knowledge" / "objects"
SCHEMA_DIR = _REPO_ROOT / "knowledge" / "schema"
ARTIFACTS_DIR = _REPO_ROOT / "knowledge" / "artifacts"
DOCS_DIR = _REPO_ROOT / "docs"
MKDOCS_YML = _REPO_ROOT / "mkdocs.yml"
REGISTRY_PATH = _REPO_ROOT / "pipeline" / "registry.json"
PENDING_DIR = _REPO_ROOT / "transcripts" / "pending"
PROCESSED_DIR = _REPO_ROOT / "transcripts" / "processed"

_PUBLISHING_SCHEMA = json.loads((SCHEMA_DIR / "artifact-publishing.schema.json").read_text(encoding="utf-8"))


def _load_ko(ko_id: str) -> dict:
    return json.loads((KO_DIR / f"{ko_id}.json").read_text(encoding="utf-8"))


def _write_ko(ko: dict) -> None:
    (KO_DIR / f"{ko['id']}.json").write_text(json.dumps(ko, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Section -> markup (Content Rendering Skill)
# ---------------------------------------------------------------------------

def _text_block(ko_id: str, sec_index: int, sec: dict) -> str:
    points = sec.get("key_points", [])
    body = f"<p>{_esc(sec.get('body', ''))}</p>"
    if points:
        items = "\n".join(f"<li>{_esc(kp)}</li>" for kp in points)
        body += f"\n<ul>\n{items}\n</ul>"
    return f'<!-- ko:{ko_id} block:{sec_index} -->\n<div class="txt-block" markdown="1">\n\n### {_esc(sec["heading"])}\n\n{body}\n\n</div>'


def _image_block(ko_id: str, sec_index: int, sec: dict) -> str:
    image = sec.get("image") or {}
    src = image.get("src", "")
    alt = _esc(image.get("alt", sec.get("heading", "")))
    caption = _esc(image.get("caption", sec.get("heading", "")))
    marker = f"<!-- ko:{ko_id} block:{sec_index} -->"
    if src:
        return f'{marker}\n<figure class="img-figure">\n<img src="{_esc(src)}" alt="{alt}">\n<figcaption>{caption}</figcaption>\n</figure>'
    return (
        f'{marker}\n<div class="img-placeholder">\n<span class="img-placeholder-icon">\U0001f5bc\ufe0f</span>\n'
        f'<div class="img-placeholder-caption">{caption}</div>\n</div>'
    )


def _flowchart_block(ko_id: str, sec_index: int, sec: dict) -> str:
    steps = "\n".join(f'<li class="flow-step">{_esc(kp)}</li>' for kp in sec.get("key_points", []))
    return (
        f'<!-- ko:{ko_id} block:{sec_index} -->\n<div class="flow-chart">\n'
        f'<div class="flow-root">{_esc(sec["heading"])}</div>\n<ol class="flow-steps">\n{steps}\n</ol>\n</div>'
    )


def _diagram_block(ko_id: str, sec_index: int, sec: dict) -> str:
    items = "\n".join(f'<li class="dg-item">{_esc(kp)}</li>' for kp in sec.get("key_points", []))
    return (
        f'<!-- ko:{ko_id} block:{sec_index} -->\n<div class="dg-diagram">\n'
        f'<div class="dg-root">{_esc(sec["heading"])}</div>\n<ul class="dg-items">\n{items}\n</ul>\n</div>'
    )


def _slideshow_block(ko_id: str, sec_index: int, sec: dict) -> str:
    slides = "\n".join(f'<li class="sl-slide">{_esc(kp)}</li>' for kp in sec.get("key_points", []))
    return (
        f'<!-- ko:{ko_id} block:{sec_index} -->\n<div class="sl-slideshow">\n'
        f'<div class="sl-root">{_esc(sec["heading"])}</div>\n<ul class="sl-slides">\n{slides}\n</ul>\n</div>'
    )


_RENDERERS = {
    "text": _text_block,
    "image": _image_block,
    "flowchart": _flowchart_block,
    "diagram": _diagram_block,
    "slideshow": _slideshow_block,
}


def _esc(text: str) -> str:
    return (text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(_REPO_ROOT))
    except ValueError:
        return str(path)


def render_ko_blocks(ko: dict) -> list[str]:
    """One markup block per section, rendered per its render_hint (default: text)."""
    blocks = []
    for i, sec in enumerate(ko.get("sections", [])):
        hint = sec.get("render_hint", "text")
        renderer = _RENDERERS.get(hint, _text_block)
        blocks.append(renderer(ko["id"], i, sec))
    return blocks


# ---------------------------------------------------------------------------
# Page merge
# ---------------------------------------------------------------------------

def _relative_link(from_category: str, to_category: str) -> str:
    from_dir = Path(from_category).parent
    to_path = Path(to_category)
    rel = os.path.relpath(to_path, from_dir)
    return rel.replace(os.sep, "/")


def merge_page(ko: dict, blocks: list[str]) -> str:
    """Return (created|updated) after merging this KO's blocks into its docs page."""
    page_path = DOCS_DIR / ko["category"]
    page_path.parent.mkdir(parents=True, exist_ok=True)

    see_also_links = []
    for rel in ko.get("relationships", []):
        target_path = KO_DIR / f"{rel['target']}.json"
        if target_path.exists():
            target = json.loads(target_path.read_text(encoding="utf-8"))
            see_also_links.append(f"- [{target['title']}]({_relative_link(ko['category'], target['category'])})")

    if not page_path.exists():
        intro = (ko.get("summary", "").split(". ") or [""])[0].strip()
        if intro and not intro.endswith("."):
            intro += "."
        tags = ko.get("tags") or [Path(ko["category"]).stem]
        frontmatter = "---\ntags:\n" + "".join(f"  - {t}\n" for t in tags) + "---\n"
        body = (
            f"{frontmatter}\n# {ko['title']}\n\n{intro}\n\n"
            + "\n\n".join(blocks)
            + "\n\n## See Also\n\n"
            + ("\n".join(see_also_links) if see_also_links else "- (none yet)")
            + "\n"
        )
        page_path.write_text(body, encoding="utf-8")
        return "created"

    text = page_path.read_text(encoding="utf-8")
    new_blocks = [b for b in blocks if b.splitlines()[0] not in text]
    if new_blocks:
        marker = "\n## See Also"
        insertion = "\n\n" + "\n\n".join(new_blocks) + "\n"
        if marker in text:
            text = text.replace(marker, insertion + marker, 1)
        else:
            text = text.rstrip() + insertion + "\n## See Also\n\n" + "\n".join(see_also_links) + "\n"
        page_path.write_text(text, encoding="utf-8")
    return "updated"


# ---------------------------------------------------------------------------
# Quiz deck merge
# ---------------------------------------------------------------------------

def merge_quiz(ko: dict) -> str | None:
    faqs = ko.get("faqs", [])
    if not faqs:
        return None
    top_level = Path(ko["category"]).parts[0]
    quiz_path = DOCS_DIR / "practice" / f"{top_level}-quiz.md"
    quiz_path.parent.mkdir(parents=True, exist_ok=True)

    def _qz_block(faq: dict) -> str:
        opts = "\n".join(f'<span class="qz-opt">{_esc(o)}</span>' for o in faq["options"])
        return (
            f'<!-- ko:{ko["id"]} q:{_esc(faq["question"])[:40]} -->\n'
            f'<div class="qz-q" data-correct="{faq["correct_index"]}" data-explanation="{_esc(faq["explanation"])}">\n'
            f'<p class="qz-question-text">{_esc(faq["question"])}</p>\n{opts}\n</div>'
        )

    blocks = [_qz_block(f) for f in faqs]

    if not quiz_path.exists():
        title = top_level.replace("-", " ").title()
        text = (
            f"---\ntags:\n  - quiz\n  - {top_level}\n---\n\n# {title} Quiz\n\n"
            f'<div class="quiz-deck" data-color="orange">\n\n' + "\n\n".join(blocks) + "\n\n</div>\n"
        )
        quiz_path.write_text(text, encoding="utf-8")
        return _safe_rel(quiz_path)

    text = quiz_path.read_text(encoding="utf-8")
    new_blocks = [b for b in blocks if b.splitlines()[0] not in text]
    if new_blocks:
        text = text.rstrip()
        if text.endswith("</div>"):
            text = text[: -len("</div>")].rstrip() + "\n\n" + "\n\n".join(new_blocks) + "\n\n</div>\n"
        quiz_path.write_text(text, encoding="utf-8")
    return _safe_rel(quiz_path)


# ---------------------------------------------------------------------------
# mkdocs.yml nav (minimal-diff text insertion — never reformats the whole file)
# ---------------------------------------------------------------------------

def append_nav_entry(tab_name: str, label: str, page_path: str) -> bool:
    text = MKDOCS_YML.read_text(encoding="utf-8")
    entry = f"      - {label}: {page_path}"
    if page_path in text:
        return False
    lines = text.splitlines()
    tab_line = f"  - {tab_name}:"
    for i, line in enumerate(lines):
        if line.strip() == tab_line.strip():
            j = i + 1
            while j < len(lines) and lines[j].startswith("      - "):
                j += 1
            lines.insert(j, entry)
            MKDOCS_YML.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True
    # Tab doesn't exist yet — append a new tab under the top-level `nav:` list.
    for i, line in enumerate(lines):
        if line.strip() == "nav:":
            j = i + 1
            while j < len(lines) and (lines[j].startswith("  -") or lines[j].startswith("      ")):
                j += 1
            lines[j:j] = [tab_line, entry]
            MKDOCS_YML.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True
    return False


# ---------------------------------------------------------------------------
# pipeline/registry.json
# ---------------------------------------------------------------------------

def update_registry(transcript_name: str, category_topics: dict[str, list[str]]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {"transcripts": {}, "categories": {}}
    entry = registry["transcripts"].setdefault(transcript_name, {"processed_at": None, "contributed_to": []})
    entry["processed_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for page in category_topics:
        if page not in entry["contributed_to"]:
            entry["contributed_to"].append(page)

    for page, topics in category_topics.items():
        cat = registry["categories"].setdefault(page, {"topics_covered": [], "sources": []})
        for t in topics:
            if t not in cat["topics_covered"]:
                cat["topics_covered"].append(t)
        if transcript_name not in cat["sources"]:
            cat["sources"].append(transcript_name)

    REGISTRY_PATH.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Visual Story insertion
# ---------------------------------------------------------------------------

def insert_visual_slides(slides: list[dict]) -> bool:
    if not slides:
        return False
    vs_path = DOCS_DIR / "visual" / "index.md"
    text = vs_path.read_text(encoding="utf-8")
    new_markup = "\n\n".join(s["markup"] for s in slides if f'vs-slide--{s["slug"]}' not in text)
    if not new_markup:
        return False
    marker = "<div class=\"vs-controls\""
    if marker in text:
        text = text.replace(marker, new_markup + "\n\n" + marker, 1)
    else:
        text = text.rstrip() + "\n\n" + new_markup + "\n"
    vs_path.write_text(text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def run_publishing(enrichment_artifact: dict, run_id: str, visualization_artifact: dict | None, transcript_name: str) -> dict:
    categories = require_categories()
    tab_by_path = {p["path"]: p["tab"] for p in flat_pages(categories)}

    pages_created, pages_updated, quiz_pages, nav_added = [], [], [], []
    category_topics: dict[str, list[str]] = {}

    for ko_id in enrichment_artifact["enriched_knowledge_objects"]:
        ko = _load_ko(ko_id)
        blocks = render_ko_blocks(ko)
        result = merge_page(ko, blocks)
        (pages_created if result == "created" else pages_updated).append(ko["category"])

        tab_name = tab_by_path.get(ko["category"], Path(ko["category"]).parts[0].replace("-", " ").title())
        if append_nav_entry(tab_name, ko["title"], ko["category"]):
            nav_added.append(ko["category"])

        quiz_page = merge_quiz(ko)
        if quiz_page:
            quiz_pages.append(quiz_page)

        category_topics.setdefault(ko["category"], []).extend(
            sec.get("heading", "") for sec in ko.get("sections", [])
        )

        ko["status"] = "published"
        ko.setdefault("published_pages", [])
        if ko["category"] not in ko["published_pages"]:
            ko["published_pages"].append(ko["category"])
        _write_ko(ko)

    update_registry(transcript_name, category_topics)

    visual_updated = False
    if visualization_artifact and visualization_artifact.get("slides"):
        visual_updated = insert_visual_slides(visualization_artifact["slides"])

    transcript_moved_to = None
    pending_path = PENDING_DIR / transcript_name
    if pending_path.exists():
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        dest = PROCESSED_DIR / transcript_name
        shutil.move(str(pending_path), str(dest))
        transcript_moved_to = str(dest.relative_to(_REPO_ROOT))

    artifact = {
        "run_id": run_id,
        "agent": "publishing",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pages_created": sorted(set(pages_created)),
        "pages_updated": sorted(set(pages_updated)),
        "quiz_pages_updated": sorted(set(quiz_pages)),
        "visual_story_updated": visual_updated,
        "nav_entries_added": sorted(set(nav_added)),
        "registry_updated": True,
        "transcript_moved_to": transcript_moved_to,
    }
    jsonschema.validate(artifact, _PUBLISHING_SCHEMA)

    run_dir = ARTIFACTS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "publishing.json").write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    return artifact
