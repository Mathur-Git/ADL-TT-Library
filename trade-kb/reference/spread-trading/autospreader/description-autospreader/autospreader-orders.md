---
title: Autospreader Orders
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/autospreader-orders/
---

# Autospreader Orders

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/autospreader-orders/)

When an Autospreader order is entered, all potential outright orders, including all quoting and all possible hedge orders, are position risk-checked before being submitted into the market. If any of the potential orders fails the risk check, no orders are placed and the whole synthetic spread order is pulled.

Once your Autospreader order passes the risk-check and is working in the market:

* Removing the spread order deletes all quoting and position reserve orders for that spread.
* If position reserve orders are changed in any way (e.g., deleted):
  * Non-legged spread orders, including all their quoting orders, are deleted.
  * Legged spread orders are not deleted, hedge orders remain working, but their quoting orders are deleted.

For example, if you configure and buy a two-legged spread with a 1 to 1 ratio and quoting in both legs, all potential orders (the two quoting orders and the two hedge orders) are risk-checked against your position limits. The resulting worst case position for this example is long two contracts in Leg A and short two contracts in Leg B. These quantities must pass the pre-trade risk check, otherwise the spread order is not allowed.

## When a contract closes in Autospreader

When any of the contracts in a working spread closes, Autospreader pulls all quoting leg orders and deletes the spread. This is to prevent spreads from getting legged when a contract closes because Autospreader cannot properly hedge the remaining working orders.

When any of the contracts in a working spread closes and there are working hedge orders, Autospreader pulls all quoting leg orders, but the hedge leg orders and spread will remain working in a legged state.

## Viewing synthetic spread orders

If a spread color identifier is selected for the synthetic spread instrument, the vertical color bar appears on the synthetic spread orders in the MD Trader widget for each leg, as well as in the
Order Book.

## Supported order types and TIFs for Autospreader orders

When submitting Autospreader parent orders, the following order types are supported:

* [Limit](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md#limit-type)
* [TT Iceberg](../../../basic-order-entry/tt-order-types/description-tt-order-types/tt-iceberg-order.md)
* [TT Timed](../../../basic-order-entry/tt-order-types/description-tt-order-types/tt-timed-order.md)
* [TT Time Weighed Average Price (TWAP)](../../../basic-order-entry/tt-order-types/description-tt-order-types/tt-time-weighted-average-price.md)

For Autospreader parent orders, the following TIFs are supported:

* [Day](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [GTC](#GTC)

**Note**: Both the quote and hedge orders are submitted with the same order type and TIF as the parent spread order.

## Autospreader GTC orders

Submitting an Autospreader order as GTC allows you to work the spread order across market sessions. Both the quote and hedge orders are submitted as GTC.

When the underlying markets transition to a closed state, Autospreader does not attempt to change or cancel the quote or hedge orders. When the markets transition back to an open state (including Pre-Open), Autospreader resumes managing the child orders.

When spreading products with different session close times, Autospreader cancels the quote order when a leaning market transitions to a closed state. When the leaning market transitions back to an open state, Autospreader resubmits the GTC quote order.

In the event of Autospreader server maintenance or a server crash, all spread orders are canceled as soon as the quote orders are canceled. If a market is closed when the server restarts, Autospreader will cancel any remaining quote orders as soon as the market transitions to a state that allows cancels (i.e., Pre Open).

### Autospreader GTC dependencies

Autospreader requires that the exchange natively supports GTC when the “Active Quoting” option is enabled for that leg. If the exchange does not support GTC, Autospreader rejects the spread order. If “Active Quoting” is disabled for that leg and the exchange does not support GTC, Autospreader submits the hedge orders as
Day (GTD) orders.

## Changes to working Autospreader orders

Parent Autospreader orders can be modified in the Order Book using the “Change” button. For example, the TextTT value on a working Autospreader order can be modified using the “Change” button without the need to perform a “Cxl/Replace”. The new value on the working parent is automatically applied to the child leg orders. Changes to a filled Autospreader parent order are not applied to the child order fills.

**Note**: If changing TIF on a working Autospreader order in the Order Book, a “Cxl/Replace” action is required.

## Parent Order Fill Quantity Calculation

Autospreader calculates the execution quantity of a parent spread order by evaluating a valid range of potential spread units across all legs.

This approach maximizes the reported parent fills without ever exceeding the actual fill capacity of any individual leg.

To determine the final execution quantity, Autospreader first calculates a potential range—defined by a lowerBound and upperBound for each leg’s spread units based on its defined ratio:

* **For legs with a ratio < 1:** The bounds are calculated to allow for the variances inherent in fractional spread units.
  * *lowerBound = (filledQty / ratio)*
  * *upperBound = (filledQty + 1 – ratio)*
* **For legs with a ratio >1:** A range is not applicable and the bounds are strictly tied to the exact mathematical calculation without the +1 variance (i.e. the lower and upper bounds are equal).

Once the bounds for all individual legs are determined, Autospreader calculates the optimal balance across the entire spread using the following formula:

* *execQty = min(max(lowerBound), min(upperBound))*

This calculation ensures that the reported parent fill quantity accurately reflects the maximum possible spread completions while strictly respecting the limiting fill capacities of each individual leg.

←[Previous PostSpread Configuration Spread Review](spread-configuration-spread-review.md)

[Next PostAutospreader rules overview](autospreader-rules-overview.md)→

