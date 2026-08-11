---
title: With A Tick OMA
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/with-a-tick-oma/
---

# With A Tick OMA

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/with-a-tick-oma/)
>
> **Interpreted in:** [Order Types & Execution § Order Management Algos (OMA) — applied to existing orders](../../../../guides/order-types-and-execution.md#order-management-algos-oma-applied-to-existing-orders)

The With A Tick OMA gives you the ability to apply With A Tick (WAT) logic to a working order using either the Order Book or Floating Order Book widget. The WAT logic automatically reprices the order one tick towards the market based on the price and quantity of the opposite inside market.

**Note:** For an overview of Order Management Algos (OMA), refer to [Order Management Algos (OMA) overview](../../../algo-trading/order-management-algos-omas/order-management-algos-oma-overview.md)

You can define the minimum quantity that must be available on the opposite side of the market a single tick from the current working order price. If the available quantity at the opposite price is less than your defined quantity, the order is repriced into the market by a single tick.

## Limitations for adopting orders

The With a Tick OMA can adopt exchange orders, [TT Order Types](tt-order-types-overview.md), [Synthetic Order Algos (SOAs)](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/synthetic-order-algos-soa.md) created in ADL, and child orders of other algos. It cannot, however, adopt:

* TT Order Type parent orders
* Autospreader® parent orders
* Aggregator parent orders
* OTC orders

## Launching “With A Tick OMA” from the Order Book

1. Select a working order in the Order Book.
2. Click **OMA** in the Order Book control panel and select **With A Tick**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-step2.png)
3. Configure the [With A Tick OMA parameters](#params) and click **Select Algo**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-config2.png)

   The working With A Tick OMA parent order appears in the Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-applied.png)

   **Tip**: The working With A Tick OMA order can also be managed using the Algo Dashboard.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-algo2.png)

## Launching “With A Tick OMA” from the Floating Order Book

1. Open the Floating Order Book for a working order in MD Trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob.png)
2. Click **OMA** and select **With A Tick**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-select.png)
3. Configure the [With A Tick OMA parameters](#params) and click **Launch Algo**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-config.png)
4. The working With A Tick OMA parent order can be managed using the Floating Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-launched.png)

   **Tip**: The working With A Tick OMA order can also be managed using the Algo Dashboard.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-algo.png)

## With A Tick OMA Example

In this example, With A Tick OMA was launched for a working Buy order in MD Trader at 7792.75. The quantity on the opposite side of the market is “29”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-mdt-price.png)

When the quantity at the inside market Ask price dropped below the defined threshold quantity of “10”, the order was repriced one tick into the market and filled at “7793.00”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-filled.png)

## Canceling a “With A Tick OMA” order

If you cancel the With A Tick OMA parent order, the order is deleted but its child orders remain working in the market.

## With A Tick OMA parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-config-1.png)

The With A Tick OMA uses the following parameters:

* **With a Tick**: Sets the quantity threshold in contracts to reprice the order.
* **Ignore Market State**: Sets whether to ignore changes in the market state.
* **Instance name**: Optional name for this algo instance.
* **Co-location**: Location of the Algo Server to run this algo.
    
  The Co-location drop down is seeded based on the market of the default instrument in the selected algo. It will also seed when multiple instruments are defined if all instruments are from the same market.
* **Disconnect action**: Action to take if the client loses its connection to TT:
  * **Leave** to allow the algo to continue running normally.
  * **Pause** to suspend the algo until you manually restart it.
  * **Cancel** to delete the algo.**Note:** You can set the default Disconnect action in the workspace [Preferences.](https://library.tradingtechnologies.com/trade/win-reference.html#algo-explorer)

←[Previous PostMinVol OMA](minvol-oma.md)

[Next PostSingle Theo (MMA)](single-theo-mma.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-step2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-config2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-applied.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-algo2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-launched.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-mdt-price.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-filled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-wat-fob-config-1.png
