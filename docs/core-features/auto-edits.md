---
title: Auto Edits Editor
description: AutoEdits Editor The Auto Edits Editor allows you to specify automatic edits that can be applied to applicable data on one or more meters. This is esp
---

# Auto Edits Editor

## Overview

AutoEdits Editor The Auto Edits Editor allows you to specify automatic edits that can be applied to applicable data on one or more meters. This is especially useful if you have data imported or entered every month for which you know you have to change specific detail(s), characteristic(s), or analysis.

## Key Characteristics

- Auto edits apply to all applicable data, regardless of the status of the record; that is, if the data is closed, an auto edit still applies if the data meets the condition of the auto edit and a PPA is also created.
- Auto edits do not apply to meter data that is created or edited from the Auto Estimate service or Master Allocations.
- To set up an auto edit: Go to Setup Meter Auto Edits Editor .
- When Auto Edit criteria are defined on more than one tab, the Auto Edits are applied in the following order: Auto edits defined on tabs that do not trigger a recalculation Auto edits defined on tabs that trigger a recalculation of the correlation factors applicable to that meter; correlation factors are then recalculated Auto edits defined on tabs that trigger a recalculation of volume and mass; volume and mass are then recalculated Gas Auto Edits Upon import of meter data, FLOWCAL attempts to apply the Auto Edit to each periodic record that is imported.
- On edits, FLOWCAL attempts to apply the Auto Edit to each periodic record that is within the Contract Month of the data that is modified.
- For meter characteristic Auto Edits, the Auto Edit only applies to characteristic records within the Contract Month.
