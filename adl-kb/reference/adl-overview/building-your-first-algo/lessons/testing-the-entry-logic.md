---
title: Testing the entry logic
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/testing-the-entry-logic/
---

# Testing the entry logic

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/testing-the-entry-logic/)

In this topic, you will test your entry order logic to make sure your algo submits the desired entry orders. In the process of testing the algo, you will:

* Set up your testing environment so you can monitor the algo’s actions.
* Play the algo in a simulated market and verify that the algo correctly places the order.
* Test the user-defined variables by specifying different order quantities before launching the algo and by changing the quantity while the algo is running,.

### Setting up your testing environment

When testing an algo, it is a good idea to have ADL open next to a workspace in TT. This workspace should be set to the simulation environment and have [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) and [Audit Trail](../../../../../trade-kb/reference/order-management/audit-trail/description-audit-trail/audit-trail-overview.md) widgets. You will be able to see the orders placed by your algo appear in your TT workspace which will let you verify that the algo is working as intended.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-environment.png)

To set up your testing environment:

1. Launch a TT workspace in the Simulation environment and place it near your algo in ADL.
2. Open an MD Trader widget for the default instrument specified in your algo.
3. Open an Audit Trail widget to watch the record of your algo’s activity.

### Playing the algo

The first test of your entry order logic is to make sure the algo correctly submits orders into the market with the default values specified in your algo. You will launch the algo in ADL and watch as it enters the market in MD Trader; you will also look for confirmation in the messages recorded in the Audit Trail.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-controls.png)

To play the algo:

1. In ADL, select the Instrument block to verify that the selected **Account** matches the active account in MD Trader.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-1.png)
2. In the ADL menu bar, click ![the Play button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-play-algo.png) to start the algo.
3. Verify that the algo submitted the entry order at the Best Bid and that the order is working the correct quantity.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-2.png)
   1. The **wrk qty** output port of the Entry Order block shows 5 (the default **Entry Order Qty** value).
   2. MD Trader shows a working order with a quantity of 5.
   3. The Audit Trail shows that the algo placed an order at the Best Bid and then was repriced when the market moved.
4. In the ADL menu bar, click ![the Play button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo.png) to stop and reset the algo.  
    **Note**: When you stop an algo, the working order is automatically canceled.

### Testing the user-defined variables

Now that you have tested the algo and verified that it correctly submits orders to the market, you should also verify that the user-defined variables in your algo also work correctly. For this test, you will change the **Entry Order Qty** to a non-default value before starting the algo. Then you will verify that changing the quantity while the algo is running also changes the working order quantity in the market.

To test your user-defined order quantity:

1. Make sure your algo is stopped; click ![the Play button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo-1.png) if necessary.
2. In the Information Panel, click the **Variables** tab to display the variables used by your algo.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-var-1.png)
3. In the **Variables** tab, click the **Value** field for the **Entry Order Qty** block; then enter a different value and click **Apply**. You should choose a value large enough that it is unlikely to be fully-filled quickly. This example will use 100.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-var-2.png)
4. In the ADL menu bar, click ![the Play button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-play-algo-1.png) to start the algo.
5. Verify that the algo submitted the entry order at the Best Bid and that the order is working the correct quantity.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-3.png)
   1. The **wrk qty** output port of the Entry Order block shows 100.
   2. MD Trader shows the order working a quantity of 100.
   3. The Audit Trail shows that the algo placed an order at the Best Bid.
6. While the algo is still running, change the **Entry Order Qty** to a lower value and click **Apply**.   
     
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-4.png)
7. Verify that the algo changed the order quantity to the new value.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-5.png)
   1. The **wrk qty** output port of the Entry Order block shows the new value (not the default **Entry Order Qty** value).
   2. MD Trader shows the new order working a quantity (50, in this case).
8. Click ![the Play button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo-2.png) to stop the algo and cancel the working order.

You have successfully tested the entry order logic for your algo. Now you are ready to update your algo to capture the price and quantity data as fills occur for your entry order.

←[Previous PostBuilding the entry logic](building-the-entry-logic.md)

[Next PostCapturing fills data](capturing-fills-data.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-environment.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-controls.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-play-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-var-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-test-var-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-play-algo-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-play-algo-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-stop-algo-2.png
