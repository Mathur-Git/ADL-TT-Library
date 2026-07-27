---
title: Conditional OMA
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/conditional-oma/
---

# Conditional OMA

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/conditional-oma/)

The Conditional OMA lets you set one order as the trigger condition (primary order) for working a second order
(conditional order). The algo works the primary order and submits the second order on hold. As the first order
receives fills, the algo submits the held order into the market and automatically increments the quantity of the
second order.

**Note:** For an overview of Order Management Algos (OMA), refer to [https://library.tradingtechnologies.com/trade/oma-overview.html](https://library.tradingtechnologies.com/trade/oma-overview.html)

The Conditional OMA is available only in “order building” mode within [MD Trader](../../md-trader/description-md-trader/md-trader-overview.md),
which lets you dynamically build an OMA from existing or new orders. After entering order building mode for the
Conditional OMA, you either create or select the primary order, then create a new conditional order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-intro.png)

1. Primary order. When this order receives a fill…
2. Conditional order. … the quantity of this order is incremented.

## Limitations for adopting orders

The Conditional OMA can adopt exchange orders, [TT Order Types](tt-order-types-overview.md), [Synthetic Order Algos (SOAs)](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/synthetic-order-algos-soa.md) created in ADL and
child orders of other algos. It cannot, however, adopt:

* TT Order Type parent orders
* Autospreader® parent orders
* Aggregator parent orders
* OTC orders

## Launching the Conditional OMA in builder mode

In this procedure, you launch the Conditional OMA to adopt an existing Buy order for a contract and create a new Sell
order for the same contract. For each Buy fill, the algo submits an offsetting Sell order for the same quantity.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-1.png)

To launch TT public OMAs in builder mode:

1. In MD Trader, click the custom action button you added for the OMA or select **Conditional** from the
   Order Type drop-down.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-2.png)

   The background color of the button and all MD Trader Header panels changes to yellow to indicate your are now in
   order builder mode, and the OMA order builder opens for the associated OMA algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-2-result.png)
2. Specify the primary order. You can either use shift-right-click to select an existing order or enter a new order in
   an MD Trader widget. In this case, you right-click the Buy order to adopt it.The selected or new order is added to order builder.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-3.png)

   1. Shift-right-click the working order to add it to the algo order.
   2. The selected order appears in the order builder.
3. Specify the conditional order. You can either shift-right-click to select an existing order or enter a new order in
   an MD Trader widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-5.png)

   1. For the conditional order, enter a new order at the desired price level.
   2. The new order is added to the order builder with a **Hold** status.
4. In the order builder, click **Launch** algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-6.png)

   You can also enable **Auto-launch** to launch the algo automatically when the algo’s required number of
   orders is added.The new algo parent order, along with its child orders, are added to the Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-7.png)

   1. Conditional OMA parent order.
   2. Primary child order. submitted as a Working order.
   3. Conditional child order, submitted as a Held order.**Note:** When launching a TT Conditional OMA, the Primary (first) order is submitted as a Working
   order, while the Conditional (second) child order is submitted as a Held order. When the primary order receives a
   fill, the conditional order changes to Working status.

## Canceling Conditional OMA orders

If you cancel the parent order of a Conditional OMA, the parent order is deleted and:

* Child orders added from existing orders will remain working in market.
* Child orders added as new orders will be deleted.

## Conditional OMA parameters

**Note:** To set parameters for the Conditional OMA, you must create an algo template in the [Template Manager](https://library.tradingtechnologies.com/trade/tm-overview.html).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-params.png)

The Conditional OMA uses the following parameters:

* **Instance name**: Optional name for this algo instance.
* **Co-location**: Location of the Algo Server to run this algo.
    
  The Co-location drop down is seeded based on the market of the default instrument in the selected algo. It will
  also seed when multiple instruments are defined if all instruments are from the same market.
* **Disconnect action**: Action to take if the client loses its connection to TT:
  * **Leave** to allow the algo to continue running normally.
  * **Pause** to suspend the algo until you manually restart it.
  * **Cancel** to delete the algo.**Note:** You can set the default Disconnect action in the [Preferences](https://library.tradingtechnologies.com/trade/win-reference.html#algo-explorer)

←[Previous PostDirect Entry (MMA)](direct-entry-mma.md)

[Next PostMinVol OMA](minvol-oma.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-2-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-conditional-params.png
