---
tags:
  - rollup-viewers
---

# Rollup Viewer Basics

Rollup viewers aggregate meter and location data across hourly, daily, and monthly timeframes, and are used to generate and export reports.

<!-- ko:ko-meter-data-roll-up-process block:0 -->
<div class="txt-block" markdown="1">

### Overview of the Roll-Up Process

<p>The roll-up process aggregates meter data from hourly to daily and then to monthly levels. After entering periodic data, it is queued in the roll-up queue. The roll-up service must be run to process this data and save it in the final form table. This allows users to view aggregated data at different time intervals.</p>
<ul>
<li>Periodic data is entered and queued in the roll-up queue.</li>
<li>The roll-up service processes data from hourly to daily and then to monthly levels.</li>
<li>Aggregated data is saved in the final form table for viewing.</li>
</ul>

</div>

<!-- ko:ko-meter-data-roll-up-process block:1 -->
<div class="flow-chart">
<div class="flow-root">Steps to Roll Up Meter Data</div>
<ol class="flow-steps">
<li class="flow-step">Enter hourly data.</li>
<li class="flow-step">Run the roll-up service.</li>
<li class="flow-step">Verify data in the roll-up queue.</li>
<li class="flow-step">Check aggregated data in the volume editor or roll-up viewer.</li>
<li class="flow-step">View final data in the final form table.</li>
</ol>
</div>

<!-- ko:ko-meter-data-roll-up-process block:2 -->
<div class="txt-block" markdown="1">

### Example of Data Roll-Up

<p>For example, if you enter 100 units of data for two hours on the first day, the daily total will be 200. If you add another 300 units on the second day, the daily total for that day will be 300. The monthly total will then aggregate these values to 500. This data can be viewed in the volume editor or roll-up viewer.</p>
<ul>
<li>Hourly data is aggregated into daily totals.</li>
<li>Daily totals are further aggregated into monthly totals.</li>
<li>Example: 200 units on Day 1 + 300 units on Day 2 = 500 units monthly.</li>
</ul>

</div>

<!-- ko:ko-meter-data-roll-up-process block:3 -->
<div class="txt-block" markdown="1">

### Viewing Aggregated Data

<p>Aggregated data can be viewed in the volume editor or roll-up viewer. Users can select the desired time interval (daily or monthly) to see the rolled-up data. The final form table stores this data for reference and reporting purposes.</p>
<ul>
<li>Use the volume editor or roll-up viewer to view aggregated data.</li>
<li>Select daily or monthly intervals to view specific roll-ups.</li>
<li>Final form table stores rolled-up data for reporting.</li>
</ul>

</div>

<!-- ko:ko-location-and-meter-roll-up-process block:0 -->
<div class="txt-block" markdown="1">

### Understanding Location and Meter Roll-Up

<p>The roll-up process aggregates data from meters within a location over specific timeframes such as hourly, daily, and monthly. For example, if a location has two meters, the data for each meter is summed up to provide a total for the location. This process ensures that data is consolidated for easier analysis and reporting.</p>
<ul>
<li>Roll-up aggregates data from multiple meters within a location.</li>
<li>Data is rolled up across different timeframes: hourly, daily, and monthly.</li>
<li>The roll-up process for locations is slower than for individual meters due to additional data checks.</li>
</ul>

</div>

<!-- ko:ko-location-and-meter-roll-up-process block:1 -->
<div class="txt-block" markdown="1">

### Relationship Between Locations and Meters

<p>A location represents a physical area where one or more meters are installed. For instance, a pipeline in a city like Pune may have multiple meters monitoring different sections. Each meter is a member of the location, and the location roll-up aggregates data from all its meters.</p>
<ul>
<li>Locations are physical areas where meters are installed.</li>
<li>A location can have one or multiple meters.</li>
<li>Meters within a location contribute to the location's aggregated data.</li>
</ul>

</div>

<!-- ko:ko-location-and-meter-roll-up-process block:2 -->
<div class="txt-block" markdown="1">

### Roll-Up Service Details

<p>The roll-up service for locations (FC SRV) processes data by first ensuring that all associated meters are rolled up. This makes the location roll-up slower compared to individual meter roll-ups. Once the roll-up is complete, the aggregated data is stored in the FC location table for further analysis.</p>
<ul>
<li>The roll-up service for locations is called FC SRV.</li>
<li>Location roll-ups depend on the completion of meter roll-ups.</li>
<li>Aggregated data is stored in the FC location table.</li>
</ul>

</div>

<!-- ko:ko-location-and-meter-roll-up-process block:3 -->
<div class="txt-block" markdown="1">

### Example of Location Roll-Up

<p>Consider a location with two meters. For January, the first meter records a value of 135, and the second meter records 27. The location roll-up for January will sum these values to 162. This aggregated data is then visible in the roll-up viewer and stored in the final form table for the location.</p>
<ul>
<li>Example: Two meters with values 135 and 27 for January.</li>
<li>The location roll-up aggregates these to 162.</li>
<li>Aggregated data is visible in the roll-up viewer and stored in the final form table.</li>
</ul>

</div>

<!-- ko:ko-understanding-data-rollups-and-batches-in-flowcal block:0 -->
<div class="dg-diagram">
<div class="dg-root">Data Rollups in FLOWCAL</div>
<ul class="dg-items">
<li class="dg-item">Periodic data aggregates into hourly data.</li>
<li class="dg-item">Hourly data aggregates into daily data.</li>
<li class="dg-item">Daily data aggregates into monthly data.</li>
</ul>
</div>

<!-- ko:ko-understanding-data-rollups-and-batches-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Contract Hours and Day Start Times

<p>The start of a new day in FLOWCAL is determined by the configured contract hour. For example, if the contract hour is set to 9:00 AM, the day begins at 9:00 AM and ends at 8:59 AM the following day. This affects how data is grouped and rolled up.</p>
<ul>
<li>Contract hours define the start of a new day.</li>
<li>Data grouping and rollups are aligned with contract hours.</li>
</ul>

</div>

<!-- ko:ko-understanding-data-rollups-and-batches-in-flowcal block:2 -->
<div class="txt-block" markdown="1">

### Batch Creation and Management

<p>Batches allow users to group data over specific time ranges. For example, a batch can cover five days or any other custom range. Once created, batches split the data accordingly, and users can view the data for each batch separately. Batches are not visible in the gas meter interface but can be managed in the volume editor.</p>
<ul>
<li>Batches group data over custom time ranges.</li>
<li>Batches can be created for specific periods, such as five days or a month.</li>
<li>Batches are managed in the volume editor and not visible in the gas meter interface.</li>
</ul>

</div>

<!-- ko:ko-understanding-data-rollups-and-batches-in-flowcal block:3 -->
<div class="flow-chart">
<div class="flow-root">Queueing and Rollup Process</div>
<ol class="flow-steps">
<li class="flow-step">Periodic data is queued for rollup after entry.</li>
<li class="flow-step">Rollup occurs in stages: periodic to hourly, hourly to daily, and daily to monthly.</li>
<li class="flow-step">The rollup process ensures systematic data aggregation.</li>
</ol>
</div>

<!-- ko:ko-generating-reports-and-managing-locations-in-flowcal block:0 -->
<div class="flow-chart">
<div class="flow-root">Generating Reports</div>
<ol class="flow-steps">
<li class="flow-step">Ensure roll-up service is running before generating reports.</li>
<li class="flow-step">Select meter, month, and data type (daily, monthly, or by product).</li>
<li class="flow-step">Preview, export, or print the generated report.</li>
</ol>
</div>

<!-- ko:ko-generating-reports-and-managing-locations-in-flowcal block:1 -->
<div class="flow-chart">
<div class="flow-root">Managing Locations and Meters</div>
<ol class="flow-steps">
<li class="flow-step">Create new locations using the Location Editor.</li>
<li class="flow-step">Specify location type and direction (inlet or outlet).</li>
<li class="flow-step">Assign a reference meter for contract day calculations.</li>
<li class="flow-step">Add multiple meters to a location for roll-up aggregation.</li>
</ol>
</div>

<!-- ko:ko-exporting-reports-and-data-in-flowcal block:0 -->
<div class="txt-block" markdown="1">

### Exporting Reports and Data

<p>FLOWCAL allows users to export reports that include meter data and location data. These reports can be generated through the rollup viewers and saved for further analysis or sharing. Once exported, the data can be shared via a shared location, and links to these files can be distributed to team members.</p>
<ul>
<li>Reports include meter and location data.</li>
<li>Data can be exported through rollup viewers.</li>
<li>Exported files can be shared via a shared location with links.</li>
</ul>

</div>

<!-- ko:ko-exporting-reports-and-data-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Additional Learning Resources

<p>Users are encouraged to watch the FLOWCAL course video for a deeper understanding of the system's features. This course provides an in-depth look at various topics and functionalities within FLOWCAL.</p>
<ul>
<li>FLOWCAL course video offers detailed insights.</li>
<li>Covers advanced topics and functionalities.</li>
</ul>

</div>

## See Also

- (none yet)
