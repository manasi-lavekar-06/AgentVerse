# <span id="aanchor490"></span> TESTit 3 Config File

This functionality is only available with TESTit 3 Integrated.

The FLOWCAL install directory contains a file named ‘TESTit_Config_template.cfg’. This file is used for configuring key information in accessing TESTit 3 Server from FLOWCAL and remote integration services. This file must be renamed to ‘TESTit_Config.cfg’ before it can be used. The template appended to the end is to prevent this file from being overwritten every time a new version of FLOWCAL is implemented.

Example text from a .cfg file:

Install Path: C:\FA\testit3\server\Bin

Service Scheme: http

Service Host: localhost

Service Port: 53879

## Config File Details

- **Install Path** - The file path of the TESTit 3 Server the user wishes to be launched from within FLOWCAL.
- **Service Scheme** - This does not need to be modified if the user is running the FLOWCAL Integration Services on the same machine as the FLOWCAL application.
- **Service Host** - This does not need to be modified if the user is running the FLOWCAL Integration Services on the same machine as the FLOWCAL application.
- **Service Port** - This does not need to be modified if the user is running the FLOWCAL Integration Services on the same machine as the FLOWCAL application.

If the user is running the services on a separate machine, Service Scheme, Service Host (computer name), and Service Port must be specified to point to that server.
