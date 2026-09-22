# Location Editor

[&lt;&lt; Back](Location%20Editor.md#Location_Editor_Menus) \| [Location](Location%20Menu.md) \| <a href="#" class="ExceptionHeading selected">Tools</a> \| [Data](Data%20Menu.md)

## Tools Menu

The following options are available on the Tools menu in the Location Editor:

- **Contact Selection** - Contact Relationships can be designated for meters, sources, and locations.

The user can associate specific contacts (email addresses) to a location. Exceptions and messages logged for the location will automatically be emailed to the associated contacts for exceptions and messages set up for the contact type.

- **Location Validations** - When a location is rolled up, if validations are enabled, an exception will be logged if the value is outside the range defined. (See: [Location Validations](Tools%20-%20Location%20Validations.md))
- **Ticket Validations** - If validation templates are attached to a location, all tickets attached to that location will be validated and exceptions will be logged if a value is outside of the range defined. (See: [Ticket Validations](Tools%20-%20Ticket%20Validations.md))
- **Info**

> - **Fluid Phase** – This field is set when the location is created and cannot be changed.
>
>   The selected fluid phase does not affect which data is rolled up or calculated at the location level. All data is calculated and rolled up the same way, regardless of Fluid Phase. The location’s fluid phase only affects how the Meter/Location Rollup Viewer initially displays the location. If you select "Gas", the location will initially display with the Measured tab selected. If you select "Liquid", then the location will initially display with the Liquid Flow Data tab selected. Some tabs displayed in the Meter/Location Rollups Viewer will also vary depending on which fluid phase is selected.
>
> - **Measurement Area** - Select a Measurement Area from the drop-down or, with System Information privileges, click new and create a new Measurement Area.
>
> - **Custom Fields** – These fields are not datetime effective. Labels can be user-defined. (See: [Define Custom Field Labels](../../Admin%20Options/Create%20User-Defined%20Fields.md))
>
> - **Notes** - The notes stored on the Info screen are only available from the Location Editor Info menu. For notes that can be accessed throughout the application (e.g. Volume Editor), right-click on the Location Editor screen to add or view notes.
>
> - **Requires Close Approval** - Indicator that flags locations that must satisfy a set of conditions before they can be closed; these locations are then closed manually through the Location Close Approval screen.
>
>   For a location to be closed manually, all location members (meter and location) must be closed first.
>
> - **Weekly Schedule** - This drop-down contains schedules created in the Annual Schedule Editor; location rollups will calculate totals for the location according to the date spans defined by this schedule. Although called Weekly Schedule, the span does not have to be for a week.
>
>   <div class="example">
>
>   <a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerBRDToggler MCTogglerHotSpot_ MCTogglerHotSpot_BRDToggler MCHotSpotImage" data-mc-targets="Example">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Example</a>
>
>   A ticket schedule can be assigned to a location, tank, inventory, liquid cavern, or comparison. This allows for location rollups to calculate values that span multiple days, but less than a month per the defined schedule.
>
>   </div>
>
>   Enable the Calculate Weekly Totals option in System Configuration to make the Weekly Schedule option visible for the locations in that system. Turning on this functionality will greatly increase the size of the user's database.
>
> - **Efficiency Options** – Determine how location rollups calculate efficiency for segment or balance locations; efficiency definition must be configured in the Efficiency Definition Editor, and Subtotal by Meter Direction and Subtotal by Meter Class options must be enabled in FLOWCAL Configuration.
>
>   - **Calculate Energy Efficiency** - Energy efficiency is calculated and displayed in Rollup Viewer, Daily Location Rollups Viewer, and Monthly Location Rollups Viewer.
>   - **Calculate Plant Recovery Efficiency** - Plant recovery efficiency is calculated and displayed in the Recovery Analysis Viewer.
>   - **Calculate System Recovery Efficiency** - System recovery efficiency is calculated and displayed in the Recovery Analysis Viewer.
>
>   If both plant and system recovery efficiencies are calculated, the system recovery values will be displayed.
>
> - **Ticket Import** - Ticket import options are used to enable adjustment of ticket dates for daylight savings time or for time zone. When these options are enabled, dates on all tickets that are imported into the location via TFX or FLOWCAL text file format are adjusted. (See: [Date and Time Adjustments During Import](../../Meters/Meter%20Editor/Date%20and%20Time%20Adjustments%20During%20Import.md))
>   - **Time Zone Shift** - When enabled, all dates and times are adjusted by the offset amount defined for the selected time zone. (Time zones are created using the Time Zone Editor.) For these purposes the time zone offset is to be user-configured based on the offset from the company's standard business time zone rather than offsets from UTC.
>   - **DST Shift** - When enabled, all dates and times occurring during daylight saving time are shifted forward one hour. All dates and times that occur outside of daylight saving time are imported.
>   - **Time Zone** - This read-only field displays the current time zone of the location as defined on the Site tab of the Location Editor.
>
> - **Scheduled Batch Movements** – See: [Scheduled Batch Movement](../../Imports/Scheduled%20Batch%20Movement/Scheduled%20Batch%20Movement.md)

- **Validate Hierarchy** - The Validate Hierarchy tool assists users in troubleshooting issues. The user opens the Validate Hierarchy tool from the Location Editor, then chooses the validation options to run: Show Invalid Tieover, Show Invalid Transfers, Validate Throughput as Tieover, and Show Unused Meters.
- **Find Parent Locations** - The Find Parent Locations tool can be used to find a location/meter within a large hierarchy, or find all locations that a location/meter belongs to. From the Location Editor Tools menu, select Find Parent Locations and enter part or all of the object number into the filter. Select the object number you are looking for from the left pane. The Right pane will show the locations that the meter is a member of.
- **Product Conversion** - Product Conversion opens the Ticket Editor with Ticket Type defaulted to Product Conversion to allow entry of conversion products, quantity converted, and accounting and analysis information. The result is two tickets, one which reduces the inventory of the “From” product and one that increases the inventory of the “To” product.
