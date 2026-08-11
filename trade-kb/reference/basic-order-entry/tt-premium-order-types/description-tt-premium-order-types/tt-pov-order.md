---
title: TT POV order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-pov-order/
---

# TT POV order

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-pov-order/)
>
> **Interpreted in:** [Order Types & Execution § TT Premium Order Types](../../../../guides/order-types-and-execution.md#tt-premium-order-types)

## Overview

The TT Percentage of Volume (POV) Premium order type tracks and reacts to real-time market volumes to target a
user-defined participation rate.

TT POV Premium Orders allow the trader to set a participation rate as a percentage of the volume traded in the
market. TT POV continues to submit child orders to match the volume percentage until the parent order is completely
filled.

Traders may use TT POV orders for certain illiquid products where a lack of data proves challenging from a modelling
perspective, or during periods where markets are exhibiting abnormal trading conditions with respect to their normal
behavior.

TT POV orders may need a larger amount of trade volume in order to completely fill the parent order. In slower
markets, this may result in the parent order only being partially filled.

For example, a trader who is looking to execute 1,000 lots on a 10-Year Futures contracts may set the
**Participation Rate** equal to 5% of volume. The POV order will will react to volume traded in the
market. If 100 contracts trade, the TT POV order will submit child orders to fill 5 contacts. To complete the entire
1,000 lot parent order, the market volume must equal a minimum of 20,000 contracts.

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

## TT POV order parameters

### Order Details parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-pov-order.png)

**Note:** Some of the parameters listed below are optional and provided so you can
enhance and customize
the execution of your orders in the market.

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Order Type | Required | Sets the order type for the parent order. Possible values include:  * [Market](../../order-ticket/description-order-ticket/order-types.md) * [Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Limit](../../order-ticket/description-order-ticket/order-types.md) * [Stop Market](../../order-ticket/description-order-ticket/order-types.md) | Market |
| Stop Price | Conditional | The desired stop order’s price level.  **Note:** Required when **Order Type** is set to either **Stop Market** or **Stop Limit**. | 0 |
| Participation Rate | Required | Gives the trader the option to set the maximum participation rate with respect to total eligible market activity.  Ineligible market volume includes orders outside of the parent limit price and orders violating the **Block Limit** parameter. | Null |
| Aggression | Optional | Influences how strongly to tilt order trajectory (TT Close, TT Brisk), how tightly to track max participation (TT POV, TT Scale POV), or how tightly to follow an order schedule (TT TWAP+, TT VWAP+).  For TT POV orders, this means:   * Setting to 0 provides the maximum fluctuation from the order’s setting. * Setting to 10 equals following the   **Maximum Participation** setting as closely as possible. | 5 |
| Block Limit | Optional | When calculating participation limits, all trades above this limit will be ignored  Supports values 5-1,000,000. | Null |
| I Would Price | Optional | Price at which you would like to aggressively attempt to fill your order, regardless of the algorithm logic.  Order aggressively tries to fill if the instrument reaches this price, irrespective of volume based tracking objectives. Should be lower than limit and arrival time ask prices for BUY orders, higher than limit and arrival time bid prices for SELL orders. | Null |
| I Would Qty | Optional | When set to any value greater than 0, **I Would Qty** setting equals the minimum top of book quantity required before the order will cross the spread.  When used, the I Would Qty parameter behaviors may cause an order to finish materially sooner than base TT Premium Order Type logic would normally determine. | Null |
| I Would Qty % | Optional | Similar to **I Would Qty**, but set as a percent of the order quantity.  **Note:** The field represents the number as a percent and should not be submitted as a decimal: a value of 70 equals 70%. | Null |
| I Would Qty Var Pct | Optional | Randomizes the **I Would Qty** and **I Would Qty %** thresholds by a specified percent in each direction.  **Note:** This field represents the number as a percent and should not be submitted as a decimal. For example, a value of 10 equals 10%.  For example, if **I Would Qty** equals 100 and **I Would Qty Variance %** equals 20, the **I Would Qty** behavior will be triggered based on available size being between 80-120, depending on randomized value selected within the variance range. |
| Max Spread Cross Ticks | Optional | If greater than 0, an order will not cut or cross a bid-ask spread that is more than the specified amount wide.  **Note:** This constraint takes precedence over I Would, With A Tick, Brisk Limit, and Cleanup % behaviors. |  |
| Cleanup Pct | Optional | Specifies maximum percent of parent order quantity to cross the market with if a parent order is not yet complete near the end time. |

### Precondition Details parameters

| Parameter Name | Required/Optional | Description | Default Value |
| --- | --- | --- | --- |
| Start Time | Required | Sets the date and time to start executing the synthetic order. Available settings include:   * **Now** to start the synthetic order immediately * **Time** to display a date/time picker so you can indicate when   to start the synthetic order. | Now |
| End Time | Required | Sets the date and time to stop executing the logic of the synthetic order. Used as an alternative to setting **Duration** |  |
| If Touched Price | Optional | Enables the inverse of Stop Price functionality: if present, a Buy/Sell order activates once the contra price is less/greater than or equal to If Touched Price. Can be used in combination with Stop and Stop Limit orders for One-Cancels-Other (OCO) type behavior, where an order activates when the market reaches either a profit taking or stop loss price. |  |
| Post Trigger Dur | Optional | The Post Trigger Duration in minutes. If set greater than 0, will adjust EndTime once market reaches Stop Price or Trigger Price to earlier of EndTime or current time plus PostTrigger Duration minutes. |  |
| End Time Override | Optional | Overrides End Time, Duration, or the default with one of several product hours related values. Available options are:   * None (Default) * Last Session Close * Next Session Close * Settlement   **Note:** If the current time is in the final continuous trading session of the day Next Session Close and Last Session Close reference the same time. | None |

←[Previous PostTT Close order](tt-close-order.md)

[Next PostTT Prowler order](tt-prowler-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-pov-order.png
