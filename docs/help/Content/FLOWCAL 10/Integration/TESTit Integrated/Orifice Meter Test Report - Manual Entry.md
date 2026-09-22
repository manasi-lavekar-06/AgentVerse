# <span id="aanchor479"></span> Orifice Meter Test Report - Manual Entry

This functionality is only available with TESTit 2 integration.

FLOWCAL allows users to manually enter data into a TESTit test report through TESTit Integrated.

<div class="procedure">

To set up a report for manual entry:

1.  Go to **View** \> **Tree View**.
2.  Select a meter.
3.  Select **New** \> **Create/View**.
4.  Select **Orifice Meter Test** from the drop-down menu.

Enter the following data to make the manually entered test report available on the Review Test Report screen:

1.  Enter the plate information and tube information on the **Orifice** tab.

2.  Enter the **Before Calibration** and **Test Points** data on the **Differential Transmitter** tab. If there are not any test points, then enter 0 in the **As Found** and **As Left** fields and change the **Number of Test Points** value to 1.

3.  Enter the **Test Points** data on the **Static Transmitter** tab. If there are not any test points, enter 0 in the **As Found** and **As Left** fields and change the **Number of Test Points** value to 1.

4.  Enter the **Test Points** data on the **Temperature Transmitter** tab. If there are not any test points, enter 0 in the **As Found** and **As Left** fields and change the **Number of Test Points** value to 1.

5.  On the **Meter** tab, select the **Volume Calculations** sub-tab and select a calculation method and FPV method from the drop-down menus.

    When "AGA-8 Detail" is selected for the FPV method, the **Detail** section will need to be completed in addition to the **Calculation Data** section. If "AGA-8 Gross 1" or "AGA-8 Gross 2" is selected for the FPV method, then data will only need to be entered in the **Calculation Data** section.

6.  Select the **Meter** sub-tab, click both calculator buttons in the **Calc. Flow Rate** section.

7.  Save your changes.

8.  Start the FcSrvTestITCalAdjApply service. The test report will now be available for viewing in FLOWCAL under **Review** \> **Review Test Report**.

</div>
