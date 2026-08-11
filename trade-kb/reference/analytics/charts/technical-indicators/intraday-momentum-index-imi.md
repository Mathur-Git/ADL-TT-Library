---
title: Intraday Momentum Index (IMI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/intraday-momentum-index-imi/
---

# Intraday Momentum Index (IMI)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/intraday-momentum-index-imi/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Intraday Momentum Index (IMI) indicator is similar to the Relative Strength Index (RSI) indicator. It is used to measure underlying strength of a market move. IMI measures the change between the current bar’s open and close prices, while RSI uses the prior bar’s close to current bar’s close change. The current price is normalized as a percentage
between 0 and 100. /p>

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/intraday-momentum-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/intraday-momentum-index-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Over Zones Enabled**: Whether to shade the area between the plot and the horizontal overbought and oversold levels.
* **Over Bought**: Overbought quantity
* **Over Sold**: Oversold quantity
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

For each period an upward and downward change is calculated as follows:

[Upward = if;Close\_{t} – Open\_{t} > 0;then;Close\_{t} – Open\_{t},;else;0 ]

[Downward = if;Close\_{t} – Open\_{t}

[IMI = frac{sum\_{i=1}^{n} Upward}{left ( sum\_{i=1}^{n} Upward + sum\_{i=1}^{n} Downward right )} times 100]

←[Previous PostIchimoku Clouds (ICH)](ichimoku-clouds-ich.md)

[Next PostSTARC Bands](starc-bands.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/intraday-momentum-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/intraday-momentum-index-1.png
