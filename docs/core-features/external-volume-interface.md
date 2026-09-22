---
title: External Volume Interface - Manual Entry for Meters
description: The External Volume Interface (manual entry screen) allows users to manually enter data for any meter in FLOWCAL. This screen requires proper configuration in the Meter Editor and System Configuration settings.
tags:
  - external-volume
  - manual-entry
  - meter-input
  - imports
  - data-entry
  - meter-configuration
---

# External Volume Interface - Manual Entry for Meters

## Introduction to External Volume Interface

The External Volume Interface, also known as the manual entry screen, enables users to manually enter data for any meter in FLOWCAL. This screen provides an alternative to automated import drivers and allows flexible data entry when needed.

- The External Volume Interface is also known as the manual entry screen
- Allows manual entry of data for any meter
- Provides flexibility in data entry workflows

## Meter Editor Configuration

To use the External Volume Interface, users typically need to configure the external volume flag in the Meter Editor. When pulling up a meter in the Meter Editor that requires hand-keyed data, the external volume flag must be set to 'yes' on the imports tab. By default, this configuration is required to use the manual entry screen.

- Access the Meter Editor to configure external volume settings
- Set the external volume flag to 'yes' on the imports tab
- This flag is required by default to use the screen
- The flag is found on the imports tab of the meter configuration

## System Configuration and Administrator Settings

The System Configuration screen within the Settings Manager provides options that allow administrators to override the default external volume flag requirement. These settings allow users to enter data for any meter, even those not configured as external volume meters. System administrators must set up these configuration options.

- Access Settings Manager from the settings gear icon in the top right corner
- Navigate to System Configuration under the System category
- External volume import options are in the top right portion of the screen
- Administrator can enable 'Can enter data for any meter' checkbox
- These settings override the meter-level external volume flag
- System configuration must be set up by local administrator

## Accessing Settings Manager

The Settings Manager provides centralized access to FLOWCAL configuration options. To access System Configuration settings for external volume options, users must first click on the settings gear icon in the top right corner, then select Settings Manager from the menu.

- Click the settings gear icon in the top right corner
- Select Settings Manager from the menu
- Once Settings Manager opens, click on System Configuration
- System Configuration is found in the bottom left under the System category

## Manual Data Entry Workflow

To enter data using the External Volume Interface, users navigate to the Import menu and select 'Meter Input'. This opens the manual entry screen where data can be entered for devices, tanks, calculated meters, and other meter types.

- Access the manual entry screen through the Import menu
- Select 'Meter Input' from the import menu options
- The screen allows entry of data for various meter types
- Used for manual entry workflows when automated imports are not suitable

## Related Topics

See also:
- [Imports](imports.md)
- [Settings Manager](settings-manager.md)
- [Application Interface](application-interface.md)
