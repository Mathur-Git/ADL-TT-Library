---
title: Using ADL algos
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/description-introduction-to-adl/using-adl-algos/
---

# Using ADL algos

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/description-introduction-to-adl/using-adl-algos/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § Standard algo](../../../../guides/algo-types.md#standard-algo)

ADL and the [Trade](https://library.tradingtechnologies.com/trade/index.html) app are closely integrated so that you can easily use custom ADL algos to submit and manage orders from the Trade app. The process for creating and using an ADL algo is as follows:

* [Create an algo in ADL](#create-algo)
* [Deploy the algo to the TT Algo Server](#algo-deployment)
* [Execute the algo from the Trade app](#algo-execution)
* [Manage an algo and its child orders](#manage-algos)

### Algo creation

Using ADL, you add blocks and create connections to design an algo that implements your desired strategy.  Blocks configured to take user-defined variables will automatically appear as editable parameters within the trading application, allowing traders to modify the values before launching the algo. In the case of the Order Stack algo below, the **Instrument**, **OrderQty** and **StackDepth** inputs are all specified as user-defined variables.

![Order Stack algo](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-intro-1.png)

Once you’ve tested your algo in ADL, you are ready to deploy it to the TT Algo Server.

### Algo deployment to the TT Algo Server

Deploying an ADL algo to the TT Algo Server makes it available to the [Trade](https://library.tradingtechnologies.com/trade/index.html) app. Once the algo is deployed, it is displayed in your list of available algos within the [Algo Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md), as shown. It is also displayed in the list of available algos within the [Autotrader](../../../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) widget.

![Deployed Algo](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-2.png)

### Algo execution

From the [Algo Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md), you can specify the parameters for the algo and launch it. Below you can see that TT automatically generated input parameters for the **Instrument**, **OrderQty** and **StackDepth** blocks you configured as user-defined variables in your algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-3.png)

Once launched, the working algo order appears in the Algo Orders Pane. The algo is a parent order on the Algo Server that begins submitting its child orders to the exchange.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-4.png)

In this case, the trader set the stack depth variable to 3 and the order quantity variable to 5. The [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) widget shows that the algo successfully submitted 5-lot orders at three price levels away on both sides of the market for the selected instrument, also chosen by the trader.

**Note**: Users who run large numbers of algo instances simultaneously should check the [Algo Server limitations](../reference-introduction-to-adl/algo-server-limits.md).

### Managing algo orders

After launching an ADL algo, you can monitor and manage the child orders submitted by the algo through various order management Trade widgets, such as [Order Book](../../../../../trade-kb/reference/order-management/order-book/description-order-book/order-book-overview.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-5.png)

1. Algo (parent) order
2. Child orders submitted by the algo

For more information about managing algo orders, see the Order Book help topic, [Algos and synthetic orders overview](../../../../../trade-kb/reference/order-management/order-book/description-order-book/algos-and-synthetic-orders-overview.md).

←[Previous PostAlgos in ADL](algos-in-adl.md)

[Next PostTT Platform requirements](tt-platform-requirements.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-intro-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-adl-algos-5.png
