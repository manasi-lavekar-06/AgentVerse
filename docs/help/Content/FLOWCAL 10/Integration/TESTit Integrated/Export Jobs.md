# <span id="aanchor513"></span> Export Jobs

This functionality is only available with TESTit 2 integration.

TESTit has the ability to allow users to create export jobs containing test report data, meter definitions, list definitions, configuration data, contact data, etc. These export jobs can then be scheduled to be exported on a recurring basis. These exports can then be uploaded to other TESTit users.

<div class="procedure">

To access the Export Jobs screen:

From the main **TESTit Integrated** menu, go to **File** \> **Export Jobs**. All current export jobs, including the export name, status, next scheduled run time, previous status, and previous run time will display on this screen.

To export the current jobs listed: Click **Export Now**.

To create a new export job:

1.  Click **New**.

2.  Enable options to configure what is included in the export.

    If you select Export Test Reports, Export Schedule Definitions, or Export Schedule Entries, and no devices are selected on the left side of the screen, all devices will be selected. If you select a particular device for export, it will display in the grid below the device selection area. If you have selected devices of a particular type, such as Meter, and then select to export all meters, the previously selected meters will be removed from the grid.

    - **Last Number of Test Reports** - Export only the last number of test reports specified by the user. This option can be combined with the date range option to export only the last number of test reports in a date range.

    - **By Date Range** - Specify a date range for which to export the test reports. You can select the current month, a previous number of months, the current week, a previous number of weeks, a previous number of days, and an exact date range.

      When selecting either previous Months, Weeks, or Days the user will select how many Months, Weeks, or Days to go back and will also have the option to include the current Month, Week, or Day

    - **Schedule Definitions** - Export the most current definition along with the most current schedule entry for the selected devices.

    - **Schedule Entries** - Export completed entries or canceled entries that are unlinked.

      Unlinked entries are completed or canceled schedule entries that do not have a test report linked to them.

    - **Contact Export** - Export all contacts and distribution lists.

    - **Agency Export** - Export all agencies.

    - **Brands and Models Export** - Export all brand and model definitions.

    - **Configuration Export** - Export field property values, drop-down lists, tasks, system defaults, state lists, schedule frequencies, and unit templates.

3.  When you have configured the options, click **Continue**.

4.  On the next screen, you will be able to enter the export job name, the export file name, the export path, as well as the export schedule.

5.  Check the **Scheduled Export** checkbox to schedule the export job.

6.  Click **Save Export Job** to save the export, or click **Export Now** to run the export.

7.  Click the **Review Export** button to review the export options.

8.  Click the **Edit** button to edit the currently selected schedule.

</div>
