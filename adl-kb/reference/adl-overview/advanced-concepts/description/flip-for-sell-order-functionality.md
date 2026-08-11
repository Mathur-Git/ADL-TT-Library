---
title: Flip for Sell Order functionality
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality/
---

# Flip for Sell Order functionality

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § OTA — Order Ticket Algo](../../../../guides/algo-types.md#ota-order-ticket-algo) · [ADL Block Catalog § Flip for Sell Order](../../../../guides/block-catalog.md#flip-for-sell-order) · [Design Patterns & Recipe Index § Bi-directional algos](../../../../guides/design-patterns.md#bi-directional-algos) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Rule anatomy](../../../../../trade-kb/guides/spread-trading-autospreader.md#rule-anatomy)

Many automated strategies in ADL will have nearly identical buy and sell side routines, with certain blocks acting as “pivot” points. As such, several blocks in ADL have Flip for Sell Order functionality, which enables them to perform an alternate function depending on the user’s selection of the **Order Side** variable (either Buy or Sell). For example, when this functionality is enabled, the [Add](../../../arithmetic-blocks/add-block.md) block will either perform an addition or a subtraction depending on the value of the **Order Side** variable.

**Example:** A bi-directional strategy using Flip for Sell Order functionality (with Flip for Sell Order-enabled blocks highlighted)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-flip-for-sell-example.png)

**Note:** Certain parts of the above strategy must be virtualized to function correctly. The virtualization is not shown for the sake of clarity in the illustration.

You must *always* design from the buy side routine and then enable the Flip for Sell Order functionality for the appropriate pivot blocks in order to switch to the sell side routine.

In Trade widgets, such as Algo Dashboard, a **Side** variable variable will appear automatically for any algorithm containing a block with the Flip for Sell Order functionality enabled, and the user must set this variable prior to launching an algorithm.

The user may alter the value of the Order Side variable through one of the following methods, but note that the Order Side variable must be declared prior to launching an algorithm and cannot be changed post-launch.

* Using the ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-side-dropdown.png) drop-down menu located at the top portion of the Designer canvas.
* Using the Variables Tab on the Algo Dashboard.
* Using the MD Trader widget: Clicking on the bid side column (blue column) will set the Order Side Variable to “Buy,” and clicking on the offer side column (red column) will set the Order Side Variable to “Sell.” This method applies to Order Ticket Algorithms (OTA) only.

#### Blocks that support Flip for Sell Order functionality

The following blocks support Flip for Sell Order functionality:

* [Add](../../../arithmetic-blocks/add-block.md) and [Subtract](../../../arithmetic-blocks/subtract-block.md) blocks
* [Greater Than](../../../logic-blocks/greater-than-blocks.md) and [Less Than](../../../logic-blocks/less-than-blocks.md) blocks
* [Field](../../../trading-blocks/field-block.md) blocks with the following fields:
  + Bid Price / Ask Price
  + Bid Qty / Ask Qty
  + High / Low
  + Direct Bid Qty / Direct Ask Qty
  + Bid Orders Qty / Ask Orders Qty
  + Direct Bid Price / Direct Ask Price

[Next PostOrder Stack Logic with Flip for Sell functionality](order-stack-logic-with-flip-for-sell-functionality.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-flip-for-sell-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-side-dropdown.png
