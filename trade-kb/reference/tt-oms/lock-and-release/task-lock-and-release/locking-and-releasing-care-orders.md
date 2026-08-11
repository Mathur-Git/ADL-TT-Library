---
title: Locking and Releasing Care Orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/lock-and-release/task-lock-and-release/locking-and-releasing-care-orders/
---

# Locking and Releasing Care Orders

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/lock-and-release/task-lock-and-release/locking-and-releasing-care-orders/)

Using the Order Book or orders pane in the Order and Fills widget, you can right-click an individual or bulked care
order and select the following **Order staging** options from the context menu:

* **Lock** — Child order fills are withheld until a later
  time.
* **Unlock** — Fills are “released” and immediately sent to the customer.

  **Note**: Released fills are [automatically allocated to the care
  order](https://library.tradingtechnologies.com/trade/all-allocation-overview.html) using the “average price with fills” algorithm in TT. The average price is calculated based on
  the price and quantity of the child order fills.

To lock and release a care order:

1. Right-click a care order in the Order Book and select **Order staging** | **Lock** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-care-order1.png)

   The status of “Locked” is displayed in the **Release** column. Any child order fills received for the care
   order will not be reported back to the customer who staged the order.

   **Note**: A split **Parent** order can be locked/unlocked, but a split **Child** order cannot be.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-column1.png)
2. To unlock the care order, right-click the order and select
   **Order staging** | **Unlock** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unlock-care-order.png)

   The **Release** column is cleared for the order and child order fill notifications will be sent back to
   the customer.

   **Note**: The **Release** column will display “Released” if the care order has any released fills.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-partially-filled1.png)

   **Tip**: Apply OMS features with a single click without having to right click and navigate the context menu to use those features. In the right-click context menu, select **Settings: Order Book | Set Order Toolbar buttons**. Select **Lock** and **Unlock**, click OK then Save. When enabled on the toolbar, each button will enable, disable and function the same as their related right click menu item.

## Locking and releasing a bulked care order

1. Right-click the parent bulked order and select **Order staging** | **Lock** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked1.png)

   The **Release** column shows that the bulked order and each original care order are locked. When the care
   order has unreleased fills, the **Release** button is enabled. Fills for working child orders will be
   delayed (locked) as long as the parent bulked order is locked.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked-after2.png)
2. To release fills for a child care order, click the “Release” button in the **Release** column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked-result-button1-1.png)

   **Note**: The column will display “Released” if the care order has any released fills.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-partial-fill-release.png)

   Released fills are also displayed in the optional **Release** column in the fills pane of the Order and
   Fills widget (the button is only available in the orders pane).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-release-fills-pane.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-care-order1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-column1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unlock-care-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-partially-filled1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked-after2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-bulked-result-button1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-partial-fill-release.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-lock-release-fills-pane.png
