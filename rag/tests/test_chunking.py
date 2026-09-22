"""Unit tests for rag.retrieval.chunk_text — no network/API calls required."""

from rag.retrieval import chunk_text


def test_chunk_text_empty_returns_no_chunks():
    assert chunk_text("") == []


def test_chunk_text_short_text_single_chunk():
    text = "This is a short sentence about FLOWCAL meters."
    chunks = chunk_text(text, chunk_size=700, overlap=100)
    assert len(chunks) == 1
    assert chunks[0].strip() == text


def test_chunk_text_is_deterministic():
    text = "FLOWCAL meter setup. " * 500
    first = chunk_text(text, chunk_size=100, overlap=20)
    second = chunk_text(text, chunk_size=100, overlap=20)
    assert first == second
    assert len(first) > 1


def test_chunk_text_overlap_produces_more_chunks_than_no_overlap():
    text = "FLOWCAL meter setup. " * 500
    with_overlap = chunk_text(text, chunk_size=100, overlap=20)
    without_overlap = chunk_text(text, chunk_size=100, overlap=0)
    assert len(with_overlap) >= len(without_overlap)
