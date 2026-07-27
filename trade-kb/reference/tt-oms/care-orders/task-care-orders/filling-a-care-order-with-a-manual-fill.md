---
title: Filling a care order with a manual fill
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/filling-a-care-order-with-a-manual-fill/
---

# Filling a care order with a manual fill

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/filling-a-care-order-with-a-manual-fill/)

TT provides the ability to fill a care order in the care order account with a manual fill and simultaneously create an offsetting fill in your own account, allowing you to fill customer orders with the firm level position in mind. An offsetting manual fill is created with the same price and quantity as the original manual fill, but in the opposite Buy/Sell direction.

Care orders can also be manually filled in your own staging account. Accounts are listed in the Order Ticket as either “Live Accounts” with exchange connections or “Internal Accounts” without exchange connections. Selecting an internal account allows you to manually fill care orders in your firm’s own staging account.

**Note**: Ensure that the manual fill account has **Update positions** allowed on the **Accounts** | **Restrictions** tab in Setup.

To fill a care order with a manual fill:

1. Click the **B** (Buy) or **S** (Sell) button in the **B/S** column for the claimed order.
2. In the Order Ticket, set the quantity and price of the manual fill or use the default values.

   **Note**: Off-tick average prices up to seven decimal digits can be entered in the Order Ticket when
   creating a manual fill for a care order.

   **Tip**: If you click the account selector and choose an internal account, **Manual Fill** is
   automatically selected in the order type field.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-internal-manual-fill.png)
3. In the Order Ticket, click the drop-down arrow in the order type field and select **Manual Fill**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-add-manual-fill-offset-1.png)

   **Note**: The **Manual Fill** option is grayed out if positions cannot be manually updated in the
   account. Contact your administrator to allow manual fills in the account.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-gray-manual-fill.png)

   The Order Ticket shows the manual fills for the care order account (e.g., CustA) and offsetting account. By
   default, the same account is used to offset the fill.

   **Tip**: When filling a care order with a manual fill, you can [add a Manual Fill custom action button to the
   Order Ticket](../../../basic-order-entry/order-ticket/task-order-ticket/adding-order-ticket-custom-action-buttons.md) using the right-click **Edit custom action buttons** option.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-custom-button-manual-fill1.png)
4. If working a staged spread order or multi-leg instrument, adjust the spread price or leg prices of the manual
   fill as needed.

   As you adjust one leg price, the price of the other leg adjusts automatically to achieve the spread price. If
   you change the spread price in the Order Ticket, the leg prices will also adjust accordingly.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-spread-manual-fill.png)

   **Note**: You can also create manual fills for synthetic inter-product spread orders that were staged into
   TT via a FIX enabled system.
5. Optional: Click the **Price off tick** selector to allow orders with off-tick prices to be entered. If
   **Price off tick** is not selected, orders with off-tick prices will be rejected.
6. Optional: Click the **Offset Account** selector to choose a different offset account (e.g., A.111) or select
   “None”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-offset-select.png)

  
7. Click the **Buy** or **Sell** button in the Order Ticket.

   The owner’s manual fill and offsetting manual fill are displayed as “Admin” fills in the **ManualFill**
   column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-add-manual-fill-offset.png)

   Both the owner and originator also see the manual fill in the care order account (e.g., CustA) in the Fills
   pane, and see the **% Filled** column updated for the partial fill in the Order Book pane of their Orders
   and Fills widgets.

**Local Fills**

To help manage your local view of positions and risk, you can select **Local Fills** in the order type dropdown menu when creating a manual fill.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/local-fills.png)

When you add a local fill and click **Publish**, the fills are only visible to you and not visible to others who share your account. Local manual fills are stored on your machine, so they do not appear in a workspace opened on another machine during the same trading day.

Local fills do not affect any risk checks or limits that are set on the account, and do not rollover to the next trading session. These fills appear in the Fills widget with a status of “Local” in the **ManualFill** column.

←[Previous PostAssigning Fills and Orders to Care Orders](assigning-fills-and-orders-to-care-orders.md)

[Next PostSubmitting related child orders](submitting-related-child-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-internal-manual-fill.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-add-manual-fill-offset-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-gray-manual-fill.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-custom-button-manual-fill1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-spread-manual-fill.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-offset-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-add-manual-fill-offset.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/local-fills.png
