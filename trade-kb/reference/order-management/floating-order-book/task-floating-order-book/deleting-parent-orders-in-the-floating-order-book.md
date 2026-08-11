---
title: Deleting parent orders in the Floating Order Book
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/floating-order-book/task-floating-order-book/deleting-parent-orders-in-the-floating-order-book/
---

# Deleting parent orders in the Floating Order Book

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/floating-order-book/task-floating-order-book/deleting-parent-orders-in-the-floating-order-book/)

Using the “Delete parent…” options in the Floating Order Book, you have the ability to delete a parent Autospreader or Aggregator order and leave the related child orders working in the market. You can use this option for a single order, all quote orders on a specific leg, or quote orders for all legs.

When you delete the parent order, Autospreader or Aggregator will abandon and no longer manage the child order, and Autospreader will not send hedge orders if the abandoned order is filled.

To delete parent orders in the Floating Order Book

1. Launch the Floating Order Book for a working child order (e.g., Autospreader quoting leg).
2. In the **Delete Parent** column, click the drop down arrow to display the delete options.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-delete-parent.png)
3. Select one of the following:
   * **Delete parent and leave this order** — The related child order remains working in the market when the parent is deleted.
   * **Delete parent and leave quote orders for this leg** — For the selected leg, all child quote orders related to the deleted parent order remain working in the market.
   * **Delete parent and leave all quote orders** — For all legs, child quote orders related to the deleted parent order remain working in the market.

   **Note**: For Aggregator orders, you can launch the Floating Order Book from the parent order for the aggregated instrument and view all related child orders for each leg.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-delete-parent-agg.png)

←[Previous PostDeleting orders in the Floating Order Book](deleting-orders-in-the-floating-order-book.md)

[Next PostLaunching an OMA in the Floating Order Book](launching-an-oma-in-the-floating-order-book.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-delete-parent.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-delete-parent-agg.png
