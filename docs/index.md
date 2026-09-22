---
tags:
  - home
  - overview
---

<div class="hero" markdown>

<span class="hero-badge">AgentVerse Knowledge Hub</span>

# FLOWCAL Knowledge Hub

Training sessions, product help, and team knowledge in one focused workspace. Follow
the meter-to-report journey, learn each entity, and find answers when work is waiting.

<div class="hero-actions">
<a href="getting-started/flowcal-data-journey/">Start the data journey</a>
<a href="help/">Search product help</a>
</div>

</div>

<div class="hub-overview" markdown>

<a class="hub-primary-link" href="getting-started/flowcal-data-journey/">
  <span class="hub-link-eyebrow">New to FLOWCAL?</span>
  <strong>Follow the data journey</strong>
  <span>Start with security, then move from meter setup to tickets, close, rollups, and reporting.</span>
</a>

<a class="hub-primary-link" href="help/">
  <span class="hub-link-eyebrow">Need an answer now?</span>
  <strong>Search the product help library</strong>
  <span>Browse the imported FLOWCAL help documentation or use the search field above.</span>
</a>

</div>

## See It In Motion

<div class="vs-container vs-container--preview" id="vsHomePreview">

<div class="vs-slide vs-slide--intro">
  <div class="vs-bg"></div>
  <div class="vs-intro-particles">
    <span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span>
    <span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span><span class="vs-particle"></span>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 1 · Overview</div>
    <h2 class="vs-title">The FLOWCAL Data Journey</h2>
    <p class="vs-body">From securing access with users and groups, to creating a liquid meter and its location, through validation, exceptions, PPA approval, imports, and rollups into reports — this is the path data takes through FLOWCAL.</p>
  </div>
</div>

<div class="vs-slide vs-slide--hierarchy">
  <div class="vs-bg"></div>
  <div class="vs-hierarchy-tree">
    <div class="vs-hier-row"><div class="vs-hier-node vs-hier-node--facility">Enterprise (System)</div></div>
    <div class="vs-hier-arrow">↓</div>
    <div class="vs-hier-row"><div class="vs-hier-node vs-hier-node--station">Location</div></div>
    <div class="vs-hier-arrow">↓</div>
    <div class="vs-hier-row vs-hier-siblings">
      <div class="vs-hier-node vs-hier-node--meter">Meter A</div>
      <div class="vs-hier-node vs-hier-node--meter">Meter B</div>
    </div>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 2 · Locations</div>
    <h2 class="vs-title">Locations &amp; Systems</h2>
    <p class="vs-body">A single location can host multiple meters underneath a system — this is the structure every workflow in FLOWCAL builds on.</p>
  </div>
</div>

<div class="vs-slide vs-slide--teal-dark">
  <div class="vs-bg"></div>
  <div class="vs-timeline">
    <div class="vs-timeline-track">
      <div class="vs-timeline-fill"></div>
      <div class="vs-timeline-marker"></div>
      <div class="vs-timeline-marker"></div>
      <div class="vs-timeline-marker"></div>
    </div>
    <span class="vs-timeline-label">Minute</span>
    <span class="vs-timeline-label">Super</span>
    <span class="vs-timeline-label">Monthly</span>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 3 · Rollups</div>
    <h2 class="vs-title">From Detail to Report</h2>
    <p class="vs-body">Data aggregates from minute-level detail up through super and monthly totals, ready for reporting.</p>
  </div>
</div>

<!-- CONTROLS -->
<div class="vs-controls">
  <button class="vs-btn vs-prev-btn" aria-label="Previous slide">‹</button>
  <div class="vs-dots"></div>
  <button class="vs-btn vs-next-btn" aria-label="Next slide">›</button>
  <button class="vs-btn vs-play-btn" aria-label="Pause/Play">⏸</button>
</div>
<div class="vs-progress-bar"><div class="vs-progress-fill"></div></div>

</div>

<p class="vs-preview-cta"><a href="visual/">Watch the full animated data journey →</a></p>

## Learn by Goal

<div class="grid cards hub-cards" markdown>

-   :material-rocket-launch-outline: **Start here**

    ---

    Learn the product language, navigation, and end-to-end data journey.

    [Open the learning path](getting-started/flowcal-data-journey.md)

-   :material-database-cog-outline: **Set up and administer**

    ---

    Find users, systems, configuration, application installation, and database guidance.

    [Explore administration](help/Content/FLOWCAL%2010/Admin%20Options/Install%20%26%20Configure%20Services.md)

-   :material-gas-station-outline: **Work with product entities**

    ---

    Understand meters, locations, products, sources, assignments, and their relationships.

    [Explore meters](core-features/meters.md)

-   :material-clipboard-check-outline: **Run daily operations**

    ---

    Handle imports, tickets, validation, close workflows, and PPA approvals.

    [Explore tickets](core-features/tickets.md)

-   :material-chart-timeline-variant-shimmer: **Understand the flow visually**

    ---

    Step through FLOWCAL's entity hierarchy and data journey with interactive visuals.

    [Open visual story](visual/index.md)

-   :material-book-search-outline: **Use detailed product help**

    ---

    Search the full internal help library for specific screens, settings, and procedures.

    [Open Help Library](help/index.md)

</div>

## The FLOWCAL Operating Model

```mermaid
flowchart LR
  A[Security setup] --> B[Systems and locations]
  B --> C[Meters and sources]
  C --> D[Incoming data and tickets]
  D --> E[Validation and exceptions]
  E --> F[Close and PPA]
  F --> G[Rollups reports and exports]
```

Use the global search to find a specific feature, or start with the visual story to see
how the entities connect.

