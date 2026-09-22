"""pipeline.py — pipeline entry point: transcript -> draft/enriched Knowledge Objects.

Writes knowledge/objects/*.json (plus an optional, schema-legal `provenance` field),
and emits run artifacts validated against knowledge/schema/artifact-rag-*.schema.json.

Does NOT write to docs/, mkdocs.yml, or pipeline/registry.json — that remains the
exclusive responsibility of the Publishing Agent, invoked afterwards by
.github/agents/orchestrator.agent.md.

CLI:
    python -m rag.pipeline transcripts/pending/<file> [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

from rag import config
from rag.categorize import require_categories
from rag.generate import draft_or_merge_ko, generate_faqs, infer_relationships
from rag.ingest import ingest_transcript
from rag.retrieval import find_similar_kos

_REPO_ROOT = Path(__file__).resolve().parent.parent
KO_DIR = _REPO_ROOT / "knowledge" / "objects"
SCHEMA_DIR = _REPO_ROOT / "knowledge" / "schema"
ARTIFACTS_DIR = _REPO_ROOT / "knowledge" / "artifacts"

_KO_SCHEMA = json.loads((SCHEMA_DIR / "knowledge-object.schema.json").read_text(encoding="utf-8"))
_EXTRACTION_SCHEMA = json.loads((SCHEMA_DIR / "artifact-rag-extraction.schema.json").read_text(encoding="utf-8"))
_ENRICHMENT_SCHEMA = json.loads((SCHEMA_DIR / "artifact-rag-enrichment.schema.json").read_text(encoding="utf-8"))


def _slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_ko(ko_id: str) -> dict | None:
    path = KO_DIR / f"{ko_id}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def _write_ko(ko: dict, dry_run: bool) -> None:
    jsonschema.validate(ko, _KO_SCHEMA)
    if dry_run:
        print(f"[dry-run] would write knowledge/objects/{ko['id']}.json")
        return
    KO_DIR.mkdir(parents=True, exist_ok=True)
    (KO_DIR / f"{ko['id']}.json").write_text(json.dumps(ko, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _extract_topics(clean_text: str, source_transcript: str) -> tuple[list[dict], list[str], list[str]]:
    """Draft/merge/dedup topics against existing KOs. Returns (topics, ko_ids, unmatched)."""
    from rag.retrieval import chunk_text

    topics: list[dict] = []
    touched_ko_ids: list[str] = []
    unmatched: list[str] = []

    for chunk in chunk_text(clean_text):
        draft = draft_or_merge_ko(chunk, source_transcript)
        match_type = draft.get("match_type", "new-category")
        similar = draft.pop("_similar_kos", [])
        top_similarity = similar[0]["similarity"] if similar else 0.0

        if match_type == "existing-ko" and draft.get("matched_ko_id"):
            ko_id = draft["matched_ko_id"]
            existing = _load_ko(ko_id)
            if existing is None:
                unmatched.append(draft.get("title", chunk[:60]))
                continue
            already_sourced = any(s["transcript"] == source_transcript for s in existing.get("sources", []))
            if not already_sourced:
                existing.setdefault("sources", []).append(
                    {"transcript": source_transcript, "extracted_at": _today()}
                )
                existing["version"] = existing.get("version", 1) + 1
                existing["updated_at"] = _today()
            topics.append({"heading": draft.get("title", ""), "match_type": match_type, "matched_ko_id": ko_id, "similarity": top_similarity})
            touched_ko_ids.append(ko_id)
            _pending_writes[ko_id] = existing
            continue

        title = draft.get("title") or chunk[:60]
        ko_id = f"ko-{_slugify(title)}"
        existing = _pending_writes.get(ko_id) or _load_ko(ko_id)
        if existing:
            existing.setdefault("sections", []).extend(draft.get("sections", []))
            existing.setdefault("sources", []).append({"transcript": source_transcript, "extracted_at": _today()})
            existing["version"] = existing.get("version", 1) + 1
            existing["updated_at"] = _today()
            ko = existing
        else:
            ko = {
                "id": ko_id,
                "slug": _slugify(title),
                "title": title,
                "category": draft.get("category", "core-features/uncategorized.md"),
                "status": "draft",
                "summary": draft.get("summary", ""),
                "sections": draft.get("sections", []),
                "tags": [],
                "sources": [{"transcript": source_transcript, "extracted_at": _today()}],
                "version": 1,
                "created_at": _today(),
                "updated_at": _today(),
                "provenance": {"pathway": "rag", "generated_at": _now_iso()},
            }
        _pending_writes[ko_id] = ko
        topics.append({"heading": title, "match_type": match_type, "matched_ko_id": ko_id, "similarity": top_similarity})
        touched_ko_ids.append(ko_id)

    return topics, sorted(set(touched_ko_ids)), unmatched


# Accumulates in-progress KO writes across chunks within a single run, keyed by ko_id.
_pending_writes: dict[str, dict] = {}


def _enrich_ko(ko: dict) -> tuple[int, list[dict]]:
    """Add FAQs and relationships to a KO in place. Returns (faqs_added, relationship_edges)."""
    faqs_added = 0
    for section in ko.get("sections", []):
        new_faqs = generate_faqs(section.get("heading", ""), section.get("key_points", []))
        if new_faqs:
            ko.setdefault("faqs", []).extend(new_faqs)
            faqs_added += len(new_faqs)

    candidates = [
        {"ko_id": m["ko_id"], "summary": m["document"][:300], "similarity": round(m["similarity"], 3)}
        for m in find_similar_kos(ko.get("summary", ""), top_k=6)
        if m["ko_id"] != ko["id"]
    ]
    new_edges = infer_relationships(ko["id"], ko.get("summary", ""), candidates)
    existing_targets = {r["target"] for r in ko.get("relationships", [])}
    added_edges = []
    for edge in new_edges:
        if edge.get("target") and edge["target"] not in existing_targets:
            ko.setdefault("relationships", []).append(edge)
            added_edges.append({"source": ko["id"], **edge})
            existing_targets.add(edge["target"])

    if ko.get("status") == "draft":
        ko["status"] = "enriched"
    return faqs_added, added_edges


def run(transcript_path: str, dry_run: bool = False, publish: bool = False) -> dict:
    require_categories()  # hard gate: refuse to run until categorize.py has been done

    global _pending_writes
    _pending_writes = {}

    path = Path(transcript_path)
    run_id = f"run-{datetime.now().strftime('%Y%m%d')}-{_slugify(path.stem)}-rag"
    clean_text, _chunks = ingest_transcript(path)

    topics, touched_ko_ids, unmatched = _extract_topics(clean_text, path.name)

    extraction_artifact = {
        "run_id": run_id,
        "agent": "rag-knowledge-extraction",
        "generated_at": _now_iso(),
        "source_transcript": path.name,
        "topics": topics,
        "knowledge_objects": touched_ko_ids,
        "unmatched_topics": unmatched,
    }
    jsonschema.validate(extraction_artifact, _EXTRACTION_SCHEMA)

    total_faqs = 0
    all_edges: list[dict] = []
    for ko_id in touched_ko_ids:
        ko = _pending_writes[ko_id]
        faqs_added, edges = _enrich_ko(ko)
        total_faqs += faqs_added
        all_edges.extend(edges)

    enrichment_artifact = {
        "run_id": run_id,
        "agent": "rag-knowledge-enrichment",
        "generated_at": _now_iso(),
        "input_knowledge_objects": touched_ko_ids,
        "enriched_knowledge_objects": touched_ko_ids,
        "faqs_added": total_faqs,
        "relationships_added": all_edges,
    }
    jsonschema.validate(enrichment_artifact, _ENRICHMENT_SCHEMA)

    for ko_id in touched_ko_ids:
        _write_ko(_pending_writes[ko_id], dry_run)

    run_dir = ARTIFACTS_DIR / run_id
    if dry_run:
        print(f"[dry-run] would write artifacts to knowledge/artifacts/{run_id}/")
    else:
        run_dir.mkdir(parents=True, exist_ok=True)
        (run_dir / "extraction.json").write_text(json.dumps(extraction_artifact, indent=2), encoding="utf-8")
        (run_dir / "enrichment.json").write_text(json.dumps(enrichment_artifact, indent=2), encoding="utf-8")

    result = {"run_id": run_id, "extraction": extraction_artifact, "enrichment": enrichment_artifact}

    if publish and not dry_run:
        from rag.visualize import run_visualization
        from rag.publish import run_publishing

        visualization_artifact = run_visualization(enrichment_artifact, run_id)
        result["visualization"] = visualization_artifact
        result["publishing"] = run_publishing(enrichment_artifact, run_id, visualization_artifact, path.name)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the pipeline on a single transcript.")
    parser.add_argument("transcript_path")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing any files.")
    parser.add_argument("--publish", action="store_true", help="Also render docs/ and move the transcript to processed/ (no agent needed).")
    args = parser.parse_args()

    result = run(args.transcript_path, dry_run=args.dry_run, publish=args.publish)
    print(f"\nrun_id: {result['run_id']}")
    print(f"Knowledge Objects touched: {result['extraction']['knowledge_objects']}")
    print(f"FAQs added: {result['enrichment']['faqs_added']}")
    print(f"Relationships added: {len(result['enrichment']['relationships_added'])}")
    if "publishing" in result:
        pub = result["publishing"]
        print(f"Pages created: {pub['pages_created']}")
        print(f"Pages updated: {pub['pages_updated']}")
        print(f"Transcript moved to: {pub['transcript_moved_to']}")
    else:
        print("\nNext step: re-run with --publish to render docs/ directly, or hand off "
              "to the Publishing Agent / orchestrator agent.")
