---
title: TT Prowler order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-prowler-order/
---

# TT Prowler order

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-prowler-order/)
>
> **Interpreted in:** [Order Types & Execution § TT Premium Order Types](../../../../guides/order-types-and-execution.md#tt-premium-order-types)

## Overview

TT Prowler Premium Order Type behaves as an enhanced Iceberg order type that
allows the user to customize values such as the minimum and maximum amounts to
show in the market.

The TT Prowler order type is a liquidity seeking strategy that aims to reduce
market impact by avoiding displaying the full order size or by selectively
crossing the spread. Combines features of Random Iceberg, PEG, and Sniper type
algorithms.

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

## TT Prowler order parameters

### Order Details parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-prowler-order.png)

**Note:** Some of the parameters listed below are optional and provided so you can
enhance and customize
the execution of your orders in the market.

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Order Type | Required | Sets the order type for the parent order. Possible values include:  * [Market](../../order-ticket/description-order-ticket/order-types.md) * [Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Market](../../order-ticket/description-order-ticket/order-types.md) | Market |
| Stop Price | Conditional | The desired stop order’s price level.  **Note:** Required when **Order Type** is set to either **Stop Market** or **Stop Limit**. | 0 |
| I Would Qty | Optional | When set to any value greater than 0, **I Would Qty** setting equals the minimum top of book quantity required before the order will cross the spread.  When used, the I Would Qty parameter behaviors may cause an order to finish materially sooner than base TT Premium Order Type logic would normally determine. | Null |
| I Would Qty % | Optional | Similar to **I Would Qty**, but set as a percent of the order quantity.  **Note:** The field represents the number as a percent and should not be submitted as a decimal: a value of 70 equals 70%. | Null |
| I Would Qty Var Pct | Optional | Randomizes the **I Would Qty** and **I Would Qty %** thresholds by a specified percent in each direction.  **Note:** This field represents the number as a percent and should not be submitted as a decimal. For example, a value of 10 equals 10%.  For example, if **I Would Qty** equals 100 and **I Would Qty Variance %** equals 20, the **I Would Qty** behavior will be triggered based on available size being between 80-120, depending on randomized value selected within the variance range. |
| Max Spread Cross Ticks | Optional | If greater than 0, an order will not cut or cross a bid-ask spread that is more than the specified amount wide.  **Note:** This constraint takes precedence over I Would, With A Tick, Brisk Limit, and Cleanup % behaviors. |  |
| Max Show | Required | Maximum open display size per price level for TT Prowler orders.Can be configured with a value of zero (0) |  |
| Min Show | Optional | Minimum open display size per price level for TT Prowler orders. If **Min Show** remains blank or set equal to 0, the order always displays the amount of order quantity set by **Max Show**. Can be configured with a value of zero (0) | Null |
| Passive Price Lvl | Conditional | Allows optimal behavior to peg orders to passive price levels in the order book. If set to **No Pegging**, child orders are sent at the full limit price. For other settings, the order will rest passively priced child orders even if the limit price is marketable.   * **No Pegging**: Send at full limit price * **Primary Peg**: Peg to the top quote. * **Second Level Peg**: Peg to second book level. * **Third Level Peg**: Peg to third book level. * **Primary Plus 1**: Primary (passive) quote price, but improve the quote at 1 tick increments on the first posted order. * **Primary Plus 2**: Primary (passive) quote price, but improve the quote at 2 tick increments on the first posted order. * **Primary Plus 3**: Primary (passive) quote price, but improve the quote at 3 tick increments on the first posted order.   **Note:** Required when **Num Post Levels** is changed from the default value. | No Pegging |
| Num Post Levels | Optional | Specifies the number of price levels at which to post child orders when pegging.  When **Passive Price Levels** is set, additional resting orders may be set at subsequent price levels in order to hold queue priority.  **Note:** Can be set to greater than 0 with **Passive Price Level** set to **No Pegging (0)**. For example, you can statically layer child orders across n **Num Post Levels** to split up a parent order quantity starting from your limit price without dynamic repricing due to **Passive Price Level logic**.  **Note:** Maximum value is 20. | Default (Off) |
| Post Ticks Apart | Conditional | Specifies how many minimum price increments apart to space passive orders resting across **Num Post** Levels. |  |
| Tactical Peg | Conditional | If enabled with **Passive Price Level** not set to **No Pegging (0)**, avoids posting a passive order at the top of book price level if the order book dynamics are unfavorable. |  |
| Average Delay | Optional | Sets a random delay, in seconds, between sending new orders or replacing existing child orders. | Null |
| Brisk Limit Mode | Optional | Specifies whether the order should get more aggressive when opposite side quote price is at the limit price.  This setting can be used to manage fill rate risk, increasing the expected fill rate if the market is nearing the limit price, at the cost of higher expected slippage on executed quantity.  Possible values include:   * Default (Off) * Aggressive More At Limit: When the opposite side quote price is equal to the limit price, the order will monitor liquidity conditions tick by tick and send extra IOC (Immediate or Cancel) orders to opportunistically take additional liquidity before the market runs away. | Default (Off) |
| With A Tick Qty | Optional | Sets the size threshold to initiate aggressing orders to cross the spread and take liquidity when the opposing quote size falls to or below the set value.  The order will cross the spread when aggressive quote size falls to or below the value set by **With A Tick Qty**. | Null |
| With A Tick Qty % | Optional | Similar to **With A Tick Qty**, but expressed as a percent of the order quantity.  **Note:** The field represents the number as a percent and should not be submitted as a decimal: a value of 70 equals 70%. | Null |
| Cleanup Pct | Optional | Specifies maximum percent of parent order quantity to cross the market with if a parent order is not yet complete near the end time. |

### Precondition Details parameters

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Start Time | Required | Sets the date and time to start executing the synthetic order. Available settings include:   * **Now** to start the synthetic order immediately * **Time** to display a date/time picker so you can indicate when   to start the synthetic order. | Now |
| End Time | Required | Sets the date and time to stop executing the logic of the synthetic order. Used as an alternative to setting **Duration** |  |
| If Touched Price | Optional | Enables the inverse of Stop Price functionality: if present, a Buy/Sell order activates once the contra price is less/greater than or equal to If Touched Price. Can be used in combination with Stop and Stop Limit orders for One-Cancels-Other (OCO) type behavior, where an order activates when the market reaches either a profit taking or stop loss price. |  |
| Post Trigger Dur | Optional | The Post Trigger Duration in minutes. If set greater than 0, will adjust EndTime once market reaches Stop Price or Trigger Price to earlier of EndTime or current time plus PostTrigger Duration minutes. |  |
| End Time Override | Optional | Overrides End Time, Duration, or the default with one of several product hours related values. Available options are:   * None (Default) * Last Session Close * Next Session Close * Settlement   **Note:** If the current time is in the final continuous trading session of the day Next Session Close and Last Session Close reference the same time. | None |

←[Previous PostTT POV order](tt-pov-order.md)

[Next PostTT Scale POV order](tt-scale-pov-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-prowler-order.png
