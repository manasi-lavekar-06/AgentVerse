"""Schema-conformance tests for generated Knowledge Objects and artifacts.

These validate shapes only (no network/API calls) using representative sample
documents, ensuring anything rag/pipeline.py writes stays compatible with the
schemas the Publishing Agent relies on.
"""

import json
from pathlib import Path

import jsonschema
import pytest

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_SCHEMA_DIR = _REPO_ROOT / "knowledge" / "schema"


def _schema(name: str) -> dict:
    return json.loads((_SCHEMA_DIR / name).read_text(encoding="utf-8"))


def test_sample_rag_ko_matches_knowledge_object_schema():
    ko = {
        "id": "ko-sample-topic",
        "slug": "sample-topic",
        "title": "Sample Topic",
        "category": "core-features/sample.md",
        "status": "draft",
        "summary": "A short summary.",
        "sections": [{"heading": "Overview", "body": "Body text.", "key_points": ["Point one."]}],
        "tags": [],
        "sources": [{"transcript": "sample.txt", "extracted_at": "2026-01-01"}],
        "version": 1,
        "created_at": "2026-01-01",
        "updated_at": "2026-01-01",
        "provenance": {"pathway": "rag", "generated_at": "2026-01-01T00:00:00+00:00"},
    }
    jsonschema.validate(ko, _schema("knowledge-object.schema.json"))


def test_sample_extraction_artifact_matches_rag_schema():
    artifact = {
        "run_id": "run-20260101-sample-rag",
        "agent": "rag-knowledge-extraction",
        "generated_at": "2026-01-01T00:00:00+00:00",
        "source_transcript": "sample.txt",
        "topics": [{"heading": "Overview", "match_type": "new-category", "matched_ko_id": None}],
        "knowledge_objects": ["ko-sample-topic"],
        "unmatched_topics": [],
    }
    jsonschema.validate(artifact, _schema("artifact-rag-extraction.schema.json"))


def test_extraction_artifact_rejects_wrong_agent_const():
    artifact = {
        "run_id": "run-20260101-sample-rag",
        "agent": "knowledge-extraction",  # wrong const for the RAG schema
        "generated_at": "2026-01-01T00:00:00+00:00",
        "source_transcript": "sample.txt",
        "knowledge_objects": [],
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(artifact, _schema("artifact-rag-extraction.schema.json"))


def test_sample_enrichment_artifact_matches_rag_schema():
    artifact = {
        "run_id": "run-20260101-sample-rag",
        "agent": "rag-knowledge-enrichment",
        "generated_at": "2026-01-01T00:00:00+00:00",
        "input_knowledge_objects": ["ko-sample-topic"],
        "enriched_knowledge_objects": ["ko-sample-topic"],
        "faqs_added": 1,
        "relationships_added": [{"source": "ko-sample-topic", "type": "related-to", "target": "ko-other"}],
    }
    jsonschema.validate(artifact, _schema("artifact-rag-enrichment.schema.json"))
