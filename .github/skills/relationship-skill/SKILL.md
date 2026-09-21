---
name: relationship-skill
description: 'Use when detecting and recording relationships (related-to, prerequisite-of, part-of, extends) between Knowledge Objects, to build the internal knowledge graph used for cross-links and Visual Story slide ordering.'
---

# Relationship Skill

Builds the graph edges between Knowledge Objects, stored in each KO's `relationships[]`
array. This graph powers two things: "See also" cross-links on published pages, and the
narrative ordering of Visual Story slides.

## When to Use

- After a Knowledge Object reaches status `draft` and needs enrichment.
- Whenever a new KO is published and might relate to existing ones.

## Relationship Types

| Type | Meaning | Example |
|---|---|---|
| `related-to` | Same domain, no strict order | `ko-scada-polling` ↔ `ko-cfx-file-import` |
| `prerequisite-of` | Reader should understand A before B | `ko-field-meters` → `ko-scada-polling` |
| `part-of` | A is a sub-topic/component of B | `ko-meter-periodic-table` part-of `ko-data-ingestion` |
| `extends` | B adds detail/edge cases to A | `ko-validation-exceptions` extends `ko-validation-overview` |

## Procedure

1. Compare the KO's `tags[]`, `category`, and section headings against all other KOs in
   `knowledge/objects/`.
2. Look for shared named entities (e.g. "SCADA", "Meter Periodic Table", "Scheduler",
   "Crystal Reports") appearing in both KOs' sections — this is the primary signal for
   `related-to`.
3. Use `category` folder structure as a hint for `part-of` (e.g. a KO whose category is
   nested under an index page's category is `part-of` that broader KO, if one exists).
4. Infer `prerequisite-of` from the existing data-journey order already encoded in
   [`docs/visual/index.md`](../../../docs/visual/index.md): field meters → SCADA →
   import → validation → export/reporting. A KO earlier in that journey is a
   prerequisite of one later in it, when both cover journey steps.
5. Add relationships as directed edges — if useful for cross-linking in both directions,
   add the inverse edge on the target KO too (e.g. `prerequisite-of` on A, and a
   `related-to` back-reference on B), but do not auto-invert every type blindly.

## Output

Appended to the KO's `relationships[]`:

```json
{ "type": "prerequisite-of", "target": "ko-scada-polling" }
```

## Constraints

- Do NOT create relationships to KOs that don't exist yet — check `knowledge/objects/`
  first.
- Do NOT use relationships as a substitute for merging near-duplicate KOs — if two KOs
  cover the same topic at high similarity, that's a merge case for the
  [Knowledge Object Skill](../knowledge-object-skill/SKILL.md), not a `related-to` edge.
