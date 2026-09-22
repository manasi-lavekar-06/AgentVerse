---
title: Meter Fundamentals
description: Meter Fundamentals - Complete Reference (Core Concepts)
tags:
  - meters
---

# Meter Fundamentals

## Core Concepts & Fundamentals

This guide explains how to import meter and ticket data into the system, including the required file formats and steps for successful data integration.

<!-- ko:ko-importing-meter-and-ticket-data block:0 -->
<div class="txt-block" markdown="1">

### File Formats for Import

<p>To import meter or ticket data, specific file formats are required. For meter data, a sample text file format is provided, which can be copied into Excel for data entry. For ticket data, both TFX (binary) and text file formats are supported. Ensure the correct file type is selected during the import process.</p>
<ul>
<li>Meter data requires a specific text file format.</li>
<li>Ticket data supports TFX (binary) and text file formats.</li>
<li>Use Excel to prepare data in the required format.</li>
</ul>

</div>

<!-- ko:ko-importing-meter-and-ticket-data block:1 -->
<div class="flow-chart">
<div class="flow-root">Steps to Import Meter Data</div>
<ol class="flow-steps">
<li class="flow-step">Obtain the sample file format for meter data.</li>
<li class="flow-step">Copy the format into Excel and enter the required data.</li>
<li class="flow-step">Save the file in the appropriate format.</li>
<li class="flow-step">Navigate to the meter import section in the system.</li>
<li class="flow-step">Select the prepared file and initiate the import process.</li>
</ol>
</div>

<!-- ko:ko-importing-meter-and-ticket-data block:2 -->
<div class="flow-chart">
<div class="flow-root">Steps to Import Ticket Data</div>
<ol class="flow-steps">
<li class="flow-step">Navigate to the meter import section and select ticket data.</li>
<li class="flow-step">Choose the file format (TFX or text file).</li>
<li class="flow-step">Select the file to import.</li>
<li class="flow-step">Verify the imported ticket in the ticket editor by selecting the appropriate date range and ticket type.</li>
</ol>
</div>

<!-- ko:ko-importing-meter-and-ticket-data block:3 -->
<div class="txt-block" markdown="1">

### Summary of Import Process

<p>The import process involves preparing data in the correct format, uploading it through the system's import functionality, and verifying the imported data. This ensures accurate integration of meter and ticket data into the system.</p>
<ul>
<li>Prepare data in the correct format.</li>
<li>Use the system's import functionality.</li>
<li>Verify imported data for accuracy.</li>
</ul>

</div>
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

- (none yet)
