---
title: Adding Order Ticket custom action buttons
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/task-order-ticket/adding-order-ticket-custom-action-buttons/
---

# Adding Order Ticket custom action buttons

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/task-order-ticket/adding-order-ticket-custom-action-buttons/)

If you frequently use one or more order types, you can add custom action buttons to the Order Ticket for each order type instead of selecting it from the order type selector. Custom action buttons can be added for:

* Manual fills for care orders
* Exchange order types
* TT order types
* User-defined Order Ticket Algos
* User-defined Synthetic Order Algos
* Time-in-Force (TIF) order restrictions

For example, if you frequently submit Stop Limit orders and TT Time Sliced orders and use a Good-Til-Cancel TIF, you can add custom action buttons as shown below.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-action-buttons.png)

When you click a custom order type button, it automatically sets the order type or TIF. The button remains active until you unselect it, so you can quickly place multiple orders without having to select an order type or TIF for each time.

To add custom action buttons to the Order Ticket:

1. Right-click in the Order Ticket and select **Edit custom action buttons**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-menu.png)

   The custom action buttons dialog box appears.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-blank.png)
2. Click “+” and click the drop-down arrow in the **Type** field to select an order type, algo, or TIF.

   **Tip**: When adding a manual fill button to the Order Ticket for a care order, scroll to the bottom
   of the order types list to select “Manual Fill”.
3. If you have created [order templates](../../tt-order-types/description-tt-order-types/tt-order-types-overview.md#order-templates) for a TT Order Type or custom algo, click **Template** and select the template to assign to the button.

   When the button is clicked, the order will automatically use the values defined in the template, and will not display the fly-out.
4. Optionally, click the **Label** field to customize the button name.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-label.png)
5. Click “+” to add additional buttons as needed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-config.png)

   **Note**: Up to 50 custom actions buttons can be configured on an order entry widget.
6. Enter a value in the **Columns** field to set the number of columns to use for displaying the buttons.
7. To automatically wrap buttons based on the length of the text, check the **Auto-wrap** checkbox.
8. Verify the display of the buttons in the **Preview** column and click **OK** if you want to add the button configuration as it appears.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-preview.png)

   The custom buttons appear in the Order Ticket.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom.png)

←[Previous PostSubmitting a block trade with the Order Ticket](submitting-a-block-trade-with-the-order-ticket.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-action-buttons.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-blank.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-label.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom-preview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-custom.png
