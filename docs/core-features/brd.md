---
title: ACBI Revision Number
description: ACBIRevision Number When ACBI batch data is edited in the Volume Editor, the revision number of the batch will not increment until the user right-clic
---

# ACBI Revision Number

## Overview

ACBIRevision Number When ACBI batch data is edited in the Volume Editor, the revision number of the batch will not increment until the user right-clicks and selects “Accept ACBI”. Although the revision does not get incremented, the corresponding totals associated with the batch will still be updated to be the sum of all underlying periodics.

## Key Characteristics

- After a user has accepted an ACBI, subsequent edits on the batch will then increment the revision number.
- Example: CFX history data is imported into FLOWCAL such that an ACBI batch record is created.
- All ACBI batch records created will be Revision number of 1.
- The user applies an edit to the batch.
- After applying the edit, the Revision column in the Volume Editor will remain 1; further edits do not increment the Revision number.
- When additional periodics are imported into the ACBI batch, the revision will remain 1.
