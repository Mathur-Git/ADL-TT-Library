---
title: TT Premium Order Types Overview
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-premium-order-types-overview/
---

# TT Premium Order Types Overview

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-premium-order-types-overview/)

## What is a TT Premium Order Type?

Similar to [TT Order Types](../../tt-order-types/description-tt-order-types/tt-order-types-overview.md), the TT Premium Order Types use
synthetic orders to manage the submission and execution of other orders in
the market. TT Premium Order Types provide more robust order execution
functionality than exchanges support natively. They offer order types not
supported by exchanges or provide more options than exchange-native order
types provide.

A TT Premium Order Type order comprises two parts:

* A synthetic parent order that runs on an Algo Server that is usually co-located with the
  exchange on which the instrument trades. The parent order manages the
  entry and execution of its child orders.
* Native child orders that are sent to an exchange for order execution based
  on the selected TT Premium Order Type and its configuration parameters.

**Note:** At this time, TT Premium Order Types are not available in the Prod-SIM
environment.

## TT Premium Order Type Features

TT Premium Order Types offer the following features:

* Historical/Empirical Trade Distributions: Automated child order sizing
  based on synthetic objective and product to blend in with “normal” market
  activity.
* Matching Engine Awareness: Product-specific order sizing logic with respect
  to Pro-Rata, FIFO, Split, etc. for optimal interaction with exchange
  matching algorithm.
* Product-specific Forecasting: Volatility and volume forecasts driving
  benchmark order logic include built-in awareness of seasonality and
  events to optimize forecasts.
* Multiple Benchmark Strategies: Variety of benchmark order types allows for
  aligning execution with the overall trading objective.
* Post-Trade Analytics: Performance reports and reviews with product experts to review, discuss and optimize usage
  for continuous improvement of execution processes.
* Simplified Trading Workflow: Create templates and custom action buttons for
  one-click initialization minimizing workflow interruptions.

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

## Available TT Premium Order Types

The following table lists all order types available on the TT platform.
However, the
[User Account
Permissions](https://library.tradingtechnologies.com/user-setup/us-user-account-permissions.html)
in TT User Setup determines the actual order types shown in order entry
widgets.

| **TT Order Type** | **Description** |
| --- | --- |
| [TT Brisk](tt-brisk-order.md) | Attempts to fill the parent order closer to when the order enters the market based on the order’s Start Time. |
| [TT Close](tt-close-order.md) | Attempts to fill the order closer to the order’s end time price. |
| [TT POV](tt-pov-order.md) | Tracks and reacts to real-time market volumes to target a user-defined participation rate. |
| [TT Prowler](tt-prowler-order.md) | Combines enhanced iceberg, pegging and sniping capabilities into an order type that allows the user to customize values such as the minimum and maximum amounts to show in the market. |
| [TT Scale POV](tt-scale-pov-order.md) | Tracks and reacts to real-time market volumes to target a user-defined dynamically adjusting participation rate. |
| [TT Splicer](https://library.tradingtechnologies.com/trade/ttpo-splicer-order.html) | Execute synthetically defined spread instruments according to selected Sub-strategy behavior while controlling the risk of diverging from the hedge ratio.  **Note:** Available Sub-strategies include: TT Brisk, TT Close, TT TWAP+, and TT VWAP+. |
| [TT TWAP+](tt-twap-order.md) | Executes a desired order at a steady rate across the order’s time horizon. |
| [TT VWAP+](tt-vwap-order.md) | Uses historical intraday volume patterns to create a trade schedule that attempts to minimize market impact while tracking closely to the volume weighted average price over the execution horizon. |

## TT Premium Order Type order lifecycle

The basic lifecycle for a TT Premium Order Type order is as follows:

1. When creating an order, a TT Premium Order Type is selected within an
   order-entry widget and its parameter values are specified in the order
   type fly-out.

   **Note:** When creating a TT Splicer order, a synthetic TT Splicer instrument
   is created from the
   Autospreader widget by selecting the **TT Splicer** formula and populating the leg information.
2. A TT Premium Order Type order is submitted from the TT platform.
3. A synthetic parent order is created for the TT Premium Order Type on an
   Algo Server co-located with the exchange.
4. The synthetic parent order submits child orders to the market as dictated
   by the specific TT Premium Order Type.In the [Order Book](../../../order-management/order-book/description-order-book/order-book-overview.md), the parent
   synthetic order is listed, followed by each of the child orders it
   submitted.
5. As fills for the child orders are received, the parent order updates its
   working and filled quantities.
6. It also sends the fill acknowledgments back to TT to order entry and order
   management widgets, such as [MD Trader](../../md-trader/description-md-trader/md-trader-overview.md) and
   [Audit Trail](../../../order-management/audit-trail/description-audit-trail/audit-trail-overview.md).
   **Note:** When filled, a synthetic parent fill is reported
   for every native child order fill.
7. When all of the child orders have finished working, the parent TT Premium
   Order Type order is fully-filled and is removed from the Algo Server.

## Accessing TT Premium Order Types

You can access TT Premium Order Types in two ways: you can select a TT
Premium Order Type from the **Order Type** drop-down in the
[MD Trader](../../md-trader/description-md-trader/md-trader-overview.md) or
[Order Ticket](../../order-ticket/description-order-ticket/order-ticket-overview.md) widgets.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-md-trader.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-order-ticket.png)

  

**Note:** When you are launching a TT Splicer order, after creating the spread in
Autospreader, the only available order
type in the drop-down will be TT Splicer. You must click TT Splicer to continue submitting the order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-splicer-order-select.png)

## Configuring TT Premium Order Type orders

Each TT Premium Order Type displays a fly-out with its associated parameters
when selected as the order type. You can enter the desired parameter values
as well as save them as
[re-usable templates](../../tt-order-types/task-tt-order-types/managing-tt-order-type-templates.md).

When using the Order Ticket, the parameters are displayed in an embedded
panel. Based on the TT Premium Order type.

## Placing a TT Premium Order Type order

To enter a TT Premium Order Type order:

1. In the
   [MD Trader®](../../md-trader/description-md-trader/md-trader-overview.md)
   or [Order Ticket](../../order-ticket/description-order-ticket/order-ticket-overview.md) widget, choose
   the contract to trade.
2. Enter the desired order quantity and price for the order.
3. Select the desired TT Premium Order Type from the order type drop-down.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-time-sliced-intro-1.png)
4. Specify the desired parent order parameters.
5. Click **OK** to close the parameters dialog.
6. Click **Buy** or **Sell** to submit the order.The parent order is added to the widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-placed-mdt-1.png)

[Next PostTT Premium Order Type Templates](tt-premium-order-type-templates.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-md-trader.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-order-ticket.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ttpo-splicer-order-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-time-sliced-intro-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-placed-mdt-1.png
