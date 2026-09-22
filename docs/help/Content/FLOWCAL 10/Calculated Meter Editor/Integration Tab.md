# <span id="aanchor346"></span> Calculated Meter Editor

[&lt;&lt; Back](Calculated%20Meter.md#Tabs) \| [Relationship](Relationship%20Tab.md) \| [General](General%20Tab.md) \| [Custom Fields](Custom%20Fields%20Tab.md) \| [Reports](Reports%20Tab.md) \| [Misc.](Misc%20Tab.md) \| [Audits](Audits%20Tab.md) \| [Operations](Operations%20Tab.md) \| [Liquids](Liquids%20Tab.md) \| [Formulas](Formulas%20Tab.md) \| <a href="#" class="selected">Integration</a>

## Integration Tab

The Integration tab contains data points required for linking a meter with the Quorum ecosystem via the Quorum Enterprise Integration (QEI) platform.

You can use the [FcLoader utility](../Admin%20Options/FcLoader.md) to import the following values in bulk:

- Integrated
- Facility (code)
- Integration ID

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Details">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Data Field Details</a>

<div class="drop-down" style="display: none;" mc-target-name="Details">

- **Integrated** - When set to "Yes", the meter is designated as being integrated or linked to the Quorum ecosystem. Data is expected to flow from FLOWCAL automatically and transparently to other Quorum integrated applications. An example of this integration is data flowing from FLOWCAL to TIPS. When set to "Yes", the following data will be automatically sent to the Integration Platform when data changes due to imports or edits:

  - Meter Header/Configuration
  - Volumes (Hourly, Daily, Monthly)
  - Analysis (Hourly, Daily, Monthly)

  The following Meter Editor data points must be populated before an Integrated meter can be saved:

  - Facility
  - Integration ID
  - State
  - County

  This option must be set to "Yes" for other options on this tab to be enabled.

- **Facility** – Allows the user to select a facility from the list of facilities designated as Integrated. This data point is necessary to properly identify a meter across the Quorum ecosystem.

- **Integration ID** – Allows the user to enter a unique ID that is necessary to properly identify a meter across the Quorum ecosystem.
  - Must be a unique value among all other existing Integration IDs
  - Maximum length is 10 characters

</div>

</div>
