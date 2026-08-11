---
title: Night desk support
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/order-passing/use-cases-order-passing/night-desk-support/
---

# Night desk support

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/order-passing/use-cases-order-passing/night-desk-support/)

A simple use case for order passing is the use of a 24 hour “night desk” to manage unfilled orders or partially filled orders still working in the market.

In the following example, a sell-side
brokerage desk in Chicago executes customer orders during their local trading
day, and also operates a separate global support
desk (night desk) that is staffed 24 hours a day. At the end of the local session, the Chicago desk passes
management and visibility of an unfilled order still working in
the market to the night desk, then reclaims ownership of the order when they return to work the next day.

1. The Chicago group passes a working TT Time Sliced order to the Night Desk by clicking **Order Passing** | **Pass Orders** and selecting “Night Desk”.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use1.png)

   After the order pass is initiated, the **Pass State** column shows the order state as “Pending Out” in the Chicago Order Book. The Order Book row is highlighted orange to indicate the order is in a pending pass state.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use2.png)
2. In the Night Desk user group’s Order Book, the passed order appears as “Pending In” in the **Pass State** column, and the **Caretaker** column shows “Chicago” as the group currently managing and passing the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use3.png)
3. The Night Desk selects the order and clicks **Order Passing** | **Accept Orders**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use4.png)

   After the order is accepted, the **Caretaker** column displays “Night Desk” as the user group now managing the order, and the **CurrentUser** column shows “Trader” as the user monitoring the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use5.png)
4. The Night Desk betters the price and changes the quantity of the working child order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use6-result.png)
5. For the next trading session, the Night Desk clicks the **Order Passing** button in their Order Book and passes the working parent order back to Chicago.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use7.png)

   The **Pass State** column now shows “Pending Out” in the Night Desk user group’s
   Order Book. The Order Book row is highlighted orange to indicate the order is in a pending pass state.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use8.png)
6. In Chicago’s Order Book, the **Pass State** column shows the order as “Pending In”, and the **Caretaker** column shows “Night Desk” as the group currently managing and passing the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use9.png)
7. The Chicago user group clicks **Order Passing** | **Accept orders** in their
   Order Book to reclaim the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use10.png)

   The order pass is accepted and “Chicago” displays in the **Caretaker** column and “Broker A” appears in the **CurrentUser** column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use11.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use6-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use9.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use10.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-use11.png
