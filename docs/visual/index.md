---
tags:
  - visual-story
hide:
  - toc
---

# Visual Story: The FLOWCAL Data Journey

<div class="vs-container" id="vsMain">

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

<div class="vs-slide vs-slide--navy-dark">
  <div class="vs-bg"></div>
  <div class="vs-meter-types-grid">
    <div class="vs-type-card"><div class="vs-type-icon">⚙️</div><div class="vs-type-label">Coriolis</div></div>
    <div class="vs-type-card"><div class="vs-type-icon">🌀</div><div class="vs-type-label">Turbine</div></div>
    <div class="vs-type-card"><div class="vs-type-icon">🔧</div><div class="vs-type-label">FLOCON Filter</div></div>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 2 · Meters</div>
    <h2 class="vs-title">Meter Fundamentals</h2>
    <p class="vs-body">A meter is the physical device that measures product volume. A FLOCON filter captures its raw data, and characteristics like meter type, pressure base, and temperature base determine how that raw data becomes flow.</p>
  </div>
</div>

<div class="vs-slide vs-slide--amber-dark">
  <div class="vs-bg"></div>
  <div class="vs-field-list">
    <span class="vs-field-chip vs-field-chip--key">product</span>
    <span class="vs-field-chip">density</span>
    <span class="vs-field-chip vs-field-chip--highlight">pressure base</span>
    <span class="vs-field-chip vs-field-chip--highlight">temperature base</span>
    <span class="vs-field-chip">meter factor = 1</span>
    <span class="vs-field-chip">contract hour/day</span>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 3 · Volume Editor</div>
    <h2 class="vs-title">Liquid Meter &amp; Product Setup</h2>
    <p class="vs-body">Choosing a product (e.g. a Table E product) auto-fills the meter's pressure base and temperature base, meter factor defaults to one, and the contract hour/day setting controls whether data is entered periodically or in batches.</p>
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
    <div class="vs-slide-tag">Step 4 · Locations</div>
    <h2 class="vs-title">Locations &amp; Systems</h2>
    <p class="vs-body">FLOWCAL's default system is called enterprise, and customers can add other systems as needed. Within a system, a single location can have multiple meters attached to it.</p>
  </div>
</div>

<div class="vs-slide vs-slide--data-dark">
  <div class="vs-bg"></div>
  <div class="vs-grid-mock">
    <div class="vs-grid-header"><div class="vs-grid-cell">Time</div><div class="vs-grid-cell">Product</div><div class="vs-grid-cell">Temp</div><div class="vs-grid-cell">Volume</div><div class="vs-grid-cell">Type</div></div>
    <div class="vs-grid-row"><div class="vs-grid-cell">Hr 1</div><div class="vs-grid-cell">-</div><div class="vs-grid-cell">-</div><div class="vs-grid-cell">-</div><div class="vs-grid-cell">periodic</div></div>
    <div class="vs-grid-row vs-row--estimated"><div class="vs-grid-cell">1 pt</div><div class="vs-grid-cell">manual</div><div class="vs-grid-cell">manual</div><div class="vs-grid-cell">manual</div><div class="vs-grid-cell">ticket</div></div>
  </div>
  <div class="vs-content">
    <div class="vs-slide-tag">Step 5 · Tickets</div>
    <h2 class="vs-title">Tickets Overview</h2>
    <p class="vs-body">Unlike a meter's continuous hourly data, a ticket captures a single point in time — so its product, temperature, and similar fields are entered manually rather than drawn from a periodic record.</p>
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
    <div class="vs-slide-tag">Step 6 · Rollup Viewers</div>
    <h2 class="vs-title">Rollup Viewer Basics</h2>
    <p class="vs-body">Once a location has meters attached, the Roll Up Viewer shows how its data aggregates — from minute-level detail up through super and monthly totals.</p>
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
