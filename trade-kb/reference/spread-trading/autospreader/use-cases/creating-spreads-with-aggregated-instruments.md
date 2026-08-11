---
title: Creating spreads with aggregated instruments
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/creating-spreads-with-aggregated-instruments/
---

# Creating spreads with aggregated instruments

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/creating-spreads-with-aggregated-instruments/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Spread definition & formulas](../../../../guides/spread-trading-autospreader.md#spread-definition-formulas) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Aggregator](../../../../guides/spread-trading-autospreader.md#aggregator)

Using Autospreader, you can create a synthetic spread using an Aggregator instrument as one of the spread legs. For example, you can create a Basis Spread using an aggregated cash instrument as the front leg and a treasury futures instrument as the back leg.

Before you begin, create and launch the [aggregated instrument](../../aggregator/description-aggregator/aggregator-overview.md) or ensure that the instrument is available in the market. The following example shows the configuration for an aggregated instrument comprising the contracts for BrokerTec 5-year bonds (5\_YEAR) and eSpeed 5-year bonds (usg\_05y). When launched in Aggregator, the aggregated instrument (e.g., 5 Yr Cash) appears in Market Explorer and product search results and is available to trade.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-agg.png)

To create spreads with aggregated instruments:

1. Click **Create** in the opened Autospreader widget and configure the synthetic [spread definition](../task-autospreader/creating-a-synthetic-spread.md) parameters.
2. For **Leg 1** of the spread, click **Select a Contract** and select the aggregated instrument (e.g., 5 Yr Cash).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis1.png)

   Autospreader handles the aggregated instrument as if it were a native exchange instrument.
3. For **Leg 2** of the spread, click **Select a Contract** and select the futures instrument (e.g., ZF Mar17).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis2.png)
4. Preview the spread price, adjust the ticking if needed, and click **Save**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis3.png)

←[Previous PostBasis Trading Metals and FX](basis-trading-metals-and-fx.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-agg.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis3.png
