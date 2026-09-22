"""generate.py — LLM-backed drafting of Knowledge Object content.

Mirrors the outputs of the Knowledge Object Skill, FAQ Generation Skill, and
Relationship Skill, but driven by retrieval (rag/retrieval.py) instead of the
manual lexical-overlap heuristics those skills use. Every function returns
plain dicts/lists shaped exactly like the corresponding
knowledge/schema/knowledge-object.schema.json fields — callers (rag/pipeline.py)
are responsible for assembling/validating the full KO document.
"""

from __future__ import annotations

import json

from rag import config
from rag.retrieval import find_similar_kos

_KO_DRAFT_SYSTEM_PROMPT = """You are drafting a Knowledge Object for a product \
knowledge base from a transcript excerpt. You are given the excerpt, the product's \
allowed page categories (assign "category" to one of these paths whenever any \
reasonably fits), and, if any exist, the most similar existing Knowledge Objects for \
context. Decide whether this excerpt is a duplicate of an existing KO, a new detail to \
merge into one, or an entirely new topic, then produce the sections. For each section \
also classify render_hint based on its content's shape — pick whichever is genuinely \
most suitable, defaulting to "text" when nothing else clearly fits better:
- "flowchart": an ordered sequence of steps, a procedure, "first/then/finally"
- "diagram": a relationship, comparison, or structural breakdown between multiple things
- "image": the excerpt is describing something inherently visual (a screenshot, photo, \
UI layout, physical device) that would be clearer shown than described
- "slideshow": a handful of distinct, loosely-related highlights better consumed one at \
a time than all at once (e.g. feature highlights) — use sparingly
- "text": general prose explanation, definitions, or anything not clearly one of the above
Respond with strict JSON only, matching this shape:
{
  "match_type": "existing-ko" | "new-ko-existing-category" | "new-category",
  "matched_ko_id": string or null,
  "title": string,
  "category": string,  // one of the allowed category paths, e.g. "core-features/example.md"
  "summary": string,   // 1-3 sentences
  "sections": [ { "heading": string, "body": string, "key_points": [string, ...], \
"render_hint": "text" | "image" | "flowchart" | "diagram" | "slideshow" } ]
}
Only mark match_type "existing-ko" if a similar KO's similarity score is high and its \
topic is clearly the same, in which case matched_ko_id must be that KO's id. Only use \
match_type "new-category" if none of the allowed categories fit at all."""

_FAQ_SYSTEM_PROMPT = """You generate multiple-choice quiz questions from a Knowledge \
Object section's key points, for the FLOWCAL product. For each key point produce one \
question with 3-4 options (one correct), an explanation, matching this JSON shape:
{ "faqs": [ { "question": string, "options": [string, ...], "correct_index": integer, \
"explanation": string } ] }
Respond with strict JSON only."""

_RELATIONSHIP_SYSTEM_PROMPT = """You infer relationships between one Knowledge Object \
and a list of candidate related Knowledge Objects (id + summary + similarity score) for \
the FLOWCAL product knowledge base. Valid relationship types: related-to, \
prerequisite-of, part-of, extends. Only propose an edge when it is clearly justified by \
the summaries — do not invent connections. Respond with strict JSON only:
{ "relationships": [ { "type": string, "target": string } ] }"""


def _chat_json(system_prompt: str, user_content: str) -> dict:
    client = config.get_client()
    settings = config.load_model_settings()
    response = client.chat.completions.create(
        model=settings.chat_model,
        response_format={"type": "json_object"},
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    )
    return json.loads(response.choices[0].message.content)


def draft_or_merge_ko(topic_text: str, source_transcript: str, top_k: int = 5) -> dict:
    """Draft a new KO or classify an excerpt against existing KOs via semantic search."""
    from rag.categorize import flat_pages, require_categories

    similar = find_similar_kos(topic_text, top_k=top_k)
    allowed_categories = [
        {"path": p["path"], "label": p["label"], "description": p.get("description", "")}
        for p in flat_pages(require_categories())
    ]
    context = {
        "excerpt": topic_text,
        "allowed_categories": allowed_categories,
        "similar_existing_kos": [
            {
                "ko_id": m["ko_id"],
                "heading": m["heading"],
                "category": m["category"],
                "similarity": round(m["similarity"], 3),
                "excerpt": m["document"][:500],
            }
            for m in similar
        ],
    }
    draft = _chat_json(_KO_DRAFT_SYSTEM_PROMPT, json.dumps(context, ensure_ascii=False))
    draft["source_transcript"] = source_transcript
    draft["_similar_kos"] = similar
    return draft


def generate_faqs(heading: str, key_points: list[str]) -> list[dict]:
    """Generate quiz FAQs for a section's key points (same shape as faqs[] in the KO schema)."""
    if not key_points:
        return []
    payload = json.dumps({"heading": heading, "key_points": key_points}, ensure_ascii=False)
    result = _chat_json(_FAQ_SYSTEM_PROMPT, payload)
    return result.get("faqs", [])


def infer_relationships(ko_id: str, ko_summary: str, candidates: list[dict]) -> list[dict]:
    """Infer relationships[] edges for a KO from a list of candidate KOs.

    candidates: [{ko_id, summary, similarity}, ...] — typically the result of
    find_similar_kos() run against this KO's own summary/sections.
    """
    if not candidates:
        return []
    payload = json.dumps(
        {"ko_id": ko_id, "summary": ko_summary, "candidates": candidates}, ensure_ascii=False
    )
    result = _chat_json(_RELATIONSHIP_SYSTEM_PROMPT, payload)
    edges = result.get("relationships", [])
    return [edge for edge in edges if edge.get("target") != ko_id]
