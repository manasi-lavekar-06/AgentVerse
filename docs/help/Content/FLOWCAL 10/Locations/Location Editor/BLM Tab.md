# <span id="aanchor307"></span> Location Editor

[&lt;&lt; Back](Location%20Editor.md#Location_Editor_Tabs) \| [Members](Members%20Tab.md) \| [Active Status](Active%20Status%20Tab.md) \| [Characteristics](Characteristics%20Tab.md) \| [Edit Reasons](Edit%20Reasons%20Tab.md) \| [Close Group](Close%20Group%20Tab.md) \| [Site](Site%20Tab.md) \| <a href="#" class="ExceptionHeading selected">BLM</a>

## BLM Tab

The BLM tab contains BLM-specific data points. The options on this tab determine how FLOWCAL handles verifications and reports generated for this location.

- **BLM Property** - Designates the location as a BLM property. When set to “Yes”, the other fields available on this tab become visible and editable.
- **FMP Number** - The BLM-approved facility measurement point (FMP) where oil or gas produced from a Federal or Native American lease, unit PA, or CA is measured; this measurement affects the calculation of the volume or quality of production on which royalty is owed. Required field if the BLM Property identifier is set to "Yes".

<!-- -->

- **Lease Number** - The number assigned to the lease location where the production occurs.
- **CA Number** - Communitization agreement (CA) number identifying an agreement to combine a lease or a portion of a lease with other tracts for purposes of cooperative development and operations, when the initial lease cannot be independently developed and operated in accordance with established well spacing or well development programs.
- **PA Number** - Participating area (PA) number representing a combined portion of the unitized area that BLM determines to be reasonably proven to produce geothermal resources or that supports production in commercial quantities, such as pressure support from injection wells; the size and configuration of all participating areas and revisions are not effective until BLM approves them.
- **FMP Tier** - A volume rate designation for this location; higher volume rates have more stringent operating requirements.

Designations for locations are as follows:

> - **High Volume:** ≥ 30,000 bbl/month (default)
> - **Low Volume:** \< 30,000 bbl/month

FMP Tier dictates how validations are triggered; locations are defaulted to High Volume as this is the most stringent designation and will require the most attention from the producer, therefore ensuring compliance.  
  
FMP Number, Lease Number, CA Number, and FMP Tier are shown on select reports designed specifically for BLM reporting requirements.
