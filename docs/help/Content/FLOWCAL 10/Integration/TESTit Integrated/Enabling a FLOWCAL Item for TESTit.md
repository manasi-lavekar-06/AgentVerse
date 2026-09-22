# <span id="aanchor392"></span> Enabling a FLOWCAL Item for TESTit

This functionality is only available with TESTit Integrated.

To specify a meter, source analysis, or list as TESTit-enabled, access the Meter Editor, Source Analysis Editor, or List Editor, and click the **Enabled for TESTit** drop-down.

With TESTit 3 Integrated service, FLOWCAL allows users to synchronously create, modify, and delete meters in the TESTit Server application. Managed meters are protected from certain edits within the TESTit Server application; however, changes made to managed meters in FLOWCAL are also made within the TESTit Server database.

<div class="procedure">

To enable a meter for TESTit:

1.  From the FLOWCAL main menu, go to **Setup** \> **Meter** \> **Editor**.
2.  Select the desired meter and click the **Reports** tab.
3.  Click **Edit**.
4.  At the bottom of the Reports tab, set the **Enable for TESTit** option to "Yes".
5.  The **Test Reports** button is now available in the Meter Editor.

The Enabled for TESTit option can be set back to "No". This functionality sends an update to TESTit 3 to indicate that the meter should no longer be protected from edits in TESTit 3. This setting cannot be reversed with TESTit 2.

To enable a source analysis for TESTit (TESTit 2 only):

1.  Go to **Setup** \> **Source Analysis** \> **Gas Quality**.
2.  Select the desired source analysis.
3.  Click **Edit**.
4.  At the bottom of the Main tab, set the **Enable for TESTit** option to "Yes".
5.  The **Test Reports** option is now available in the Tools menu.

To enable a list for TESTit (TESTit 3 only):

1.  Go to **Setup** \> **List**.
2.  Select the desired list.
3.  Click **Edit**.
4.  In the upper-right corner of the editor, set the **Enable for TESTit** option to "Yes".
5.  Click **Save**. The list can now be sent to a TESTit 3 server for integration.

TESTit-enabled lists are protected from edits within the TESTit Server application. Any changes must be made in the FLOWCAL List Editor and pushed to the TESTit 3 server. Dynamic lists are transmitted to the TESTit server as static, but updates are periodically sent to TESTit as changes occur to the lists in FLOWCAL.

</div>
