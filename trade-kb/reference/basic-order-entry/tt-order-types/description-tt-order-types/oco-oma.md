---
title: OCO OMA
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/oco-oma/
---

# OCO OMA

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/oco-oma/)

The OCO OMA lets you adopt two or more working orders in the Order Book and apply an OCO (one-cancels-other) OMA (Order Management Algo) to them. When one order is fully-filled, the other orders are canceled. Also, when partial fills are received for one order, the quantities of the other orders are reduced accordingly. The OCO OMA also lets you choose whether cancel the order if the market state of one of the child orders changes to a non-tradable state.

**Note:** For an overview of Order Management Algos (OMA), refer to [https://library.tradingtechnologies.com/trade/oma-overview.html](https://library.tradingtechnologies.com/trade/oma-overview.html)

## Limitations for adopting orders

The OCO OMA can adopt exchange orders, [TT Order Types](tt-order-types-overview.md), [Synthetic Order Algos (SOAs)](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/synthetic-order-algos-soa.md) created in ADL and child orders of other algos. It cannot, however, adopt:

* TT Order Type parent orders
* Autospreader® parent orders
* Aggregator parent orders
* OTC orders

## Launching the OCO OMA

To launch the OCO OMA:

1. In the Order Book (or a Floating Order Book), select the orders you want the OCO OMA to adopt and manage.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-1.png)
2. Click OMA and select OCO from the dropdown.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-2.png)
3. Customize any desired [algo parameters](#params) and click Select algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-3.png)

   The OCO parent algo is added to the Order Book above the orders it adopted. If you collapse the parent OCO orders, its child orders will be hidden in the Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-4.png)

## OCO OMA parameters

The OCO OMA uses the following parameters:

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
    
  The **Co-location** drop down is seeded based on the market of the default instrument in the selected algo. It will also seed when multiple instruments are defined if all instruments are from the same market.
* **Disconnect action**: Action to take if the client loses its connection to TT:
  * **Leave** to allow the algo to continue running normally.
  * **Pause** to suspend the algo until you manually restart it.
  * **Cancel** to delete the algo.**Note:** You can set the default Disconnect action in the [Preferences](https://library.tradingtechnologies.com/trade/win-reference.html#algo-explorer)

←[Previous PostBrackeTT (OTA)](brackett-ota.md)

[Next PostOCO 2 OMA](oco-2-oma.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-oco-4.png
