---
title: TRIX
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/trix/
---

# TRIX

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/trix/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Triple Exponential Moving Average Oscillator (TRIX) by Jack Hutson is a momentum indicator that oscillates around zero. It displays the percentage rate of change between two triple smoothed exponential moving averages.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trix.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trix-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[EMA1 = EMA1\_\text{n-1} + \left ( \left (\frac{2}{(n + 1)} \right) \* (P\_n – EMA1\_\text{n-1}) \right)\]

\[EMA2 = EMA2\_\text{n-1} + \left ( \left (\frac{2}{(n + 1)} \right) \* (EMA1\_n – EMA2\_\text{n-1}) \right)\]

\[EMA3 = EMA3\_\text{n-1} + \left ( \left (\frac{2}{(n + 1)} \right) \* (EMA2\_n – EMA3\_\text{n-1}) \right)\]

\[ TRIX = \frac{(EMA3\_n – EMA3\_\text{n-1})}{EMA3\_\text{n-1}} \]

Where:

* Pn =the current price.
* EMA1n-1 = the exponential moving average value of n periods back
* EMA2n-1 = the exponential moving average value of n periods back
* EMA3n-1 = the exponential moving average value of n periods back

←[Previous PostTrend Intensity Index](trend-intensity-index.md)

[Next PostTwiggs Money Flow](twiggs-money-flow.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trix.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trix-1.png
