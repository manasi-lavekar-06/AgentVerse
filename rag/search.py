"""search.py — retrieval-augmented Q&A over published Knowledge Objects.

Parallel to the Search Agent, but uses semantic (embedding) retrieval instead of
keyword matching over knowledge/objects/*.json. Read-only: never writes files.

CLI:
    python -m rag.search "How is access to FLOWCAL controlled?"
"""

from __future__ import annotations

import argparse
import json

from rag import config
from rag.retrieval import find_relevant_chunks

_SEARCH_SYSTEM_PROMPT = """You answer questions about the FLOWCAL product using ONLY \
the provided Knowledge Object excerpts. Do not use outside knowledge or speculate. If \
the excerpts don't cover the question, say so plainly. Respond with strict JSON only:
{ "answer": string, "sources": [string, ...] }  // sources = ko_id values used"""


def answer_question(query: str, top_k: int = 5) -> dict:
    """Retrieve relevant KO chunks and answer strictly from that context.

    Returns: {"answer": str, "sources": [ko_id, ...]}
    """
    matches = find_relevant_chunks(query, config.KB_COLLECTION, top_k=top_k)
    if not matches:
        return {"answer": "No matching Knowledge Objects found for this question.", "sources": []}

    context = [
        {
            "ko_id": m["metadata"].get("ko_id"),
            "heading": m["metadata"].get("heading"),
            "excerpt": m["document"],
            "similarity": round(m["similarity"], 3),
        }
        for m in matches
    ]

    client = config.get_client()
    settings = config.load_model_settings()
    response = client.chat.completions.create(
        model=settings.chat_model,
        response_format={"type": "json_object"},
        temperature=0.0,
        messages=[
            {"role": "system", "content": _SEARCH_SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps({"question": query, "context": context}, ensure_ascii=False)},
        ],
    )
    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask a question over the RAG-indexed Knowledge Objects.")
    parser.add_argument("query", help="The question to answer.")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    result = answer_question(args.query, top_k=args.top_k)
    print(result["answer"])
    if result.get("sources"):
        print("\nSources:", ", ".join(result["sources"]))
