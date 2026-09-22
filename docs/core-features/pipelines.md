---
tags:
  - pipelines
  - compression
  - core-features
---

# Pipeline Infrastructure and Compression

Describes natural gas pipeline infrastructure including quality requirements, compressor stations, line pack storage in pipelines, and how compression maintains gas flow across long distances. Explains the fuel consumption measurement needs for accurate gain/loss accounting.

## Pipeline Quality Requirements

Natural gas pipelines have strict quality requirements that the gas must meet before acceptance. These requirements include specifications for BTU content (energy density), water content, and hydrogen sulfide levels. Gas that does not meet these specifications cannot enter a particular pipeline and must either be treated to improve quality or routed to a different pipeline with less stringent requirements. Pipeline operators enforce these standards to ensure product quality and system integrity throughout the distribution network.

- Pipelines have strict quality specifications for accepted gas.
- Key quality parameters: BTU content, water content, hydrogen sulfide.
- Non-conforming gas cannot enter pipelines.
- Gas may be treated to meet quality requirements.
- Quality management protects product integrity and system reliability.

## Compressor Stations and Pressure Management

As natural gas moves through pipelines over long distances, pressure decreases due to friction and loss of potential energy. Compressor stations are installed along pipelines to maintain adequate pressure and keep the gas moving forward. Compressor stations also enable line pack operations where gas is deliberately pressurized into the pipeline for temporary storage. There are pressure limits on pipes, and compressor stations manage pressurization to keep gas flowing while respecting these mechanical limits.

- Compressor stations maintain pressure along pipelines.
- Pressure decreases naturally as gas travels distance.
- Compressors increase pressure to maintain flow velocity.
- Compressors enable line pack storage within pipelines.
- Pressure limits on pipelines constrain compressor operations.

## Line Pack and Strategic Gas Storage

Natural gas is highly compressible, allowing large volumes to be temporarily stored within pipelines themselves through line pack operations. Additional gas is intentionally pumped into pipelines in anticipation of high demand periods, such as before cold weather events when heating demand increases. FLOWCAL uses line pack meters to track the volume of gas stored in pipelines, which can represent significant financial value. Line pack is managed through strategic use of compressor stations to pack gas in advance of predictable demand surges.

- Natural gas's compressibility enables pipeline storage (line pack).
- Gas is packed in advance of high demand periods.
- Cold weather events drive line pack strategy for heating demand.
- Line pack meters track stored gas volume and value.
- Strategic packing maintains supply reliability during demand peaks.

## Compressor Fuel Consumption and Measurement

Compressor stations use fuel (typically natural gas) to operate. Ideally, fuel consumption is measured directly with fuel meters. However, in some cases, fuel measurement is expensive and the volume consumed is small, so measurement is not implemented. Instead, fuel consumption should be calculated using FLOWCAL's calculated meter functionality based on compressor specifications and operating parameters. Accurate measurement or calculation of compressor fuel consumption is essential for gain/loss accounting, as fuel burned represents gas leaving the system that must be accounted for to explain total flow changes.

- Compressor stations consume fuel for operation.
- Fuel measurement is ideal but sometimes economically impractical.
- Calculated meters can estimate fuel consumption.
- Fuel consumption must be accounted for in gain/loss calculations.
- Without fuel accounting, unexplained losses will appear in the system.

## See Also

- [Gathering Systems](gathering-systems.md)
- [Meter Calibration and Testing](meter-testing.md)
- [Gas Distribution and End Users](distribution.md)

## Images & Visual References

### Pipeline Infrastructure

![Pipeline System](../assets/images/pipelines/extracted_image_0122.gif "Natural Gas Pipeline Network")
![Compressor Station](../assets/images/pipelines/extracted_image_0123.gif "Compressor Station Layout")

### Pressure Management & Line Pack

![Pressure Control](../assets/images/pipelines/extracted_image_0124.png "Pressure Management System")

---
