---
title: OCO 2 OMA
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/oco-2-oma/
---

# OCO 2 OMA

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/oco-2-oma/)

The OCO 2 OMA lets you select two orders and apply an OCO (one-cancels-other) OMA to them. When one order is fully-filled, the other order is canceled. Also, when partial fills are received for one order, the quantity of the other order is reduced accordingly.

**Note:** For an overview of Order Management Algos (OMA), refer to [https://library.tradingtechnologies.com/trade/oma-overview.html](https://library.tradingtechnologies.com/trade/oma-overview.html)

The OCO 2 OMA also supports an “order building” mode that lets you dynamically build an OMA from existing or new orders in [MD Trader](../../md-trader/description-md-trader/md-trader-overview.md). You can then select existing orders or create new orders to be managed by the OMA. New orders are added to MD Trader in a held state so they don’t start working until the OMA is launched.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-intro.png)

## Limitations for adopting orders

The OCO 2 OMA can adopt exchange orders, [TT Order Types](tt-order-types-overview.md), [Synthetic Order Algos (SOAs)](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/synthetic-order-algos-soa.md) created in ADL and child orders of other algos. It cannot, however, adopt:

* TT Order Type parent orders
* Autospreader® parent orders
* Aggregator parent orders
* OTC orders

## Launching the OCO 2 OMA in builder mode

In this procedure, you launch the OCO 2 OMA and adopt two existing Sell orders, one each for different contracts. For each fill in one order, the algo reduces the quantity of the other order by the same amount.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-1.png)

To launch the OCO 2 OMA in builder mode:

1. In MD Trader, click the custom action button you added for the OCO 2 OMA or select OCO 2 from the **Order Type** drop-down.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-2.png)

   The background color of the button and all MD Trader Header panels changes to yellow to indicate your are now in order builder mode, and the OMA order builder opens for the associated OMA algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-4.png)
2. Either use shift-right-click to select an existing order or enter a new order in an MD Trader widget.The selected or new order is added to order builder.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-5.png)

   1. Shift-right-click the working order to add it to the algo order.
   2. The selected order appears in the order builder.
3. Either use shift-right-click to select an existing order or enter a new order in an MD Trader widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-6.png)

   1. Shift-right-click to select the second order.
   2. The selected order is added to the order builder.
4. In the order builder, click **Launch algo**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-7.png)

   You can also enable **Auto-launch** to launch the algo automatically when the algo’s required number of orders is added.The new algo parent order, along with its child orders, are added to the Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-8.png)

   1. OCO 2 OMA parent order.
   2. Child orders being managed by the OCO 2 OMA.

## Canceling OCO 2 parent orders

If you cancel the parent order of an OCO 2 parent order, the parent order is deleted and:

* Child orders added from existing orders will remain working in market.
* Child orders added as new orders will be deleted.

## OCO 2 OMA parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-params.png)

The OCO 2 public OMA uses the following parameters:

* **Delete orphan**: Whether to delete the balance of a larger order when an order with a smaller quantity is fully-filled.
    
  If, at any time, the working quantity of any one of the OCO OMA child orders goes to zero, the other orders are considered to be “orphans.” When this parameter is TRUE, all remaining orders are deleted, regardless of their working quantities.
* **Enforce Mkt State**: Whether to delete the OCO order, and its child orders, if the market state of one of the child instruments changes to a non-tradable state.
    
  If the market state of an instrument changes to something other than Open, and Enforce Mkt State is enabled, all orders will be deleted.
* **Proportional**: Method to use when reducing the quantities of other legs when one leg is filled.
  * **True**: Reduce the other leg quantities by the same proportion of the fill quantity to the order quantity of the filled order.
  * **False**: (Default) Reduce the other leg quantities by the fill quantity of the filled order.For example, suppose you create an OCO OMA algo for a 100-lot order and two 50-lot orders and that the 100-lot order receives a fill for 20 lots (20%). If the **Proportional** parameter is **True**, the quantities of the remaining two 50-lot leg orders will also be reduced by 20%, or 10 lots each. If the parameter is false, the quantities of each of the other orders will be reduced by 20 contracts.
* **Ignore Market State**: Whether to ignore the market state when submitting the parent OCO OMA.
* **Instance name**: Optional name for this algo instance.
* **Co-location**: Location of the Algo Server to run this algo.
    
  The Co-location drop down is seeded based on the market of the default instrument in the selected algo. It will also seed when multiple instruments are defined if all instruments are from the same market.
* **Disconnect action**: Action to take if the client loses its connection to TT:
  * **Leave** to allow the algo to continue running normally.
  * **Pause** to suspend the algo until you manually restart it.
  * **Cancel** to delete the algo.**Note:** You can set the default Disconnect action in the [Preferences](https://library.tradingtechnologies.com/trade/win-reference.html#algo-explorer)

←[Previous PostOCO OMA](oco-oma.md)

[Next PostDirect Entry (MMA)](direct-entry-mma.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-oco2-params.png
