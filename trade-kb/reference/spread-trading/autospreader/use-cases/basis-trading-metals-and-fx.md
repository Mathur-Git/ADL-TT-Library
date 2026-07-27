---
title: Basis Trading Metals and FX
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/basis-trading-metals-and-fx/
---

# Basis Trading Metals and FX

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/basis-trading-metals-and-fx/)

The following use cases illustrate how you can leverage Autospreader to create a strategy to capitalize on relative
value
spread pricing by buying/selling the spot cash and selling/buying the futures contract for:

* [a Silver basis strategy](#setting-up-silver-basis-strategy)
* [a EUR/USD basis strategy](#setting-up-eur-usd-basis-strategy)

## Basis Trading

The basis measures the rate of return for carrying a given commodity over a specific period of time. You can view the
basis as the difference between the spot and futures prices. Basis trading involves simultaneously buying or selling
the spot cash commodity and doing the opposite (selling or buying) with the futures contract for the commodity. A
trader will take a long position if the basis is expected to widen, and, conversely, take a short position if the
basis is expected to shrink.

With the availability of cash spot metals and FX on TT, you can execute basis trading strategies using all of
the tools provided on the TT platform. For example, Autospreader provides the ability to create synthetic spreads and
launch them to a co-located server for low-latency execution. You can configure Autospreader to display the basis as
well as simultaneously execute orders for the cash spot and future to achieve a designated synthetic spread price.

### Setting up a Silver Basis Strategy

In this use case, Autospreader is configured to create a basis strategy for silver using the cash spot silver (**XAG/USD**) as Leg 1 and the silver future (**SI Jun24**) for Leg 2. Both the cash spot and future are quoted in USD-per-ounce, so the **Multiplier** settings for each leg have the same value (**1.0**) but the opposite sign, resulting in a spread formula of “1 \* Leg1.MergedPrice – 1 \* Leg2.MergedPrice”. In other words, this is the cash spot price minus the future’s price expressed in USD-per-ounce.

The **Ratio** for the spot leg is set to **5000** since the contract size of the future is **5000** ounces. So for every future that is bought or sold, 5000 ounces of the cash spot instrument will be sold or bought.

The MD Trader below reflects the market for a spread with the configured settings. It displays a tick size of 1/1000 since the cash spot tick size is 1/1000 and the future’s tick size is 5/1000.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-silver-1.png)

In this use case, **Active Quoting** is enabled on the cash spot leg. This is strongly recommended since FX Liquidity Providers (LPs) tend to favor flow where you’re adding liquidity to the market. Also note that the spread will be executed on an Autospreader server in the data center closest to the instrument associated with Leg 1, which in this case is NY.

When the quote order for the spot leg is filled, Autospreader will submit a hedge order for the future to achieve the desired spread price. For complete transparency, Autospreader quote and hedge latency data is displayed in the Audit Trail widget.

When launched, the synthetic spread instrument (left) and its legs will display as shown below.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-silver-2.png)

### Setting up a EUR/USD Basis Strategy

In another use case, Autospreader is configured to create a basis strategy for EUR/USD using the cash spot EUR/USD for **Leg 1** and the EUR/USD future (**6E May24**) for **Leg 2**.

Both the cash spot and the future are quoted as USD-per-EUR, but the spot leg **Ratio** is set to **125,000** since the future’s contract size is 125,000 EUR. So for every future that is bought or sold, 125,000 EUR of the cash spot instrument will also be sold or bought.

In the following image, MD Trader reflects the market for a spread with the configured settings, displaying a tick size of 1/100000 since the cash spot tick size is 1/10000 and the future’s tick size is 5/10000.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-fx-1.png)

Again, note that active quoting will only be done on the cash spot leg to provide better quality flow to the FX LPs. And the spread will be executed on an Autospreader server in the data center closest to the instrument associated with Leg 1, which in this case is NY.

When launched, the synthetic spread instrument (left) and its legs will display as shown below.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-fx-2.png)

←[Previous PostConfiguring Common Spreads](configuring-common-spreads.md)

[Next PostCreating spreads with aggregated instruments](creating-spreads-with-aggregated-instruments.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-silver-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-silver-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-fx-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-usecase-basis-fx-2.png
