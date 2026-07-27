---
title: User-defined variables
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/user-defined-variables/
---

# User-defined variables

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/user-defined-variables/)

A user-defined variable is setting for certain blocks that lets the trader set a block value when starting an algo. User-defined variables help you create multi-purpose algos than can be configured dynamically and differently each time the algo is used. The following blocks can be designated as variable blocks:

* [Bool](../../../basic-blocks/bool-block.md) block
* [Instrument](../../../trading-blocks/instrument-block.md) block
* [Number](../../../basic-blocks/number-block.md) block
* [Price](../../../trading-blocks/price-block.md) block

By setting one or more of these blocks as user-defined variables, you create an algo that can be used for different instrument, prices, and quantities. User-defined variables appear as algo parameters in [Algo Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) and [Autotrader](../../../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) widgets in the [Trade](https://library.tradingtechnologies.com/trade/index.html) app.

![User-defined variables in Algo Dashboard](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bc-user-variables-in-algo-dashboard.png)

Additionally, some variable blocks can be linked to Microsoft Office Excel, allowing the trader to alter the block’s value directly through an Excel sheet (see [Excel Integration with TT](../../../../../trade-kb/reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md) for more information).

When a block is designated as a user-defined variable, its information appears as a new entry in the **Variables** tab of the **Information Panel**, allowing you to reconfigure the name, value, type, and the description of the variable during development.

![User-defined variables in the Variables tab](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-variables-panel.png)

**Notes:**

* The value of a user-defined Instrument block cannot be altered while the algorithm is running; it must be set prior to the launch of the algorithm.
* Changing values of user-defined variables in the tab during development and testing does not change the values defined for the blocks in the **Block Properties** panel.

←[Previous PostMessage timing](message-timing.md)

[Next PostAlgo deployment and approvals](algo-deployment-and-approvals.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bc-user-variables-in-algo-dashboard.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-variables-panel.png
