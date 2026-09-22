# <span id="aanchor125"></span> Message Directory

[&lt;&lt; Back](../Message%20Directory.md) \| [0-99](System%20000.md) \| [100](System%20100.md) \| [200](System%20200.md) \| [300](System%20300.md) \| [400](System%20400.md) \| [500](System%20500.md) \| [600](System%20600.md) \| [700](System%20700.md) \| [800](System%20800.md) \| [900](System%20900.md) \| [1000](System%201000.md) \| [2000](System%202000.md) \| [3000](System%203000.md) \| [4000](System%204000.md) \| <a href="#" class="selected">5000</a> \| [6000](System%206000.md)

## System Messages

### 5500 - 5700

#### 5500 - Difference between FLOWCAL and TESTit data

#### 5501 - Create disabled (unknown meter in test report)

#### 5502 - Create disabled (unknown source in test report)

#### 5503 - Create disabled (unknown contact in test report)

#### 5504 - Create disabled (unknown company in test report)

#### 5600 - Create disabled (unknown meter in transaction queue)

#### <a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerexception MCTogglerHotSpot_ MCTogglerHotSpot_exception MCHotSpotImage" data-mc-targets="80001">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />5700 - Invalid GasTextFileExchange template</a>

<div class="drop-down" style="display: none;" mc-target-name="80001">

This message is logged when an export schedule job attempts to use an export template that cannot be found in the database.

- Message Class: Error
- Message Priority: 11
- Date: System date and time when the error occurred
- Message: Invalid Export Template
- Message Data 1: Export DLL Name - GasTextFileExchange.dll
- Message Data 2: Export Template Name
- Message Data 2: Scheduled Export Job - Name of the Export Schedule that was attempted
- Message Data 4: Application Server - Name of the server the error occurred on

</div>

#### <a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerexception MCTogglerHotSpot_ MCTogglerHotSpot_exception MCHotSpotImage" data-mc-targets="80002">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />5701 - Edited GasTextFileExchange template</a>

<div class="drop-down" style="display: none;" mc-target-name="80002">

This message is logged when a GasTextFileExchange export template is created, modified, or deleted. GasTextFileExchange export templates are created, modified, and deleted from the FLOWCAL Text File Exchange form (Reports \> Export \> GasTextFileExchange.dll \> Export Template Browse button).

- Message Class: Information
- Message Priority: 1
- Date: System date and time when the template is created, edited, or deleted
- Message: GasTextFileExchange Template Edit
- Message Data 1: Template Name
- Message Data 2: Edit Operation - Message is "New" for a template being created; "Edit" for a template being edited; and "Delete" for a template being deleted.
- Message Data 3: Application Server - Name of the machine the operation was done on

</div>

</div>
