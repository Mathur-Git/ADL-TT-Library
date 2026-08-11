---
title: Weighted Close
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/weighted-close/
---

# Weighted Close

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/weighted-close/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Weighted Close indicator takes the average between the close, high, and low prices. However, in the calculation, the Close price is doubled in the numerator which gives the value more weight.

Selecting the Weighted Close indicator allows you to set the **Period** (as number of minutes) and the color of the result.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/weighted-close.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/weighted-close-1.png)

* **Period**: Number of bars to use in the calculations.
* **Overlay**: Whether to display the curve on top of the chart instead of at the bottom of the chart.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

The Weighted Close indicator includes the close price twice in the numerator and adds this value to the high and the low price. The total is then averaged (i.e., divided by a factor of 4).

\[ WC = \frac{(Close \*2)+ High + Low}{4} \]

←[Previous PostVWAP](vwap.md)

[Next PostWilliams % R (WillR)](williams-r-willr.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/weighted-close.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/weighted-close-1.png
