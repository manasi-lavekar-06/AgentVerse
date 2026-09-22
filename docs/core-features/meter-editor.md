---
tags:
  - meter-editor
---

# Meter Editor

The Meter Editor is where meters are created, configured, imported, validated, closed, and adjusted throughout their lifecycle.

<!-- ko:ko-creating-and-configuring-meters block:0 -->
<div class="txt-block" markdown="1">

### Meter Types and Creation Process

<p>Meters can be created as either gas meters or liquid meters, with slight differences in features based on their nature. To create a meter, navigate to the Meter Editor via the setup menu or a shortcut. Provide a meter name (required) and a meter number. The meter attributes will be stored in the FC meter table, accessible by meter number or index.</p>
<ul>
<li>Meters can be gas or liquid types.</li>
<li>Navigate to the Meter Editor to create a meter.</li>
<li>Provide a meter name and number; attributes are stored in the FC meter table.</li>
</ul>

</div>

<!-- ko:ko-creating-and-configuring-meters block:1 -->
<div class="txt-block" markdown="1">

### Configuring Meter Characteristics

<p>After creating a meter, you can configure its characteristics, such as location, legal description, and operational ranges (e.g., temperature, pressure). These settings are validated to ensure data accuracy. For example, you can set a minimum and maximum temperature range, and the system will flag data that falls outside these limits.</p>
<ul>
<li>Characteristics include location, legal description, and operational ranges.</li>
<li>Validation rules ensure data accuracy (e.g., temperature limits).</li>
<li>Settings can be edited manually in the Meter Editor.</li>
</ul>

</div>

<!-- ko:ko-creating-and-configuring-meters block:2 -->
<div class="txt-block" markdown="1">

### Using the Volume Editor for Data Entry

<p>To manually enter characteristics or validate data, use the Volume Editor. Access it either through the Meter Editor's 'Open Data' option or directly via the Volume Editor tile. This tool allows you to input and validate data specific to the meter.</p>
<ul>
<li>The Volume Editor is used for manual data entry and validation.</li>
<li>Access it via 'Open Data' in the Meter Editor or directly through its tile.</li>
<li>Allows for detailed data input and validation for specific meters.</li>
</ul>

</div>

<!-- ko:ko-meter-setup-and-data-entry-in-meter-editor block:0 -->
<div class="txt-block" markdown="1">

### Setting Up a Meter

<p>To set up a meter, begin by selecting the presser base and temperature base from the product. The meter factor is typically set to one. After setting these parameters, provide an editor reason to save the setup. You can also configure the meter's operation frequency (hourly, daily, or monthly) and define the contract hour and day, which determine the start time and date for data entry. These settings can be customized or left as system defaults.</p>
<ul>
<li>Select presser base and temperature base from the product.</li>
<li>Set the meter factor, typically to one.</li>
<li>Configure operation frequency (hourly, daily, or monthly).</li>
<li>Define contract hour and day for data entry start time and date.</li>
<li>Settings can be customized or left as defaults.</li>
</ul>

</div>

<!-- ko:ko-meter-setup-and-data-entry-in-meter-editor block:1 -->
<div class="txt-block" markdown="1">

### Entering Analysis Data

<p>Analysis data includes mole percent, mass percent, and liquid volume percent. These values can be manually entered or imported. Alternatively, a source can be created and assigned to the meter. Ensure that the total of these percentages equals 100; otherwise, the system will highlight discrepancies in yellow for correction.</p>
<ul>
<li>Enter or import mole percent, mass percent, and liquid volume percent.</li>
<li>Create and assign a source to the meter if needed.</li>
<li>Ensure total percentages equal 100 to avoid validation errors.</li>
</ul>

</div>

<!-- ko:ko-meter-setup-and-data-entry-in-meter-editor block:2 -->
<div class="txt-block" markdown="1">

### Managing Flow Data

<p>Flow data can be entered for specific months. For example, selecting January will open the grid for that month, with days starting at the defined contract hour. Data can be entered for individual days or for a range of days using the span edit feature. Double-clicking a cell also opens a detailed view for data entry. Characteristics and analysis can be set up directly from this interface as well.</p>
<ul>
<li>Enter flow data for specific months, starting at the contract hour.</li>
<li>Use span edit for bulk data entry or double-click for detailed entry.</li>
<li>Characteristics and analysis can also be configured from this interface.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-meter-data block:0 -->
<div class="txt-block" markdown="1">

### Overview of Data Import Options

<p>Meter data can be imported using various file types, including CFX and text files. The process involves selecting the appropriate meter, specifying the file path, and ensuring the file is correctly formatted. For CFX files, renaming may be required before import. The system provides feedback on the date range of the data being imported.</p>
<ul>
<li>Supports CFX and text file imports.</li>
<li>Requires selecting the meter and specifying the file path.</li>
<li>Provides feedback on the data's date range during import.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-meter-data block:1 -->
<div class="txt-block" markdown="1">

### Manual Data Entry and Editing

<p>Data can also be entered manually through the Meter Editor. Users can select specific records, open detailed windows for flow data or characteristics, and input or modify data for selected time ranges. The system allows for precise control over which records are updated or purged based on user selection.</p>
<ul>
<li>Manual entry is possible for flow data and characteristics.</li>
<li>Users can select specific records and time ranges for editing.</li>
<li>The system supports precise control over data updates and purges.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-meter-data block:2 -->
<div class="txt-block" markdown="1">

### Using the Volume Editor for Data Verification

<p>After importing or manually entering data, users can verify and review the data in the Volume Editor. This ensures that the data aligns with the expected parameters and calculations.</p>
<ul>
<li>Volume Editor is used for data verification.</li>
<li>Ensures data aligns with expected parameters and calculations.</li>
</ul>

</div>

<!-- ko:ko-importing-and-managing-meter-data block:3 -->
<div class="txt-block" markdown="1">

### Pushing and Purging Data

<p>The system allows users to push or purge data for specific time ranges. By selecting records and specifying options, users can control which data is retained or removed. This functionality is essential for maintaining accurate and relevant data sets.</p>
<ul>
<li>Supports pushing and purging data for specific time ranges.</li>
<li>Users can control data retention and removal.</li>
<li>Ensures accurate and relevant data sets.</li>
</ul>

</div>

<!-- ko:ko-importing-data-and-assigning-sources-in-flowcal block:0 -->
<div class="flow-chart">
<div class="flow-root">Importing Data Using Text Files</div>
<ol class="flow-steps">
<li class="flow-step">Meter numbers in text files must match the meter in FLOWCAL.</li>
<li class="flow-step">Batch data indicates a liquid meter text file.</li>
<li class="flow-step">Verify imported data in the Volume Editor.</li>
</ol>
</div>

<!-- ko:ko-importing-data-and-assigning-sources-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Importing Data Using CFX Files

<p>When importing data using CFX files, the meter number does not need to match as the file points to a specific meter. Simply select the file and proceed with the import process.</p>
<ul>
<li>Meter numbers do not need to match for CFX file imports.</li>
<li>CFX files are linked to specific meters.</li>
</ul>

</div>

<!-- ko:ko-importing-data-and-assigning-sources-in-flowcal block:2 -->
<div class="dg-diagram">
<div class="dg-root">Assigning Sources to Meters</div>
<ul class="dg-items">
<li class="dg-item">Sources are based on product composition (e.g., methane, propane).</li>
<li class="dg-item">Sampling the pipeline determines the product composition.</li>
<li class="dg-item">Assign sources to meters, especially when multiple meters share a pipeline.</li>
</ul>
</div>

<!-- ko:ko-setting-up-and-importing-cfx-files-in-the-meter-editor block:0 -->
<div class="flow-chart">
<div class="flow-root">Configuring the Driver for CFX File Import</div>
<ol class="flow-steps">
<li class="flow-step">Navigate to the Meter Editor and open the import tab.</li>
<li class="flow-step">Create a new driver and load the standard CFX driver.</li>
<li class="flow-step">Save the configuration to make the driver available for selection.</li>
</ol>
</div>

<!-- ko:ko-setting-up-and-importing-cfx-files-in-the-meter-editor block:1 -->
<div class="flow-chart">
<div class="flow-root">Importing a CFX File</div>
<ol class="flow-steps">
<li class="flow-step">Select the CFX file in the import tab.</li>
<li class="flow-step">Use the CFX utility to open or create a new CFX file.</li>
<li class="flow-step">Configure the file with meter characteristics and product details.</li>
<li class="flow-step">Ensure product details match the meter setup to avoid errors.</li>
</ol>
</div>

<!-- ko:ko-setting-up-and-importing-cfx-files-in-the-meter-editor block:2 -->
<div class="flow-chart">
<div class="flow-root">Running the Import Service</div>
<ol class="flow-steps">
<li class="flow-step">Run the import service after setting up the CFX file.</li>
<li class="flow-step">The service will process the file, import data, and rename the file.</li>
<li class="flow-step">Imported data will be stored in the database.</li>
</ol>
</div>

<!-- ko:ko-revision-tracking-and-cfx-file-import-in-meter-editor block:0 -->
<div class="txt-block" markdown="1">

### Revision Tracking in Meter Editor

<p>Revisions in the Meter Editor are automatically incremented as changes are made. Each revision is captured with a sequence number, where '0' represents the original data, and negative numbers (-1, -2, etc.) represent subsequent changes. For example, if a key factor is changed or a contract hour is updated, these changes are reflected in new revisions. The data is stored in specific tables, such as the periodic table for flow data and characteristics tables for other parameters.</p>
<ul>
<li>Revisions are tracked with sequence numbers.</li>
<li>Original data is marked as '0', and changes are marked with negative numbers.</li>
<li>Changes are stored in specific database tables for verification.</li>
</ul>

</div>

<!-- ko:ko-revision-tracking-and-cfx-file-import-in-meter-editor block:1 -->
<div class="flow-chart">
<div class="flow-root">Importing CFX Files Using Service Configuration</div>
<ol class="flow-steps">
<li class="flow-step">Service login credentials must be correctly configured.</li>
<li class="flow-step">Set the path to the folder containing CFX files in the service configuration.</li>
<li class="flow-step">Use the Meter Editor's import tab to select and import files.</li>
</ol>
</div>

<!-- ko:ko-assigning-sources-and-validating-meter-data block:0 -->
<div class="flow-chart">
<div class="flow-root">Assigning Sources to Meters</div>
<ol class="flow-steps">
<li class="flow-step">Set the effective date before assigning a source.</li>
<li class="flow-step">The system flags missing or incorrect sources.</li>
<li class="flow-step">Volume recalculates automatically after source assignment.</li>
<li class="flow-step">Edits to the source can be made in the Source Editor.</li>
</ol>
</div>

<!-- ko:ko-assigning-sources-and-validating-meter-data block:1 -->
<div class="txt-block" markdown="1">

### Understanding Meters and Their Data

<p>Meters are physical devices installed in specific locations, such as pipelines or extraction sites, to measure flow volumes. Each meter has a unique identity, ensuring no duplicates in the system. Meters measure data like temperature and pressure, which are used to calculate volume. Issues like frozen meters or incorrect readings are captured in the flow computer and can be addressed during data validation.</p>
<ul>
<li>Meters are physical devices with unique identities.</li>
<li>They measure flow data like temperature and pressure.</li>
<li>Issues such as frozen meters or missing data are captured in the flow computer.</li>
</ul>

</div>

<!-- ko:ko-assigning-sources-and-validating-meter-data block:2 -->
<div class="txt-block" markdown="1">

### Data Validation in FLOWCAL

<p>FLOWCAL validates measurement data by importing files from flow computers, such as CFX files. It checks for anomalies, such as unexpected temperature readings, and flags exceptions for technicians to address. Once the data is validated and corrected, it is ready for further processing.</p>
<ul>
<li>FLOWCAL imports data from flow computers for validation.</li>
<li>Anomalies like unexpected temperature readings are flagged.</li>
<li>Technicians correct flagged issues before finalizing data.</li>
</ul>

</div>

<!-- ko:ko-monthly-data-validation-and-closing-process block:0 -->
<div class="txt-block" markdown="1">

### Overview of Monthly Data Validation

<p>Technicians validate monthly data by reviewing it for correctness. If the data appears accurate, they proceed to close the month. However, the system enforces rules to ensure no unresolved exceptions exist before closing.</p>
<ul>
<li>Technicians review and validate monthly data.</li>
<li>The system prevents closing if there are unresolved exceptions.</li>
<li>Validation ensures data accuracy before finalizing the month.</li>
</ul>

</div>

<!-- ko:ko-monthly-data-validation-and-closing-process block:1 -->
<div class="txt-block" markdown="1">

### Handling Exceptions in Monthly Data

<p>Exceptions, such as unreasonable meter temperatures, are flagged by the system. These exceptions must be resolved before the month can be closed. For example, if a temperature value is flagged as incorrect, the system will highlight it and prevent the month from being closed.</p>
<ul>
<li>Exceptions are flagged when data appears incorrect.</li>
<li>Unresolved exceptions block the closing of the month.</li>
<li>Highlighted exceptions indicate areas requiring attention.</li>
</ul>

</div>

<!-- ko:ko-monthly-data-validation-and-closing-process block:2 -->
<div class="flow-chart">
<div class="flow-root">Steps to Close a Month</div>
<ol class="flow-steps">
<li class="flow-step">Navigate to 'Close Schedule' to initiate the closing process.</li>
<li class="flow-step">Only past months can be closed; current and future months are restricted.</li>
<li class="flow-step">Closed months are marked as finalized and locked for edits.</li>
</ol>
</div>

<!-- ko:ko-monthly-data-validation-and-closing-process block:3 -->
<div class="txt-block" markdown="1">

### Visual Indicators for Closed Months

<p>After a month is successfully closed, the system marks it with a blue indicator. This signifies that the data for that month is finalized and cannot be modified unless specific approval settings are in place.</p>
<ul>
<li>Closed months are visually marked with a blue indicator.</li>
<li>Finalized data cannot be edited without approval settings.</li>
</ul>

</div>

<!-- ko:ko-closing-and-editing-meters-in-flowcal block:0 -->
<div class="flow-chart">
<div class="flow-root">Closing a Meter</div>
<ol class="flow-steps">
<li class="flow-step">Closed meters are marked with a blue indicator.</li>
<li class="flow-step">Closed meters cannot be edited unless approval settings are enabled.</li>
</ol>
</div>

<!-- ko:ko-closing-and-editing-meters-in-flowcal block:1 -->
<div class="flow-chart">
<div class="flow-root">Handling Exceptions During Closing</div>
<ol class="flow-steps">
<li class="flow-step">Exceptions must be resolved before closing a meter.</li>
<li class="flow-step">Use the 'Exception Resolver' and 'Volume Editor' to address issues.</li>
</ol>
</div>

<!-- ko:ko-closing-and-editing-meters-in-flowcal block:2 -->
<div class="flow-chart">
<div class="flow-root">Editing Closed Meters</div>
<ol class="flow-steps">
<li class="flow-step">Editing closed meters requires configuring approval settings.</li>
<li class="flow-step">Approval modes include 'Not Allowed', 'Apply Without Approval', and 'Approval Required'.</li>
<li class="flow-step">Users must belong to the assigned approval group to approve changes.</li>
</ol>
</div>

<!-- ko:ko-closing-and-editing-meters-in-flowcal block:3 -->
<div class="txt-block" markdown="1">

### Relaunching FLOWCAL After Configuration Changes

<p>After making updates to system configurations, it is recommended to relaunch FLOWCAL to ensure that changes are properly applied. This step is necessary as updates may not always take effect immediately.</p>
<ul>
<li>Relaunch FLOWCAL after system configuration changes.</li>
<li>This ensures updates are applied correctly.</li>
</ul>

</div>

<!-- ko:ko-managing-ppa-and-exporting-meter-data block:0 -->
<div class="flow-chart">
<div class="flow-root">Clearing PPA to Open Meters</div>
<ol class="flow-steps">
<li class="flow-step">Meters with PPA cannot be opened until the PPA is cleared.</li>
<li class="flow-step">Use the 'Parse PPA' option to remove the PPA.</li>
<li class="flow-step">Edits to meters queue them for roll-up to update daily and monthly data.</li>
</ol>
</div>

<!-- ko:ko-managing-ppa-and-exporting-meter-data block:1 -->
<div class="flow-chart">
<div class="flow-root">Exporting Meter Data</div>
<ol class="flow-steps">
<li class="flow-step">Export meter data by selecting the meter, date range, and granularity.</li>
<li class="flow-step">Save the exported data in a text file format.</li>
<li class="flow-step">Exported files can be reused for importing data.</li>
</ol>
</div>

<!-- ko:ko-managing-ppa-and-exporting-meter-data block:2 -->
<div class="txt-block" markdown="1">

### Importing Meter Data

<p>To import meter data, ensure the text file follows the required format. The format includes specific headers and data structure. Documentation and sample files for the import format are available for reference. Properly formatted files can be used to import meter or ticket data.</p>
<ul>
<li>Import files must follow a specific format with headers and structure.</li>
<li>Sample files and documentation are available for reference.</li>
<li>Formatted files can be used to import meter or ticket data.</li>
</ul>

</div>

## See Also

- (none yet)
