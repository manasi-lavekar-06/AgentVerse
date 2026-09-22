---
tags:
  - processing
  - integration
---

# Processing and Integration

Processing turns detailed records into usable business results. Use this section for
rollups, automated loaders, import configuration, and data-flow investigation.

<div class="pf-flow" markdown>
<div class="pf-node"><div class="pf-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C7.58 3 4 4.79 4 7s3.58 4 8 4 8-1.79 8-4-3.58-4-8-4M4 9v3c0 2.21 3.58 4 8 4s8-1.79 8-4V9c0 2.21-3.58 4-8 4s-8-1.79-8-4m0 5v3c0 2.21 3.58 4 8 4s8-1.79 8-4v-3c0 2.21-3.58 4-8 4s-8-1.79-8-4z"/></svg></div><div class="pf-title">Source data</div></div>
<div class="pf-arrow"><span class="pf-arrow-tip"></span></div>
<div class="pf-node"><div class="pf-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 16h6v-6h4l-7-7-7 7h4z M5 18h14v2H5z"/></svg></div><div class="pf-title">Import</div></div>
<div class="pf-arrow"><span class="pf-arrow-tip"></span></div>
<div class="pf-node"><div class="pf-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4m-1.4 15L6 11.4l1.4-1.4 3.2 3.2 6-6L18 8.6 10.6 16z"/></svg></div><div class="pf-title">Validation</div></div>
<div class="pf-arrow"><span class="pf-arrow-tip"></span></div>
<div class="pf-node"><div class="pf-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12,16L19.36,10.27L21,9L12,2L3,9L4.63,10.27M12,18.54L4.62,12.81L3,14.07L12,21.07L21,14.07L19.37,12.8L12,18.54Z"/></svg></div><div class="pf-title">Rollup</div></div>
<div class="pf-arrow"><span class="pf-arrow-tip"></span></div>
<div class="pf-node"><div class="pf-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6m2 16H8v-2h8v2m0-4H8v-2h8v2m-3-5V3.5L18.5 9H13z"/></svg></div><div class="pf-title">Reporting</div></div>
</div>

## Detailed Flow

```mermaid
flowchart LR
  Source[Source data] --> Import[Import]
  Import --> Validation[Validation]
  Validation --> Rollup[Rollup]
  Rollup --> Report[Reporting]
```

## Processing Tools

- [Calculated meter rollup process](../help/Content/FLOWCAL%2010/Calculated%20Meter%20Editor/Formulas/Calculated%20Meter%20Rollup%20Process.md)
- [Meter-location rollups](../help/Content/FLOWCAL%2010/Rollup%20Viewers/Meter-Location%20Rollups/Meter-Location%20Rollups.md)
- [FcLoader](../help/Content/FLOWCAL%2010/Admin%20Options/FcLoader.md)
- [Configure imports](../help/Content/FLOWCAL%2010/Admin%20Options/Configure%20Imports.md)
- [Import rules](../help/Content/FLOWCAL%2010/Settings%20Manager/Application/Import%20Rules%20Editor.md)

## Data Flow Reference

The [FLOWCAL Data Journey](../getting-started/flowcal-data-journey.md) explains the
business sequence. The [visual story](../visual/index.md) makes the core meter-to-report
path easier to inspect during onboarding.

> FcDataBoss is not represented by a dedicated page in the imported help corpus. Add its
> controlled operational runbook under this section when it becomes available.