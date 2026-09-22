# <span id="aanchor176"></span> Location Close Revisions

Volume, mass, volume and mass inventory, and component volume and mass inventory data are stored whenever a location is closed through the location [Close Approval](Close%20Approval.md) screen. This allows for a closed location to have a revision number stored and manually incremented by a user.

When it first opens, the Location Close Revisions screen displays the stored volume, mass, inventory, and component data in the units that are selected on the Location Close Approval screen. The user may then select to have the values displayed in either Measured or Standard units.

In the top row, the current rolled-up data for the selected location and month is displayed. In the bottom grid, all revision records for the selected location and month are displayed, including the revision number for each record.

Users can select and right-click on a single row in the bottom grid to bring up a pop-up menu from which they can choose to print the Location Inventory Ticket report for that row to display the appropriate data for the revision.

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Generating a Revision Number">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Generating a Revision Number</a>

<div class="drop-down" style="display: none;" mc-target-name="Generating a Revision Number">

The New Revision button on the Location Close Revisions screen is enabled when all rollup operations for the selected location and month are complete and the current rolled-up values differ from the latest revision in any of the stored fields, e.g. due to a PPA. The user privilege required for this button is the same as for approving a location to be closed. When the button is clicked, the current values are stored in the database with a revision number.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Location Messages">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Locations Messages for Inventory Changes after Close Approval</a>

<div class="drop-down" style="display: none;" mc-target-name="Location Messages">

When the Location Rollup Service rolls up a location month that has been closed, and if the values that have just been rolled up differ from the latest revision stored in the database, a location exception message is generated. When multiple data columns differ, FLOWCAL decides which column data to display using the following priority:

- Sum of component volume
- NSV
- GSV
- Mass
- Individual component volume and mass

The location exception message is generated effective the beginning of the month at contract hour with a default priority of 0. The user can adjust the priority of the exception message as desired.

A new message is generated only when there are no unacknowledged messages for the same measurement month. Upon creating a new revision, any existing unacknowledged messages for the location and measurement month becomes acknowledged.

</div>
