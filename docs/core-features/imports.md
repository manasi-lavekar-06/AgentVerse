---
title: Additional Import Drivers
description: Additional Import Drivers FLOWCAL provides drivers for many manufacturer native file formats. The table below shows the typical configuration of these
---

# Additional Import Drivers

## Overview

Additional Import Drivers FLOWCAL provides drivers for many manufacturer native file formats. The table below shows the typical configuration of these drivers.

## Key Characteristics

- Some driver types require additional information.
- Two generic option fields, Option 1 and Option 2, will display in FLOWCAL depending on the driver selected and should be populated as noted below.
- All import configurations require Import Path.
- Driver Notes Details Applied.dll Driver for Applied Automation TotalFlow flow computers Typical collection files have CFX extension Filename: The name portion of the collection file Option 1: n/a Option 2: n/a Bristol.dll Driver for Bristol TeleFlow flow computers There are typically three collection files with extensions of CFG, AUD and HLY This driver uses a mapping file with the extension FCS to map Bristol signal names to FLOWCAL data points Filename: The name portion of the collection files Option 1: The name of the FCS file Option 2: The name portion of the CFG file if different ChartAtf.dll File is output by Chart-32 chart integration software One file per meter Extension is typically ATF, any extension will work Filename: The name and extension of the import file Option 1: n/a Option 2: n/a CtrlWave.dll Driver for Bristol ControlWave RTUs There are typically three collection files with extensions of CFG, AUD and HLY This driver uses a mapping file with the extension FCS to map ControlWave signal names to FLOWCAL data points Filename: The name portion of the collection files Option 1: The name portion of the FCS file Option 2: The name portion of the CFG file if different FcLiq01.dll A minimal driver for simple liquid periodic flow data, no characteristics One file per meter Filename: The name and extension of the import file Option 1: n/a Option 2: n/a OMNIs can output a text file called a 701 report that can be configured to match our FcLiq01 format.
- Fisher.dll Driver for Fisher ROC flow computers The import file will typically have an extension of AGA or DET, depending on the version of EFM Filename: The name and extension of the import file Option 1: Run or tube number within the file Option 2: n/a If the flow computer uses AGA7 calculation, then Option 1 may also include an asterisk (*) which will adjust the pulse count by a factor of 1000.
- For example, Option 1 = 3* would mean run 3 and adjust the count by a factor of 1000.
