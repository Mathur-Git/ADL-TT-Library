---
title: Submitting an Queue Holder Order
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-an-queue-holder-order/
---

# Submitting an Queue Holder Order

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-an-queue-holder-order/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Quoting and hedging](../../../../guides/spread-trading-autospreader.md#quoting-and-hedging)

To submit a queue holder order:

1. For an Autospreader spread with the **Queue Holder Orders** setting enabled, open or launch it in an MD Trader widget.
2. Specify the order parameters and enable the **QH** button.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-1.png)
3. Enter the order at the desired side and price level.

   Orders are placed in the legs at the number of price levels specified in Queue Holder settings for the spread. In this example, the NOB spread submits twice the spread quantity for the ZN leg with queue holding orders at two additional price levels.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-2.png)

**Note**: If you submit an order for a spread with queue holder enabled from a [Market Grid](../../../viewing-market-data/market-grid/description-market-grid/introduction-to-market-grid.md) widget, the order always submits it with the configured queue holder settings. If you want to disable queue holder functionality, you must use the [MD Trader](../../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) widget.

When Autospreader determines that it needs to reprice the quoting order to maintain the spread price, it updates the queue holder orders as follows:

* When the new quoting order needs to move away from the inside market, Autospreader removes the order nearest the inside market and submits a new order at the price level at the end of the queue holder trail.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-away.png)
* When the new quoting order moves toward from the inside market, Autospreader removes the order at the end of queue holder trail and submits a new order at a price level toward the inside market.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-toward.png)

←[Previous PostSubmitting a Sniper Order](submitting-a-sniper-order.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-away.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-qh-toward.png
