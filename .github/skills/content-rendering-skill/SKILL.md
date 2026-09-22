---
name: content-rendering-skill
description: 'Use when the Publishing Agent renders a Knowledge Object''s sections into a docs/*.md page. Defines the five content-adaptive markup patterns — text, image, flowchart, diagram, slideshow — and which one to pick per section based on render_hint.'
---

# Content Rendering Skill

Knowledge Object content on `docs/*.md` pages is never dumped as one long wall of
prose — each `sections[]` entry is rendered in whichever of five forms actually suits
its content, so a reader gets the shape of information that's easiest to grasp for that
specific fact, not a one-size-fits-all layout.

## Choosing a render type

Each `sections[]` entry carries an optional `render_hint` field (set by `rag/generate.py`
during drafting). Dispatch on it — default to `text` when absent or unrecognized:

| `render_hint`   | Markup to emit    | When |
|-----------------|-------------------|------|
| `text` / absent | `.txt-block` | General prose, definitions, anything without a clearer shape |
| `image`         | `.img-figure` | The content is inherently visual (screenshot, photo, UI layout, device) |
| `flowchart`     | `.flow-chart` | Ordered steps, a procedure, "first/then/finally" |
| `diagram`       | `.dg-diagram` | Relationships, comparisons, structural breakdowns between multiple things |
| `slideshow`     | `.sl-slideshow` | A handful of loosely-related highlights better consumed one at a time |

Each KO section renders as its own independent block — a page can mix a `.txt-block`,
a `.flow-chart`, and a `.dg-diagram` side by side, one per section, in section order.

## `.txt-block` — text sections (default)

```html
<div class="txt-block" markdown="1">

### {Section Heading}

<p>{body prose}</p>
<ul><li>{key_point 1}</li><li>{key_point 2}</li></ul>

</div>
```

No JavaScript is involved — this is plain styled HTML, always readable, always indexed.
The `markdown="1"` attribute is required — without it, `md_in_html` treats the div's
contents as raw HTML and the `### heading` line renders as literal text, not a heading.

## `.img-figure` — image sections

```html
<figure class="img-figure">
<img src="{image.src}" alt="{image.alt}">
<figcaption>{image.caption}</figcaption>
</figure>
```

If the section has no `image.src` yet (most transcripts don't produce real image
assets), render a `.img-placeholder` box instead so the page never shows a broken image:

```html
<div class="img-placeholder">
<span class="img-placeholder-icon">🖼️</span>
<div class="img-placeholder-caption">{image.caption or heading}</div>
</div>
```

## `.flow-chart` — flowchart sections

```html
<div class="flow-chart">
<div class="flow-root">{Section Heading}</div>
<ol class="flow-steps">
  <li class="flow-step">{key_point 1}</li>
  <li class="flow-step">{key_point 2}</li>
</ol>
</div>
```

One `<li class="flow-step">` per `key_points[]` entry, in order — order is meaningful
(it's a sequence), never reorder. `javascripts/flowchart.js` renders connected,
numbered, click-to-expand boxes; the raw `<ol>` is the no-JS fallback.

## `.dg-diagram` — diagram sections

```html
<div class="dg-diagram">
<div class="dg-root">{Section Heading}</div>
<ul class="dg-items">
  <li class="dg-item">{key_point 1}</li>
  <li class="dg-item">{key_point 2}</li>
</ul>
</div>
```

One `<li class="dg-item">` per `key_points[]` entry. `javascripts/diagram.js` renders a
top-down hub-and-spoke diagram (heading as the hub, items as connected spokes below) —
keep each item self-contained text since items aren't paired into explicit columns.

## `.sl-slideshow` — slideshow sections

```html
<div class="sl-slideshow">
<div class="sl-root">{Section Heading}</div>
<ul class="sl-slides">
  <li class="sl-slide">{key_point 1}</li>
  <li class="sl-slide">{key_point 2}</li>
</ul>
</div>
```

One `<li class="sl-slide">` per `key_points[]` entry. `javascripts/slideshow.js` renders
a small carousel (one point large at a time, prev/next + dots, light auto-advance).
Use sparingly — most content reads better as `text`, `flowchart`, or `diagram`.

## Page Structure

1. Frontmatter `tags:` (one tag per KO tag).
2. `# {Page Title}` — the H1, matching the page's primary KO title.
3. One short intro sentence (the KO's `summary`, trimmed).
4. One rendered block per `sections[]` entry, in order.
5. `## See Also` — cross-links from `relationships[]`.

## Constraints

- DO NOT render a section's raw `body` prose alongside its rendered block for
  non-`text` hints — for `flowchart`/`diagram`/`slideshow`/`image`, `key_points[]` (or
  the `image` object) are the rendered content; `body` stays in the KO as the
  audit-able source only. For `text` sections, `body` IS the rendered content.
- DO NOT remove or restructure the `## See Also` section or frontmatter tags.
- DO NOT touch `javascripts/flowchart.js`, `diagram.js`, `slideshow.js`, or their CSS
  rules in `docs/stylesheets/extra.css` — they already support any number of
  items/steps without changes.
- ONLY the Publishing Agent writes this markup into `docs/`, per the Knowledge Object
  Skill's single-writer rule.
- This is raw HTML embedded in Markdown (`md_in_html`, already enabled) — leave a blank
  line before and after each block, and around any Markdown (like `### heading`) nested
  inside a `<div>`.
