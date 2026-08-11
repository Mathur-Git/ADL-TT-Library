---
title: Commodity Channel Index (CCI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/commodity-channel-index-cci/
---

# Commodity Channel Index (CCI)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/commodity-channel-index-cci/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Commodity Channel Index (CCI) compares the current mean price with the average mean price over a typical window of 20 periods.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/commodity-channel-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/commodity-channel-index-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Over Zones Enabled**: Whether to shade the area between the plot and the horizontal overbought and oversold levels.
* **Over Bought**: Overbought quantity
* **Over Sold**: Oversold quantity
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[CCI = \frac{( P – A )}{( 0.015 \* D )}\]

where

\[\bullet\; P = Pivot = \frac{(High\_{n-period} + Low\_{n-period} + Close\_{current\;close})}{3}\]

\[\bullet\; High\_{n-period} = Highest\;price\;over\;n-periods\]

\[\bullet\; Low\_{n-period} = Lowest\;price\;over\;n-periods\]

\[\bullet\; Close\_{current\;close} = Current\;close\;price\]

\[\bullet\; A = n\text{-}period\;moving\;average\;of\;the\;pivot\;value\;P \]

\[\bullet\; D = mean\;deviation\;of\;the\;absolute\;value\;of\;the\;difference\;between\;the\;mean\;price\;and\;the\;moving\;average\;of\;the\;mean\;price, P-A \]

←[Previous PostChoppiness Index](choppiness-index.md)

[Next PostCoppock Curve (CC)](coppock-curve-cc.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/commodity-channel-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/commodity-channel-index-1.png
