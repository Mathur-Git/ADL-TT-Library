---
title: Care orders overview
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-orders-overview/
---

# Care orders overview

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-orders-overview/)
>
> **Interpreted in:** [Order Types & Execution § Care orders & the TT OMS lifecycle](../../../../guides/order-types-and-execution.md#care-orders-the-tt-oms-lifecycle)
>
> **Also in this section:** [Order Book reference](../reference-care-orders/order-book-reference-2.md)

TT provides the ability to submit and manage care orders, which allow you to submit order intentions to another
trader or trading desk for customized handling and execution. For example, a portfolio manager might need to buy a
quantity of contracts sufficiently large that it would adversely affect the contract price. In such a case, the
portfolio manager might want to create the initial care order, but give it to an execution trader or broker to work
the order.

Care orders can be submitted from a FIX-enabled system such as a
third-party order management system, from another user via a TT screen, or [directly from the Order Ticket](../task-care-orders/submitting-care-orders.md) on your own TT screen. Care orders can
specify the contract, price, quantity and buy/sell direction, or provide a fully qualified order specification
including detailed order parameters. They can also include specific text instructions for the execution trader or
broker to better understand your intentions for staging the order.

## Care Order users

User’s who share an account or have been assigned to the same account with order staging permissions enabled can view
and manage care orders in their Order Book or orders pane of their Order and Fills widget:

Note The Order Book and Orders and Fills widget (OFW) strictly prevent actions on care orders when “OMS Allowed” is not enabled for the user in Setup. This includes preventing cancelling care orders, modifying care orders, claim/unclaim, placing child orders on care orders, bulking/stitching/splitting, passing care orders, accepting/rejecting passed care orders, and releasing fills on care orders. TT Admins can enable “OMS Allowed” via [TT user Setup User Permissions](https://library.tradingtechnologies.com/user-setup/oms-enabling-tt-oms-for-users.html).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-care-order-overview1.png)

## Care Order terms

When describing care order functionality in this topic, the following terms are used:

* Originator — The user who creates a care order to be executed or managed by another
  user. For example, an originator might be a portfolio manager at a buy-side firm or a buy-side internal
  execution trader.
* Owner — The user who currently claimed and owns the order submitted by another user and enters orders to
  the exchange (i.e., manages a care order). For example, an owner typically may be a sell-side broker executing
  trades on behalf of the buy-side firm, or a broker who has received a phone call and uses the TT screen to stage
  the order to himself.
* Care order — An order submitted for the purpose of being worked and managed by another user.
* Parent order — In TT, care orders are treated as synthetic “parent” orders processed internally by the TT
  system and never sent to the exchange.
* Child order — In TT, the “child” order is associated with the parent care order, and is sent to the
  exchange as either exchange native orders or TT synthetic orders to fill the care order.

[Next PostOrder Exceptions Widget](order-exceptions-widget.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-care-order-overview1.png
