---
title: Chaikin Money Flow (CMF)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chaikin-money-flow-cmf/
---

# Chaikin Money Flow (CMF)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chaikin-money-flow-cmf/)

The Chaikin Money Flow (CMF) indicator measures Money Flow Volume over a period of time to determine buying and selling pressure by comparing the closing price in relation to the high-low range and the volume. When the CMF is above zero, it can indicate buying pressure; likewise, it indicates selling pressure when the CMF is below zero. Values farther away from zero indicate greater pressures.

When CMF crosses the zero Line, it can identify a potential trend reversal.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chaikin-money-flow.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chaikin-money-flow-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[CMF = \frac{\sum\_{1}^{n} Money\;Flow\;Volume}{\sum\_{1}^{n} Volume}\]

where:

\[Money\;Flow\;Volume = Money\;Flow\;Multiplier\_{n} \times Volume\_{n}\]

\[
Money\;Flow\;Multiplier =
\frac{\left( (Close\_{n}-Low\_{n}) – (High\_{n} – Close\_{n}) \right)}
{(High\_{n}-Low\_{n})}
\]

←[Previous PostCenter of Gravity (COG)](center-of-gravity-cog.md)

[Next PostChaikin Volatility (CV)](chaikin-volatility-cv.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chaikin-money-flow.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chaikin-money-flow-1.png
