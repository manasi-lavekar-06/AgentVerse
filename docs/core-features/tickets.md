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

## What Is a Ticket

A ticket is similar to a meter in that it belongs to a meter, but where a meter has
flowing data captured continuously (for example, each hour), a ticket represents data
for a single point in time rather than a periodic record.

- A meter captures flowing data continuously, e.g. each hour.
- A ticket represents a single point-in-time record rather than a periodic one.

## Creating a New Ticket

To create a ticket, click on the meter to see its empty data grid, then choose the
option to create a new ticket. Because a ticket is a one-time record rather than a
periodic one, the product and applicable temperature (and similar fields) must be
selected manually for that entry.

- New tickets are created from the meter's empty grid via a "create new ticket" option.
- Ticket entries require manually selecting fields such as product and temperature,
  since there is no periodic record to draw from.

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

