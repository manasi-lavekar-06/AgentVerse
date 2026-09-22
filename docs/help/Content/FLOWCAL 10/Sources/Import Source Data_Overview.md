# <span id="aanchor454"></span> Import Source Data

Several options are available for importing quality source data, varying based on data type and import format.

#### General Data

General source attributes, characteristics, and validations as seen in the Quality Source Editor can be populated using the following methods:

- Manual entry through the Quality Source Editor
- Bulk edits through the Bulk Changes screen
- Bulk imports using the FcLoader utility

#### Source Analysis Data

Source analysis can be imported using the following methods:

- Manual or automatic file imports (such as source text files or imported with meter data)
- Manual data entry
- Transaction Queue import

#### Manual File Imports

- **Source Text Files** - When a lab supplies analysis data in Quroum’s Source Text File format, the files can be manually imported from the **Import** \> **Source Analysis Text File** menu. Once imported, the data is applied to all assigned meters. (See: [Import Source Analysis Text File](../Imports/Import%20Source%20Analysis%20Text%20File.md))

- **Import with Meter Data** - When analysis data is supplied with the meter data, such as in a CFX file, the meter/source assignment can be configured to send the analysis from the meter to the source where it can then be applied to other assigned meters.

  Most files imported into FLOWCAL are in Quorum’s proprietary file format. A signed non-disclosure agreement (NDA) must be on file to receive these file formats. Contact <a href="mailto:flowcal.support@quorumsoftware.com" class="notelink">Customer Support</a> to obtain the appropriate NDA.

#### Automatic File Imports

The File Import service is a Windows service that can be installed on the application server where FLOWCAL is installed. The service automatically processes import files based on the file path specified within FLOWCAL. The service can be used to import different file types, such as source analysis text files and CFX files.

#### Manual Data Entry

Source data can be entered manually in the Quality Source Editor by selecting the **Source Analysis** tab and clicking the **New Detail** button.

#### Transaction Queue

Transaction Queue provides an alternative to file imports and can be used to import online chromatograph data into FLOWCAL on a near real-time basis. The data is written to the database from SCADA or other intermediate solution. The Transaction Queue service monitors the Transaction Queue tables and imports the data into the appropriate source. The source data is then queued to be applied to all assigned meters.

Contact <a href="mailto:flowcal.support@quorumsoftware.com" class="InlineLink">Customer Support</a> for additional information about Transaction Queue.

This feature requires the Online Transaction Processing module.

 

#### See also:

- [Create &amp; Delete Sources](Create-Delete%20Sources.md)
- [View Source Data](View%20Source%20Data.md)
- [Edit Source Data](Edit%20Source%20Data.md)

</div>
