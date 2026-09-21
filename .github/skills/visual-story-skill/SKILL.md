---
name: visual-story-skill
description: 'Use when transforming enriched Knowledge Objects into Visual Story slide markup for docs/visual/index.md, extending the existing animated vs-slide deck driven by javascripts/visual.js. Always append/update slides tied to specific Knowledge Objects — never replace or reorder the existing deck wholesale.'
---

# Visual Story Skill

Produces slide markup fragments for the existing animated "Visual Story" experience at
[`docs/visual/index.md`](../../../docs/visual/index.md), driven by
[`javascripts/visual.js`](../../../docs/javascripts/visual.js). This skill only proposes
markup — the Publishing Agent is the sole writer of `docs/visual/index.md`.

## When to Use

- An enriched Knowledge Object has `visual_story.eligible: true`.
- The existing slide deck needs a new step inserted for a newly-published KO that fits
  the product data journey (field meters → SCADA → import → validation → export/reporting).

## Existing Markup Pattern (must be reused, not reinvented)

Every slide follows this structure — study
[`docs/visual/index.md`](../../../docs/visual/index.md) before authoring a new one:

```html
<div class="vs-slide vs-slide--{slug}">
  <div class="vs-bg"></div>
  <!-- optional slide-specific visual, e.g. vs-scada-viz, vs-checks, vs-export-viz -->
  <div class="vs-content">
    <div class="vs-slide-tag">Step {n} · {ShortPhase}</div>
    <h2 class="vs-title">{Title}</h2>
    <p class="vs-body">{1-3 sentence narrative}</p>
  </div>
</div>
```

- `vs-slide--{slug}` must be a unique, kebab-case class per slide.
- The `<div class="vs-controls">…</div>` and `<div class="vs-progress-bar">…</div>` blocks
  at the end of `#vsMain` are shared chrome — never duplicate or remove them; new slides
  are inserted **before** that block.
- `javascripts/visual.js` auto-discovers `.vs-slide` elements and builds dots/progress
  from however many exist — no JS changes are needed to add a slide, only markup.

## Procedure

1. Select eligible KOs and order them via `visual_story.journey_order` (set by the
   Relationship Skill's journey inference).
2. For each KO, write one slide: `vs-slide-tag` = "Step {order} · {short phase}",
   `vs-title` = KO title (or a punchier variant), `vs-body` = a tightened version of the
   KO `summary` (2–3 sentences max — this is a glanceable animated slide, not a doc page).
3. Optionally include a simple inline visual (icon grid, arrow flow, checklist) following
   the visual vocabulary already used (`vs-meters-grid`, `vs-scada-viz`, `vs-checks`,
   `vs-export-viz`) — reuse these CSS classes/patterns from
   [`docs/stylesheets/extra.css`](../../../docs/stylesheets/extra.css) where a new slide's
   concept matches an existing pattern, rather than inventing new CSS.
4. Output the slide list per `knowledge/schema/artifact-visualization.schema.json`.

## Constraints

- Do NOT write to `docs/visual/index.md` directly — hand the slide markup to the
  Publishing Agent via the visualization artifact.
- Do NOT remove, reorder, or rewrite existing slides that aren't tied to the KOs being
  processed in this run — extend the deck, don't regenerate it.
- Keep `vs-body` short — this component is animated and time-boxed, unlike a full docs page.
