# <span id="aanchor506"></span> Calculated Meter Editor

[&lt;&lt; Back](Calculated%20Meter.md#Tabs) \| [Relationship](Relationship%20Tab.md) \| [General](General%20Tab.md) \| [Custom Fields](Custom%20Fields%20Tab.md) \| [Reports](Reports%20Tab.md) \| [Misc.](Misc%20Tab.md) \| [Audits](Audits%20Tab.md) \| <a href="#" class="selected">Operations</a> \| [Liquids](Liquids%20Tab.md) \| [Formulas](Formulas%20Tab.md) \| [Integration](Integration%20Tab.md)

## Operations Tab

The following items are available on the Operations tab of the Calculated Meter Editor:

**Meter Direction** - Meter or location direction (e.g., Inlet, Outlet). The directions for a calculated meter determine the math that will be used.

**For inlet meters:**  
Inlets - Outlets

**For outlet meters:**  
Outlets - Inlets

**For throughput meters:**  
Positive Quantities\* - Negative Quantities

\*Specified in the [Relationship tab](Relationship%20Tab.md)

**Meter Class** - A meter class or "meter purpose" used to provide FLOWCAL categories for grouping meters within viewers and reports (e.g., Sales, Receipt, Delivery).

**Calculate Component (Calculated Meter Type)** - A calculated meter is normally set to calculate the net total for the members based on the defined arithmetic or it can calculate the volume for one specific component as configured in the Calculated Meter Type section. If configured to calculate the volume for a given component, the mole % of each member is applied to the member volume and those totals are used to arrive at the net. That is FLOWCAL does not total a net and then apply a calculated mole %.

Meter direction and class can be defined from the Calculated Meter Editor when in new mode. Once a calculated meter is created, direction and class can only be edited from the Volume Editor.

</div>
