# <span id="aanchor121"></span> Edit Location Data

Meter members can be added to or removed from a location based on a datetime effective relationship. This keeps rollup totals accurate over time and maintains the membership history.

The reference meter and the meter/location membership within the location are date effective. When the location members need to be edited due to changes, such as new meters being placed in service, or a change in pipeline configuration occurring, a new date range should be created. This assures that the existing historical rollup data remains unchanged prior to these edits.

When editing existing locations, failing to create a new effective datetime will cause a new rollup for the existing balance to show results for the entire date period shown. This could result in many months of historical data being submitted to the Location Rollup Queue, which could create a backlog and impact system performance.

The [Service Configuration](../Settings%20Manager/Services/Service%20Configuration.md) screen offers rollup options that can limit the lookback period for rollups. If this option is enabled, data prior to the configured data is not rolled up.

<div class="procedure">

To edit a location:

1.  Go to **Setup** \> **Location** \> **Editor**.
2.  Select a location using the Location drop-down.
3.  Click the **Edit** button.
4.  Enter a date range that the changes apply to.
5.  Make necessary changes and click **Save**. The changes will be applied and the location will be queued to roll up the location data based on the changes.

You can delete a specific time frame for a location by selecting the time frame in the upper right corner and clicking the **Delete** button while in View mode.

</div>

#### See also:

- [Location Editor](Location%20Editor/Location%20Editor.md)
- [Service Queues](../Settings%20Manager/Services/Service%20Queues.md)

</div>
