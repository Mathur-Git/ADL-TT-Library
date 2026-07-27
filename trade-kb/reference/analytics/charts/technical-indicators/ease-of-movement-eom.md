---
title: Ease of Movement (EOM)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/ease-of-movement-eom/
---

# Ease of Movement (EOM)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/ease-of-movement-eom/)

Ease of Movement, developed by Richard W. Arms, Jr., relates price change to volume and is particularly useful for assessing the strength of a trend. High positive values indicate the price is increasing on low volume and strong negative values indicate the price is dropping on low volume.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ease-of-movement.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ease-of-movement-1.png)

* **Period**: Number of bars to use in the calculations.
* **Moving Average Type**: Type of moving average to use in the calculations:
  * Simple
  * Exponential
  * Time Series
  * Triangular
  * Variable
  * VIDYA
  * Weighted
  * Welles Winder
  * Hull
  * Double Exponential
  * Triple Exponential
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

The four calculation below are required for Ease of Movement indicator:

\[Distance\;Moved = DM = \left(\frac{High\_{current} – Low\_{current}}{2}\right) – \left(\frac{High\_{previous} – Low\_{previous}}{2}\right) \]

\[Box Ratio = BR = \left(\frac{\frac{Volume\_{current}}{1,000,000,000}}{High\_{current} – Low\_{current}}\right) \]

Calculate a one period EOM:

\[EOM\_{1} = \frac{DM}{BR}\]

Calculate the moving average where the user can pick from various moving average types:

\[EOM\_{n-period MA} = MA(EOM\_{1})\]

←[Previous PostDonchian Width](donchian-width.md)

[Next PostEhler Fisher Transformation (EFT)](ehler-fisher-transformation-eft.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ease-of-movement.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ease-of-movement-1.png
