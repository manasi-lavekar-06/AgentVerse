# <span id="aanchor135"></span> Analysis to TESTit

This functionality is only available with TESTit Integrated (Version 2.14.2 or later and Version 3.3 and later).

The service FcSrvTestITAnalysisSync copies the current gas meter analysis in FLOWCAL to TESTit gas analysis database table. Meters need to be enabled for TESTit and rolled up in order for their analysis data to be copied to TESTit. Meter analysis data that is a part of autoestimated records are not copied by this service.

The FcSrvTestITAnalysisSync service is installed in the same manner that any other FLOWCAL service is installed. (See: [Install and Configure Services](../../Admin%20Options/Install%20%26%20Configure%20Services.md))

The flowcal.enterprise.integration.service must also be installed and running for this service to work.

Once installed, the service is started from the Windows Service Monitor. The service runs at 7:00 AM every day by default.

The hour and port for this service can be adjusted by directly updating values stored in the database. Configuration of this service is not available on the Service Monitor screen.

- **FC_APPLICATION_OPTIONS.FCSRV_TIANASYNC_HOUR** - The hour at which the service should run. If null, the default setting is 7.
- **FC_APPLICATION_OPTIONS.FCSRV_TIANASYNC_PORT** - The port the service should use.

This service processes all meters that are enabled for TESTit (See: [Enabling a FLOWCAL Item for TESTit](Enabling%20a%20FLOWCAL%20Item%20for%20TESTit.md)) and are not on the meter rollup queue when it runs. It searches the final form hourly meter data table (FC_FFMTR_HOURLY) for the most recent hourly record for the meter before the current system time, and checks whether there are values in SPECIFIC_GRAVITY, C1, C2 and C3 columns. If the record does not have these columns populated or if the record is auto estimated, it does nothing. If the record contains non-null values in the checked columns, it copies the analysis values to corresponding columns of FC_TRANALYSIS table.

For TESTit 3 integration, the FC_TRANALYSIS table is no longer used. Analysis data is instead transmitted to the TESTit 3 Server database and stored in the FA_SOURCE_ANALYSIS table there.
