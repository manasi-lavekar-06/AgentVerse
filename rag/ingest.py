"""ingest.py — turn a raw transcript file into embedded chunks in Chroma.

Reuses pipeline/extract.py and pipeline/clean.py as-is (imported, never modified)
so both the agent-based pipeline and this RAG pathway share one text-normalization
implementation.

CLI:
    python -m rag.ingest transcripts/pending/<file>
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pipeline.clean import clean
from pipeline.extract import extract

from rag import config
from rag.retrieval import chunk_text, upsert_chunks


def ingest_transcript(file_path: str | Path) -> tuple[str, list[str]]:
    """Extract, clean, chunk, and embed a transcript file.

    Returns:
        (clean_text, chunks) so callers (rag/pipeline.py) can reuse both without
        re-reading the file.
    """
    path = Path(file_path)
    raw_text = extract(path)
    clean_text = clean(raw_text)
    chunks = chunk_text(clean_text)

    ids = [f"{path.name}::{i}" for i in range(len(chunks))]
    metadatas = [{"source_file": path.name, "chunk_index": i} for i in range(len(chunks))]
    upsert_chunks(config.TRANSCRIPT_COLLECTION, ids, chunks, metadatas)

    return clean_text, chunks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a transcript into the RAG transcript_chunks collection.")
    parser.add_argument("file_path", help="Path to a transcript file under transcripts/pending/")
    args = parser.parse_args()

    _, chunks = ingest_transcript(args.file_path)
    print(f"Ingested {len(chunks)} chunks from {args.file_path} into '{config.TRANSCRIPT_COLLECTION}'.")
