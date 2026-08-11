---
title: TT Cumulative Volume Delta (TT_CVD)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/tt-cumulative-volume-delta-tt_cvd/
---

# TT Cumulative Volume Delta (TT_CVD)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/tt-cumulative-volume-delta-tt_cvd/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The TT Cumulative Volume Delta (TT CVD Study)
displays a running total of net transactions as calculated by Volume
Delta. Transactions occurring on the Ask are considered Buying Pressure
and are added to the total, and those occurring on the Bid are considered
Selling Pressure and are subtracted from the cumulative total.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tt-cumulative-volume-delta.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tt-cumulative-volume-delta-1.png)

* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

TT CVD = Cumulative ( Vol Δ )

Vol Δ = Difference between Bid Volume and
Ask volume over specified interval

Bid Volume = – ( Accumulated Bid Volume )

Ask Volume = + ( Accumulated Ask Volume )

Buying Pressure = TT CVD > 0

Selling Pressure = TT CVD < 0

←[Previous PostTrue Range](true-range.md)

[Next PostVolume](volume.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tt-cumulative-volume-delta.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tt-cumulative-volume-delta-1.png
