# <span id="aanchor217"></span> Import Meter Data

#### General Data

General meter information as seen on the Meter Editor can be populated using the following methods:

- Manual entry through the [Meter Editor](Meter%20Editor/Meter%20Editor.md)
- Bulk edits through the Bulk Changes screen
- Bulk imports using the [FcLoader](../Admin%20Options/FcLoader.md) utility

#### Flow Data

Meter volumes, characteristics, and analysis can be imported using the following methods:

- Manual or automatic file imports (such as text file, CFX, or other FLOWCAL supported file type)
- Manual data entry
- Transaction Queue import

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Manual File Imports">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Manual File Imports</a>

<div class="drop-down" style="display: none;" mc-target-name="Manual File Imports">

The following table lists the various screens available for importing meter volumes, characteristics and analyses:

| Screen | Description |
|:---|:---|
| [Meter Data](../Imports/Meter%20Data/Import%20Meter%20Data.md) | Import gas or liquid meter data in the form of a CFX file, which can contain meter flow history, meter configuration, events, alarms, product information and/or analysis data. Access other FLOWCAL meter import drivers from the Driver drop-down on this screen. |
| [Meter Text File](../Imports/Meter%20Data/Import%20Meter%20Text%20File%20-%20Gas.md) | Import gas or liquid meter data for a single meter or multiple meters using Quroum’s proprietary text file format. |
| [Prove Data](../Imports/Import%20Prove%20Data.md) | Import prove data in the form of a PFX created by PROVEit or an external SCADA system. |
| [Lab Analysis](../Imports/Lab%20Analysis/Import%20Lab%20Analysis.md) | If you do not have the Source Analysis module, use the Import Lab Analysis screen to import gas analysis sample data that uses the lab analysis text file format. |

 

Most files imported into FLOWCAL are in Quorum’s proprietary file format. A signed non-disclosure agreement (NDA) must be on file to receive these file formats. Contact <a href="mailto:flowcal.support@quorumsoftware.com" class="notelink">Customer Support</a> to obtain the appropriate NDA.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Automatic File Imports">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Automatic File Imports</a>

<div class="drop-down" style="display: none;" mc-target-name="Automatic File Imports">

The File Import service is a Windows service that can be installed on the application server where FLOWCAL is installed. The service automatically processes import files based on the file path specified within FLOWCAL. The service can be used to import different file types, such as meter text files and CFX files.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Manual Data Entry">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Manual Data Entry</a>

<div class="drop-down" style="display: none;" mc-target-name="Manual Data Entry">

Flow data, meter characteristics, and meter analyses can be entered manually in the Volume Editor. You can also manually enter data for other types of meters from various Import screens.

This data is rolled up into hourly, daily and monthly records, which can then be seen from the Meter/Location Rollup Viewer. This rolled data is primarily used for reporting externally and internally to other departments and downstream systems.

The following table lists the various screens available for manually entering meter volumes, characteristics or analyses:

| Screen | Description |
|:---|:---|
| Manual Entry \> [Meter Input](../Imports/Manual%20Entry/Manual%20Meter%20Input.md) | Manually enter data for external volume meters (designated within the Meter Editor). |
| Manual Entry \> [PD Entry By List](../Imports/Positive%20Displacement/Positive%20Displacement%20Entry%20by%20List.md) | Quickly enter index readings for positive displacement and turbine meters. |
| Manual Entry \> [Planimeter](../Imports/Manual%20Entry/Manual%20Planimeter%20Entry.md) | Calculate the process variable for differential pressure, static pressure, and temperature for a specific meter for a specified date. |

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Transaction Queue">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Transaction Queue</a>

<div class="drop-down" style="display: none;" mc-target-name="Transaction Queue">

Transaction Queue provides an alternative to file imports and can be used to import data into FLOWCAL on a near real-time basis. The data is written to the database from SCADA or other intermediate solution.

Contact <a href="mailto:flowcal.support@quorumsoftware.com" class="notelink">Customer Support</a> for additional information about Transaction Queue.

</div>

</div>
