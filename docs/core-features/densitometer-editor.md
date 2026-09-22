---
title: Densitometer Editor
description: Densitometer Editor The Densitometer Editor allows users to create densitometers that can be assigned to meters. Densitometers can be set up to either
---

# Densitometer Editor

## Overview

Densitometer Editor The Densitometer Editor allows users to create densitometers that can be assigned to meters. Densitometers can be set up to either apply a particular density meter factor (DMF) to a meter or validate the meter’s DMF at import time.

## Key Characteristics

- The densitometer can also be set up to validate that edited DMF values are within a certain tolerance and the edited value does not vary from the value being replaced by a certain percentage.
- Using the densitometer to apply a DMF at import time is useful if the DMF is not being kept up to date in the flow computer in the field.
- You can create a date time effective DMF entry on a per product basis.
- As data is imported, FLOWCAL will apply the DMF.
- At import time, applying a DMF to a meter will set the DMF characteristic of that meter to the specified value.
- If a DMF is applied to a meter from the FLOWCAL densitometer and the Uncorrected Observed Density is present and NO Corrected Observed Density is present, a corrected observed density will be calculated from the Uncorrected Observed Density and the applied DMF.
