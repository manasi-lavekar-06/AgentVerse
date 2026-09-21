---
name: knowledge-object-skill
description: 'Use when creating, updating, merging, or versioning a Knowledge Object JSON file under knowledge/objects/. Defines the canonical schema, ID rules, merge/dedup rules, and status lifecycle. Knowledge Objects are the single source of truth for all published content — docs/*.md is always generated FROM them, never the reverse.'
---

# Knowledge Object Skill

The core skill of the whole system. A **Knowledge Object (KO)** is the canonical,
structured record of one unit of FLOWCAL product knowledge. Everything downstream —
MkDocs pages, quiz decks, Visual Story slides — is *rendered from* Knowledge Objects by
the Publishing Agent. Nothing downstream is ever hand-edited as the primary source.

Full schema: [`knowledge/schema/knowledge-object.schema.json`](../../../knowledge/schema/knowledge-object.schema.json).

## Storage

- One file per KO: `knowledge/objects/<id>.json`
- `id` format: `ko-<slug>`, e.g. `ko-scada-polling`, `ko-meter-periodic-table`
- `slug` is kebab-case, derived from `title`, and **stable for the life of the KO** — never
  renamed even if the title changes later (relationships and `published_pages` reference
  the `id`).

## Status Lifecycle

```
draft  →  enriched  →  published
```

- `draft` — created by the Knowledge Extraction Agent, sections/summary present, no FAQs/relationships yet
- `enriched` — Knowledge Enrichment Agent has added `faqs[]` and `relationships[]`
- `published` — Publishing Agent has rendered it into `docs/` and recorded `published_pages[]`

## Merge Rules (when new transcript content touches an existing KO)

| Situation | Action |
|---|---|
| New content covers a topic already in a `sections[]` entry | Skip — no duplicate |
| New content adds detail to an existing section | Append to that section's `body` / `key_points[]` |
| New content introduces a new sub-topic for this KO's category | Append a new entry to `sections[]` |
| New content matches no existing KO or category | Create a new KO (new `id`, status `draft`) |

Similarity thresholds: treat topics at or above 0.75 similarity as duplicates (skip) and
at or above 0.45 similarity as detail-of-existing-section, when judging how similar new
content is to existing sections.

## Versioning Rules

- Every write to a KO: bump `version` by 1, set `updated_at` to today (ISO date).
- `sources[]` is **append-only** — always add a new `{transcript, extracted_at}` entry,
  never remove or overwrite prior sources. This is the audit trail of what fed the KO.
- `created_at` is set once and never changes.

## Constraints

- ONLY the Knowledge Extraction Agent creates new KOs (status `draft`).
- ONLY the Knowledge Enrichment Agent adds `faqs[]` / `relationships[]` and advances
  status to `enriched`.
- ONLY the Publishing Agent sets status to `published`, fills `published_pages[]`, and
  writes anything under `docs/`.
- If a rendered page in `docs/` and its backing KO(s) ever disagree, the KO is correct —
  regenerate the page, do not edit the KO to match stale Markdown.
