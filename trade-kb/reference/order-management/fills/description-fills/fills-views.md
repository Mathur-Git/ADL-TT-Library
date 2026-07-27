---
title: Fills Views
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/fills/description-fills/fills-views/
---

# Fills Views

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/fills/description-fills/fills-views/)

When launched, the Fills widget displays only fill activity for the current day. You can also display other views of the fill activity, including:

* Fill [details](fills-views.md#detail) for a specific day.
* Fills [summarized](fills-views.md#summary) by price for the current or a specific day.
* [Individual](fills-views.md#individual) fills that make a total fill quantity for an order.
* [Child](fills-views.md#child) order fills of a synthetic parent order.
* All fills shown [continuously](fills-views.md#continuous) in reverse order, beginning with the current day’s fill activity.
* [Aggregate fill quantities at each price level](fills-views.md#price) grouped by contract.

To display a list of fills for a specific day, select **Detail** from the drop-down and specify the desired date.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-detail-view.png)

To display a summarized view of a day’s fills, select **Summary** from the drop-down and specify the desired date.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-summary-view.png)

To display individual fills that make up the total fill quantity for an order, select **By Order** from the drop-down and specify the desired date.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-by-order-view.png)

**Note**: TT “slicer” order types (e.g., TT Iceberg) submit each slice as a separate child order with an individual TTorder ID, so the **By Order** option treats each slice as a separate order and groups the fills within each child order.

To display the child order fills of a synthetic parent order, such as a TT Iceberg or custom algo, select **By Order (Summary)** from the drop-down and specify the desired date.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fls-by-order-summary-view.png)

To display a continuous view of the previous session’s and current session’s incoming fills, select **Continuous** from the drop-down menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-continuous-view.png)

To see older fill activity, simply scroll down the list. As you scroll down, the Fills widget automatically retrieves another set of fills and adds them to the bottom of the list.

When selected from the drop-down menu, the **Price with Detail** view sums all child order fills and partial fills by price and displays summarized quantity totals at each price level grouped by contract. You can also view these fill details for a specific date.

Click the expander in the **Price** column to view each fill at that price level. You can rearrange and show/hide columns to create a simple summary view of your fills at each price level as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-price-with-detail-view.png)

←[Previous PostFills overview](fills-overview.md)

[Next PostFill Confirmation](fill-confirmation.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-detail-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-summary-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-by-order-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fls-by-order-summary-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-continuous-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fills-price-with-detail-view.png
