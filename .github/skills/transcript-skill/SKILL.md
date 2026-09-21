---
name: transcript-skill
description: 'Use when ingesting a raw course transcript file (PDF, DOCX, TXT, SRT, VTT) from transcripts/pending/ to produce clean, normalized text ready for topic extraction. Wraps the existing pipeline/extract.py and pipeline/clean.py logic — reuse it, do not reimplement it.'
---

# Transcript Skill

Turns a raw file in `transcripts/pending/` into a clean transcript record that the
Topic Extraction Skill can work with. This is the first step of the Knowledge Extraction
Agent's job.

## When to Use

- A new file appears in `transcripts/pending/`.
- Re-processing a transcript already in `transcripts/processed/` (e.g. to backfill a
  Knowledge Object).

## Procedure

1. **Identify the format** from the file extension: `.pdf`, `.docx`, `.txt`, `.srt`, `.vtt`.
2. **Extract raw text**, reusing the existing logic in [`pipeline/extract.py`](../../../pipeline/extract.py):
   - `.pdf` → page-by-page text extraction (PyMuPDF)
   - `.docx` → paragraph extraction (python-docx)
   - `.txt` → direct UTF-8 read
   - `.srt` / `.vtt` → strip timing/cue metadata, join caption text
   - If a terminal is available, prefer literally invoking the existing function
     (`python -c "from pipeline.extract import extract; ..."`) over re-deriving extraction
     logic by hand — it is already tested and handles edge cases per format.
3. **Clean and normalize**, reusing [`pipeline/clean.py`](../../../pipeline/clean.py):
   - Strip timestamps/sequence numbers, filler words, repeated lines
   - Normalize whitespace, smart quotes, em-dashes
4. **Record source metadata** — filename, format, character counts before/after cleaning.

## Output

Hand this record to the Topic Extraction Skill (in-memory or as part of the extraction
artifact's working notes — it is not itself persisted to `knowledge/`):

```json
{
  "source_file": "course_05_reporting.pdf",
  "format": "pdf",
  "extracted_at": "2026-09-17",
  "raw_char_count": 18320,
  "clean_char_count": 15890,
  "clean_text": "…"
}
```

## Constraints

- Do NOT move or delete the source file — the Orchestrator Agent moves it to
  `transcripts/processed/` only after the Publishing Agent succeeds.
- Do NOT write anything to `docs/` or `knowledge/objects/` from this skill — it only
  produces clean text.
