"""retrieval.py — shared Chroma + embedding + chunking helpers.

Used by both the ingestion side (rag/kb_index.py, rag/ingest.py) and the
generation/search side (rag/generate.py, rag/search.py) so there is exactly
one place that talks to Chroma and the embeddings API.
"""

from __future__ import annotations

import tiktoken
import chromadb

from rag import config

_encoding = tiktoken.get_encoding("cl100k_base")
_chroma_client: chromadb.ClientAPI | None = None


def get_chroma_client() -> chromadb.ClientAPI:
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.PersistentClient(path=config.CHROMA_DIR)
    return _chroma_client


def get_collection(name: str):
    return get_chroma_client().get_or_create_collection(name)


def chunk_text(
    text: str, chunk_size: int = config.CHUNK_SIZE, overlap: int = config.CHUNK_OVERLAP
) -> list[str]:
    """Split text into token-bounded chunks with overlap, preserving order."""
    tokens = _encoding.encode(text)
    if not tokens:
        return []

    chunks: list[str] = []
    start = 0
    step = max(chunk_size - overlap, 1)
    while start < len(tokens):
        window = tokens[start : start + chunk_size]
        chunks.append(_encoding.decode(window))
        if start + chunk_size >= len(tokens):
            break
        start += step
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a batch of texts via the configured provider (OpenAI or Azure OpenAI)."""
    if not texts:
        return []
    client = config.get_client()
    settings = config.load_model_settings()
    response = client.embeddings.create(model=settings.embedding_model, input=texts)
    return [item.embedding for item in response.data]


def upsert_chunks(
    collection_name: str,
    ids: list[str],
    texts: list[str],
    metadatas: list[dict],
) -> None:
    """Embed and upsert a batch of chunks into a Chroma collection."""
    if not texts:
        return
    embeddings = embed_texts(texts)
    collection = get_collection(collection_name)
    collection.upsert(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)


def _to_similarity(distance: float) -> float:
    """Chroma's default space is squared L2 on normalized embeddings; convert to a
    0-1 similarity score that mirrors the old lexical-overlap thresholds."""
    return max(0.0, 1.0 - distance / 2.0)


def find_similar_kos(query_text: str, top_k: int = 5) -> list[dict]:
    """Return the top-k most similar Knowledge Object chunks for a piece of text.

    Each result: {ko_id, heading, category, tags, similarity, document}
    """
    collection = get_collection(config.KB_COLLECTION)
    if collection.count() == 0:
        return []
    [embedding] = embed_texts([query_text])
    result = collection.query(query_embeddings=[embedding], n_results=top_k)

    matches: list[dict] = []
    ids = result.get("ids", [[]])[0]
    docs = result.get("documents", [[]])[0]
    metas = result.get("metadatas", [[]])[0]
    dists = result.get("distances", [[]])[0]
    for chunk_id, doc, meta, dist in zip(ids, docs, metas, dists):
        matches.append(
            {
                "chunk_id": chunk_id,
                "ko_id": meta.get("ko_id"),
                "heading": meta.get("heading"),
                "category": meta.get("category"),
                "tags": meta.get("tags"),
                "document": doc,
                "similarity": _to_similarity(dist),
            }
        )
    return matches


def find_relevant_chunks(query: str, collection_name: str, top_k: int = 5) -> list[dict]:
    """Generic top-k retrieval from any collection, used by rag/search.py."""
    collection = get_collection(collection_name)
    if collection.count() == 0:
        return []
    [embedding] = embed_texts([query])
    result = collection.query(query_embeddings=[embedding], n_results=top_k)

    matches: list[dict] = []
    ids = result.get("ids", [[]])[0]
    docs = result.get("documents", [[]])[0]
    metas = result.get("metadatas", [[]])[0]
    dists = result.get("distances", [[]])[0]
    for chunk_id, doc, meta, dist in zip(ids, docs, metas, dists):
        matches.append(
            {"chunk_id": chunk_id, "document": doc, "metadata": meta, "similarity": _to_similarity(dist)}
        )
    return matches
