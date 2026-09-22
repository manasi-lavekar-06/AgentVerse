"""kb_index.py — build/refresh the `knowledge_objects` Chroma collection from
knowledge/objects/*.json. Read-only with respect to knowledge/ — never writes KOs.

CLI:
    python -m rag.kb_index --rebuild
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from rag import config
from rag.retrieval import chunk_text, get_chroma_client, upsert_chunks

_REPO_ROOT = Path(__file__).resolve().parent.parent
KO_DIR = _REPO_ROOT / "knowledge" / "objects"


def _load_kos() -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(KO_DIR.glob("*.json"))]


def build_index(rebuild: bool = False) -> int:
    """(Re)build the knowledge_objects collection. Returns number of chunks indexed."""
    client = get_chroma_client()
    if rebuild:
        try:
            client.delete_collection(config.KB_COLLECTION)
        except Exception:
            pass  # collection may not exist yet

    ids, texts, metadatas = [], [], []
    for ko in _load_kos():
        ko_id = ko["id"]
        tags = ",".join(ko.get("tags", []))
        # Index the summary as its own chunk so top-level questions still match.
        for section_idx, section in enumerate([{"heading": "Summary", "body": ko.get("summary", "")}] + ko.get("sections", [])):
            heading = section.get("heading", "")
            body = section.get("body", "")
            key_points = "\n".join(section.get("key_points", []))
            section_text = f"{heading}\n{body}\n{key_points}".strip()
            if not section_text:
                continue
            for chunk_idx, chunk in enumerate(chunk_text(section_text)):
                ids.append(f"{ko_id}::{section_idx}::{chunk_idx}")
                texts.append(chunk)
                metadatas.append(
                    {
                        "ko_id": ko_id,
                        "heading": heading,
                        "category": ko.get("category", ""),
                        "tags": tags,
                        "status": ko.get("status", ""),
                    }
                )

    upsert_chunks(config.KB_COLLECTION, ids, texts, metadatas)
    return len(ids)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build/refresh the RAG knowledge_objects index.")
    parser.add_argument("--rebuild", action="store_true", help="Drop and recreate the collection first.")
    args = parser.parse_args()

    count = build_index(rebuild=args.rebuild)
    print(f"Indexed {count} chunks from {len(_load_kos())} Knowledge Objects into '{config.KB_COLLECTION}'.")
