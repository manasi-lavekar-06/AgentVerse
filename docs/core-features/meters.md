---
tags:
  - meters
---

# Meter Fundamentals

Explains what a meter represents physically in FLOWCAL, how a FLOCON filter attaches to
it to capture raw data, and how meter type and characteristics (such as base pressure
and base temperature) affect how flow is calculated.

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

## See Also

- [FLOWCAL Data Journey Overview](../getting-started/flowcal-data-journey.md)
- [Liquid Meter and Product Setup](volume-editor.md)
