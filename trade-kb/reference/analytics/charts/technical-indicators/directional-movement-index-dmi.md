---
title: Directional Movement Index (DMI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/directional-movement-index-dmi/
---

# Directional Movement Index (DMI)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/directional-movement-index-dmi/)

The Directional Movement Indicators (DMI) are components of the Directional Movement system published by J. Welles Wilder, and are computed with the Average Directional Movement Index (ADX). Two indicators are plotted, a Positive DI ( +DI ) and a Negative DI ( -DI ).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/directional-movement-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/directional-movement-index-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

Directional Movement (DM) is defined as the largest part of the current period’s price range that lies outside the previous period’s price range. For each period calculate:

\[+DM = High – Previous\;High\]

\[-DM = Previous\;Low – Low\]

The smaller of the two values is set to zero, i.e., if +DM > -DM, then -DM = 0. On an inside bar (a lower high and higher low), both +DM and -DM are negative values, so both get reset to zero as there was no directional movement for that period.

The True Range (TR) is calculated for each period, where:

\[TR = max(High\_{t} – Close\_{t-1}\;,\;Close\_{t-1} – Low\_{t}\;,\;High\_{t} – Low\_{t})\]

The \(+DM\_{n}, -DM\_{n}\) and \(TR\_{n}\) are averaged over a usered defined n-periods. The intial calculation uses a pure moving average, with the remain calculations use an accumulation technique which produces a smoothed line, similar to an exponential smoothing:

\[\bullet\; +DM\_{n-periods} = +DM\_{n-1} – \left ( \frac{+DM\_{n-1}}{n} \right ) +( +DM\_{n})\]

\[\bullet\; -DM\_{n-periods} = -DM\_{n-1} – \left ( \frac{-DM\_{n-1}}{n} \right ) +( -DM\_{n})\]

\[\bullet\; ATR\_{n-periods} = ATR\_{n-1} – \left ( \frac{ATR\_{n-1}}{n} \right ) +( TR\_{n})\]

Compute the positive/negative Directional Indexes, +DI and -DI, as a percentage of the True Range:

\[\bullet\; +DI = \left ( \frac{+DM}{TR} \right ) times 100\]

\[\bullet\; -DI = \left ( \frac{-DM}{TR} \right ) times 100\]

The next step is to calculate DX, where:

\[\bullet\; DI\_{diff} = \left |\; ((+DI) – (-DI))\; \right| \]

\[\bullet\; DI\_{sum} = ((+DI) + (-DI)) \]

\[\bullet\; DX = \left( \frac{DI\_{dif}}{DI\_{sum}}\right) \times 100\]

The DX is always a value between 0 and 100. The accumulated moving average technique is used to smooth the DX. The result is the ADX or average directional movement index.

\[ADX\_{n} = +ADX\_{n-1} – \left ( \frac{ADX\_{n-1}}{n} \right )+(DX\_{n})\]

←[Previous PostDetrended Price Oscillator (DPO)](detrended-price-oscillator-dpo.md)

[Next PostDisparity Index](disparity-index.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/directional-movement-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/directional-movement-index-1.png
