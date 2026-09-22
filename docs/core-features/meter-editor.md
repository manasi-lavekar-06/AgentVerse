---
tags:
  - meter-editor
  - frozen-values
  - final-form
  - exceptions
  - auto-estimate
---

# Meter Editor Overview

Walks through the FLOWCAL Meter Editor screen: accessing it, its core tabs, its data
handling options, and its validation/audit settings.

<div class="km-mindmap">
<ul class="km-tree">
<li class="km-root-item">
<span class="km-node km-root">Meter Editor</span>
<ul>
<li class="km-branch-item">
<span class="km-node km-branch">Accessing the Meter Editor and Selecting a Device</span>
<ul>
<li><span class="km-node km-leaf">The Meter Editor can be opened from the dashboard tile or from Setup &gt; Meter Editor.</span></li>
<li><span class="km-node km-leaf">Devices can be selected by typing a Meter ID or Meter Name into a searchable drop-down.</span></li>
<li><span class="km-node km-leaf">The browse icon next to Meter ID opens a tree view for locating and selecting a device.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">General Tab</span>
<ul>
<li><span class="km-node km-leaf">Meter type, fluid phase, meter direction, meter status, and system are read-only, populated from meter characteristics.</span></li>
<li><span class="km-node km-leaf">Meter characteristics are edited in the Volume Editor's characteristic view.</span></li>
<li><span class="km-node km-leaf">The General tab also shows alternate meter number, customer name/meter number, check meter, and location/legal description.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Custom Fields Tab</span>
<ul>
<li><span class="km-node km-leaf">60 user-defined Custom Fields are available for company-specific information.</span></li>
<li><span class="km-node km-leaf">Custom Fields are configured by a system administrator.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Calculations Tab</span>
<ul>
<li><span class="km-node km-leaf">The Calculations tab is read-only and shows pressure base, temperature base, heating value base condition, calculation method, and sea method.</span></li>
<li><span class="km-node km-leaf">This information comes from the meter's characteristics validation, the same characteristics defined in the Volume Editor.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Quality Tab</span>
<ul>
<li><span class="km-node km-leaf">Quality settings range from relative density to GPM.</span></li>
<li><span class="km-node km-leaf">Bad values can be handled by Replace (overwrite) or Fill In (only when missing).</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Meter Data Handling Options</span>
<ul>
<li><span class="km-node km-leaf">Update Meter Name (default yes) auto-imports the meter name from files/transaction queue unless set to no.</span></li>
<li><span class="km-node km-leaf">Link Operational to Contractual syncs operational limits to contractual limits.</span></li>
<li><span class="km-node km-leaf">Ignore Contract Hour allows reporting at a contract hour different from the field device's own contract hour.</span></li>
<li><span class="km-node km-leaf">External Volume flags a meter as third-party (default no).</span></li>
<li><span class="km-node km-leaf">Periodic Snap corrects data timing to the top of the hour on import.</span></li>
<li><span class="km-node km-leaf">An edit indicator flag shows whether data was edited on import, and can be turned off.</span></li>
<li><span class="km-node km-leaf">A print option controls whether interval or fixed factor appears on the volume statement.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Frozen Values Tab and Component Validation</span>
<ul>
<li><span class="km-node km-leaf">Frozen Values validates gas components (CO2, nitrogen, methane, ethane, ... water) and component totals.</span></li>
<li><span class="km-node km-leaf">It flags values that repeat beyond a configured duration threshold.</span></li>
<li><span class="km-node km-leaf">A percent-difference threshold can also be set, with an always option for steady-flowing meters.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Final Form Validations</span>
<ul>
<li><span class="km-node km-leaf">Final Form sets hourly/daily/monthly validations for volume, energy, or mass.</span></li>
<li><span class="km-node km-leaf">Validation history is retained so seasonal changes can be reviewed later.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Exceptions Tab and Audit Criteria</span>
<ul>
<li><span class="km-node km-leaf">Exceptions are configured per device on the Exceptions tab.</span></li>
<li><span class="km-node km-leaf">Min/max exception ranges can be adjusted for known meter conditions, such as a small-plate orifice meter.</span></li>
<li><span class="km-node km-leaf">Audit criteria can trigger on an absolute volume limit or a percentage change between two devices, evaluated by an audit service.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Auto-Estimate for Missing Data</span>
<ul>
<li><span class="km-node km-leaf">Enabling auto-estimate lets FLOWCAL estimate values for missing meter data using defined techniques.</span></li>
<li><span class="km-node km-leaf">Risk and frequency settings control how exceptions are logged for these situations.</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>

## See Also

- [Meter Fundamentals](meters.md)
- [Liquid Meter and Product Setup](volume-editor.md)
- [FLOWCAL Data Journey Overview](../getting-started/flowcal-data-journey.md)
