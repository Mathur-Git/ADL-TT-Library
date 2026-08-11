---
title: Accumulation Distribution (ACC Dist)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/accumulation-distribution-acc-dist/
---

# Accumulation Distribution (ACC Dist)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/accumulation-distribution-acc-dist/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Accumulation/Distribution (AD) indicator attempts to quantify the amount of volume flowing into or out of an instrument by identifying the position of the close of the period in relation to that period’s high/low range. The volume for the period is then included in a running continuous total.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulation-distribution.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulation-distribution-1.png)

* **Use Volume**: Whether to use trade volume in the formula calculation.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[AD = cumulative \left ( \frac{(Close – Low) – (High -Close)}{(High – Low)} \times Volume \right )\]

←[Previous PostAbsolute Price Oscillator](absolute-price-oscillator.md)

[Next PostAccumulative Swing Index (ASI)](accumulative-swing-index-asi.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulation-distribution.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulation-distribution-1.png
