---
title: Rollup Viewer Basics
description: Rollup Viewer Basics - Complete Reference (Core Concepts)
tags:
  - rollup-viewers
---

# Rollup Viewer Basics

## Core Concepts & Fundamentals

Introduces the Roll Up Viewer, which shows how a location's meter data aggregates (e.g.
minute, super, and monthly) once a location has meters attached.

## Viewing Rolled-Up Data for a Location

After a location has one or more meters attached, the Roll Up Viewer shows how that
location's data rolls up - for example at a minute, super, and monthly level. For a
liquid meter/location, the rollup view reflects the liquid-specific data captured for
that location.

- The Roll Up Viewer aggregates a location's meter data at levels such as minute, super,
  and monthly.
- Rollup output reflects the type of meter (e.g. liquid) attached to the location.

## See Also

- [Locations and Systems](locations.md)
- [Tickets Overview](tickets.md)

---

## Implementation Details

## Overview

- # Carry/Borrow Method

 Carry/Borrow Method The periodic volumes that comprise an hour are totaled and stored in the measured_volume column of the Final-Form Hourly table.
- A rounded, integer version of this value is calculated using a carry/borrow method and is stored in the rollup_volume column.

## Key Characteristics

- Hourly Records Consider a meter with volumes as shown (column A) for the first four hours of a day.
- Presume the rest of the hours for the day are exactly 0.
- Day Measured Volume Current Day + Last Carry Amount Carry/Borrow Rounded Value Monthly Carry (Borrow)Amount Straight Rounding - A B = A +D C = Round(B) D = B - C E = Round(A) 1 10.4 - 10 0.4 10 2 10.4 10.8 11 (0.2) 10 3 10.4 10.2 10 0.2 10 4 10.4 10.6 11 (0.4) 10 Hour 1 is rounded to 10 (column C), and the leftover amount of 0.4 is noted (column D) as the carry amount.
- The Hour 1 carry amount is added to the Hour 2 Measured Volume (result in column B).
- This result, 10.8, is rounded to 11 (column C).
- The leftover amount of -0.2 is carried to Hour 3 (i.e., 0.2 is borrowed from Hour 3), and so on through the day.

## Related Topics

- Configuration and Setup
- Data Management
- Reports and Analytics

