# <span id="aanchor409"></span> Additional Import Drivers

FLOWCAL provides drivers for many manufacturer native file formats. The table below shows the typical configuration of these drivers. Some driver types require additional information.

Two generic option fields, Option 1 and Option 2, will display in FLOWCAL depending on the driver selected and should be populated as noted below.

All import configurations require Import Path.

<table class="FcTable" style="margin-left: 0;margin-right: auto;width: 834px;">
<thead>
<tr>
<th style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Driver</th>
<th style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Notes</th>
<th style="text-align: center; background-color: #696969; color: #ffffff; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px;">Details</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;">Applied.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Driver for Applied Automation TotalFlow flow computers</p>
<p>Typical collection files have CFX extension</p></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: The name portion of the collection file</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5; font-weight: bold;">Bristol.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><ul>
<li>Driver for Bristol TeleFlow flow computers</li>
<li>There are typically three collection files with extensions of CFG, AUD and HLY</li>
<li>This driver uses a mapping file with the extension FCS to map Bristol signal names to FLOWCAL data points</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Filename: The name portion of the collection files</p>
<p>Option 1: The name of the FCS file</p>
<p>Option 2: The name portion of the CFG file if different</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;">ChartAtf.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><ul>
<li>File is output by Chart-32 chart integration software</li>
<li>One file per meter</li>
<li>Extension is typically ATF, any extension will work</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: The name and extension of the import file</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5; font-weight: bold;">CtrlWave.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><ul>
<li>Driver for Bristol ControlWave RTUs</li>
<li>There are typically three collection files with extensions of CFG, AUD and HLY</li>
<li>This driver uses a mapping file with the extension FCS to map ControlWave signal names to FLOWCAL data points</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Filename: The name portion of the collection files</p>
<p>Option 1: The name portion of the FCS file</p>
<p>Option 2: The name portion of the CFG file if different</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;"><p>FcLiq01.dll</p>
<p> </p></td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><ul>
<li>A minimal driver for simple liquid periodic flow data, no characteristics</li>
<li>One file per meter</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: The name and extension of the import file</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: bold; background-color: #ffffff;"> </td>
<td colspan="2" style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>OMNIs can output a text file called a 701 report that can be configured to match our FcLiq01 format.</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5; font-weight: bold;">Fisher.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><ul>
<li>Driver for Fisher ROC flow computers</li>
<li>The import file will typically have an extension of AGA or DET, depending on the version of EFM</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Filename: The name and extension of the import file</p>
<p>Option 1: Run or tube number within the file</p>
<p>Option 2: n/a</p>
<p>If the flow computer uses AGA7 calculation, then Option 1 may also include an asterisk (*) which will adjust the pulse count by a factor of 1000. For example, Option 1 = 3* would mean run 3 and adjust the count by a factor of 1000.</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;">FlowAuto.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><ul>
<li>Driver for Flow Automation brand flow computers. Common models include SuperFlo, AutoPILOT and AutoMATE</li>
<li>This driver requires that either the Import ID or Meter Number in FLOWCAL match the Meter Name in the flow computer</li>
<li>The usual collection file names are MBS##.DIR and MBS##.DAT</li>
<li>The files can contain data for multiple meters and multiple data sets for each meter</li>
<li>To see a list of meters and datasets in a file, set Option 1 to "LIST" in the override section of the manual import screen; this will display a list of meter names. FLOWCAL will only look for and import Periodic data, not Daily</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: The last node in the path to where the import files are located, or the DAT file prefix if not MBS##; do not repeat the last node in the path</p>
<p>Option 1: Unused in normal use</p>
<p>Option 2: Entry number; if blank, the last/latest data set in the file for this meter is used</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5; font-weight: bold;">LQTicket.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><ul>
<li>Driver for liquid meters set up in run ticket mode (See: [Meter Editor &gt; Liquids tab &gt; Setup sub-tab](../Meters/Meter%20Editor/Liquids%20Tab.md#Setup))</li>
<li>The import files can contain data for multiple meters</li>
<li>The file extension is LQT; any extension will work for manual imports</li>
<li>This driver requires that the meter numbers in the file match the meter numbers in FLOWCAL; import IDs are not used</li>
<li>The driver requires the file to use encoding UTF-8</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Filename: The name and extension of the import file</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;">Mercury1.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><ul>
<li>Driver for Mercury Mini-Max and Mini-AT correctors</li>
<li>There are typically two collection files with extensions ATM and ADT</li>
<li>ADT files contain the flow data for one meter</li>
<li>ATM files contain meter specific values</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: Name portion of the ATM/ADT files</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5; font-weight: bold;">Mercury2.dll*</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><ul>
<li>Driver for Mercury Mini-Max and Mini-AT correctors</li>
<li>This must be configured in the [Meter Editor](../Meters/Meter%20Editor/Imports%20Tab.md); cannot use overrides during manual import</li>
<li>There are typically two collection files with extensions CSD and ITM</li>
<li>CSD files contain flow data and may contain data for multiple meters</li>
<li>ITM files contain meter specific values. The ITM file name must match the FLOWCAL meter number or must be specified in either Option 1 or import ID</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"><p>Filename: Name portion of the CSD file</p>
<p>Option 1: Name portion of the ITM file if different from meter number</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff; font-weight: bold;">Reynolds.dll*</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><ul>
<li>Driver for Reynolds Pro flow computers</li>
<li>There are typically two collection files with the same file name and the extensions PRO and IDB</li>
<li>The files contain data for one flow meter</li>
</ul></td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #ffffff;"><p>Filename: Name portion of the PRO/IDB files.</p>
<p>Option 1: n/a</p>
<p>Option 2: n/a</p></td>
</tr>
<tr>
<td style="text-align: left; border-left-style: solid; border-left-width: 0px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; font-weight: bold; background-color: #f5f5f5;">Stndcfx.dll</td>
<td style="text-align: left; font-weight: normal; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;">A CFX (Common File Exchange) file is a proprietary binary file format used to bring meter flow data and configuration information into FLOWCAL. It is used to import data from a variety of meter manufacturers.</td>
<td style="text-align: left; border-left-style: solid; border-left-width: 1px; border-left-color: #c0c0c0; border-right-style: solid; border-right-width: 0px; border-right-color: #c0c0c0; border-top-style: solid; border-top-width: 0px; border-top-color: #c0c0c0; border-bottom-style: solid; border-bottom-width: 0px; border-bottom-color: #c0c0c0; padding-left: 5px; padding-right: 5px; padding-top: 5px; padding-bottom: 5px; background-color: #f5f5f5;"> </td>
</tr>
</tbody>
</table>

**\*** These drivers are not supported by the File Import service. They are only available when manually importing data using the [Import \> Meter Data screen](Meter%20Data/Import%20Meter%20Data.md).

The Stndtfx and Stndpfx drivers cannot be loaded. These import drivers are automatically used by FLOWCAL when importing tickets or PROVEit files, respectively.

#### See also:

[Configure Imports](../Admin%20Options/Configure%20Imports.md)
