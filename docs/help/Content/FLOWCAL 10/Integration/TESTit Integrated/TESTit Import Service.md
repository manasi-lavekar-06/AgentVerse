# <span id="aanchor429"></span> TESTit Import Service

This functionality is only available with TESTit 2 integration.

To import test reports from the field, the TESTit Import Service will need to be installed and configured. This service is used to automatically import data from TESTit into FLOWCAL. The service name that will need to be installed is called FcSrvTESTItSchedulerImport.exe. This service is located in the FLOWCAL installation directory on the server where FLOWCAL is installed. To install this service the administrator can utilize the \_installservices.bat within the FLOWCAL installation folder.

Once the service is installed, the service will need to be configured in FLOWCAL by going to the Settings Manager \> Services \> Service Configuration menu. At the bottom of the screen you will see the configuration for the TESTit Imports. The TESTit options within FLOWCAL will appear if the TESTit module has been purchased from FLOWCAL.

The ‘Folder to check’ is the main import folder for TESTit data. After the service processes each TESTit (.TSX) file it will be moved to a folder under the import directory, labeled with the timestamp, indicating when it was processed. A Success or Failed folder will be created within the main import folder so that it is easy to see what files have processed successfully and which ones have failed. The main import folder may also contain additional folders for saved mapping configurations

Meters and/or source analyses that do not exist in FLOWCAL will be created by the TESTit Import Service using a default mapping; however, it is strongly recommended that the meters and/or source analyses are setup in FLOWCAL before any TESTit data is imported.
