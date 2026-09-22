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
    <div class="vs-type-card"><div class="vs-type-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.43 12.98c.04-.32.07-.64.07-.98 0-.34-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65A.488.488 0 0 0 14 1h-4c-.24 0-.44.18-.47.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.22-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.23.42.47.42h4c.24 0 .44-.18.47-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.22.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5 3.5 1.57 3.5 3.5-1.57 3.5-3.5 3.5z"/></svg></div><div class="vs-type-label">Coriolis</div></div>
    <div class="vs-type-card"><div class="vs-type-icon"><svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="2"/><path d="M12 11c0-3.2 1.6-6.3 4.3-7.6.9 2.7-.1 6-4.3 7.6z"/><path d="M12 13c-3.2.9-6.3-.7-7.6-3.4 2.7-.9 6-.1 7.6 3.4z"/><path d="M13 12.4c2.6 1.8 3.6 5 2.2 7.9-2.6-1.1-4-4.2-2.2-7.9z"/></svg></div><div class="vs-type-label">Turbine</div></div>
    <div class="vs-type-card"><div class="vs-type-icon"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.7 4.7C.6 7.1 1 10.1 3 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.4-.4.4-1 0-1.4z"/></svg></div><div class="vs-type-label">FLOCON Filter</div></div>
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
