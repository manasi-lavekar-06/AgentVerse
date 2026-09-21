"""
clean.py — Transcript normalizer.

Takes raw text and returns clean, readable prose:
- Removes timestamps and sequence numbers (SRT/VTT artifacts)
- Strips filler phrases ("um", "uh", "you know", "so basically")
- Normalizes whitespace and line breaks
- Fixes common encoding issues (smart quotes, em-dashes)
- Removes repeated consecutive sentences
"""

from __future__ import annotations

import re
import unicodedata


# Filler words/phrases to remove (case-insensitive, surrounded by word boundaries or commas)
_FILLERS = [
    r"\bum+\b",
    r"\buh+\b",
    r"\byou know\b",
    r"\bso basically\b",
    r"\bbasically\b",
    r"\bi mean\b",
    r"\bright\?\b",
    r"\bokay so\b",
    r"\balright\b",
    r"\bkind of\b",
    r"\bsort of\b",
    r"\blike I said\b",
    r"\bactually\b",
    r"\bjust\b",
]

# SRT/VTT timestamp patterns  e.g.  00:00:01,500 --> 00:00:04,000
_TIMESTAMP_RE = re.compile(
    r"\d{1,2}:\d{2}:\d{2}[,\.]\d{1,3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[,\.]\d{1,3}"
)

# SRT sequence numbers (a lone integer on its own line)
_SEQ_NUM_RE = re.compile(r"^\s*\d+\s*$", re.MULTILINE)

# VTT cue headers  e.g.  NOTE, WEBVTT, timestamps like 00:05.000
_VTT_HEADER_RE = re.compile(r"^(WEBVTT|NOTE|STYLE|REGION).*$", re.MULTILINE)
_VTT_CUE_RE = re.compile(r"^\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}.*$", re.MULTILINE)


def clean(raw_text: str) -> str:
    """Clean and normalize raw transcript text.

    Args:
        raw_text: Raw text extracted from a transcript file.

    Returns:
        Clean, normalized text string.
    """
    text = raw_text

    # Fix encoding artifacts
    text = _fix_encoding(text)

    # Remove SRT/VTT structural lines
    text = _TIMESTAMP_RE.sub("", text)
    text = _SEQ_NUM_RE.sub("", text)
    text = _VTT_HEADER_RE.sub("", text)
    text = _VTT_CUE_RE.sub("", text)

    # Strip filler phrases
    for filler in _FILLERS:
        text = re.sub(filler, "", text, flags=re.IGNORECASE)

    # Remove stray HTML tags (some VTT files use <i>, <b>, etc.)
    text = re.sub(r"<[^>]+>", "", text)

    # Normalize whitespace: collapse multiple spaces/tabs to single space
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Collapse more than 2 consecutive blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip leading/trailing whitespace on each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove consecutive duplicate lines
    deduped: list[str] = []
    prev = None
    for line in lines:
        if line != prev:
            deduped.append(line)
        prev = line

    text = "\n".join(deduped).strip()

    return text


def _fix_encoding(text: str) -> str:
    """Replace common encoding artifacts with clean ASCII/Unicode equivalents."""
    replacements = {
        "\u2018": "'",   # left single quotation mark
        "\u2019": "'",   # right single quotation mark
        "\u201c": '"',   # left double quotation mark
        "\u201d": '"',   # right double quotation mark
        "\u2013": "-",   # en-dash
        "\u2014": "--",  # em-dash
        "\u2026": "...", # ellipsis
        "\u00a0": " ",   # non-breaking space
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text
