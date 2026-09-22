# <span id="aanchor477"></span> Calculated Meter Editor

[&lt;&lt; Back](Calculated%20Meter.md#Tabs) \| [Relationship](Relationship%20Tab.md) \| <a href="#" class="selected">General</a> \| [Custom Fields](Custom%20Fields%20Tab.md) \| [Reports](Reports%20Tab.md) \| [Misc.](Misc%20Tab.md) \| [Audits](Audits%20Tab.md) \| [Operations](Operations%20Tab.md) \| [Liquids](Liquids%20Tab.md) \| [Formulas](Formulas%20Tab.md) \| [Integration](Integration%20Tab.md)

## General Tab

The General tab shows basic information about the meter, such as where it is located and what Close Group it belongs to. The fields that are shaded in gray such as Meter Type and Meter Direction are read-only and are retrieved from the meter’s characteristics. These read-only fields are editable in the Volume Editor.

The following items are available on the General tab of the Calculated Meter Editor:

- **Meter Type** - Read-only field that displays the type of meter, which is a Calculated Meter.

- **Alt. Meter Number** - Informational field used to document an alternate meter number. This typically references a third party or contract meter number.

- **Meter Direction** - Read-only field that displays whether a meter is classified as Inlet, Outlet, Throughput, Balance Check, Transfer, Tieover, or Off System for balancing purposes. This value is retrieved from the meter’s characteristics and can be edited from the Volume Editor.

- **Customer** - The customer the meter belongs to.

- **Cust. Meter Number** - Informational field used to document the customer's meter number.

- **Check Meter Exists** - Specifies whether an existing check meter is associated to the meter; commonly used if data from another meter is being measured at the same measurement point.

- **Helium Meter** - Designates whether a meter is a helium meter. This option would be set to “Yes” for the member meters within the Meter Editor. Helium is calculated at the member meter level. However, the user could set this option “Yes” in order to run the Helium reports for a calculated meter.

- **Close Groups** - Close Groups only appear if the close schedule type is set to Close Group in the FLOWCAL Configuration screen.

- **Fluid Phase** - Defines the meter phase conditions as gas or liquid. The fluid phase is defined on meter creation and cannot be changed once the meter is created.

- **Meter Status** - Indicates whether the meter is active; pulled from meter’s characteristics and applicable to the current system time.

- **Business Status** - This status is not datetime effective and can be updated manually via the Calculated Meter Editor. This status overrides the Meter Status.

  Meters that have any Business Status other than "On" are treated as out of service and will not be included when running reports for a list.

- **System** - Informational field that indicates which system the meter is assigned to, typically set during meter creation.

- **Notes** - Additional notes about the meter; up to 320 characters.

  The notes stored on the General tab are only available from the Calculated Meter Editor. For notes that can be accessed throughout the application (e.g., Volume Editor), right-click on the Calculated Meter Editor screen to add or view notes.

- **City** - City the meter is in; up to 50 characters.

- **County** - County the meter is in; up to 20 characters. Options are defined in the County Editor.

- **State** - State the meter is in; up to 50 characters. Options are defined in the State Editor.

- **Country** - Country the meter is in; up to 50 characters. Options are defined in the Country Editor.

- **Time Zone** - Time zone the meter is in; up to 80 characters. Options are defined in the Time Zone Editor.

- **Quarter** - Each section is divided into quarter sections, which are each further divided into quarter sections, for a total of 16 parts per section; up to 25 characters.
  <div class="example">

  <a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerBRDToggler MCTogglerHotSpot_ MCTogglerHotSpot_BRDToggler MCHotSpotImage" data-mc-targets="Example">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Example</a>

  <div style="display: none;" mc-target-name="Example">

  "NW 1/4 of the SE 1/4" refers to the northwestern-most quarter of the southeastern quarter.

  

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAACDCAYAAABMQbMfAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKvSURBVHhe7dyxqhxlAIbh3N0xybG38kIsvQivxP54ELEOdvY2ImxECQaRdSffW259NrDPCx/LMs0wPMx0/6uHp9P58fm+9+aH0/n1Zdeu3dMOC6/eXh7Evff9b/+cv/v1Q//ut8MCEJeAWEAUEAuIAmIBUUAsIAqIBUQBsYAoIBYQBcQCooBYQBQQC4gCYgFRQCwgCogFRAGxgCggFhAFxAKigFhAFBALiAJiAVFALCAKiAVEAbGAKCAWEAXEAqKAWEAUEAuIAmIBUUAsIAqIBUQBsYAoIBYQBcQCooBYQBQQC4gCYgFRQCwgCogFRAGxgCggFhAFxAKigFhAFBALiAJiAVFALCAKiAVEAbGAKCAWEAXEAqKAWEAUEAuIAmIBUUAsIAqIBUQBsYAoIBYQBcQCooBYQBQQC4gCYgFRQCwgCogFRAGxgCgg1icQD0+n8+Pzfe/N5UF8cXkOx+8td+3eXnKHBW+IS8cb4ngYt9zXP//Z3dwun4wCYgFRQCwgCogFRAGxgCggFhAFxAKigFhAFBALiAJiAVFALCAKiAVEAbGAKCAWEAXEAqKAWEAUEAuIAmIBUUAsIAqIBUQBsYAoIBYQBcQCooBYQBQQC4gCYgFRQCwgCogFRAGxgCggFhAFxAKiPgcQXz6/P3/z7q+b7jgjA4hLB4hvf/n7/O7070324+8fz1/99P7qtZfccWgJEJcOELc8UuiPj//5ZHxOAbGAKCAWEAXEAqKAWEAUEAuIAmIBUUAsIAqIBUQBsYAoIBYQBcQCooBYQBQQC4gCYgFRQCwgCogFRAGxgCggFhAFxAKigFhAFBALiAJiAVFALCAKiAVEAbGAKCAWEAXEAqKAWEAUEAuIAmJ9AnEcVvH4fN87zkV4fdm1ay+xt5cdh3Vcu/aSe3g6nf8Hu1WrzYm2Xx4AAAAASUVORK5CYII=" style="width: 132;height: 131;" />

  </div>

  </div>

- **Section** - The basic unit of a township and range; each section refers to an area of a square mile; up to three characters.

- **Township** - A measure of the distance north or south from the baseline, six miles in length; up to four characters.

- **Range** - A measure of the distance east or west from the principal meridian, six miles in length; up to four characters.

- **Meridian** - A geographical north to south reference point; up to 25 characters.

- **Latitude** - A geographic coordinate specifying a north-south location on the Earth’s surface, measured from the Equator; up to 12 characters.

- **Longitude** - A geographic coordinate specifying an east-west location on the Earth’s surface, measured from the Prime Meridian; up to 12 characters.

</div>
