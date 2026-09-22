---
title: FLOWCAL Toolbox Overview
description: FLOWCAL Toolbox Overview - Complete Reference (Core Concepts)
tags:
  - toolbox
  - validation
  - auto-edit
  - recalculation
  - batch-operations
  - tools
---

# FLOWCAL Toolbox Overview

## Core Concepts & Fundamentals

The FLOWCAL Toolbox is a utility accessible from the Tools menu that allows users to perform batch operations on meters, locations, lists, sources, and close groups across a selected date range. The Toolbox provides options to run validations, apply auto edits, recalculate volumes, accept auto estimates, and perform other administrative tasks.

## Accessing and Configuring the Toolbox

The FLOWCAL Toolbox is accessed via Tools > Toolbox from the main menu. Once open, users can select the object type they want to operate on (meter, location, list, source, source list, or close group), choose a date range type (contract month, contract days, or date time range), and specify the particular date or range to apply the toolbox operation to.

**Key Points:**

- Access the Toolbox via Tools > Toolbox menu.
- Select an object type: meter, location, list, source, source list, or close group.
- Choose a date range type: contract month, contract days, or date time range.
- Specify the date or range for which the operation applies.

## Toolbox Operations

The Toolbox provides several operations at the bottom of the screen. Recap rule of IDs should only be run at the request of support. Run validations executes configured validations for meters, locations, and sources within the selected timeframe. Apply defined auto edit applies all auto edits assigned to a meter. Apply this auto edit allows selecting a specific auto edit from a dropdown to apply to a meter or list. Force recalcov forces recalculation of volume or volume correlation factor when edits did not trigger recalculation in the Volume Editor. Accept auto estimates accepts auto-estimated values if the auto estimate feature is enabled.

**Key Points:**

- Recap rule of IDs: reserved for support team use only.
- Run validations: executes configured validations for the selected timeframe.
- Apply defined auto edit: applies all auto edits assigned to the object.
- Apply this auto edit: select and apply a specific auto edit from a dropdown.
- Force recalcov: recalculates volume or volume correlation factor after manual edits.
- Accept auto estimates: accepts auto-estimated values when auto estimate is enabled.

## Related Topics

- [Meter Fundamentals](meters.md)
- [Locations and Systems](locations.md)
- [Liquid Meter Product Setup](../core-features/volume-editor.md)
- [FLOWCAL Data Journey](../getting-started/flowcal-data-journey.md)
- [Rollup Viewer Basics](rollup-viewers.md)

---

## Implementation Details

## Overview

- # Audits

 Audits Audits allow users to define criteria for meters to be flagged for audit on a meter by meter basis.
- The criteria can be based on: Time (monthly, quarterly, semi-annually, or annually) Volume or energy change from one month to the next Total volume or energy for the month Difference in volume or energy for a check to sales relationship (meter or check location) Before starting, consider the following questions: Is this for volume recovery or a second layer of data validation?

## Key Characteristics

- Will individual analysts or a small group manage the setup and review?
- Is there a current list of ins and outs for gathering systems or one-to-one relationships for checks on sales meters?
- Will this roll out to one geographic area or one-to-one relationships first?
- This feature requires the Audit Package module.
- Configuring a Meter to Audit A meter’s audit criteria can be set up within the Meter Editor Audits tab, to validate potential discrepancies with an Audit, Custody, or Check Meter.
- Audits can be performed based on volume/energy differences or using a time criteria.

## Related Topics

- Configuration and Setup
- Data Management
- Reports and Analytics

