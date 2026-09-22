# <span id="aanchor328"></span> Data Reconciliation

When FLOWCAL is upgraded from Version 7 to Version 8, data values must be migrated from the old Version 7 database to a new Version 8 database. After this migration process has been performed, differences in the calculated rollup values may occur.

This could be caused by any number of reasons:

- A rounding effect due to differences between Version 7 and Version 8 in the number of decimal digits values are stored with.
- Values that were rolled and totaled up incorrectly in Version 7 which are now summed correctly in Version 8.

The upgrade to Version 8 should be complete before the user begins the process of accepting or ignoring these differences between Version 7 and Version 8 rolled up values. These differences can then be evaluated and accepted or ignored as appropriate to each case.

Until these differences are accepted or ignored, the rollup services will continue to use the original values, regardless of any differences calculated during the migration.

<div class="procedure">

To access the Data Reconciliation tool:

1.  Go to **Tools** \> **Data Reconciliation**.

2.  Choose a meter, location, list, or close group.

3.  Double-click a row to bring up detailed daily information about that row (or month) in a new tab. A reason (or reasons) for the selected difference will display.

    A reason (or reasons) for the selected difference will be displayed.

4.  Click the blue up or down arrow buttons to move back and forth through the data for the meters (or locations) in the list. Differences can be accepted or ignored for each individual data row. When a difference is rejected, the data remains as it was prior to the migration. When a difference is accepted, a PPA is created instantly.

    Once a PPA is accepted, it cannot be rejected.

5.  Select the **Data** tab to go back to the full overview display. Double-click another data row or select multiple rows and click the **Open** button to display each meter in its own tab and easily compare the results.

</div>
