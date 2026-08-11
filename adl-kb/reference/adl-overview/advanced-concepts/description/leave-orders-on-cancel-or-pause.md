---
title: Leave orders on cancel or pause
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/leave-orders-on-cancel-or-pause/
---

# Leave orders on cancel or pause

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/leave-orders-on-cancel-or-pause/)
>
> **Interpreted in:** [Core Semantics § 10. What pauses or cancels an algo](../../../../guides/core-semantics.md#10-what-pauses-or-cancels-an-algo)

### Leave orders on cancel or pause

Every smart trading block in ADL can be enabled to leave child orders in the book when the algorithm is paused or canceled. The option can be accessed by double-clicking on the respective trading block.

**Example:** Leave orders options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-leave-orders-example.png)

The following actions can cause the algorithm to pause or cancel:

* When one of the markets reported by an Instrument block in the algorithm closes: pause (unless the checkbox is selected in the Variables Tab of Information Panel)
* A smart trading block attempts to submit an order at an invalid price: pause
* Risk Check Violation (imposed by [Pnl block](../../../miscellaneous-blocks/pnl-block.md)): pause
* The [Terminal block](../../../miscellaneous-blocks/terminal-block.md) is triggered: pause
* The “Pause” button is hit on the Dashboard: pause
* The “Cancel” button is hit on the Dashboard: cancel
* Client disconnects (either voluntarily or involuntarily): the algorithm can be set up to continue running, pause or cancel using the variable on the Algo Dashboard (this variable appears automatically for all algorithms)

←[Previous PostLinking Excel Data to the Algo Dashboard](linking-excel-data-to-the-algo-dashboard.md)

[Next PostOrder Ticket Algos (OTA)](order-ticket-algos-ota.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-leave-orders-example.png
