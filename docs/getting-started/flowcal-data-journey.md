---
tags:
  - overview
  - getting-started
---

# FLOWCAL Data Journey Overview

A high-level walkthrough of how a new user moves through FLOWCAL end to end, from
security setup through validation, PPA approval, and rolled-up reporting.

<div class="km-mindmap">
<ul class="km-tree">
<li class="km-root-item">
<span class="km-node km-root">FLOWCAL Data Journey</span>
<ul>
<li class="km-branch-item">
<span class="km-node km-branch">Security: Users and Groups</span>
<ul>
<li><span class="km-node km-leaf">Users are created individually and then assigned to one or more groups.</span></li>
<li><span class="km-node km-leaf">Groups are created with distinct privilege levels to control what a user can access or do in FLOWCAL.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">End-to-End Data Flow</span>
<ul>
<li><span class="km-node km-leaf">Liquid product/meter setup requires a base pressure and base temperature.</span></li>
<li><span class="km-node km-leaf">Core setup order: meter -&gt; location -&gt; tickets -&gt; characteristics -&gt; meter data -&gt; validation.</span></li>
<li><span class="km-node km-leaf">Data that fails validation closes on an exception and must be resolved before the meter can be closed.</span></li>
<li><span class="km-node km-leaf">Changes to an already-closed meter (e.g. an equation change) require PPA approval.</span></li>
<li><span class="km-node km-leaf">Manual imports bring data into FLOWCAL outside of automated collection.</span></li>
<li><span class="km-node km-leaf">Rolled-up data is the basis for FLOWCAL reports.</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>

## See Also

- [Meter Fundamentals](../core-features/meters.md)
- [Liquid Meter and Product Setup](../core-features/volume-editor.md)
- [Locations and Systems](../core-features/locations.md)
- [Tickets Overview](../core-features/tickets.md)
- [Rollup Viewer Basics](../core-features/rollup-viewers.md)
- [Meter Editor Overview](../core-features/meter-editor.md)
