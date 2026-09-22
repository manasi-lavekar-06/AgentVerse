---
tags:
  - overview
  - getting-started
---

# FLOWCAL Data Journey Overview

This overview traces how data flows through FLOWCAL, from field meters and flow computers, through validation and calculation, to rolled-up reports.

<!-- ko:ko-overview-of-data-flow-and-meter-operations-in-flokal block:0 -->
<div class="txt-block" markdown="1">

### Introduction to Flokal Data Flow

<p>Flokal manages data from field meters to generate accurate reports. Meters are physical devices installed to measure product flow, such as oil or gas, from the ground or pipelines. These meters are connected to flow computers that capture measurements like volume, pressure, and temperature at regular intervals.</p>
<ul>
<li>Meters measure product flow from the ground or pipelines.</li>
<li>Flow computers capture volume, pressure, and temperature data.</li>
<li>Data is recorded at intervals (e.g., 15 minutes, hourly, daily).</li>
</ul>

</div>

<!-- ko:ko-overview-of-data-flow-and-meter-operations-in-flokal block:1 -->
<div class="dg-diagram">
<div class="dg-root">Meter Setup and Characteristics</div>
<ul class="dg-items">
<li class="dg-item">Different meter types include Coriolis and turbine meters.</li>
<li class="dg-item">Characteristics like pressure base and temperature base are critical.</li>
<li class="dg-item">Measurement intervals can be 15 minutes, hourly, daily, or monthly.</li>
</ul>
</div>

<!-- ko:ko-overview-of-data-flow-and-meter-operations-in-flokal block:2 -->
<div class="flow-chart">
<div class="flow-root">Data Validation and Exception Handling</div>
<ol class="flow-steps">
<li class="flow-step">Data is imported in CFX format for validation.</li>
<li class="flow-step">Exceptions are raised for inaccurate data and must be resolved.</li>
<li class="flow-step">Changes to closed meters require PPA approval.</li>
</ol>
</div>

<!-- ko:ko-overview-of-data-flow-and-meter-operations-in-flokal block:3 -->
<div class="txt-block" markdown="1">

### Reporting and Rollup

<p>After validation and exception resolution, data is rolled up for reporting. Reports provide insights into product flow and are essential for operational decisions.</p>
<ul>
<li>Validated data is rolled up for reporting.</li>
<li>Reports provide insights into product flow and operations.</li>
</ul>

</div>

<!-- ko:ko-data-validation-calculation-and-rollup-in-flowcal block:0 -->
<div class="txt-block" markdown="1">

### Data Validation in FLOWCAL

<p>FLOWCAL validates imported data by checking it against predefined characteristics set in the Meter Editor. For example, temperature thresholds can be defined, and if the imported data exceeds these thresholds, an exception is raised. Missing data also triggers exceptions, ensuring that calculations are only performed on complete and accurate datasets.</p>
<ul>
<li>Validation rules are set in the Meter Editor.</li>
<li>Exceptions are raised for missing or incorrect data.</li>
<li>Examples include temperature thresholds and missing time periods.</li>
</ul>

</div>

<!-- ko:ko-data-validation-calculation-and-rollup-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Volumetric Calculations

<p>FLOWCAL uses specific formulas to calculate gross standard volume and net standard volume. Gross standard volume includes all liquid, while net standard volume excludes water content. Factors like temperature and pressure are considered in these calculations, ensuring accurate volume measurements.</p>
<ul>
<li>Gross standard volume includes all liquid, while net standard volume excludes water.</li>
<li>Calculations account for temperature, pressure, and other factors.</li>
<li>Formulas are used to ensure precise volume measurements.</li>
</ul>

</div>

<!-- ko:ko-data-validation-calculation-and-rollup-in-flowcal block:2 -->
<div class="txt-block" markdown="1">

### Data Rollup Process

<p>Hourly data in FLOWCAL is aggregated into daily and monthly summaries. For example, hourly data collected throughout January is summed to provide a total monthly volume. The rollup process considers contract hours to determine the aggregation period.</p>
<ul>
<li>Hourly data is rolled up into daily and monthly summaries.</li>
<li>The rollup process uses contract hours to define aggregation periods.</li>
<li>Summarized data provides a clear view of total volumes over time.</li>
</ul>

</div>

## See Also

- (none yet)
