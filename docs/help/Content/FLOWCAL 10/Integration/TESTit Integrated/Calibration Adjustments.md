# <span id="aanchor222"></span> Calibration Adjustments

This functionality is only available with TESTit 3 integration.

FLOWCAL has the ability to adjust data based on TESTit Test Reports through edits or Prior Period Adjustments (PPAs). The adjustments can be made automatically on import of a Test Report or through the Review Test Report screen. For details, refer to: [Review Test Report](TESTit%20Manager/Test%20Report/Review%20Test%20Report.md).

For an adjustment to be applied, the adjustment amount must be greater than a specified error tolerance level and minimum unit difference. Error tolerance is a percentage difference of volume or energy for the month that must exist between the current monthly volume or energy and the adjusted monthly volume or energy. Minimum unit difference is volume or energy (in units) for the month that must exist between the current monthly volume or energy and the adjusted monthly volume or energy.

Applying a test report means that adjustment values are calculated, and adjustments are made if the adjustment value was greater than the error tolerance and the minimum unit difference. If the calculations yield an adjustment amount less than or equal to that required by the error tolerance or minimum unit difference no adjustment to the data will be made.

Logical flow for applying a test report to a meter:

For Error Tolerance set to "%" and Minimum Unit Difference set to "Unit":

If volume adjustment \> % AND volume adjustment \> unit

Result: Applied test report. An edit or PPA will be made.

Else if energy adjustment \> % AND energy adjustment \> unit

Result: Applied test report. An edit or PPA will be made.

Else

Result: Attempted test report. No edit or PPA will be made.

## Auto Calibration Adjustments

Error tolerance and minimum unit difference are set within the **Master Characteristics** section on the **Operational** tab.

These values need to be in place before the import of test reports or the user will have to manually apply the adjustment. Error tolerance (the Min Calibration Adjustment Pct) is a percentage and should be entered as a whole number (ex. Two percent = 2). If the monthly adjustment value exceeds the error tolerance and minimum unit difference (the Min Calibration Adjustment Unit Diff), the adjustment will be applied and meter data will be adjusted.

Auto calibration adjustments can be made on open or closed data. PPAs must be allowed at the system level for auto adjustments on closed data or open data.

The date span for a calibration adjustment is based on the date of the test and the last test date. For this reason, at least test report is required in the system before auto adjustments can be made.
