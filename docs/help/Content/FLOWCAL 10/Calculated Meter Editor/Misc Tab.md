# <span id="aanchor335"></span> Calculated Meter Editor

[&lt;&lt; Back](Calculated%20Meter.md#Tabs) \| [Relationship](Relationship%20Tab.md) \| [General](General%20Tab.md) \| [Custom Fields](Custom%20Fields%20Tab.md) \| [Reports](Reports%20Tab.md) \| <a href="#" class="selected">Misc.</a> \| [Audits](Audits%20Tab.md) \| [Operations](Operations%20Tab.md) \| [Liquids](Liquids%20Tab.md) \| [Formulas](Formulas%20Tab.md) \| [Integration](Integration%20Tab.md)

## Misc. Tab

Most of the items listed are informational fields about the meter. Meter Type, Meter Make, and Default Temperature are retrieved from the meter characteristics table for the current characteristic and are read-only. The user can enter other details about the meter such as the Serial Number, Site ID, Power Source, Pressure Mode, and Temperature Mode.

- **Last Modified** - Read-only field that shows the last user that edited the meter within the Meter Editor and the datetime that it was edited. This could be something as simple as a Custom Fields update.

- **Existing Data** - Read-only field that shows the meter’s Creation Date (first date that the meter's data was imported into FLOWCAL), Unarchived Data Start (date of the first data record in the database for the meter) and Unarchived Data End (date of the last data record in the database for the meter).

  The Unarchived Data End should not exceed the current datetime.

- **First Flow** - These fields are utilized to notify a contact when the meter begins to flow. The analyst manually enters the date once they have confirmed real flow within the Volume Editor. A notification email is then sent to the Contact Type set up in the Notify field.

</div>
