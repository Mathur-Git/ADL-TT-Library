---
title: Using instruments as pricing components of a spread
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/using-instruments-as-pricing-components-of-a-spread/
---

# Using instruments as pricing components of a spread

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/using-instruments-as-pricing-components-of-a-spread/)

Autospreader allows users to designate one or more legs of a spread solely as pricing components. This enables a user to configure and trade a spread with an instrument that is neither quoted nor hedged and doesn’t require position limits. For example, you can configure a spread with Mar17 contracts for ICE Futures U.S. Cocoa (CC) and London Cocoa (C) as the spread legs, and British Pound Futures (6B) as a component in calculating the spread price.

To configure legs as price components:

1. Click **Create** in the opened Autospreader widget and configure the synthetic [spread definition](../task-autospreader/creating-a-synthetic-spread.md) parameters.
2. Select contracts for each leg of the spread.
3. Uncheck **Active Quoting** for the leg used as a pricing component.

   The **Enable Hedging** options are displayed and flash yellow for all legs.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-quote-off1.png)
4. Uncheck **Enable Hedging** for the same leg.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-hedge-off1.png)

   When the spread in this example is launched and traded, the 6B Mar17 leg is neither quoted nor hedged, but Autospreader includes the instrument when calculating the spread price.
5. Preview the spread price, adjust the ticking if needed, and click **Save**.

[Next PostConfiguring Common Spreads](configuring-common-spreads.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-quote-off1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-hedge-off1.png
