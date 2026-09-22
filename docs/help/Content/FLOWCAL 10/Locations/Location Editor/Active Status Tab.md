# <span id="aanchor365"></span> Location Editor

[&lt;&lt; Back](Location%20Editor.md#Location_Editor_Tabs) \| [Members](Members%20Tab.md) \| <a href="#" class="ExceptionHeading selected">Active Status</a> \| [Characteristics](Characteristics%20Tab.md) \| [Edit Reasons](Edit%20Reasons%20Tab.md) \| [Close Group](Close%20Group%20Tab.md) \| [Site](Site%20Tab.md) \| [BLM](BLM%20Tab.md)

## Active Status Tab

Indicates whether a location is active or disconnected and is determined by the status of the meter members. The status is datetime effective and is split based on the status changes of its members during the meter rollup process.

The status can be seen on the Location Editor form and the history can be seen on the Active Status tab. The following are examples of what the user can expect for a location Active Status based on different scenarios:

- If the user has a location with 1,000 meter members and even one is active, the location status is Active.
- If the user has a location with 1,000 meter members and none are active, but even one is inactive, the location status is Inactive.
- If the user has a location with 1,000 meter members with no active or inactive members, the location status is Disconnected.
- If the user has a location with no members, the location status is Disconnected.
