---
tags:
  - overview
  - getting-started
---

# FLOWCAL Data Journey Overview

A high-level walkthrough of how a new user moves through FLOWCAL end to end: security
setup (users and groups), creating a liquid product/meter, building out locations and
tickets, validating incoming meter data, resolving exceptions, closing meters, routing
changes through PPA approval, manually importing data, and rolling up results into
reports.

## Security: Users and Groups

Access to FLOWCAL is controlled through users and groups. Administrators create groups,
each with a different privilege level, and then assign individual users to the group
that matches the access they need.

- Users are created individually and then assigned to one or more groups.
- Groups are created with distinct privilege levels to control what a user can access or
  do in FLOWCAL.

## End-to-End Data Flow

After security is configured, the basic FLOWCAL workflow is: create a liquid product and
meter (with a base pressure and base temperature), create the meter's location and
tickets, assign characteristics to the meter, receive meter data, and validate whether
the incoming data is good. Data that fails validation closes on an exception, which must
be resolved. Once data looks good, the meter is closed for the period; any later change
to a closed meter (such as an equation change) requires approval through the PPA
(post-processing approval) workflow. Data can also be brought in through manual imports,
after which results are rolled up and viewed in reports.

- Liquid product/meter setup requires a base pressure and base temperature.
- Core setup order: meter -> location -> tickets -> characteristics -> meter data -> validation.
- Data that fails validation closes on an exception and must be resolved before the
  meter can be closed.
- Changes to an already-closed meter (e.g. an equation change) require PPA approval.
- Manual imports bring data into FLOWCAL outside of automated collection.
- Rolled-up data is the basis for FLOWCAL reports.

## See Also

- [Meter Fundamentals](../core-features/meters.md)
- [Liquid Meter and Product Setup](../core-features/volume-editor.md)
- [Locations and Systems](../core-features/locations.md)
- [Tickets Overview](../core-features/tickets.md)
- [Rollup Viewer Basics](../core-features/rollup-viewers.md)
