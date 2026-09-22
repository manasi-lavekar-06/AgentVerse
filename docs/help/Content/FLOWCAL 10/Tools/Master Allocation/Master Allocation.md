# <span id="aanchor378"></span> Master Allocation

The Master Allocation process allows you to create a master meter (gas) or location (liquid) that will redistribute volumes back to wellheads based on the volume at a master level.

Theoretically, the master meter or location volume will be equivalent to the difference of volume between its outlet and inlet meter members. For instances where this is not the case, an allocation calculation is performed to distribute the surplus or deficit back to its member meters.

After Master Allocation associations are created, the Master Allocation must be manually triggered to redistribute the volumes. For gas allocations, the daily rollup records are updated and then rolled to the monthly level. For liquid allocations, periodic data is edited and queued to rollup.

[Master Allocation Setup](Master%20Allocation%20-%20Setup.md)

[Applying a Master Allocation](Applying%20a%20Master%20Allocation.md)
