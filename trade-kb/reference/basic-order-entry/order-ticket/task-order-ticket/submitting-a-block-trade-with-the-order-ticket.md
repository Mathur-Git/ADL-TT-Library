---
title: Submitting a block trade with the Order Ticket
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/task-order-ticket/submitting-a-block-trade-with-the-order-ticket/
---

# Submitting a block trade with the Order Ticket

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/task-order-ticket/submitting-a-block-trade-with-the-order-ticket/)

You can submit block trades using the Order Ticket in the Market Grid widget. In the Order Ticket, the **Block** Order Type is only available for exchanges (e.g., EEX) and accounts that support block trades.

To submit a block trade with the Order Ticket

1. In the Market Grid, left-click the Ask/Bid or the AskQty/BidQty cell next to the selected contract to open an **Order Ticket**.

   The Order Ticket widget appears.

   **Note**: You can also open an order ticket with a right click and selecting Order Ticket from the Open menu.
2. In the Order Ticket widget, select the **Block** order type.

   When **Block** is selected as the Order Type, the additional fields required for submitting the order are displayed. The Account and TIF fields are cleared, grayed out, and disabled.
3. Enter the Price and Quantity for the order.

   You must adhere to the exchange’s rules for minimum quantity to send a block order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/block-submit1.png)
4. In the block trade configuration, populate the Counterparty field with the Exchange Member ID of the sell-side trader.

   This value comes from the exchange and also appears as the first five (5) characters of the Default User ID listed in Setup. For more information, refer to the Counterparty ID section below.
5. Press **Submit** to send the order into the market.

←[Previous PostSubmitting a cross trade](submitting-a-cross-trade.md)

[Next PostAdding Order Ticket custom action buttons](adding-order-ticket-custom-action-buttons.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/block-submit1.png
