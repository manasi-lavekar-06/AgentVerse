"""One-off ingestion: fold docs/flowcal10/* content into knowledge/objects/*.json
Knowledge Objects (the real source of truth), then regenerate docs/core-features
pages from those objects and remove the separate FLOWCAL 10 nav tab.

Run once: python pipeline/ingest_flowcal10_to_ko.py
"""
import json
import re
import html
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
FLOWCAL10 = ROOT / "docs" / "flowcal10"
OBJECTS = ROOT / "knowledge" / "objects"
CORE = ROOT / "docs" / "core-features"
TODAY = date.today().isoformat()
SOURCE_NAME = "FLOWCAL 10 Online Help"

# slugs already merged by hand earlier -> existing KO id + doc file
MERGED = {
    "meters": ("ko-meter-fundamentals", "meters.md"),
    "locations": ("ko-locations-and-systems", "locations.md"),
    "tickets": ("ko-tickets-overview", "tickets.md"),
    "rollup-viewers": ("ko-rollup-viewer-basics", "rollup-viewers.md"),
    "tools": ("ko-flowcal-toolbox-overview", "toolbox.md"),
    "volume-editor": (None, "volume-editor.md"),  # no KO existed yet
}

# avoid slug collisions with existing nav
RENAME = {"getting-started": "flowcal10-getting-started"}
META = {"_brd": "brd", "_glossary": "glossary", "_home-page-content": "home-page-content"}


def parse_flowcal10_md(path: Path):
    text = html.unescape(path.read_text(encoding="utf-8"))
    title_m = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else path.parent.name

    def section(name):
        m = re.search(rf"## {name}\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    overview_raw = section("Overview")
    overview_lines = [l.strip("- ").strip() for l in overview_raw.splitlines() if l.strip()]
    overview_lines = [l for l in overview_lines if not l.startswith("#")]
    overview_text = " ".join(overview_lines)

    key_raw = section("Key Characteristics")
    key_points = [l.strip("- ").strip() for l in key_raw.splitlines() if l.strip()]

    return title, overview_text, key_points


def make_new_ko(slug_final, title, overview_text, key_points, category):
    sections = [{"heading": "Overview", "body": overview_text, "key_points": []}]
    if key_points:
        sections.append({"heading": "Key Characteristics", "body": "", "key_points": key_points})
    return {
        "id": f"ko-{slug_final}",
        "slug": slug_final,
        "title": title,
        "category": category,
        "status": "published",
        "summary": (overview_text[:280] or title),
        "sections": sections,
        "tags": [slug_final.replace("-", " ")],
        "sources": [{"transcript": SOURCE_NAME, "extracted_at": TODAY}],
        "version": 1,
        "created_at": TODAY,
        "updated_at": TODAY,
        "published_pages": [category],
    }


def render_md(ko):
    lines = ["---", f"title: {ko['title']}", f"description: {ko['summary'][:150]}", "---", "", f"# {ko['title']}", ""]
    for s in ko["sections"]:
        lines.append(f"## {s['heading']}")
        lines.append("")
        if s.get("body"):
            lines.append(s["body"])
            lines.append("")
        for kp in s.get("key_points", []):
            lines.append(f"- {kp}")
        if s.get("key_points"):
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def load_ko(ko_id):
    return json.loads((OBJECTS / f"{ko_id}.json").read_text(encoding="utf-8"))


def save_ko(ko):
    (OBJECTS / f"{ko['id']}.json").write_text(json.dumps(ko, indent=2) + "\n", encoding="utf-8")


new_pages = []  # (nav_title, doc_relpath) for mkdocs.yml Core Features section

for folder in sorted(FLOWCAL10.iterdir()):
    if not folder.is_dir():
        continue
    slug = folder.name
    md_path = folder / "index.md"
    if not md_path.exists():
        continue
    title, overview_text, key_points = parse_flowcal10_md(md_path)

    if slug in MERGED:
        ko_id, doc_file = MERGED[slug]
        if ko_id is None:
            # volume-editor: no KO existed; build one from what's already merged in the .md
            existing_md = (CORE / doc_file).read_text(encoding="utf-8")
            impl = re.search(r"## FLOWCAL 10 Implementation Details\n(.*)", existing_md, re.DOTALL)
            body = impl.group(1).strip() if impl else overview_text
            ko = make_new_ko("volume-editor", "Volume Editor", body, key_points, "core-features/volume-editor.md")
            save_ko(ko)
        else:
            ko = load_ko(ko_id)
            if not any(s["heading"] == "FLOWCAL 10 Reference Detail" for s in ko["sections"]):
                ko["sections"].append({
                    "heading": "FLOWCAL 10 Reference Detail",
                    "body": overview_text,
                    "key_points": key_points,
                })
                ko["version"] += 1
                ko["updated_at"] = TODAY
                ko["sources"].append({"transcript": SOURCE_NAME, "extracted_at": TODAY})
                save_ko(ko)
        continue  # .md already correct, no regeneration needed

    slug_final = RENAME.get(slug, META.get(slug, slug))
    category = f"core-features/{slug_final}.md"
    ko = make_new_ko(slug_final, title, overview_text, key_points, category)
    save_ko(ko)
    (CORE / f"{slug_final}.md").write_text(render_md(ko), encoding="utf-8")
    new_pages.append((title, category))

# remove the old flowcal10 doc tree — content now lives in knowledge/objects + core-features
import shutil
shutil.rmtree(FLOWCAL10)

print(f"Created/updated KOs. New standalone pages: {len(new_pages)}")
for t, c in new_pages:
    print(f"  {t} -> {c}")
