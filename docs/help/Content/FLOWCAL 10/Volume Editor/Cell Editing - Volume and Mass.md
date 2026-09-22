# <span id="aanchor275"></span> Cell Editing - Volume & Mass

When cell editing volume and mass quantities in the FLOWCAL Volume Editor, the values are tracked with two columns: A Closed column and an Adjusted Total column, which includes PPAs.

The Closed column tracks the volume or mass until the meter goes through the month-end close process. Once the meter is closed, the value in the Closed column will no longer change in the database. The value in the Adjusted Total column will match the corresponding value in the Close column through the close. If adjustments are made to the data once the meter is closed, the value will be updated in the Adjusted Total column.

Each of these columns can be displayed in the tabular view of the Volume Editor.

While in cell edit mode in the Volume Editor, only one of these columns will be editable for a given quantity such as mass, net standard volume (NSV), and gross standard volume (GSV).

The following tables explain which column is editable for each quantity while in cell edit mode.

## Gas Meters

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 795px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Quantity</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Closed Column</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Adjusted Total<br />
Column</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Editable<br />
Column</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1" style="text-align: center;">Notes</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Total Adj Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Volume</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">On apply, the Total Adj. Vol. column will be updated to match the Volume column. If this is a PPA edit, then on save, the Volume column will revert to the closed value for volume and the Total Adj. Vol. column will reflect the total volume including the PPA.</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Total Adj Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Edited mass is overridden by calculated mass.</td>
</tr>
</tbody>
</table>

## Liquid Meters

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../Resources/TableStyles/FCtable.css&#39;);margin-left: 0;margin-right: auto;width: 795px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Quantity</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Closed Column</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Adjusted Total<br />
Column</th>
<th class="TableStyle-FCtable-HeadE-Column-Header1" style="text-align: center;">Editable<br />
Column</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1" style="text-align: center;">Notes</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">GSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">GSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Adj Total GSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">GSV</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">On apply, the Adj Total GSV Column will be updated to match the GSV column. If this is a PPA edit, then on save, the GSV column will revert to the closed value for GSV and the Adj Total GSV column will reflect the total GSV including the PPA.</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">NSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">NSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Adj Total NSV</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Adj Total NSV</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">If this is not a PPA edit, then on apply, the NSV column will be updated to match the Adj Total NSV column.</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">S&amp;W Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">SW Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Adj Total SW Volume</td>
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Adj Total SW Volume</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">If this is not a PPA edit, then on apply, the SW Volume column will be updated to match the Adj SW Volume column.</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Total Adj. Mass</td>
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="text-align: center; vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; border-right-style: solid; border-right-width: 1px; border-right-color: #c0c0c0;">Mass</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">On apply, the Adj Total mass column will be updated to match the Mass column. If this is a PPA edit, then on save, the Mass column will revert to the closed value for Mass and the Adj Total Mass column will reflect the total Mass including the PPA.</td>
</tr>
</tbody>
</table>
