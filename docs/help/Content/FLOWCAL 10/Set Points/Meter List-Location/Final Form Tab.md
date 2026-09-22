# Validation Set Points

## Meter List/Location

[&lt;&lt; Back](Meter%20List-Location.md#Tabs) \| [Flowing Parameters](Flowing%20Parameters%20Tab.md) \| [Analysis](Analysis%20Tab.md) \| [Single Run](Single%20Run%20Tab.md) \| [Expert Systems](Expert%20Systems%20Tab.md) \| <a href="#" class="selected">Final Form</a>

#### Final Form Tab

##### Min/Max Sub-Tab

While other validation set points are calculated using periodic data, final form validations allow users to validate that hourly, daily, and monthly totals for volume, energy, mass, and net standard volume fall within defined set points.

The Set Point calculator for final form min/max validations requires that the user specify whether the set points should be run against measured conditions, standard conditions, or both.

##### Expert Systems Sub-Tab

The final form expert systems validations apply expert system validations to hourly and daily totals for volume, energy, mass, and net standard volume.

The following options are available:

- **Comparison Type** - Specified as percent difference or standard deviation. The set point calculator will calculate both, but when validating data, it will use the type specified here.
  - For **percent difference**, the set point calculated is the percentage difference between the average of the current record and records prior to the current record.
  - For **standard deviations**, the set point calculated is the number of standard deviations that can exist between the current record and the average without an exception being generated.
- **Data Window** -The number of records prior to the record being analyzed, to be used for the average.
- **Average Method** - Specified as running or weighted. A **running** average treats each record the same when calculating the average. A **weighted** average gives more weight to records closer to the current record when calculating the average.
- **Closed Data Only** - If this option is checked, only closed data will be used in the calculation.

</div>
