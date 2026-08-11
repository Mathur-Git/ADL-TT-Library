---
title: Rainbow Moving Average
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/rainbow-moving-average/
---

# Rainbow Moving Average

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/rainbow-moving-average/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Rainbow Moving Average indicator shows multiple simple moving averages (SMAs) all at once for a specific time period. Each SMA is calculated based on the previous SMA and is color-coded in the chart.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rainbow-moving-average.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rainbow-moving-average-1.png)

**Field**: Price or combination of prices to use as the base for average calculations. Possible values include:

* Open
* High
* Low
* Close
* Adjusted Close
* HL/2 \( \left ( \frac{High + Low}{2} \right ) \)
* HLC/3 \( \left ( \frac{High + Low + Close}{3} \right ) \)
* HLCC/4 \( \left ( \frac{High + Low + Close + Close}{4} \right ) \)
* OHLC/4 \( \left ( \frac{Open + High + Low + Close}{4} \right ) \)

* **Period**: Number of bars to use in the calculations.
* **Underlay**: Whether to display the curve behind the graph.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[Simple = MA = \frac{\sum\_{i=1}^{n} Close\_{i}}{n}\]

←[Previous PostQStick](qstick.md)

[Next PostRainbow Oscillator](rainbow-oscillator.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rainbow-moving-average.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rainbow-moving-average-1.png
