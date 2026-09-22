---
tags:
  - volume-editor
  - liquid-meter
---

# Liquid Meter and Product Setup

The Volume Editor is where liquid and gas meter data is entered, validated, sourced, closed, and approved.

<!-- ko:ko-setting-up-liquid-and-gas-meters-in-the-volume-editor block:0 -->
<div class="txt-block" markdown="1">

### Batch and Periodic Data in the Volume Editor

<p>The Volume Editor allows you to manage batch and periodic data for liquid and gas meters. Batch data is non-periodic and can represent data collected over intervals like two days or 15 days. Periodic data, on the other hand, is consistent and can be daily or monthly. Gas meters typically only support periodic data, while liquid meters can handle both batch and periodic data. When setting up characteristics for batch data, they apply only to the selected batch, whereas for periodic data, the characteristics apply across the entire timeline.</p>
<ul>
<li>Batch data is non-periodic and specific to intervals.</li>
<li>Periodic data is consistent and can be daily or monthly.</li>
<li>Gas meters support only periodic data; liquid meters support both.</li>
<li>Characteristics for batch data apply to specific batches, while periodic data characteristics apply across the timeline.</li>
</ul>

</div>

<!-- ko:ko-setting-up-liquid-and-gas-meters-in-the-volume-editor block:1 -->
<div class="txt-block" markdown="1">

### Configuring Meter Types and Characteristics

<p>To configure a meter in the Volume Editor, you must first select the meter type. For liquid meters, turbine meters are commonly used, though other types are also supported. The setup includes defining the calculation method and specifying the product flowing through the meter. The product setup determines the temperature base and pressure base values, which are critical for accurate calculations. These values are automatically pulled from the product configuration once selected.</p>
<ul>
<li>Select the meter type (e.g., turbine meter for liquids).</li>
<li>Define the calculation method and product flowing through the meter.</li>
<li>Product setup determines temperature and pressure base values.</li>
<li>Temperature and pressure bases are pulled from the product configuration.</li>
</ul>

</div>

<!-- ko:ko-setting-up-liquid-and-gas-meters-in-the-volume-editor block:2 -->
<div class="txt-block" markdown="1">

### Setting Up Products and Units

<p>When setting up a product in the Volume Editor, you must specify the product name and its associated characteristics, such as density and units. For US units, relative density is used, and the pressure base is typically 14.6 PSI. For metric units, temperature bases like 15°C or 20°C and pressure bases in kilopascals are used. Once the product is configured, it can be selected for the meter, and its characteristics will be applied automatically.</p>
<ul>
<li>Specify product name and characteristics (e.g., density, units).</li>
<li>US units use relative density and PSI for pressure base.</li>
<li>Metric units use temperature in °C and pressure in kilopascals.</li>
<li>Configured products automatically apply their characteristics to meters.</li>
</ul>

</div>

<!-- ko:ko-setting-up-liquid-and-gas-meters-in-the-volume-editor block:3 -->
<div class="txt-block" markdown="1">

### Finalizing Meter Setup

<p>After configuring the meter type, product, and characteristics, you must provide a reason for the edits and save the configuration. The meter factor is typically set to 1 by default. Once saved, the setup is complete, and the meter is ready for operation.</p>
<ul>
<li>Provide a reason for edits before saving.</li>
<li>Meter factor is usually set to 1 by default.</li>
<li>Save the configuration to finalize the setup.</li>
</ul>

</div>

<!-- ko:ko-creating-and-assigning-quality-sources-in-flowcal block:0 -->
<div class="flow-chart">
<div class="flow-root">Creating a Quality Source</div>
<ol class="flow-steps">
<li class="flow-step">Navigate to gas or liquid quality source section.</li>
<li class="flow-step">Define characteristics and provide an edit reason.</li>
<li class="flow-step">Save the source for further use.</li>
</ol>
</div>

<!-- ko:ko-creating-and-assigning-quality-sources-in-flowcal block:1 -->
<div class="flow-chart">
<div class="flow-root">Importing or Manually Entering Source Analysis Data</div>
<ol class="flow-steps">
<li class="flow-step">Source analysis data can be imported or entered manually.</li>
<li class="flow-step">Specify import file date, product, and mole percent.</li>
<li class="flow-step">Mass and liquid volume are automatically calculated.</li>
</ol>
</div>

<!-- ko:ko-creating-and-assigning-quality-sources-in-flowcal block:2 -->
<div class="flow-chart">
<div class="flow-root">Assigning a Quality Source to Meters</div>
<ol class="flow-steps">
<li class="flow-step">Use the quality source assignment editor to assign sources.</li>
<li class="flow-step">Select the meter and source, and specify the effective date.</li>
<li class="flow-step">Sources can be assigned to multiple meters.</li>
<li class="flow-step">Volume is recalculated after source assignment.</li>
</ol>
</div>

<!-- ko:ko-creating-and-assigning-quality-sources-in-flowcal block:3 -->
<div class="flow-chart">
<div class="flow-root">Verifying Assigned Sources in the Volume Editor</div>
<ol class="flow-steps">
<li class="flow-step">Open the volume editor to verify source assignments.</li>
<li class="flow-step">Select the meter for the relevant month.</li>
<li class="flow-step">Review the statement for accuracy.</li>
</ol>
</div>

<!-- ko:ko-importing-and-managing-data-in-volume-editor block:0 -->
<div class="txt-block" markdown="1">

### Importing Data Using the Import Service

<p>The import service (FC SRV) is used to import data into the Volume Editor. You can run the service either as an installed service or as an application, which is useful for testing across different versions. When the service runs, it first checks the configured database and username. If everything is correct, it starts importing the data. Once the data is processed, the file is renamed, indicating successful import. Imported data can come from various file types, such as CFX or text files.</p>
<ul>
<li>FC SRV is the import service for the Volume Editor.</li>
<li>The service can be run as an installed service or as an application.</li>
<li>It verifies the database and username before importing.</li>
<li>Processed files are renamed to indicate successful import.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-data-in-volume-editor block:1 -->
<div class="txt-block" markdown="1">

### Identifying Imported Data

<p>Imported data can be distinguished in the Volume Editor by its text color. For example, data entered manually may appear in blue, while data imported from a file (e.g., CFX file) appears in black. This visual distinction helps users identify the source of the data.</p>
<ul>
<li>Manually entered data appears in blue text.</li>
<li>Imported data appears in black text.</li>
<li>The text color helps identify the data source.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-data-in-volume-editor block:2 -->
<div class="txt-block" markdown="1">

### Purging Data in the Volume Editor

<p>The Volume Editor provides a 'Purge' option to delete data. Users can select specific time ranges or delete all data for a meter. This feature is useful for correcting mistakes or re-importing data. To purge data, select the desired time range, provide an edit reason, and confirm the deletion. Be cautious, as purging can delete all data within the selected range or even the entire meter.</p>
<ul>
<li>The 'Purge' option allows deletion of data by time range or for all time.</li>
<li>Purging is useful for correcting mistakes or re-importing data.</li>
<li>Users must provide an edit reason before purging.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-data-in-volume-editor block:3 -->
<div class="txt-block" markdown="1">

### Additional Data Entry Options

<p>The Volume Editor offers multiple ways to enter data. Users can double-click to open a detailed window for data entry or use options like 'Flow Data' to access specific entry fields. These options provide flexibility in managing and editing data.</p>
<ul>
<li>Double-clicking opens a detailed data entry window.</li>
<li>Options like 'Flow Data' allow specific data entry.</li>
<li>The editor provides flexibility for managing data.</li>
</ul>

</div>

<!-- ko:ko-using-the-volume-editor-for-data-entry-and-exception-handling block:0 -->
<div class="txt-block" markdown="1">

### Data Entry in the Volume Editor

<p>The Volume Editor allows users to enter data for specific time ranges. You can select all data in the grid using 'Ctrl + A' or choose a selective range. Right-clicking on the selection provides options like 'Span Edit' and 'Flow Data'. Double-clicking a cell also opens the detail view for entering flow data.</p>
<ul>
<li>Select all data with 'Ctrl + A' or choose a specific range.</li>
<li>Right-click for options like 'Span Edit' and 'Flow Data'.</li>
<li>Double-click a cell to open the detail view for data entry.</li>
</ul>

</div>

<!-- ko:ko-using-the-volume-editor-for-data-entry-and-exception-handling block:1 -->
<div class="txt-block" markdown="1">

### Copying Data Across Time Ranges

<p>The 'Copy Data' functionality allows users to replicate data across a specified time range. For example, if you have characteristics set up for one month, you can copy them throughout the entire time range by selecting 'Copy' and adjusting the date range.</p>
<ul>
<li>Use 'Copy Data' to replicate data across time ranges.</li>
<li>Adjust the date range to define the scope of the copy operation.</li>
</ul>

</div>

<!-- ko:ko-using-the-volume-editor-for-data-entry-and-exception-handling block:2 -->
<div class="txt-block" markdown="1">

### Validation and Exception Handling

<p>The Volume Editor highlights validation issues, such as temperature exceeding a threshold, in yellow. Users can resolve these exceptions by double-clicking the highlighted cell, navigating to the 'Exception' tab, and addressing the issue. Options include acknowledging the exception, marking it as pending, or fixing the data. Exceptions can also be managed through the 'Exception Result' view, where unresolved issues are listed and can be resolved or acknowledged.</p>
<ul>
<li>Validation issues are highlighted in yellow.</li>
<li>Resolve exceptions via the 'Exception' tab or 'Exception Result' view.</li>
<li>Options include acknowledging, marking as pending, or fixing the data.</li>
</ul>

</div>

<!-- ko:ko-using-volume-editor-and-bulk-changes-for-meter-characteristics block:0 -->
<div class="txt-block" markdown="1">

### Resolving Exceptions in the Volume Editor

<p>The Volume Editor allows users to resolve exceptions by highlighting and acknowledging them. Once an exception is acknowledged, its status changes, and the record is updated. Users can double-click on an exception to navigate directly to the Volume Editor for resolution.</p>
<ul>
<li>Highlight exceptions to review their details.</li>
<li>Acknowledge exceptions to update their status.</li>
<li>Double-clicking an exception navigates to the Volume Editor for resolution.</li>
</ul>

</div>

<!-- ko:ko-using-volume-editor-and-bulk-changes-for-meter-characteristics block:1 -->
<div class="flow-chart">
<div class="flow-root">Updating Meter Characteristics Using Bulk Changes</div>
<ol class="flow-steps">
<li class="flow-step">Create a static list of meters for bulk updates.</li>
<li class="flow-step">Use the Bulk Changes tool to modify characteristics like contract hours.</li>
<li class="flow-step">Changes are reflected in the Volume Editor and tracked with revisions.</li>
</ol>
</div>

<!-- ko:ko-using-volume-editor-and-bulk-changes-for-meter-characteristics block:2 -->
<div class="txt-block" markdown="1">

### Tracking Changes and Revisions

<p>Each change made to meter characteristics is tracked as a new revision. The Volume Editor displays the updated characteristics and the revision count, ensuring a clear history of modifications.</p>
<ul>
<li>Revisions are incremented with each change.</li>
<li>The Volume Editor shows updated characteristics and revision counts.</li>
<li>A clear history of modifications is maintained.</li>
</ul>

</div>

<!-- ko:ko-manual-closing-and-ppa-adjustments-in-volume-editor block:0 -->
<div class="txt-block" markdown="1">

### Manual Closing of a Month

<p>To manually close a month in the Volume Editor, ensure all exceptions are resolved. For example, if an exception is raised, set the required value (e.g., 60-meter temperature) to resolve it. Once all exceptions are cleared, you can manually close the month. Note that there is an option to schedule the closing, but this is considered an advanced feature and is not covered here.</p>
<ul>
<li>Resolve all exceptions before closing a month.</li>
<li>Manually closing is the primary method covered.</li>
<li>Scheduled closing is an advanced feature.</li>
</ul>

</div>

<!-- ko:ko-manual-closing-and-ppa-adjustments-in-volume-editor block:1 -->
<div class="txt-block" markdown="1">

### Making Edits and Triggering PPA

<p>When you edit a volume (e.g., changing it from 500 to 1500), it triggers a recalculation. Any recalculation after closing a meter results in a prior period adjustment (PPA). A pop-up will appear asking if you want to accept the PPA, showing the current and new volume values. Accepting the PPA applies the changes.</p>
<ul>
<li>Editing a volume triggers recalculation and PPA.</li>
<li>A pop-up displays current and new volume values for confirmation.</li>
<li>Accepting the PPA applies the changes.</li>
</ul>

</div>

<!-- ko:ko-manual-closing-and-ppa-adjustments-in-volume-editor block:2 -->
<div class="txt-block" markdown="1">

### Approval Process for Changes

<p>If the 'approval required' option is enabled, changes will not take effect until approved. Pending approvals can be accessed via 'Edit Approval' or 'Review Approvals'. Only group members can approve changes. Once approved, the changes are finalized, and the new values are applied.</p>
<ul>
<li>Changes require approval if the 'approval required' option is enabled.</li>
<li>Pending approvals can be reviewed and approved by group members.</li>
<li>Approval finalizes changes and applies new values.</li>
</ul>

</div>

<!-- ko:ko-approving-changes-and-rollup-process-in-volume-editor block:0 -->
<div class="txt-block" markdown="1">

### Approving Changes in Volume Editor

<p>When you are a member of the relevant group, you can approve changes in the Volume Editor. If you are not a member, the approval option will be disabled. To approve a change, select the record, review the details, and confirm the approval. Once approved, the record's status will update to 'Approved,' and the adjusted volume will be visible in the Volume Editor. For example, if the original volume was 500 and the new adjusted volume is 1500, the difference (Delta PPA) is calculated as 1000. This difference can be viewed in a hidden column that can be added to the editor.</p>
<ul>
<li>Approval is restricted to group members.</li>
<li>Changes must be reviewed before approval.</li>
<li>Approved records update their status and reflect adjusted volumes.</li>
<li>Delta PPA shows the difference between original and adjusted volumes.</li>
</ul>

</div>

<!-- ko:ko-approving-changes-and-rollup-process-in-volume-editor block:1 -->
<div class="txt-block" markdown="1">

### Rollup Process After Changes

<p>After making changes to a meter in the Volume Editor, the data is queued for rollup. The rollup process aggregates the data to update reports, such as the volume statement. If the rollup service is stopped, the changes will remain queued until the service is restarted. Once the rollup is complete, the updated data can be included in reports.</p>
<ul>
<li>Changes are queued for rollup after edits.</li>
<li>Rollup aggregates data for reporting purposes.</li>
<li>Rollup service must be running for changes to be processed.</li>
<li>Updated data appears in reports like the volume statement.</li>
</ul>

</div>

## See Also

- (none yet)
