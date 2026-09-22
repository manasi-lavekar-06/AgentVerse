---
title: Meter Fundamentals
description: Meter Fundamentals - Complete Reference (Core Concepts)
tags:
  - meters
---

# Meter Fundamentals

## Core Concepts & Fundamentals

Explains what a meter represents physically in FLOWCAL, how a FLOCON filter attaches to
it, and how meter characteristics affect how flow is calculated.

## Meter Data Flow

```mermaid
graph LR
    A["⛽ Physical Meter"] -->|Captures| B["📊 Raw Data"]
    B -->|FLOCON Filter| C["🔢 Volume Data"]
    C -->|Characteristics| D["📈 Flow Calculation"]
    D -->|Result| E["✅ Processed Flow"]
    
    style A fill:#1a2742,stroke:#E65100,stroke-width:3px,color:#fff
    style B fill:#233257,stroke:#E65100,stroke-width:2px,color:#fff
    style C fill:#233257,stroke:#E65100,stroke-width:2px,color:#fff
    style D fill:#233257,stroke:#E65100,stroke-width:2px,color:#fff
    style E fill:#0f7e5f,stroke:#E65100,stroke-width:3px,color:#fff
```

## What Is a Meter

In FLOWCAL, everything originates from meter data. A meter is a physical device
installed where product is pulled from the ground or transferred through a pipeline,
and it measures volume - how much product is moving. A FLOCON filter is attached to the
meter and captures the raw data based on the meter's pressure base at the time of
measurement.

- A meter is a physical device that measures product volume as it is pulled from the
  ground or transferred through a pipeline.
- A FLOCON filter attaches to the meter and captures raw measurement data.

## Meter Types and Characteristics

Different meter types - such as Coriolis or turbine - calculate flow differently, so
each meter's characteristics must be defined. Two key characteristics are the pressure
base and the temperature base: the temperature of the product, the meter's own
temperature, and the pressure base together determine how raw data is converted into
flow.

- Meter types include Coriolis and turbine, each with its own calculation method.
- Pressure base and temperature base are core characteristics assigned to a meter.
- Both product temperature and meter temperature feed into the flow calculation.

## Meter Configuration Map

| Characteristic | Purpose | Example |
|---|---|---|
| **Meter Type** | Determines calculation method | Coriolis, Turbine |
| **Pressure Base** | Reference pressure for flow | 14.73 psia |
| **Temperature Base** | Reference temperature for flow | 60°F |
| **Meter Factor** | Adjustment multiplier | 1.0 (default) |
| **FLOCON Attachment** | Raw data capture | Serial connection |

## See Also

- [FLOWCAL Data Journey Overview](../getting-started/flowcal-data-journey.md)
- [Liquid Meter and Product Setup](volume-editor.md)
- [Meter Editor Overview](meter-editor.md)
