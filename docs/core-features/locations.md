---
tags:
  - locations
  - systems
---

# Locations and Systems

This guide explains how to set up users, assign them to systems, and configure groups and privileges in FLOWCAL.

<!-- ko:ko-user-and-system-setup-in-flowcal block:0 -->
<div class="flow-chart">
<div class="flow-root">Setting Up Users and Assigning Systems</div>
<ol class="flow-steps">
<li class="flow-step">Create a user and assign them to a system.</li>
<li class="flow-step">Configure user privileges (view-only or full access).</li>
<li class="flow-step">Set system-specific configurations like unit settings.</li>
<li class="flow-step">Unit changes apply only to future dates.</li>
</ol>
</div>

<!-- ko:ko-user-and-system-setup-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Creating and Configuring Meters

<p>Meters can be created and assigned specific characteristics based on their location and type. For example, liquid meters may handle batch data (e.g., data arriving every 2-15 days), while gas meters typically handle periodic data (daily or monthly). Characteristics such as temperature conditions (e.g., hot or cold environments) can also be configured to suit the meter's operational context.</p>
<ul>
<li>Liquid meters handle batch data; gas meters handle periodic data.</li>
<li>Characteristics depend on the meter's location and environmental conditions.</li>
<li>Meters are configured based on their type and data handling requirements.</li>
</ul>

</div>

<!-- ko:ko-setting-up-users-groups-and-systems-in-flowcal block:0 -->
<div class="txt-block" markdown="1">

### Accessing the Volume Editor

<p>To access the Volume Editor, there are two options: you can navigate through 'Open Data' to open the Volume Editor for a specific meter, or you can access it directly via the tile. The first method is often preferred to avoid closing and reopening other windows.</p>
<ul>
<li>Two ways to access the Volume Editor: via 'Open Data' or directly through the tile.</li>
<li>Using 'Open Data' is often more efficient.</li>
</ul>

</div>

<!-- ko:ko-setting-up-users-groups-and-systems-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Creating a System

<p>To create a new system, navigate to the Setting Manager. By default, the system 'Enterprise' is available, but you can create additional systems for different configurations, such as metric units. Assign users or groups to the system and configure their access privileges.</p>
<ul>
<li>Default system is 'Enterprise'.</li>
<li>New systems can be created for different configurations (e.g., metric units).</li>
<li>Users and groups must be assigned to systems to grant access.</li>
</ul>

</div>

<!-- ko:ko-setting-up-users-groups-and-systems-in-flowcal block:2 -->
<div class="txt-block" markdown="1">

### Setting Up Users and Groups

<p>Begin by creating a user in the Setting Manager. You can create either a standard user or an instant login user. Assign privileges directly to the user or add them to a group with predefined privileges. For example, the 'FC Admin' group can be created with all privileges, and users can be added to this group to inherit those privileges.</p>
<ul>
<li>Users can be created as standard or instant login users.</li>
<li>Privileges can be assigned directly or through groups.</li>
<li>Groups like 'FC Admin' can be set up with all privileges for easier management.</li>
</ul>

</div>

<!-- ko:ko-setting-up-users-groups-and-systems-in-flowcal block:3 -->
<div class="txt-block" markdown="1">

### Assigning Privileges to Users

<p>To assign privileges to a user, select the user in the Setting Manager, highlight the privileges, and check all relevant options. Ensure the user has 'no limit' access and assign them to the appropriate system. Changes must be saved to take effect.</p>
<ul>
<li>Privileges can be assigned individually or via group membership.</li>
<li>Users must be assigned to a system to access it.</li>
<li>Changes need to be saved for privileges to apply.</li>
</ul>

</div>

## See Also

- (none yet)
