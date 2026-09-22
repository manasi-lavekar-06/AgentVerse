# <span id="aanchor189"></span> Meter Characteristics from TESTit

This functionality is only available with TESTit 3 Integrated.

When a new meter test is received from TESTit, any new Meter Characteristics will be brought in for validation. An exception is generated whenever a field in the TESTit Meter Characteristics differs from a field in the current FLOWCAL Meter Characteristics. For any unwanted validations, the user may set the Exception severity for that particular field to 0 to avoid displaying it in the Exception Resolver.

## Characteristics Sent to FLOWCAL for Validation

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="General">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />General (applies to all gas meter types)</a>

<div class="drop-down" style="display: none;" mc-target-name="General">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);border-top-left-radius: 12px 12px;border-top-right-radius: 12px 12px;border-bottom-right-radius: 12px 12px;border-bottom-left-radius: 12px 12px;border-left-style: solid;border-left-width: 2px;border-left-color: #696969;border-right-style: solid;border-right-width: 2px;border-right-color: #696969;border-top-style: solid;border-top-width: 2px;border-top-color: #696969;border-bottom-style: solid;border-bottom-width: 2px;border-bottom-color: #696969;margin-left: 0;margin-right: auto;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">Meter Type</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Calibration</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Calibration Range (Static Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Transducer</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Transmitter Range (Static Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Calibration</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Calibration Range (Temperature Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Transducer</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Transmitter Range (Temperature Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2"><p>Contract Hour</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1"><p>Calc Method</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2"><p>Z Method</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1"><p>Pressure Base</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2"><p>Temperature Base</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1"><p>Atmospheric Pressure</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Pipe Diameter</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Tube ID</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Pressure Gauge</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Pressure Type</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2"><p>Full Wellstream</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1"><p>Meter Status</p></td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Dehydrated Gas</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Dehydrated</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyA-Column-Standard1"><p>Contract Hour</p></td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Orifice">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Orifice</a>

<div class="drop-down" style="display: none;" mc-target-name="Orifice">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Orifice Diameter</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Plate Size</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Cutoff</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">DP Zero Cutoff</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Calibration</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Calibration Range (Differential Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Transducer</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Transmitter Range (Differential Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">Tap Type</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2">Tap Location</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyB-Column-Standard1">Chart</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard1">Measurement Type</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Cone">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Cone</a>

<div class="drop-down" style="display: none;" mc-target-name="Cone">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Cone Diameter</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Plate Size</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Cutoff</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">DP Zero Cutoff</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1">Calibration</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1">Calibration Range (Differential Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2">Transducer</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2">Transmitter Range (Differential Low and High)</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">Tap Location</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2">Chart</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2">Measurement Type</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Coriolis">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Coriolis</a>

<div class="drop-down" style="display: none;" mc-target-name="Coriolis">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">K Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyA-Column-Standard2">Meter Factor</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Positive Displacement">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Positive Displacement</a>

<div class="drop-down" style="display: none;" mc-target-name="Positive Displacement">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">K Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2">Meter Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">Number of Dials</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2">Chart</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2">Measurement Type</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Turbine">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Turbine</a>

<div class="drop-down" style="display: none;" mc-target-name="Turbine">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">K Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard2">Meter Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">Number of Dials</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2">Chart</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2">Measurement Type</td>
</tr>
</tbody>
</table>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Ultrasonic">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Ultrasonic</a>

<div class="drop-down" style="display: none;" mc-target-name="Ultrasonic">

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 510px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th colspan="2" class="TableStyle-FCtable-HeadD-Column-Header1">Field Names</th>
</tr>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">FLOWCAL</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">TESTit</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td colspan="2" class="TableStyle-FCtable-BodyD-Column-Standard1">K Factor</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td colspan="2" class="TableStyle-FCtable-BodyA-Column-Standard2">Meter Factor</td>
</tr>
</tbody>
</table>

</div>
