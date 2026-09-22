# <span id="aanchor209"></span> <span id="aanchor210"></span> Ticket Editor

Use the Ticket Editor to view, create and edit standalone tickets and view batch data.

Three ticket types are available in FLOWCAL:

- Meter batch tickets
- Tickets associated with a location
- Standalone tickets

Standalone tickets can be applied to a location directly. These can be used for blowdowns where there is not a measurement point or trucks being loaded from a tank among other things.

<div class="procedure">

To view and edit tickets:

1.  Go to **Open** \> **Tickets** \> **Ticket Editor**.
2.  Select a date range and click **Open**. All tickets for the selected time frame will display.
    - Double-click a location or standalone ticket to access the [Ticket Details](Ticket%20Details/Ticket%20Details%20Editor.md) screen.

    - Double-click a batch ticket to access the [Batch Details](../Volume%20Editor/Batch%20Tab.md#BatchDetail) screen, or right-click a batch ticket to access the [Volume Editor](../Volume%20Editor/Volume%20Editor.md).

      If you access the Batch Details screen from the Ticket Editor, and then edit the batch data, the edit will only apply to that batch and its selected underlying periodics. Because of this, the effective dates for flow data, characteristics and analysis are read-only.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Details">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Ticket Editor Screen Details</a>

<div class="drop-down" style="display: none;" mc-target-name="Details">

The following items are available on the Ticket Editor screen:

- **Date/Time Span Selector** - Limit the tickets returned by the search to those with an effective date in the specified range. Click the refresh button to reload the tickets within that range to view the most current data.

- **Ticket Type Selector** - Select the type of tickets to view. Select Batch Meter to view batch data for all of the pipeline meters. Select Undefined tp view custom ticket types or ticket types that were not recognized during TFX import.

  Tank Run, Tank Gauge Level, and Inventory Empty Ticket Types require a license for the Liquids Inventory Module.

- **Grid** - Displays data for tickets that fit the specified date and type criteria. Changes made to ticket details will be reflected in the grid automatically. Refresh the view to see changes made by other users or processes.

- **Data Type tabs** - Sub-categories of ticket information. All tickets have the following tabs: Measurement, Analyses, Accounting, Components, Net Allowable, Custom Fields, and Close Data. Meter tickets also have a Configuration tab. Click the arrow buttons to the far right to access tabs that may be cut off or hidden.

##### Right-Click Menu Options

- **New Ticket** - Creates a new Ticket of the Type currently selected. If this option is selected and a Default Autofill Profile has been set for that Ticket Type, then the ticket is automatically populated with the default fields for the default profile.

- **New From Profile** - When this option is hovered over, a sub-menu displays the Profile Name of all Autofill Profiles for the corresponding Ticket Type. Once an Autofill Profile is selected, a new ticket is automatically populated with the default values for that profile. (See: [Ticket Autofill Editor](Ticket%20Autofill%20Editor.md))

- **Delete Ticket** - This option allows the user to delete the selected ticket.

  Closed tickets cannot be deleted from within the Ticket Editor or Ticket Search screens as they have already been processed.

- **Attach Analysis** - This option allows the user to attach a standalone sample or source analysis to a ticket.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Edit to Original">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Edit to Original</a>

<div class="drop-down" style="display: none;" mc-target-name="Edit to Original">

Right-click a ticket and select Edit to Original to reapply the original data to the ticket. This edit will display as a new revision, but will contain only the original data. This process can be applied to multiple tickets; any tickets that cannot be updated will be flagged.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Prior Period Adjustments">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Prior Period Adjustments</a>

<div class="drop-down" style="display: none;" mc-target-name="Prior Period Adjustments">

A PPA is automatically created when a new ticket is attached to a location and the effective date occurs in a measurement month when the location is closed. If a PPA is automatically created during import, a location-level message is generated. If the System PPA option is set to "Not Allowed", the ticket will not import, and a location-level message is generated.

</div>

#### See also:

- [Ticket Details Editor](Ticket%20Details/Ticket%20Details%20Editor.md)
- [Ticket Types](../Settings%20Manager/Liquids/Ticket%20Types.md)
- [Cavern Inventory Tickets](../Liquid%20Cavern%20Editor/Liquid%20Cavern%20Editor.md#CavernTickets)
- [Tank Tickets](../Tank%20Editor/Flow%20Data/Tank%20Editor_Flow%20-%20Tickets.md)
- [Ticket Validations](../Locations/Location%20Editor/Tools%20-%20Ticket%20Validations.md)
