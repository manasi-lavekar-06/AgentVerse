"""visualize.py — standalone (no-agent) port of the Visualization Agent.

For enriched Knowledge Objects with visual_story.eligible: true, generates a Visual
Story slide (LLM call for tightened title/body copy, deterministic markup render)
matching the pattern documented by the Visual Story Skill. Returns an artifact shaped
like artifact-visualization.schema.json; rag/publish.py is the only writer of
docs/visual/index.md.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

from rag import config

_REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = _REPO_ROOT / "knowledge" / "schema"
KO_DIR = _REPO_ROOT / "knowledge" / "objects"

_VISUALIZATION_SCHEMA = json.loads((SCHEMA_DIR / "artifact-visualization.schema.json").read_text(encoding="utf-8"))

_SLIDE_COPY_SYSTEM_PROMPT = """You write copy for one slide of an animated, time-boxed \
product data-journey story. Given a Knowledge Object's title and summary, tighten it \
into a short slide tag, a punchy title, and a 1-3 sentence body. Respond with strict \
JSON only:
{ "slide_tag": string, "title": string, "body": string }"""


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def _slide_copy(ko: dict, order: int) -> dict:
    client = config.get_client()
    settings = config.load_model_settings()
    payload = json.dumps({"title": ko["title"], "summary": ko.get("summary", ""), "order": order}, ensure_ascii=False)
    response = client.chat.completions.create(
        model=settings.chat_model,
        response_format={"type": "json_object"},
        temperature=0.3,
        messages=[
            {"role": "system", "content": _SLIDE_COPY_SYSTEM_PROMPT},
            {"role": "user", "content": payload},
        ],
    )
    return json.loads(response.choices[0].message.content)


def _slide_markup(ko: dict, order: int, copy: dict) -> tuple[str, str]:
    slug = _slugify(ko.get("visual_story", {}).get("slide_hint") or ko["title"])
    markup = (
        f'<div class="vs-slide vs-slide--{slug}">\n<div class="vs-bg"></div>\n'
        f'<div class="vs-content">\n<div class="vs-slide-tag">{copy.get("slide_tag", f"Step {order}")}</div>\n'
        f'<h2 class="vs-title">{copy.get("title", ko["title"])}</h2>\n'
        f'<p class="vs-body">{copy.get("body", ko.get("summary", ""))}</p>\n</div>\n</div>'
    )
    return slug, markup


def run_visualization(enrichment_artifact: dict, run_id: str) -> dict:
    eligible = []
    for ko_id in enrichment_artifact["enriched_knowledge_objects"]:
        ko = json.loads((KO_DIR / f"{ko_id}.json").read_text(encoding="utf-8"))
        if ko.get("visual_story", {}).get("eligible"):
            eligible.append(ko)
    eligible.sort(key=lambda k: k.get("visual_story", {}).get("journey_order", 0))

    slides = []
    for ko in eligible:
        order = ko.get("visual_story", {}).get("journey_order", 0)
        copy = _slide_copy(ko, order)
        slug, markup = _slide_markup(ko, order, copy)
        slides.append({"ko_id": ko["id"], "slug": slug, "order": order, "markup": markup})

    artifact = {
        "run_id": run_id,
        "agent": "visualization",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "knowledge_objects": [s["ko_id"] for s in slides],
        "target_file": "docs/visual/index.md",
        "slides": slides,
    }
    jsonschema.validate(artifact, _VISUALIZATION_SCHEMA)
    return artifact
