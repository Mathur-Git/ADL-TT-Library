---
title: Spread Configuration
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/spread-configuration/
---

# Spread Configuration

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/spread-configuration/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Spread definition & formulas](../../../../guides/spread-trading-autospreader.md#spread-definition-formulas) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Tick size and the synthetic spread](../../../../guides/spread-trading-autospreader.md#tick-size-and-the-synthetic-spread)

The spread definition fields apply to the entire synthetic spread. Use the configuration settings to select a
contract and begin configuring spread behavior in each leg of your synthetic spread instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-spread-config.png)

### Name

The name of the synthetic spread. The name that you enter appears in the MD Trader® and Market Grid widgets when
trading the synthetic spread.

### Share

Shares the spread configuration with users in your company. Refer to [Sharing synthetic spreads](../task-autospreader/sharing-a-synthetic-spread.md).

### Color

Selects the color of working spreads and corresponding leg orders in MD Trader and the Market Grid. This color also
displays next to the spread name in the Autospreader widget.

**Note**: When an offsetting hedge order is not immediately executed, the working order displays in a non-standard
orange color. This color is not configurable. The color black indicates there are orders with more than one color at a
given price level.

### Spread Formula Selection

Select one of the following formulas for calculating the spread price:

* **Price Differential**. Using the values from the leg settings, prices display as the implied price of the
  spread (A-B formula). The Standard Implied Price formula is displayed by default.
* **Ratio**. Using the values from the leg settings, prices display as a percentage ratio (A/B formula).
* **Net change (in ticks)**. Prices display based on the individual legs’ net change from the previous day
  settlement.
* **Custom**. Create your own custom formula in the spread formula editor.
* **TT Splicer.** Define a synthetic spread to execute according to a selected Sub-strategy (TT Brisk, TT
  Close,
  TT TWAP+, TT VWAP+). Prices displayed are in terms of the first leg of the synthetic instrument being created, based upon the following formula:
![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-spread-formula.png)

### Spread Formula Editor

Edit formulas for the selected spread formula or create a custom formula using standard arithmetic operators (the
text field makes “intellisense” suggestions as you type). Enter a leg identifier followed by the “.” to see a list of
modifiers. As you type the custom spread formula, it is periodically checked and provides visual indication of the
validity of the current arithmetic operation (text box highlights in green).

**Note**: Currently, the use of exponents in formulas is not supported.

### Contract Selection

Specifies the contract for the leg. Click **Select a Contract** and use the search or market explorer
functionality to select a contract.

When selecting a contract, you can select an aggregated instrument as one of the legs of the spread. Aggregated
instruments are created and launched into the market using the [Aggregator](../../aggregator/description-aggregator/aggregator-overview.md)
widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-contract-agg.png)

Refer to [Use Cases](../use-cases/creating-spreads-with-aggregated-instruments.md) for an example of creating
spreads with aggregated instruments.

### Ratio

Indicates the quantity of each leg in relation to the others. A negative sign (-) before the number indicates a short
leg.

Values entered in the Ratio field do not affect the spread price.

### Multiplier

Weights the value of the leg price to calculate the spread price when using the Price Differential, Ratio or Net
Change (in ticks) formulas.

**Note**: The multiplier can be a whole number, decimal number, or fraction. Fractional representation optimizes
ticking accuracy.

**Example**: A Spread Multiplier of 0.333333 displays as 1/3 in the Tick Information section..

### Tick Size

Displays the calculated minimum tick size of the spread.

**Note**: If the products making up the legs of the spread tick at different increments, the **Calculated Tick
Size** field displays the minimum tick size for the spread.

### Min Tick Increment

Displays the minimum tick size for instruments in the spread legs. The value is defined by the exchange.

**Example**: Some instruments may tick in 64ths, while others may tick in 32nds.

### Delta

Displays a value representing the effect on the spread with a one-tick move in an outright leg.

←[Previous PostAutospreader Configuration Interface](autospreader-configuration-interface.md)

[Next PostSpread Configuration Order Execution](spread-configuration-order-execution.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-spread-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-spread-formula.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-contract-agg.png
