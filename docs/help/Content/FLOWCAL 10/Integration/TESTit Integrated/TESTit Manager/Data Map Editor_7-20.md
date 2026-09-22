# <span id="aanchor460"></span> Data Map Editor

The Data Map Editor allows the user to set up and save data mappings of TESTit fields into FLOWCAL fields when TESTit Test Reports are imported into FLOWCAL.

This functionality is only available with TESTit 2 integration.

<div class="procedure">

To access the Data Map Editor:

1.  From the FLOWCAL main menu, go to **Setup** \> **TESTit Manager** \> **Data Map Editor**.

2.  Note that the FLOWCAL objects on the right (Meter, GQSource, Contact, and Company) only have the following update options:
    - **Create** - Create the object in FLOWCAL if it does not already exist

      Users can select to have the business status set to Pending Create for meters that are created by the TESTit Import service. Meter status is not affected by this option. If a meter is created by TESTit Import, the meter status will default to "In Service/Active".

    - **Ignore** - Ignore the object (will not be created)

    - **Report** - Create a system message indicating that the unknown meter was not created

3.  Contacts and customers can also be imported from TESTit, but individual columns are not mapped. You can set customers/contacts to either report, ignore, or create.

4.  Drag and drop TESTit fields from the left side onto the destination FLOWCAL field on the right side.

    Supported fields include those from the FC_METER, FC_METER2, FC_METER_CHARACTERISTIC, FC_GQ_SOURCE, and FC_GQ_SOURCE_CHARACTERISTIC tables.

5.  After a field is mapped, the user needs to choose import options for each field mapped. On the far right is the update option. TESTit data can update the field it is mapped to by replacing data with values or values & nulls. The ignore option will allow the field to be compared without updating any information in FLOWCAL. When the Compare checkbox is selected, the FLOWCAL values will be compared to those being imported from TESTit. If the values do not match an exception is created

</div>

## Additional Mappings

The default mapping affects any import in the main import path. Users can create multiple mappings by clicking new at the top of the data map editor. All user created mappings must be named something other than Default Mapping. The import service will create a sub folder in the main import path with the same name as the user-created mapping configuration in FLOWCAL. The import service will import TSX files from these subfolders using that mapping configuration.
