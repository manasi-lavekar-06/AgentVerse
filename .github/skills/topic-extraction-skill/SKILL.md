---
name: topic-extraction-skill
description: 'Use when splitting cleaned transcript text into topic blocks, generating section headings and key points, and matching each block against existing knowledge base categories and Knowledge Objects.'
---

# Topic Extraction Skill

Converts clean transcript text into a list of candidate topics, each classified against
the existing knowledge base so the Knowledge Extraction Agent knows whether to update an
existing Knowledge Object or draft a new one.

## When to Use

- After the Transcript Skill has produced clean text.
- Whenever re-scoring unmatched topics after new Knowledge Objects are published.

## Procedure

1. **Split into topic blocks** using paragraph breaks and transition phrases ("next",
   "another", "additionally", "let's talk about", "step N", …). Drop fragments under
   ~10 words.
2. **Derive a heading** from the leading sentence of each block; **extract key points**
   as bullets.
3. **Match against the knowledge base** — for each block, compare against:
   - Existing `knowledge/objects/*.json` (`title`, `tags`, `sections[].heading`)
   - `pipeline/registry.json` `categories` map (legacy pages not yet backed by a KO)
   - Score similarity conceptually the way TF-IDF / cosine-similarity would (shared
     terms and phrasing), and classify each block as one of:
     - `existing-ko` — high similarity to a Knowledge Object → update it
     - `new-ko-existing-category` — no KO match, but the category page exists → new KO in that category
     - `new-category` — no match anywhere → flag as unmatched, may need a new docs section
4. Keep topic labels short (≤ 60 chars) for use in artifact summaries and registry entries.

## Output

A `topics` list, in the shape used by `knowledge/schema/artifact-extraction.schema.json`:

```json
{
  "heading": "SCADA polling frequency",
  "match_type": "existing-ko",
  "matched_ko_id": "ko-scada-polling"
}
```

Plus an `unmatched_topics` list for anything that didn't match a category.

## Constraints

- Do NOT create or edit Knowledge Object files here — that is the
  [Knowledge Object Skill](../knowledge-object-skill/SKILL.md)'s job. This skill only
  classifies and hands off `topics[]`.
