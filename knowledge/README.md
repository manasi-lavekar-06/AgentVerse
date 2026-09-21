# Knowledge Store

This folder is the **source of truth** for the agent-based content pipeline described in
`.github/agents/` and `.github/skills/`. It sits alongside the existing `pipeline/*.py`
scripts and `docs/` site — it does not replace them.

```
knowledge/
├── schema/          JSON Schemas for Knowledge Objects and inter-agent artifacts
├── objects/         Knowledge Objects (*.json) — one file per unit of knowledge
└── artifacts/       Transient JSON artifacts exchanged between agents, one folder per run_id
```

## Why a JSON store exists alongside `docs/` and `pipeline/registry.json`

- `pipeline/registry.json` tracks *which transcripts contributed to which Markdown pages*.
  It stays as-is and is still updated by the legacy `pipeline/run_pipeline.py` path.
- `knowledge/objects/*.json` tracks *the knowledge itself* — structured, versioned, and
  independent of any single Markdown page. The Publishing Agent renders `docs/*.md`,
  `docs/practice/*.md`, and `docs/visual/index.md` **from** Knowledge Objects, never the
  other way around. If a Knowledge Object and a rendered page ever disagree, the
  Knowledge Object wins and the page must be regenerated.
- Only the **Publishing Agent** writes to `docs/`, `mkdocs.yml`, and `pipeline/registry.json`.
  All other agents read/write only inside `knowledge/`.

See [`.github/skills/knowledge-object-skill/SKILL.md`](../.github/skills/knowledge-object-skill/SKILL.md)
for the full schema, ID rules, and merge/versioning rules.
