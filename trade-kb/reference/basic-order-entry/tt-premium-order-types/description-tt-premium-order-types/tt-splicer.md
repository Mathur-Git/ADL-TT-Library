---
title: TT Splicer
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-splicer/
---

# TT Splicer

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-splicer/)
>
> **Interpreted in:** [Order Types & Execution § TT Premium Order Types](../../../../guides/order-types-and-execution.md#tt-premium-order-types)

## Overview

The TT Splicer Premium Order Type allows a user to define a synthetic spread and execute according to a selected
Sub-strategy (TT Brisk, TT Close, TT TWAP+, TT VWAP+). The Brisk, Close, and VWAP+ sub-strategies utilize a weighted volume forecast based on the leg composition to form the baseline of the coordinated execution schedule.

Optional parameters for Leg Risk Aversion and Hedge Discretion Ticks allow a user to control hedging behavior when
leg fills occur to exert additional control over synthetic legging risk.

**Note:** At this time, TT Premium Order Types are not available in the Prod-SIM
environment.

## Prerequisites

### FIX Order Gateway

Access to TT Premium Order Types requires a dedicated FIX Order Gateway. Please [contact our Sales team](https://tradingtechnologies.com/contact/) to discuss connectivity options and setup.

### Enabling User’s Access

Prior to using any TT Premium Order Type, your administrator must enable access by updating the settings at the user level in the [User Account Permissions](https://library.tradingtechnologies.com/user-setup/us-user-account-permissions.html) settings or at the account level using the [Account Restrictions](https://library.tradingtechnologies.com/user-setup/ac-setting-account-restrictions.html) settings in Setup.

### Setting the Order Cross Prevention Rules

TT strongly recommends that accounts both enabled for the TT Premium Order Types and using account-level Order Cross Prevention, should utilize the **Cancel Resting (wait for ACK)** option to avoid parent orders from being cancelled.

Using the **Reject New** option may cause parent orders to be cancelled due to excessive rejects preventing the order from progressing.

The **Cancel Resting (wait for ACK)** option may have child orders receive unsolicited cancels if interacting with Order Cross Prevention, and this will result in new orders being issued in place of those which were cancelled. The unsolicited cancellations will not result in a cancellation of the parent order.

For more information on Order Cross Prevention Rules, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/rl-order-cross-prevention-and-position-transfer.html) section of the Setup help.

**Note:** Firms may consult with their TT Onboarding representative with any questions regarding how these settings may impact their overall account structure.

## TT Splicer order parameters

### Order Details parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-splicer-order.png)

**Note:** Some of the parameters listed below are optional and provided so you can
enhance and customize
the execution of your orders in the market.

**Note:** Order replacement is not currently supported for TT Splicer orders.

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Order Type | Required | Sets the order type for the parent order. Possible values include:  * [Market](../../order-ticket/description-order-ticket/order-types.md) * [Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Market](../../order-ticket/description-order-ticket/order-types.md) | Market |
| Stop Price | Conditional | The desired stop order’s price level.  **Note:** Required when **Order Type** is set to either **Stop Market** or **Stop Limit**. | 0 |
| Aggression | Optional | See description of Aggression for underlying Sub-strategies. |  |
| I Would Price | Optional | Price at which you would like to aggressively attempt to fill your order, regardless of the algorithm logic.  Order aggressively tries to fill if the instrument reaches this price, irrespective of volume based tracking objectives. Should be lower than limit and arrival time ask prices for BUY orders, higher than limit and arrival time bid prices for SELL orders. | Null |
| Sub Strategy | Required | Sets the underlying Premium Order Type behavior managing execution of the TT Splicer instrument.  Possible values include:   * TT Brisk * TT Close * TT TWAP+ * TT VWAP+   **Note:** Default value is null so a user must select a Sub Strategy in order to place an order | Null |
| Leg Risk Aversion | Optional | Influences how long the algorithm will leave the parent order partially hedged after a new fill on one of the legs. Lower values give the algorithm more leeway to hold positions that are out of hedge; higher values will force the parent order to execute any unfilled legs to maintain hedge more quickly. | 5 |
| Hedge Discretion Ticks | Optional | Non-negative integer to give hedge orders allowance beyond inferred limit price in order to complete a hedge leg order. | 0 |

### Precondition Details parameters

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Start Time | Required | Sets the date and time to start executing the synthetic order. Available settings include:   * **Now** to start the synthetic order immediately * **Time** to display a date/time picker so you can indicate when   to start the synthetic order. | Now |
| End Time | Required | Sets the date and time to stop executing the logic of the synthetic order. Used as an alternative to setting **Duration** |  |
| If Touched Price | Optional | Enables the inverse of Stop Price functionality: if present, a Buy/Sell order activates once the contra price is less/greater than or equal to If Touched Price. Can be used in combination with Stop and Stop Limit orders for One-Cancels-Other (OCO) type behavior, where an order activates when the market reaches either a profit taking or stop loss price. |  |
| Post Trigger Dur | Optional | The Post Trigger Duration in minutes. If set greater than 0, will adjust EndTime once market reaches Stop Price or Trigger Price to earlier of EndTime or current time plus PostTrigger Duration minutes. |  |

←[Previous PostTT Scale POV order](tt-scale-pov-order.md)

[Next PostTT TWAP+ order](tt-twap-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-splicer-order.png
