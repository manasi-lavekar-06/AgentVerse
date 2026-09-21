---
name: faq-generation-skill
description: 'Use when generating FAQ / quiz-style question-answer pairs from enriched Knowledge Objects. Output must be compatible with the existing practice/ quiz deck HTML format (qz-q divs) consumed by javascripts/quiz.js and flashcards.js.'
---

# FAQ Generation Skill

Generates question/answer pairs from a Knowledge Object's sections and key points, stored
in `faqs[]` on the KO itself, and later rendered by the Publishing Agent into
`docs/practice/<category>-quiz.md` using the site's existing quiz markup.

## When to Use

- A Knowledge Object has reached status `draft` and needs enrichment before publishing.
- An existing `published` KO gains new sections and needs additional FAQ coverage.

## Procedure

1. For each `sections[].key_points[]` entry (or, absent key points, each section body),
   write one question that tests understanding of that specific fact — not trivia about
   wording.
2. Write exactly one correct answer plus 2–3 plausible, mutually-exclusive distractors.
   Distractors should be wrong in a way a real user might plausibly guess (e.g. a
   different but real FLOWCAL feature), not absurd options.
3. Write a 1–2 sentence explanation that restates the correct answer and cites the KO
   section it came from.
4. Append each item to the KO's `faqs[]` array in this shape (matches
   `knowledge/schema/knowledge-object.schema.json`):

```json
{
  "question": "What is the FLOWCAL Scheduler used for?",
  "options": [
    "Managing user login sessions",
    "Automatically generating and distributing reports on a timed basis",
    "Scheduling field meter maintenance",
    "Controlling SCADA polling intervals"
  ],
  "correct_index": 1,
  "explanation": "The Scheduler is FLOWCAL's built-in automation engine for report generation and distribution, configured once and run on a defined timetable."
}
```

## Rendering Contract (for the Publishing Agent)

Each `faqs[]` entry renders to the existing quiz deck markup, e.g.
[`docs/practice/reporting-quiz.md`](../../../docs/practice/reporting-quiz.md):

```html
<div class="qz-q" data-correct="{correct_index}" data-explanation="{explanation}">
  <p class="qz-question-text">{question}</p>
  <span class="qz-opt">{options[0]}</span>
  <span class="qz-opt">{options[1]}</span>
  ...
</div>
```

All such `.qz-q` divs for a category live inside a single `<div class="quiz-deck" data-color="...">`
wrapper per existing convention — the Publishing Agent appends new `.qz-q` blocks to the
matching category's quiz deck, it does not create a new deck per KO.

## Constraints

- Do NOT invent facts not present in the KO's `sections[]` — FAQs must be traceable to
  KO content.
- Do NOT write directly to `docs/practice/*.md` — this skill only populates `faqs[]` on
  the KO; the Publishing Agent renders the page.
