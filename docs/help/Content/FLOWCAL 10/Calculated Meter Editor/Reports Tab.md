# <span id="aanchor458"></span> Calculated Meter Editor

[&lt;&lt; Back](Calculated%20Meter.md#Tabs) \| [Relationship](Relationship%20Tab.md) \| [General](General%20Tab.md) \| [Custom Fields](Custom%20Fields%20Tab.md) \| <a href="#" class="selected">Reports</a> \| [Misc.](Misc%20Tab.md) \| [Audits](Audits%20Tab.md) \| [Operations](Operations%20Tab.md) \| [Liquids](Liquids%20Tab.md) \| [Formulas](Formulas%20Tab.md) \| [Integration](Integration%20Tab.md)

## Reports Tab

The Reports tab contains various meter level report options that are associated to and affect the behavior of several standard reports. In addition, contract hour, contract day, and data span are displayed as read-only fields from the meter’s most recent characteristic record.

The following items are available on the Reports tab of the Calculated Meter Editor:

- **Print Customer Name** - If set to Yes, the customer name will be printed at the top of all meter reports (that display one meter per page), such as the Hourly and Daily Gas Volume Statements. The customer is selected on the General tab of the Meter Editor. If set to Yes, the customer name will take precedence over a company name or logo defined in FLOWCAL.
- **Print Edit Reasons on Gas Volume Statement** - By default, Daily and Hourly Gas Volume Statements identify each record as edited or not, but do not print the edit reasons. With this option, you can choose to:
  - Show Codes and Reasons
  - Indicate Edited Data, No Reasons
  - No Edit Indicators
- **Print Interval or Fixed Factor on Gas Volume Statement** - Determines whether the interval or fixed factor will be displayed on the Gas Volume Statement. For charts, this is the rotation and for EFMs, this is the data resolution as defined in the meter’s characteristics.
- **Print Alternate Meter Number Instead of Meter Name** - On most meter reports where the meter name is displayed, the Alternate Meter Number can be displayed in its place. The Alt. Meter Number is set on the General tab of the Meter Editor.
- **Print Volume at Optional Pressure Base** - If set to Yes, the volume will be recalculated at the pressure base specified in the Use Pressure Base of field. This recalculated volume will then be printed at the bottom of the Daily Gas Volume Statement, along with the optional pressure base. The value entered for the optional pressure base must be between 9.000 and 20.000 psi.
- **Use Pressure Base of** - Used in conjunction with the Print Volume at Optional Pressure Base option.
- **Print Measurement Area** - If set to Yes, the Measurement Area will be printed at the top of most meter reports that display one meter per page.
- **Measurement Area** - Select a Measurement Area from the drop-down or, with the correct privileges, click the New button to create a new Measurement Area. Measurement Areas are managed from the Measurement Area Editor.
- **Chart Change Schedule** - Chart labels can be created for scheduled chart routes. A schedule is used to specify the on and off dates for the charts, which is used when printing the Bar Code Labels report.
- **Skip Closing Data** - Any meter can be closed, but the closing of a meter can be prohibited by setting this option to Yes. The default is No.

</div>
