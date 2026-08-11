---
title: Spread Configuration Order Execution
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution/
---

# Spread Configuration Order Execution

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Quoting and hedging](../../../../guides/spread-trading-autospreader.md#quoting-and-hedging)
> · the **Minimum Lean Quantity** depth-walk below is also load-bearing for
> [§ What AutoSpreader is — how the quote gets its price](../../../../guides/spread-trading-autospreader.md#what-autospreader-is)

In addition to providing you with the basic spread definition and configuration settings, the Autospreader
Configuration dialog provides you with the ability to control the quoting and hedging behavior of orders submitted for
your synthetic spread.

Quoting settings include:

* [Active Quoting](#quoting)
* [Lean on Indicative](#lean-on)
* [Minimum Lean Quantity](#lean)
* [Queue Holder](#queue)
* [Convert Quote to Hedge](#convert)

Hedging order settings include:

* [Enable Hedging](#hedging)
* [Payup Ticks](#payup)

Additional execution options:

* [Reload](#reload)
* [Sniper](#sniper)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-execution-options.png)

### Active Quoting

This quoting setting determines whether or not Autospreader actively quotes the leg. If unchecked, orders for that
leg are only sent when the other leg fills.

**Note**: You must enable this setting for at least one leg of the spread.

When creating a new Autospreader instrument, you can enable Active Quoting for a maximum of five legs. If more than five legs are enabled, a warning message is displayed:

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/06/auto-quote-max-5-legs.png)

After the instrument is created, you can enable Active Quoting for more than five legs by amending the spread.

### Lean on Indicative

This option allows you to lean on the Indicative Open price provided by an exchange during Pre-Open or Auction market
states. For Eurex, the Indicative Open price is published by the exchange when the market is crossed (Bids and Asks at
same price level) during the opening auction state. If the **Lean on Indicative** setting is enabled for a leg,
Autospreader uses the Indicative Bid/Ask or Indicative Open price as the leaning price for that leg during the opening
auction.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-lean-on-indicative1.png)

### Minimum Lean Quantity

This quoting property defines the quantity required for other legs to lean against it. Values can be predefined
variables (ThisLeg.TotalRemainingQuantity or ThisLeg.DisclosedRemainingQuantity), a formula (e.g.,
ThisLeg.DisclosedRemainingQuantity + 10) or a numeric value (e.g., 1).

When entering a formula, the text field makes intellisense suggestions for which parameters to use. The default value
of ‘ThisLeg.DisclosedRemainingQuantity’ is calculated as the disclosed remaining order quantity multiplied by that
leg’s ratio.

For example, if you set **Min Lean Qty** = ThisLeg.DisclosedRemainingQuantity for Leg 1 with a **Ratio** of “2”
and enter a spread order quantity of “10” after launching the spread, then the quote order in Leg 2 will be priced
based on walking the depth in Leg 1 until “20” are available.

**Note**: To lean against the inside market, set **Min Lean Quantity** to “1”.

### Queue Holder

This quoting property uses multiple orders per leg to maintain your position in the queue when requoting to a new
price level. The standard quoting order enters the outright market at the price determined by the spread price. The
Queue Holder orders enter at consecutive price levels away from the inside market. When Autospreader needs to reprice
quoting orders to maintain the spread price, it automatically adjusts the queue holder orders to trail the new quoting
order price.

To configure a queue holder order, you specify values that determine the number of additional price levels to quote
for the desired legs in the Autospreader widget. The following example quotes only one leg of the spread and enables
queue holder order with two additional price levels for the quoting leg.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-spread-qh-settings.png)

When you set values for one or more legs, the [MD Trader](../../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) widget adds a
**QH** button that allows a user to enable or disable the queue holder functionality before placing an
order.

For more information about submitting queue holder orders from MD Trader, refer to [Submitting a queue holder order](../task-autospreader/submitting-an-queue-holder-order.md).

### Convert Quote to Hedge

When Active Quoting is enabled for multiple legs, the default Autospreader behavior is to submit a new hedge order as
soon as it receives a quote fill and then cancel (or reduce in a partial fill scenario) the working quote order in the
hedge leg. By enabling the **Convert Quote to Hedge** parameter, you can configure Autospreader to use the working
quote order for hedging purposes.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-convert-quote-to-hedge.png)

The Convert Quote to Hedge parameter has the following options:

* **Attempt To Use Quote Order to Hedge** — Autospreader attempts to adjust the price and quantity of a
  working quote order for hedging. If there’s a pending change on the quote order in the hedge leg when Autospreader
  receives the quote order fill, it will revert to the default behavior of submitting a new hedge order instead of
  waiting for the in-flight change to complete. This option provides the lowest latency performance, but may result
  in the spread order getting overfilled.
* **Always Use Quote Order to Hedge** — Similar to the option above, this option also changes the working
  quote order for hedging. However, if there’s a pending change on the quote order in the hedge leg, Autospreader
  waits for the change to complete before converting it to a hedge order. Waiting for the exchange acknowledgment
  adds latency, but this option always guarantees the spread order will not get overfilled.
* **Always Preserve Queue Position** — This option also guarantees no overfills but prioritizes the queue
  position of quote orders in the hedge leg. In a partial fill scenario, Autospreader will first reduce the working
  quote order in the hedge leg and then send a new hedge order. This option adds latency while it’s waiting for the
  exchange acknowledgement of the quantity reduction. In a full fill scenario, this option behaves the same as the
  “Always Use Quote Order to Hedge” option.

### Enable Hedging

This setting determines whether or not Autospreader submits a hedge order for the leg after receiving a fill for the
quoting leg. This option is checked (enabled) and hidden by default when **Active Quoting** is checked
(enabled).

If **Active Quoting** is unchecked (disabled), the **Enable Hedging** option is shown for each leg of the
spread and is checked (enabled) by default. When **Active Quoting** is unchecked and **Enable Hedging** is
checked for a leg, Autospreader will only submit hedge orders for that leg.

When both **Active Quoting** and **Enable Hedging** are unchecked (disabled) for a leg as shown below, the
instrument for the leg is used simply as a pricing component for the spread. This allows a user to configure and trade
a spread that includes an instrument that is neither quoted nor hedged and doesn’t require position limits.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-ratio-zero.png)

Refer to [Use Cases](../use-cases/using-instruments-as-pricing-components-of-a-spread.md) for an example of
creating a spread using a leg as a pricing component.

### Pay Up Ticks

This hedging property indicates the number of ticks by which Autospreader will adjust the hedge order price. As soon
as a quoting order receives a fill, Autospreader would normally send an offsetting hedge order at a price that fills
the spread at the desired spread price. By configuring a Pay Up Ticks value for a leg, Autospreader works the hedge
order for a spread price based on your setting (e.g., 1 tick away from the best bid or ask) rather than hitting the
bid or lifting the offer when your quote order fills.

### Reload

This setting applies to the entire spread and gives you the ability to split a spread order into smaller disclosed
quantities to fill the total spread order quantity. When a disclosed spread order quantity is filled, the next
disclosed quantity order is submitted until the entire spread order quantity fills.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-config-reload.png)

To specify default values for submitting a spread as a reload order, enable the **Reload** checkbox and specify
the following parameters:

* **Disclosed Qty**: Indicates the portion of the spread order quantity to disclose to the market in separate
  orders until the total quantity is filled. **Note**: If set to “0” or to a value greater than the order quantity,
  the spread order will be rejected.
* **Max Exposure (clips)**: Sets the number of times the order can reload while waiting for hedge orders to fill. This setting overrides the default behavior of the **Reload** functionality. The **Max Exposure (clips)** setting specifies the number of clips or “slices”, instead of quantity, that the spread order can be legged before Autospreader stops quoting. The default value of **1** indicates that Autospreader stops reloading until any working hedge orders are filled. A disclosed quantity of **5** and a **Max Exposure (clips)** setting of **3** means Autospreader quotes up to 15 contracts (3 clips of 5) before waiting for hedge orders to fill.
* **Offset**: Sets the Reload order price to enter the market at a set number of spread increments away from the
  spread price of the initial order (lower for buys, higher for sells).
* **Delay (ms)**: Number of milliseconds to wait before submitting the next disclosed quantity order.

When you enable reload orders for a spread, the MD Trader widget automatically enables the **RLD** button. It also
pre-populates the total and disclosed order quantities with the value specified in the configuration’s **Disclosed
Qty** parameter. The user can enable or disable the reload order functionality before placing an order.

**Note**: **Reload** can be used in conjunction with **Sniper**.

For more information about submitting reload orders from MD Trader, see
[Submitting a reload order](../task-autospreader/submitting-a-reload-order.md).

### Sniper

Sniper allows users to execute orders without quoting a leg. Autospreader will monitor the synthetic market and
simultaneously submit orders across all legs when the spread price and liquidity becomes available. When a leg order
is submitted, it enters the market and is immediately filled to the extent possible. The remaining balance of the
order is left working in the market as a resting Limit order. Though not part of the spread configuration,
Autospreader provides Sniper functionality as an order routing option through MD Trader.

**Note**: In Sniper mode, the Autospreader engine will send all the orders as hedge orders to the legs to achieve the spread. The **Active Quoting** spread configuration parameter is therefore ignored. Both Pre-Hedge and Post-Hedge rules are applied to Sniper hedge orders.
When using Sniper and Reload together, for the legs that are not enabled on **Active Quoting**, **Enable Hedging** must be ticked for those legs so they would be sent as hedge orders as well.

For more information about submitting sniper orders from MD Trader, see
[Submitting a sniper order](../task-autospreader/submitting-a-sniper-order.md).

←[Previous PostSpread Configuration](spread-configuration.md)

[Next PostSpread Configuration Rules](spread-configuration-rules.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-execution-options.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/06/auto-quote-max-5-legs.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-lean-on-indicative1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-spread-qh-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-convert-quote-to-hedge.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-ratio-zero.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-config-reload.png
