---
title: Autospreader Reference
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/reference-autospreader/autospreader-reference/
---

# Autospreader Reference

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/reference-autospreader/autospreader-reference/)

### Spread configuration parameters

| Field | Description |
| --- | --- |
| Add Leg | Adds more legs to a new or modified spread. |
| Color | Selects the color of working spreads and corresponding leg orders in [MD Trader](../../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) and the [Market Grid](../../../viewing-market-data/market-grid/description-market-grid/introduction-to-market-grid.md). This color also displays next to the spread name in the Autospreader widget.  **Note**: When an offsetting hedge order is not immediately executed, the working order displays in a non-standard orange color. This color is not configurable. The color black indicates there are orders with more than one color at a given price level. |
| Contract | Specifies the contract for the leg. Click **Select a Contract** and use the search or explore functionality to choose a contract. |
| Ratio | Indicates the quantity of each leg in relation to the others. A negative sign (-) before the number indicates a short leg.  Values entered in the Ratio field do not affect the spread price. |
| Multiplier | Weights the value of the leg price to calculate the spread price when using the “Price Differential” formula:  `Spread_Price = (LegA_Price * LegA_Spread_Multiplier) - (LegB_Price * LegB_Spread_Multiplier)`  **Note**: The multiplier can be a whole number, decimal number, or fraction. Fractional representation optimizes ticking accuracy.  **Example**: A Spread Multiplier of 0.333333 displays as 1/3 in the **Tick Information** section. |
| Pay Up Ticks | Indicates the number of ticks by which Autospreader will adjust the hedge order price. |
| Active Quoting | Sets whether or not Autospreader actively quotes the leg. If unchecked, orders for that leg are only sent when the other leg fills.  **Note**: You must enable this setting for at least one leg of the spread. |
| Enable Hedging | This setting determines whether or not Autospreader submits a hedge order for the leg after receiving a fill for the quoting leg. This option is checked (enabled) and hidden by default when **Active Quoting** is checked (enabled).  If **Active Quoting** is unchecked (disabled), the **Enable Hedging** option is shown for each leg of the spread and is checked (enabled) by default. When **Active Quoting** is unchecked and **Enable Hedging** is checked for a leg, Autospreader will only submit hedge orders for that leg.  When both **Active Quoting** and **Enable Hedging** are unchecked (disabled) for a leg, the instrument for the leg is used simply as a pricing component for the spread. |
| Min Lean Qty | Defines a minimum quantity required for quoting orders to lean against. Enter a formula or numeric value (e.g., 10) to determine the minimum quantity. When entering a formula, the text field makes intellisense suggestions for which parameters to use.  **Note**: To lean against the inside market, set **Min Lean Quantity** to “1”. |
| Queue Holder Orders | Sets the number of price levels to trail the quoting order. Autospreader will place duplicate orders at the specified number of consecutive price levels.  You can enable queue holder for up to five legs of a spread and up to 20 price levels. |
| >Min Tick Increment | Displays the minimum tick size for instruments in the spread legs. The value is defined by the exchange.  **Example**: Some instruments may tick in 64ths, while others may tick in 32nds. |
| Delta | Displays a value representing the effect on the spread with a one-tick move in an outright leg. |
| Rules | Adds a quote, pre-hedge, or post-hedge rule to a leg of your spread. Rules are available in the [Autospreader Rules](../description-autospreader/autospreader-rules-overview.md) widget |
| Calculated Tick Size | Displays the calculated minimum tick size of the spread.  **Note**: If the products making up the legs of the spread tick at different increments, the **Calculated Tick Size** field displays the minimum tick size for the spread. |
| Override Tick Size | Lets you override the value displayed in the **Calculated Tick Size** field. You can view a greater range of prices without reducing the view of the total quantity available.  By enabling **Override Tick Size**, you can specify a greater tick size to fit your needs. |

