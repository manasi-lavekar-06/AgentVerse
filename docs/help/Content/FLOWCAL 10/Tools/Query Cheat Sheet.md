# <span id="aanchor440"></span> Query Cheat Sheet

Use this cheat sheet when creating queries in the Query Editor. The following tables list possible values for the most commonly used tables and fields. The values in the tables correspond to the values in the Table, Field, and Values fields on the Criteria tab.

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Meter Tables">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Meter Tables</a>

<div class="drop-down" style="display: none;" mc-target-name="Meter Tables">

<table class="FcTable" style="margin-left: 0;margin-right: auto;width: 475px;">
<thead>
<tr>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Field</th>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Values</th>
</tr>
<tr>
<th colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Meter Characteristics Table</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Meter Status</td>
<td style="text-align: center; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Active = A or " " (null)</p>
<p>To return all active meters, select both A and " "</p>
<p>Inactive = T</p>
<p>Disconnected = D</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Calculation Method</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; padding: 0px; background-color: #f5f5f5;"><table style="width: 320px;">
<tbody>
<tr>
<td><p>AGA 3 1985 = 0</p>
<p>AGA 3 1992 = 1</p>
<p>AGA 2013 = Y</p>
<p>AGA 7 = 7</p>
<p>Gas V-Cone = V</p>
<p>AGA 11 = C</p></td>
<td><p>Gas Linepack = I</p>
<p>ISO 5167 = S</p>
<p>API 12.2 Inf. Vol = 8</p>
<p>API 12.2 Liq. Vol = A</p>
<p>API 14.7 Inf. Mass = B</p>
<p>API Direct Mass = D</p>
<p>Data Only = E</p>
<p>API 14.3.3 Mass = 3</p>
<p>API 14.3.3 Inf. Vol = 4</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Data Span</td>
<td style="text-align: center; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Time Trails = T</p>
<p>Time Leads = L</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Data Resolution</td>
<td style="text-align: center; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>15 Minute = 70</p>
<p>Hour = 72</p>
<p>Day = 68</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">DP Alarm High</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Meter Make</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Z Method</td>
<td style="text-align: center; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>NX-19 = N</p>
<p>AGA-8 Detail (1992) = D</p>
<p>AGA-8 Detail (2017) = A</p>
<p>AGA-8 GERG (2017) = E</p>
<p>AGA-8 Gross 1 (1992) = 1</p>
<p>AGA-8 Gross 1 (2017) = B</p>
<p>AGA-8 Gross 2 (1992) = 2</p>
<p>AGA-8 Gross 2 (2017) = C</p>
<p>Fpv = 1.0 = Z</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Orifice Plate Diameter</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Chart EFM Indicator</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>EFM = E</p>
<p>Chart = C</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Static Pres. Range High</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Meter Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">Pos Disp = P<br />
Orifice = O<br />
Turbine = T<br />
Ultrasonic = U<br />
Calculated = E<br />
Linepack = I<br />
Coriolis = C<br />
Cone = V</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Pipe Material/<br />
Plate Material/<br />
Cone Material</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">Carbon Steel = C<br />
Stainless Steel = S<br />
Monel = M<br />
304 SS = 4<br />
316 SS = 6<br />
Monel 400 = 1</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Tap Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Flange = F<br />
Pipe = P</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Tap Location</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">Upstream = U<br />
Downstream = D</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Pressure Gauge</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">Gauge = G<br />
Absolute = A</td>
</tr>
<tr>
<td colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; color: #000000; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Meter Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Fluid Phase</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Gas = G</p>
<p>Liquid = L</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Business Status</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>On = " " (null)</p>
<p>Off = F</p>
<p>Pending New = N</p>
<p>Pending Disconnect = D</p>
<p>Pending Reconnect = R</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Alternate Meter Number</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Check Meter Index</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Autoestimate Data</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Yes = Y</p>
<p>No = N</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Meter Name</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Meter Number</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Meter Serial Number</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Temp Src Mtr Num Idx</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Data Stream Code</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Measurement Area</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; color: #000000; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Meter Analysis Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">GPA 2172 Gas Sat Cond</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Dry = D</p>
<p>Sat at Base = B</p>
<p>Sat at Flowing = F</p>
<p>Partially Sat at Flowing = P</p>
<p>Max of SatB or SatF = M</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left; color: #000000; font-weight: bold; background-color: #d3d3d3; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Meter Close Dates Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Status</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Closed = C</p>
<p>Open = O</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left; color: #000000; font-weight: bold; background-color: #dcdcdc; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Meter Monthly Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Measured Volume</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td colspan="2" style="text-align: left; color: #000000; font-weight: bold; background-color: #dcdcdc; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Periodic Values Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Flow Duration</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Measured Volume</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Location Table">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Location Table</a>

<div class="drop-down" style="display: none;" mc-target-name="Location Table">

<table class="FcTable" style="margin-left: 0;margin-right: auto;width: 475px;">
<thead>
<tr>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Field</th>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Relationship Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Station Location = T</p>
<p>Segment Location = G</p>
<p>Balance Location = B</p>
<p>Inventory Location = I</p>
<p>Inventory2 Location = V</p>
<p>Calculated Meter Location = M</p>
<p>Calculated Meter Sub Location = N</p>
<p>Tank Location = K</p>
<p>Comparison Location = C</p>
<p>Cavern Location = R</p>
<p>Section Location = S</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Segment Direction</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Inlet = I</p>
<p>Outlet = O</p>
<p>Discontiguous = D</p>
<p>Throughput = T</p>
<p>Positive = P</p>
<p>Negative = N</p>
<p>Injection = I</p>
<p>Withdrawal = O</p>
<p>Both = B</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Tank Roof Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Floating Roof = F</p>
<p>Fixed Roof = X</p>
<p>No Roof = N</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Tank Material</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Mild Carbon = D</p>
<p>Stainless 304 = 4</p>
<p>Stainless 316 = 6</p>
<p>Stainless 17 4Ph = 7</p>
<p>Other = O</p></td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Source Tables">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Source Tables</a>

<div class="drop-down" style="display: none;" mc-target-name="Source Tables">

<table class="FcTable" style="margin-left: 0;margin-right: auto;width: 475px;">
<thead>
<tr>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Field</th>
<th style="text-align: left; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">GQ Source Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Analysis Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Gas = G</p>
<p>Liquid = L</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Gqsource Number</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">* User-defined</td>
</tr>
<tr>
<td colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">GQ Source Characteristic Table</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Gqsource Type</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Gas Analysis = A</p>
<p>Chromatograph = C</p>
<p>RTU Average = R</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;">Gqsource Status</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>In Service = I</p>
<p>Temporarily Out = T</p>
<p>Permanently Out = P</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">Effective Date</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
<tr>
<td colspan="2" style="text-align: left; font-weight: bold; background-color: #d3d3d3; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 2px; border-top-color: #808080; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #808080; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">GQ Source Analysis</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;">N2</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;">* User-defined</td>
</tr>
</tbody>
</table>

</div>
