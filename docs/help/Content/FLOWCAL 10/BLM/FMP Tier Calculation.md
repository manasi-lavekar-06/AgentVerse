# <span id="aanchor52"></span> FMP Tier Calculation

This feature requires the Monthly Close Functions and Service module.

The FMP tier is determined by evaluating the daily average volume for an averaging period. "Averaging period" is defined by the BLM (43 CFR, subpart 3170.3) as the previous 12 months or the life of the meter, whichever is shorter.

For FMPs that measure production from a newly drilled well, the averaging period excludes any production from that well that occurred in or before the first full month of production.

<div class="example">

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerBRDToggler MCTogglerHotSpot_ MCTogglerHotSpot_BRDToggler MCHotSpotImage" data-mc-targets="Example">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Example </a>

If an FMP was installed to measure the production from a new well that first produced on April 10, the averaging period for that FMP would not include the production that occurred in April (partial month) and May (full month) of that year.

</div>

FLOWCAL interprets "previous" as "closed". As a result, when the calculation runs, FLOWCAL starts with the most recent closed month. Within the averaging period, FLOWCAL will also:

- Exclude time frames for which the meter status is "Inactive" or "Disconnected". The averaging period is not extended to "make up" for these time frames.
- Include zero flow days where the meter status is "Active".

<table class="FcTable" style="margin-left: 0;margin-right: auto;width: 640px;">
<thead>
<tr>
<th colspan="2" style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 1px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;"><p><strong>First Flow Date:</strong> 1/1/2017</p>
<p>Per BLM rules, 1/2017 and 2/2017 are not used in the averaging period.</p></th>
</tr>
<tr>
<th style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Scenario</th>
<th style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Expected Results</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;"><p>Run on 2/15/2018</p>
<p>Closed for January</p></td>
<td style="text-align: left; border-top-style: solid; border-top-width: 0px; border-bottom-style: solid; border-bottom-width: 0px; background-color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">The calculation will use the months 3/2017 through 1/2018, a total of 10 months.</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;"><p>Run on 4/15/2018</p>
<p>Closed for March</p></td>
<td style="text-align: left; border-top-style: solid; border-top-width: 0px; border-bottom-style: solid; border-bottom-width: 0px; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">The calculation will use the months 4/2017 through 3/2018, a total of 12 months.</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #ffffff;"><p>Run on 4/15/2018</p>
<p>Closed for March</p>
<p>Zero Flow for month of June</p></td>
<td style="text-align: left; border-top-style: solid; border-top-width: 0px; border-bottom-style: solid; border-bottom-width: 0px; background-color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">The calculation will use the months 4/2017 through 3/2018, a total of 12 months.</td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: normal; background-color: #f5f5f5;"><p>Run on 4/15/2018</p>
<p>Closed for March</p>
<p>Inactive for month of June</p></td>
<td style="text-align: left; border-top-style: solid; border-top-width: 0px; border-bottom-style: solid; border-bottom-width: 0px; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>The calculation will use the months 4/2017, 5/2017, and 7/2017 through 3/2018, a total of 11 months.</p>
<p>Note that the inactive period does not need be on a month boundary as used in this example. It is the days that are inactive that are excluded.</p></td>
</tr>
</tbody>
</table>

 

The First Flow field on the [Misc. tab](../Meters/Meter%20Editor/Misc%20Tab.md) of the Meter Editor is used to calculate the Calculated Tier when a meter started flowing within the last 12 months.

#### See also:

[Meter Editor BLM Tab](../Meters/Meter%20Editor/BLM%20Tab.md)
