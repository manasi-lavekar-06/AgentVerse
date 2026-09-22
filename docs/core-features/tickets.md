---
title: Tickets Overview
description: Tickets Overview - Complete Reference (Core Concepts)
tags:
  - tickets
---

# Tickets Overview

## Core Concepts & Fundamentals

Explains how a ticket differs from a meter's flowing data and how a new ticket is
created for a single point in time.

<div class="km-mindmap">
<ul class="km-tree">
<li class="km-root-item">
<span class="km-node km-root">Tickets</span>
<ul>
<li class="km-branch-item">
<span class="km-node km-branch">What Is a Ticket</span>
<ul>
<li><span class="km-node km-leaf">A meter captures flowing data continuously, e.g. each hour.</span></li>
<li><span class="km-node km-leaf">A ticket represents a single point-in-time record rather than a periodic one.</span></li>
</ul>
</li>
<li class="km-branch-item">
<span class="km-node km-branch">Creating a New Ticket</span>
<ul>
<li><span class="km-node km-leaf">New tickets are created from the meter's empty grid via a "create new ticket" option.</span></li>
<li><span class="km-node km-leaf">Ticket entries require manually selecting fields such as product and temperature, since there is no periodic record to draw from.</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>

## See Also

- [Locations and Systems](locations.md)
- [Rollup Viewer Basics](rollup-viewers.md)

## Implementation Details

### Ticket Creation and Management

![Ticket Grid](../assets/images/tickets/extracted_image_5285.png "Ticket Data Grid")
![Create Ticket](../assets/images/tickets/extracted_image_5286.png "Creating a New Ticket")

### Gas Loss Tickets

![Gas Loss Entry](../assets/images/tickets/extracted_image_5287.png "Gas Loss Ticket Editor")

---

## Implementation Details

## Overview

- # Gas Loss Tickets

 Gas Loss Tickets The Gas Loss Ticket Viewer is used for viewing and creating Gas Loss ticket data.
- Gas loss tickets are used to account for unmeasured gas volumes such as from the blowdown of a line.

## Key Characteristics

- You can view and edit Gas Loss tickets in the Gas Loss Ticket Editor as well as Ticket Search.
- To access the GasLoss Ticket Viewer and view Gas Loss tickets: Go to Open Tickets Gas Loss Tickets .
- Specify a date range and click Refresh .
- All saved Gas Loss tickets will display.
- Double-click a ticket entry to view the ticket details.
- Add a GasLoss Ticket To create a Gas Loss ticket: Refresh the GasLoss Ticket Viewer.

## Related Topics

- Configuration and Setup
- Data Management
- Reports and Analytics

