---
title: Floating Order Book reference
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/floating-order-book/reference-floating-order-book/floating-order-book-reference/
---

# Floating Order Book reference

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/floating-order-book/reference-floating-order-book/floating-order-book-reference/)

### Floating Order Book columns

| Field | Description |
| --- | --- |
| Delete (Cxl) | Delete a single line (order) |
| Algo | Launch an Order Management Algo (OMA) for the order |
| Contract | The name and contract expiry for the instrument or strategy. |
| WrkQty | Working quantity of the order |
| Send | Green check button appears when a change is made to the order quantity or price |
| Price | Price of the order or fill. |
| TrigPrc | Price at which to enter an order (Shown only when an order has an associated Trigger price, such as a TT Stop or TT If-Touched order) |
| TrigQty | The quantity for triggering a TT Stop or TT If-Touched order |
| TIF | Time In Force for the order. |
| Account | Account number associated with the transaction. |
| Type | The type of instrument or options strategy. |
| Time | The workstation time the order or action was sent. In a shared order book, if users are in different time zones, the **Time** field will display in the local time of the initiated workstation and will *not* convert to the workstation times for users in other time zones.  For synthetic and algo orders, the **Time** field displays the local time based on where the Algo Server is located |
| OrdQty | Total order quantity |
| UndQty | Undisclosed quantity of a disclosed quantity order (e.g. Iceberg. TT Iceberg, Time Sliced) |
| Account | Account number associated with the transaction. |
| Type | The type of instrument or options strategy. |
| CurrentUser | TT user name of the trader associated with the transaction  For users who share an order book, this column allows you to determine which user submitted each order. You can also sort the orders by this column. |
| Parent Order | Name of the parent algo order |
| Mod | Modify user-defined parameters for a parent algo order |
| Delete Parent | Allows you to delete a parent order and leave the child orders working in the market. Refer to [Deleting parent orders in the Floating Order Book](../task-floating-order-book/deleting-parent-orders-in-the-floating-order-book.md). |
| OrigTime | Time the order was originally submitted. |
| PIQ | Shows your position in queue (PIQ) for each of your orders at a given price level. The column is hidden by default. The PIQ value is displayed when you enable PIQ in your workspace preferences. |
| TextA | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextA** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextB | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextB** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextTT | Displays an optional, user-defined text value from the Setup app or entered in the **TextTT** free-form text field in the Order Ticket. The value displayed in this column remains on submitted orders for tracking purposes in the TT system, but is not routed to the exchange.  You can show or hide the Text TT text box for a selected working order in the Order Toolbar. You can add or modify the text that displays in the **TextTT** column for the selected order.  In the **Position Manager** widget, you can now edit the **TextTT** column for **Local Fills** and **Admin Fills**. However, this is not available for **Admin SODs**.  **Note**: For Autospreader orders submitted by an ADL algo, the value is populated with the order tag of the parent algo order. |

