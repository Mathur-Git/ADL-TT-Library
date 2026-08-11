---
title: Submitting a Sniper Order
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-a-sniper-order/
---

# Submitting a Sniper Order

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-a-sniper-order/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Quoting and hedging](../../../../guides/spread-trading-autospreader.md#quoting-and-hedging)

Autospreader provides the Sniper functionality as an order routing option. Sniper allows users to work spread orders without quoting a leg. Autospreader will monitor the synthetic market and simultaneously submit hedge orders across all legs when the spread price becomes available.

The ‘Active Quoting’ configuration parameter is ignored when the spread order is submitted in Sniper mode. Both Pre-Hedge and Post-Hedge rules are applied to Sniper hedge orders.

To submit a sniper order:

1. From Autospreader, launch the desired spread in an MD Trader widget.
2. Set the order parameters and enter an order quantity.
3. Click the **SNP** button to enable the Sniper functionality and enter the spread order at the desired price level.

   The SNP button is highlighted to show that SNP has been selected. Subsequent orders will be submitted as Sniper orders. To disable the Sniper function, click the highlighted (enabled) SNP button.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-submit1.png)

   When the order is entered at the implied spread price, the Sniper functionality does not submit a quoting order, but waits to submit child hedge orders in both legs that fill the working parent spread order.

   The Order Book shows the colors for the working spread order and hedge orders.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-ob.png)

   Spread fills are displayed in the Fills widget.

   The related child order fills show the parent spread order ID.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-fills-2.png)

   **Tip**: You can double-click the parent spread order ID to filter the related child order fills.

### Using Reload with Sniper Orders

The Reload order type can be used in conjunction with a Sniper order. New Reload spread orders are submitted only after the previous Sniper order is completely filled. This means that any new Sniper spread orders will not be submitted until all components from the previously-submitted spread, including working and pending units, are either filled or deleted.

For more information about submitting reload orders from MD Trader, see
[Submitting a reload order](submitting-a-reload-order.md).

←[Previous PostSubmitting a Reload Order](submitting-a-reload-order.md)

[Next PostSubmitting an Queue Holder Order](submitting-an-queue-holder-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-submit1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-as-sniper-fills-2.png
