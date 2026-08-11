---
title: Vertical Horizontal Filter
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/vertical-horizontal-filter/
---

# Vertical Horizontal Filter

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/vertical-horizontal-filter/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

Created by Adam White, the Vertical Horizontal Filter helps the user determine whether a particular price is trending. The higher the Vertical Horizontal Filter value, the more a particular contract is trending. In addition, the direction of the Vertical Horizontal Filter shows what phase the Vertical Horizontal Filter is entering:

* A rising Vertical Horizontal Filter means that prices are trending.
* A falling Vertical Horizontal Filter means that prices are stablizing around a specific range.

Selecting the Vertical Horizontal Filter allows you to set the **Period** (as number of minutes) and the color of the result.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/vertical-horizontal-filter.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/vertical-horizontal-filter-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

The Vertical Horizontal Filter is calculated as follows:

\[ VHF = \frac{ABS(High Closing Price – Low Closing Price)}{ \sum\_{j=1}^{n}ABS(Close\_{j} – Close\_{j-1})} \]

←[Previous PostValuation Lines](valuation-lines.md)

[Next PostVolume Oscillator](volume-oscillator.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/vertical-horizontal-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/vertical-horizontal-filter-1.png
