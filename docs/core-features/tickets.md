---
title: Tickets Overview
description: Tickets Overview - Complete Reference (Core Concepts)
tags:
  - tickets
---

# Tickets Overview

## Core Concepts & Fundamentals

Tickets capture single-moment transactions, distinct from a meter's periodic record, and can be created, assigned, closed, edited, and reopened.

<!-- ko:ko-understanding-meters-and-tickets-in-flowcal block:0 -->
<div class="dg-diagram">
<div class="dg-root">Meters vs. Tickets: Key Differences</div>
<ul class="dg-items">
<li class="dg-item">Meters capture periodic data, such as hourly flow rates.</li>
<li class="dg-item">Tickets represent one-time transactions and act as receipts.</li>
<li class="dg-item">Both are used to track product flow and transactions at specific locations.</li>
</ul>
</div>

<!-- ko:ko-understanding-meters-and-tickets-in-flowcal block:1 -->
<div class="txt-block" markdown="1">

### Product Separation and Ticket Creation

<p>When products are extracted, they often consist of a mix of liquid and gas. These are separated through processes like de-ethanization, propanization, and butanization. At each stage, tickets are created to record the volume of product separated and transported. For example, ethane, propane, and butane are separated and tracked individually, with tickets documenting each transaction.</p>
<ul>
<li>Products are separated into components like ethane, propane, and butane.</li>
<li>Tickets document the volume of product separated and transported at each stage.</li>
<li>The process ensures accurate tracking of product flow and transactions.</li>
</ul>

</div>

<!-- ko:ko-understanding-meters-and-tickets-in-flowcal block:2 -->
<div class="txt-block" markdown="1">

### How Locations and Tickets Interact

<p>Locations in FLOWCAL serve as organizational units where meters and tickets are grouped. A location can have multiple tickets associated with it, each representing a specific transaction. This allows for detailed tracking and reporting of product flow and transactions within a single location.</p>
<ul>
<li>Locations group meters and tickets for organizational purposes.</li>
<li>Multiple tickets can be associated with a single location.</li>
<li>This setup enables detailed tracking and reporting of product flow.</li>
</ul>

</div>

<!-- ko:ko-creating-and-managing-meter-tickets block:0 -->
<div class="txt-block" markdown="1">

### Difference Between Meters and Tickets

<p>Meters keep a periodic record (e.g., hourly data), while tickets represent a single point in time. Tickets can be standalone or associated with a specific location, and they capture details like product, temperature, pressure, and direction at the time of the transaction.</p>
<ul>
<li>Meters record periodic data; tickets capture a single moment.</li>
<li>Tickets can be standalone or linked to a location.</li>
<li>Details like product, temperature, and pressure are recorded in tickets.</li>
</ul>

</div>

<!-- ko:ko-creating-and-managing-meter-tickets block:1 -->
<div class="txt-block" markdown="1">

### Accessing the Ticket Editor

<p>To create or edit tickets, navigate to the Ticket Editor via the setup menu or use the shortcut. The Ticket Editor allows users to create various ticket types, including meter tickets.</p>
<ul>
<li>Access the Ticket Editor through the setup menu or a shortcut.</li>
<li>The editor supports creating different types of tickets.</li>
</ul>

</div>

<!-- ko:ko-creating-and-managing-meter-tickets block:2 -->
<div class="flow-chart">
<div class="flow-root">Steps to Create a Meter Ticket</div>
<ol class="flow-steps">
<li class="flow-step">Open the Ticket Editor and select 'Meter Ticket.'</li>
<li class="flow-step">Fill in transaction details and add analysis.</li>
<li class="flow-step">Associate the ticket with a location or leave it standalone.</li>
</ol>
</div>

<!-- ko:ko-creating-and-managing-meter-tickets block:3 -->
<div class="txt-block" markdown="1">

### Editing and Closing Tickets

<p>Tickets can be edited even after being closed, but changes will trigger recalculations and revisions. Analysis can be attached or updated by right-clicking and selecting the appropriate option. The analysis tab reflects all applied changes.</p>
<ul>
<li>Closed tickets can be edited, triggering recalculations.</li>
<li>Attach or update analysis via right-click options.</li>
<li>The analysis tab shows all applied changes.</li>
</ul>

</div>

<!-- ko:ko-managing-tickets-assigning-closing-editing-and-reopening block:0 -->
<div class="txt-block" markdown="1">

### Assigning an Analysis to a Ticket

<p>To assign an analysis to a ticket, right-click on the ticket and select the option to attach the analysis. Once attached, the analysis is applied, and the ticket's revision is updated. You can verify this by opening the ticket and checking the Analysis tab.</p>
<ul>
<li>Right-click to attach an analysis to a ticket.</li>
<li>The ticket's revision updates after the analysis is applied.</li>
<li>Verify the analysis in the Analysis tab of the ticket.</li>
</ul>

</div>

<!-- ko:ko-managing-tickets-assigning-closing-editing-and-reopening block:1 -->
<div class="txt-block" markdown="1">

### Closing a Ticket

<p>Tickets can be closed by right-clicking and selecting the close option. However, tickets with exceptions or those in the current or future month cannot be closed. Exceptions must be resolved before closing. Once closed, the ticket is marked blue, indicating it is finalized.</p>
<ul>
<li>Tickets with exceptions or in the current/future month cannot be closed.</li>
<li>Resolve exceptions to enable closing.</li>
<li>Closed tickets are marked blue.</li>
</ul>

</div>

<!-- ko:ko-managing-tickets-assigning-closing-editing-and-reopening block:2 -->
<div class="txt-block" markdown="1">

### Editing a Closed Ticket

<p>Closed tickets can be edited without requiring approval. For example, you can update values like GSB directly, and the changes apply immediately. However, tickets with a PPA cannot be deleted after being closed.</p>
<ul>
<li>Edits to closed tickets do not require approval.</li>
<li>Changes apply immediately upon editing.</li>
<li>Tickets with a PPA cannot be deleted after closure.</li>
</ul>

</div>

<!-- ko:ko-managing-tickets-assigning-closing-editing-and-reopening block:3 -->
<div class="txt-block" markdown="1">

### Reopening Tickets and Meters

<p>Tickets cannot be reopened once closed. However, meters can be reopened through the setup menu by accessing closed dates. Meters with a PPA must have the PPA removed before reopening. For example, a February meter without a PPA can be reopened, but a January meter with a PPA cannot.</p>
<ul>
<li>Closed tickets cannot be reopened.</li>
<li>Meters can be reopened via the setup menu.</li>
<li>Meters with a PPA must have the PPA removed before reopening.</li>
</ul>

</div>

## See Also

- (none yet)
