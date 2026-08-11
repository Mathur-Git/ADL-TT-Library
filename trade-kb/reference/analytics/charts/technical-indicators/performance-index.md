---
title: Performance Index
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/performance-index/
---

# Performance Index

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/performance-index/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Performance Index indicator is used to compare the price trend of one instrument with the performnance of a benchmark index.

**Note:** The Performance Index is valid only when comparing multiple instruments using either [Comparisons](../task-charts/adding-a-comparison.md) or [Series](../task-charts/adding-a-series.md). When more that two instruments are used, each correlation indicator is compared to the chart’s first instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/performance-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/performance-index-1.png)

* **Period**: Number of bars to use in the calculations.
* Comparison Symbol: Instrument from the chart to compare.
* **Color Selectors**: Colors to use for graph elements.

## Formula

\[ PI = \frac {Instr Close}{Index Close} \times \frac {Index MA}{Instr MA} \]

where MA is the moving average.

←[Previous PostParabolic Sar (SAR)](parabolic-sar-sar.md)

[Next PostPivot Points](pivot-points.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/performance-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/performance-index-1.png
