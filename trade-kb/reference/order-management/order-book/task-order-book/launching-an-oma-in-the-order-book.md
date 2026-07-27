---
title: Launching an OMA in the Order Book
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/launching-an-oma-in-the-order-book/
---

# Launching an OMA in the Order Book

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/launching-an-oma-in-the-order-book/)

If you have access to an Order Management Algo (OMA), you can launch it for an order from the Order Book. To launch an algo for an existing order:

1. Select the desired order.
2. Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-launch-oma-algo-2.png), and select the OMA algo to run.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oma.png)
3. Enter the information required by the algo, and click ![Launch Algo](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-green-select-algo.png).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-oma-params.png)

## Linking two orders using the OCO Order Management Algo

TT provides you with the ability to select two working orders in the Order Book, and apply an OCO (Order Cancels Order) Order Management Algo (OMA). This allows you to select which child orders you want working in the market as part of an OCO.

**Note**: The following types of orders cannot be converted to OCOs:

* TT Order Type parent orders
* Autospreader® parent orders
* Aggregator parent orders
* OTC orders

To link two orders as an OCO:

1. Select two orders in the Order Book.
2. Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-launch-oma-algo-3.png), and select the **OCO** algo from the **Shared with me**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma.png)
3. Ensure there are TT Order IDs for both working orders in the **TTOrderKey** fields and enter the other algo parameters as needed (e.g., Co-location).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma2.png)
4. Click ![Launch Algo](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-green-select-algo-1.png).The parent OCO order appears in the Order Book with “OCO” displayed in the **Contract** column and **AlgoName** column. The related child orders have the same OMA order ID displayed in the **OMAOrderID** column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma3.png)

←[Previous PostMonitoring rejected orders in the order book](monitoring-rejected-orders-in-the-order-book.md)

[Next PostConfirming fills in the Order Book](confirming-fills-in-the-order-book.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-launch-oma-algo-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oma.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-green-select-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-oma-params.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-launch-oma-algo-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-green-select-algo-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-launch-oco-oma3.png
