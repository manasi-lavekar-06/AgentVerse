# Validation Set Points

## Meter List/Location

[&lt;&lt; Back](Meter%20List-Location.md#Tabs) \| [Flowing Parameters](Flowing%20Parameters%20Tab.md) \| <a href="#" class="selected">Analysis</a> \| [Single Run](Single%20Run%20Tab.md) \| [Expert Systems](Expert%20Systems%20Tab.md) \| [Final Form](Final%20Form%20Tab.md)

#### Analysis Tab

Use the Analysis sub-tab to configure validation settings for the meter analysis data.

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Set Dead Band Factors">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Set Dead Band Factors</a>

<div class="drop-down" style="display: none;" mc-target-name="Set Dead Band Factors">

To prevent excessive exceptions resulting from set points that are too tight, you can specify a dead band. Click the **Set** button to access the Dead Band screen.

The dead band calculation for Flowing Analysis is based on a percentage difference between the minimum and maximum values calculated. The dead band value entered in the Dead Band Factors screen is the fraction of the difference to be added to the maximum or subtracted from the minimum calculated values.

<div class="procedure">

To perform the calculation:

1.  Calculate minimum and maximum values for the field (ethane, propane, helium, etc.) for the given percentage to be flagged.

2.  If dead band values are to be ignored, no further calculations are needed, and the numbers in step 1 will be used; otherwise, determine the difference between the maximum value and the minimum value and multiply this difference by the appropriate dead band factor. This yields an amount to subtract from the minimum or add to the maximum from step 1.

    The offset for the minimum and maximum values must be greater than the minimum allowed dead band value. This is fixed for every parameter.

3.  For each field, minimum and maximum values may exist. For example, ethane is not allowed to go below 0. If the number calculated in step 2 falls outside the boundaries established, the result is set to this value. Thus, if the ethane value fell below 0, 0 would be used instead.
    <div class="example">

    Example 1:

    Suppose that in step 1, the minimum and maximum values for ethane are calculated as 0.2 and 7.5, respectively. The difference is 7.3.

    Suppose that a dead band factor of 1.0 is used for the minimum, and a dead band factor of 0.1 is used for the maximum. Multiplying the difference by the appropriate dead band factor yields the following:

    7.3 X 1.0 = 7.3 (minimum)

    7.3 X 0.1 = .73 (maximum)

    Subtracting the numbers from the appropriate values for each yields the following:

    0.2 - 7.3 = -7.1 (minimum)

    7.5 + .73 = 8.23 (maximum)

    For ethane, 0 is the lowest value allowed, so 0 will be used instead of the calculated minimum (-7.1). The maximum allowed ethane value is 100. Since 8.23 is less than 100, that value will be used.

    Example 2:

    Suppose that in step 1, the minimum and maximum values for DP are calculated as 10.0 and 10.05, respectively. The difference is 0.05.

    Suppose that a dead band factor of 1.0 is used for the minimum, and a dead band factor of 0.1 is used for the maximum. Multiplying the difference by the appropriate dead band factor yields the following:

    0.05 X 1.0 = 0.05 (minimum)

    0.05 X 0.1 = 0.005 (maximum)

    The minimum offset for ethane is 0.02, so for the maximum, 0.021 would be used instead of 0.005.

    Subtracting the numbers from the appropriate values for each yields the following:

    10.0 - 0.05 = 9.95 (minimum)

    10.5 + 0.02 = 10.52 (maximum)

    These values fall within the minimum and maximum allowed values, so these values will be used.

    </div>

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Min Offset Values">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Minimum Offset Values for Analysis Fields</a>

<div class="drop-down" style="display: none;" mc-target-name="Min Offset Values">

|      Field       | Minimum Offset |
|:----------------:|:--------------:|
| Specific Gravity |     0.005      |
|  Heating Value   |       2        |
|       CO2        |      0.02      |
|        N2        |      0.02      |
|     Methane      |      0.02      |
|      Ethane      |      0.02      |
|     Propane      |      0.02      |
|    Iso-Butane    |      0.02      |
|     N-Butane     |      0.02      |
|   Iso-Pentane    |      0.02      |
|    N-Pentane     |      0.02      |
|   Neo-Pentane    |      0.02      |
|      Hexane      |      0.02      |
|     Heptane      |      0.02      |
|      Octane      |      0.02      |
|      Nonane      |      0.02      |
|      Decane      |      0.02      |
|      Water       |      0.02      |
|       H2S        |      0.02      |
| Component Total  |      0.02      |
|       GPMs       |      0.02      |

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="Min Max Allowed Values">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Minimum and Maximum Allowed Values for Analysis Fields</a>

<div class="drop-down" style="display: none;" mc-target-name="Min Max Allowed Values">

|      Field       | Minimum | Maximum |
|:----------------:|:-------:|:-------:|
| Specific Gravity |  0.07   |  1.57   |
|  Heating Value   |    0    |  1800   |
|       CO2        |    0    |   100   |
|        N2        |    0    |   100   |
|     Methane      |    0    |   100   |
|      Ethane      |    0    |   100   |
|     Propane      |    0    |   12    |
|    Iso-Butane    |    0    |    6    |
|     N-Butane     |    0    |    6    |
|   Iso-Pentane    |    0    |    4    |
|    N-Pentane     |    0    |    4    |
|   Neo-Pentane    |    0    |    4    |
|      Hexane      |    0    |    4    |
|     Heptane      |    0    |    4    |
|      Octane      |    0    |    4    |
|      Nonane      |    0    |    4    |
|      Decane      |    0    |    4    |
|      Water       |    0    |   100   |
|       H2S        |    0    |   100   |
| Component Total  |    0    |   101   |
|       GPMs       |    0    |  2000   |

</div>

</div>

</div>
