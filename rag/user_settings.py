"""user_settings.py — locally persisted provider settings for the standalone app.

Lets the packaged app's Settings page collect an API key/endpoint/deployments from
whoever is running it, without ever writing into the repo's tracked `.env`. Values are
stored in a JSON file under the user's home directory and merged into the process
environment (as defaults, never overriding an already-set env var) on import of
`rag.config`.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

SETTINGS_PATH = Path.home() / ".flowcal-hub" / "settings.json"

_ENV_KEYS = (
    "OPENAI_API_KEY",
    "AZURE_OPENAI_ENDPOINT",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_EMBEDDING_DEPLOYMENT",
    "AZURE_OPENAI_CHAT_DEPLOYMENT",
    "RAG_EMBEDDING_MODEL",
    "RAG_CHAT_MODEL",
)


def load_user_settings() -> dict:
    """Return the persisted settings dict, or {} if none have been saved yet."""
    if not SETTINGS_PATH.exists():
        return {}
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_user_settings(values: dict) -> None:
    """Persist provider settings (only the known keys) to SETTINGS_PATH."""
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    current = load_user_settings()
    current.update({k: v for k, v in values.items() if k in _ENV_KEYS})
    SETTINGS_PATH.write_text(json.dumps(current, indent=2), encoding="utf-8")


def apply_to_environment() -> None:
    """Set persisted settings as environment defaults (never overrides a real env var)."""
    for key, value in load_user_settings().items():
        if key in _ENV_KEYS and value:
            os.environ.setdefault(key, value)


def is_configured() -> bool:
    """True if either an OpenAI key or a full Azure OpenAI config is present."""
    has_openai = bool(os.getenv("OPENAI_API_KEY"))
    has_azure = bool(
        os.getenv("AZURE_OPENAI_ENDPOINT")
        and os.getenv("AZURE_OPENAI_API_KEY")
        and os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
        and os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    )
    return has_openai or has_azure
