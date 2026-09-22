# <span id="aanchor105"></span> Create & Delete Sources

Gas or liquid sources can be created in FLOWCAL manually or automatically via file imports. Following a new implementation of FLOWCAL, merger, or other type of data acquisition, many sources may need to be created in bulk. Other times, analysts may need to create a handful of sources periodically.

This feature requires the Source Analysis module.

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Manually Creating Sources">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Manually Creating Sources</a>

<div class="drop-down" style="display: none;" mc-target-name="Manually Creating Sources">

In FLOWCAL, you can manually create sources from the Quality Source Editor screen.

<div class="procedure">

To create a **gas** quality source:

1.  Go to **Setup** \> **Source Analysis** \> **Gas Quality** and click the **New** button, or go to **File** \> **New** from the Gas Quality Source Editor menu.
2.  Populate required data fields (highlighted in green). These fields must be populated before you can save the source record.

By default, the only required field to save a new gas quality source is Source Number and Reason. Additional fields may be required based on how FLOWCAL options are configured.

1.  Enter any additional source information and click **Save**.

To create a **liquid** quality source:

1.  Go to **Setup** \> **Source Analysis** \> **Liquid Quality** and click the **New** button, or go to **File** \> **New** from the Liquid Quality Source Editor menu.
2.  Populate required data fields (highlighted in green). These fields must be populated before you can save the source record.

By default, the only required field to save a new gas quality source is Source Number and Reason. Additional fields may be required based on how FLOWCAL options are configured.

1.  Enter any additional source information and click **Save**.

</div>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Automatically Creating Sources">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Automatically Creating Sources</a>

<div class="drop-down" style="display: none;" mc-target-name="Automatically Creating Sources">

The “Auto Create Sources” options allow you to automatically create sources during data import using Quorum’s proprietary source text file format or Transaction Queue. These options must be configured under the Service Configuration screen.

- **Text Files** - When the “Auto Create” option for Sources is enabled, sources imported by text file using the Import \> Source Analysis Text File screen will be created automatically if they do not already exist. (See: [Import Source Analysis Text File](../Imports/Import%20Source%20Analysis%20Text%20File.md))

  You can also use the File Import service to automatically import source text files and create sources.

- **TESTit Integrated** - Sources can also be created automatically using TESTit Integrated.

  This feature requires TESTit Integrated.

- **T3** - This feature is not supported with TESTit V3 Integrated.

- **T2** - When you set the Update column to Create for GQSource on the Data Map Editor, sources will be created automatically when test reports are imported.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Bulk Creating Sources">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Bulk Creating Sources</a>

<div class="drop-down" style="display: none;" mc-target-name="Bulk Creating Sources">

A new FLOWCAL implementation or data acquisition can require the creation of hundreds or thousands of sources. The FcLoader utility is available for creating sources in bulk. FcLoader ships with FLOWCAL and is located in the installation folder.

A signed non-disclosure agreement (NDA) must be on file to receive the source text file, FcLoader, and Transaction Queue file formats. Contact <a href="mailto:flowcal.support@quorumsoftware.com" class="notelink">Customer Support</a> to obtain the appropriate NDA.

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Copying Sources">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Copying Sources</a>

<div class="drop-down" style="display: none;" mc-target-name="Copying Sources">

You can also create a source by making a copy of an existing source. Users will often create a set of default sources to use as the basis for new sources, so that certain settings or custom fields are automatically specified in the new source. You can copy an existing source through the Gas or Liquid Quality Source Editor.

<div class="procedure">

To copy a source from the Gas or Liquid Quality Source Editor:

1.  Go to **Setup** \> **Source Analysis** \> **Gas Quality** or **Liquid Quality** and click **New**.
2.  Click the **Copy** button and select the source to copy from the list.
3.  Enter a source number and name.
4.  Make any required edits and click **Save**.

</div>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Deleting Sources">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Deleting Sources</a>

<div class="drop-down" style="display: none;" mc-target-name="Deleting Sources">

Sources can only be deleted from the Quality Source Editor. Deleting a source requires the “Quality Source Edit – Can Delete” privilege.

<div class="procedure">

To delete a source:

1.  Go to **Setup** \> **Source Analysis** \> **Gas Quality** or **Liquid Quality**, and select a source to delete using the Source drop-down.
2.  Click the **Delete** button.
3.  When prompted, confirm the deletion.

When a source is deleted, FLOWCAL will generate a message logging the deletion (available in the Message Viewer).

</div>

</div>

#### See also:

- [View Source Data](View%20Source%20Data.md)
- [Import Source Data](Import%20Source%20Data_Overview.md)
- [Edit Source Data](Edit%20Source%20Data.md)

</div>
