# <span id="aanchor93"></span> Balance Explorer

[Overview](Balance%20Explorer.md) \| <a href="#" class="selected">Date Selector</a> \| [Location Explorer](Balance%20Explorer_Location%20Explorer.md) \| [Viewers](Balance%20Explorer_Viewers.md) \| [Location Rollup Queue](Balance%20Explorer_Location%20Rollup%20Queue.md) \| [Templates](Balance%20Explorer_Templates.md) \| [Notes](Balance%20Explorer_Notes.md) \| [Settings](Balance%20Explorer_Settings.md)

## Date Selector

Use the date selector to select a datetime range to display. Three date options are available:

- **Current Month** – Displays results from the current contract month, from the first day of the month to the current date.
- **Previous Month** – Displays results from the previous contract month, from the first day of the month to the last.
- **Effective Date** - Displays results based on the effective date of the associated data.

By default, the Date Selector is set to Effective Date with the First Date being the beginning of the previous month (e.g., if the current date is April 10, then the First Date is March 1) and the Last Date being the current date based on system time.

Select the start time for the First Date by clicking in the field to access the calendar, and then clicking the Start of Time button or pressing Alt+S.

Select the end time for the Last Date by clicking in the field to access the calendar, and then clicking the End of Time button or pressing Alt+E.

The First and Last Dates are inclusive. If the First Date value is later than the Last Date value, the Date Selector displays in red, indicating that there is an issue with the dates.

Based on the datetime range selected, displayed data will be calculated as follows:

<table class="TableStyle-FCtable" style="mc-table-style: url(&#39;../../../Resources/TableStyles/FCtable.css&#39;);width: 750px;" data-cellspacing="0">
<thead>
<tr class="TableStyle-FCtable-Head-Header1">
<th class="TableStyle-FCtable-HeadE-Column-Header1">Selected Date Range</th>
<th class="TableStyle-FCtable-HeadD-Column-Header1">Date View (L&amp;U and Member)</th>
</tr>
</thead>
<tbody>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Range selected are full months<br />
(e.g., April 1 – June 30)</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">In monthly columns, show monthly values from database.</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyE-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Range is a full month and partial month (e.g., April 1 – June 15)</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Full months show values from database; Partial month data are calculated by accumulation if applicable (i.e., volume, energy, mass, etc.), or displayed as NA (i.e. calculated factors, flowing parameters).</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard1">
<td class="TableStyle-FCtable-BodyE-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Range is all partial<br />
(e.g., April 15 – May 15)</td>
<td class="TableStyle-FCtable-BodyD-Column-Standard1" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Partial month data are calculated by accumulation if applicable (i.e., volume, energy, mass, etc.), or displayed as NA (i.e., calculated factors, flowing parameters).</td>
</tr>
<tr class="TableStyle-FCtable-Body-Standard2">
<td class="TableStyle-FCtable-BodyB-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">Filter days in data grid</td>
<td class="TableStyle-FCtable-BodyA-Column-Standard2" style="vertical-align: top; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px">In monthly columns, the accumulation is calculated and displayed.</td>
</tr>
</tbody>
</table>
