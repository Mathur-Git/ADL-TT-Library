---
title: Market-making algos
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/market-making-algos/market-making-algos/
---

# Market-making algos

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/market-making-algos/market-making-algos/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Market-making algos (MMAs)](../../../guides/algo-ops.md#market-making-algos-mmas)

TT offers a suite of algos that provide automated order entry strategies to quote a market based on a set of input
parameters. Users are able to customize the quoting behavior, specify an action taken after a fill occurs, and control
the risk parameters per instance. The strategies can be run from either [Autotrader](../autotrader/description-autotrader/autotrader-overview.md) or [Algo Dashboard](../algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md).
The values can be supplied manually by the user, [linked from
Excel](../excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md), or [loaded using order templates](../algo-dashboard/task-algo-dashboard/managing-algo-templates.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pa-accessing-market-making-algos.png)

TT provides the following market-making algos:

* **[Direct Entry](../../basic-order-entry/tt-order-types/description-tt-order-types/direct-entry-mma.md)**:
  Submits the quoting orders based on the direct price supplied in the **Bid
  Prc** and **Ask Prc** inputs. The working orders will automatically reprice based on any
  changes to the supplied bid/ask price values.
* **[Single Theo](../../basic-order-entry/tt-order-types/description-tt-order-types/single-theo-mma.md)**:
  Submits the quoting orders a user-defined number of ticks (**Bid Offset**
  and **Ask Offset**) from a single theoretical price (**Theo Price**). The working orders
  will automatically reprice based on any changes to the supplied theoretical value or offsets.
* **[Bid/Ask Theo](../../basic-order-entry/tt-order-types/description-tt-order-types/bid-ask-theo-mma.md)**:
  Submits the quoting orders a user-defined number of ticks (**Bid
  Offset** and **Ask Offset**) from theoretical bid/ask price (**Theo Bid** and
  **Theo Ask)**. The working orders will automatically reprice based on any changes to the supplied
  theoretical values or offsets.
* **[Market Base](../../basic-order-entry/tt-order-types/description-tt-order-types/market-base-mma.md)**:
  Submits the quoting orders a user-defined number of ticks (**Bid Offset**
  and **Ask Offset**) from the current inside market of the quoted instrument. The working orders will
  automatically reprice based on the movement of the market or changes to the offsets.
* **[Reference
  Market](../../basic-order-entry/tt-order-types/description-tt-order-types/reference-base-mma.md)**: Submits the quoting orders a user-defined number of ticks (**Bid
  Offset** and **Ask Offset**) from the current inside market of the reference instrument
  (**Ref Instrument**). The working orders will automatically reprice based on the movement of the
  reference market or changes to the offsets.

## How the algos work

The [algo parameters](#algo-parameters) allow you to customize the quoting behavior, specify an action
taken after a fill occurs, and control the risk parameters per instance.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pa-direct-entry-algo-in-autotrader.png)

The quoting orders are submitted based on the base price and quantity inputs and may be adjusted depending on the
**If Quote Outside Join Mkt, If Quote Inside Join Mkt**, and **Don’t Cross Market**
settings. The strategy will automatically reprice quoting orders upon updates to the base price inputs. You can
control the frequency of order updates with the **Quote Throttle** parameter. When a fill is received,
the algo can automatically submit cover orders a specified number of ticks (**Cover Offset**) away from
the fill price.

Based on the **Manual Requote** setting, the algo will automatically requote after the **Fill
Throttle** has passed or suspend quoting on the side of the market that received the fill until the
**Requote** button is clicked. The quote order will either be reduced or canceled based on the open
position per instance versus the **Max Pos** allowed. The algo also gives you the option to reset the
open position, if needed.

Notes:

* The user must enter a max position value for the algo to run; otherwise the strategy will pause.
* If the **Enable Cover Orders** parameter is enabled after starting the strategy, it will only
  consider fills achieved after that point.
* If no fill throttle is entered, the algo will consider the quote throttle prior to requoting.

Warnings:

* At this time TT recommends that you do not attempt to resume the algo from a paused state. Doing so will result in
  the momentary use of stale prices which can result in an unintentional fill.
* Any manual intervention with the orders managed by the algo will cause the strategy to stop managing those orders.
  The algo will no longer work an order on that side of the market.

## Viewing and Editing an Algo

TT’s Market Making Algos are shared globally by TT. This allows you to use TT’s [Algo Design Lab (ADL)](../../../../adl-kb/reference/adl-overview/introduction-to-adl/description-introduction-to-adl/adl-algo-design-lab-overview.md) to view and edit any Market Making Algo’s logic.

To view and edit an algo, open the [ADL Canvas](../../../../adl-kb/reference/adl-overview/introduction-to-adl/description-introduction-to-adl/introducing-the-new-adl-canvas.md) and select **File**, then **Open** from the toolbar at the top of the canvas. ADL displays a list of all available [Shared Algos](../../../../adl-kb/reference/adl-overview/advanced-concepts/description/algo-sharing.md).

Once opened, you can save a copy and update this version of the algo with your own logic. Viewing the Market Making Algos can serve as a starting point for understanding the logic’s intentions and a great way to learn how to build algos in ADL.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-logic-source.png)

## Algo parameters

| Parameter | Description | Used by |
| --- | --- | --- |
| Instrument | Contract for which to submit quote/cover orders (and the market to use when determining the base price for the Market Base algo). | All |
| Bid Prc | Direct price to submit the buy quoting order. | [Direct Entry](#direct-entry) |
| Ask Prc | Direct price to submit the sell quoting order. | [Direct Entry](#direct-entry) |
| Theo Price | Base price to submit the buy and sell quoting orders (Single Theo) | [Single Theo](#single-theo) |
| Theo Bid | Base price to submit the buy quoting order | [Bid/Ask Theo](#bid-ask-theo) |
| Theo Ask | Base price to submit the sell quoting order. | [Bid/Ask Theo](#bid-ask-theo) |
| Ref Instrument | Contract to use for the base price to submit buy and sell quoting orders. | [Reference Market](#reference-market) |
| Ref Prc Multiplier | Adjusts the price of the reference market before calculating the base price for the quoting orders. Default setting is 1. | [Reference Market](#reference-market) |
| Bid Offset | Offset, in ticks, from the base price for the buy quoting order. Positive value is away from market, negative value is toward market | [Single Theo](#single-theo)  [Bid/Ask Theo](#bid-ask-theo)  [Market Base](#market-base)  [Reference Market](#reference-market) |
| Ask Offset | Offset, in ticks, from the base price for the sell quoting order. Positive value is away from market, negative value is toward market | [Single Theo](#single-theo)  [Bid/Ask Theo](#bid-ask-theo)  [Market Base](#market-base)  [Reference Market](#reference-market) |
| Bid Qty | Quantity of the buy quoting order. | All |
| Ask Qty | Quantity of the sell quoting order. | All |
| Enable Cover Orders | Whether to submit an offsetting order to the market when you receive a fill on the quoting order. | All |
| Cover Order Offset | Number of ticks away from the quoting order fill price at which your cover order will be submitted. | All |
| Quote Throttle: | Delay (in milliseconds) in which a quote order may be updated. The throttle is observed from the time of last order update. If a price update occurs within the throttle time, the order update will be suppressed until the throttle time has elapsed. This parameter can be used to reduce excessive quoting. | All |
| Fill Throttle | Delay (in milliseconds) in which a quote order will not update after receiving a fill. Should a second fill occur during the throttle duration, the throttle time will be reset. | All |
| Max Pos | Maximum open position (used for both long and short) before the algo stops quoting the position-increasing side of the market. | All |
| Manual Requote | Whether to stop the algo from automatically requoting the same side of the market as the fill; cover orders will remain working. If this parameter is set to True, the **Requote** button will need to be clicked to resume quoting. | All |
| If Quote Outside, Join Mkt | Whether to adjust a quoting order to the current market price when the calculated quote price is outside the inside market price. | All |
| If Quote Inside, Join Mkt | Whether to adjust a quoting order to the current market price when the calculated quote price is better than the inside market price. | All |
| Don’t Cross Market | Whether to prevent a quoting order from crossing the inside market. | All |
| Use Cancel/ Replace | Whether to reprice the quoting order with a cancel/replace rather than using change. | All |
| TIF | Allows you to set one of the following time-in-force order restrictions for the algo: Day, GTC, IOC, FOK, Day+ (night session), GTC+ (night session). **Note**: Supported TIFs vary by exchange. | [Single Theo](#single-theo)  [Bid/Ask Theo](#bid-ask-theo)  [Direct Entry](#direct-entry) [Reference Market](#reference-market) |
| Requote | Click the button to resume quoting after a fill has occurred when Manual Requote is set to True. | All |
| Reset Open Pos | Click the button to reset your current open position for the running instance back to zero | All |

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pa-accessing-market-making-algos.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pa-direct-entry-algo-in-autotrader.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-logic-source.png
