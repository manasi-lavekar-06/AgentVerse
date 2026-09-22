"""config.py — central settings for the RAG pathway.

All API keys and model names are read from environment variables (loaded from
a local .env file via python-dotenv). Never hardcode secrets here.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from rag.user_settings import apply_to_environment

# Load .env from the repo root regardless of current working directory.
_REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_REPO_ROOT / ".env")

# Settings saved via the standalone app's Settings page (~/.flowcal-hub/settings.json)
# fill in any env vars .env didn't already set — used when there is no repo checkout,
# e.g. running from a packaged exe.
apply_to_environment()

CHROMA_DIR = str(_REPO_ROOT / os.getenv("RAG_CHROMA_DIR", "rag/.chroma_store"))

KB_COLLECTION = "knowledge_objects"
TRANSCRIPT_COLLECTION = "transcript_chunks"

# Chunking defaults (tokens, per tiktoken cl100k_base).
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

# Similarity thresholds mirroring the Topic Extraction Skill's heuristic,
# now expressed as cosine similarity (1 - cosine distance) instead of lexical overlap.
DUPLICATE_SIMILARITY_THRESHOLD = 0.75
DETAIL_OF_EXISTING_THRESHOLD = 0.45


@dataclass(frozen=True)
class ModelSettings:
    use_azure: bool
    api_key: str
    azure_endpoint: str | None
    azure_api_version: str
    embedding_model: str
    chat_model: str


def load_model_settings() -> ModelSettings:
    """Read model/provider settings from the environment.

    Raises:
        RuntimeError: If no usable API key is configured.
    """
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") or None
    use_azure = bool(azure_endpoint)

    if use_azure:
        api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
        embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "")
        chat_model = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT", "")
    else:
        api_key = os.getenv("OPENAI_API_KEY", "")
        embedding_model = os.getenv("RAG_EMBEDDING_MODEL", "text-embedding-3-small")
        chat_model = os.getenv("RAG_CHAT_MODEL", "gpt-4o-mini")

    if not api_key:
        raise RuntimeError(
            "No API key configured. Copy .env.example to .env and set "
            "OPENAI_API_KEY (or AZURE_OPENAI_ENDPOINT/AZURE_OPENAI_API_KEY) — or, if "
            "you're running the standalone app, fill these in on its Settings page."
        )
    if use_azure and (not embedding_model or not chat_model):
        raise RuntimeError(
            "AZURE_OPENAI_ENDPOINT is set but AZURE_OPENAI_EMBEDDING_DEPLOYMENT and/or "
            "AZURE_OPENAI_CHAT_DEPLOYMENT are empty. Set them to the exact deployment "
            "names from your Azure AI Foundry/Azure OpenAI resource (Deployments tab) — "
            "not the underlying model names."
        )

    return ModelSettings(
        use_azure=use_azure,
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        azure_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
        embedding_model=embedding_model,
        chat_model=chat_model,
    )


def get_client():
    """Return an OpenAI-compatible client, routed to Azure OpenAI if configured."""
    settings = load_model_settings()
    if settings.use_azure:
        from openai import AzureOpenAI

        return AzureOpenAI(
            api_key=settings.api_key,
            azure_endpoint=settings.azure_endpoint,
            api_version=settings.azure_api_version,
        )
    from openai import OpenAI

    return OpenAI(api_key=settings.api_key)
