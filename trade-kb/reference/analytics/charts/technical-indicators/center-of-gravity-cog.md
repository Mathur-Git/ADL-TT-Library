---
title: Center of Gravity (COG)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/center-of-gravity-cog/
---

# Center of Gravity (COG)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/center-of-gravity-cog/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Center of Gravity oscillator, developed by John Ehler, produces less lag indicating pivot points. The indicator was the result of studies of adaptive filters.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/center-of-gravity.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/center-of-gravity-1.png)

* **Period**: Number of days in the to use for calculations.
* **Field**: Price or combination of prices to use as the base for average calculations. Possible values include:
  * Open
  * High
  * Low
  * Close
  * Adjusted Close
  * HL/2 ( left ( frac{High + Low}{2} right ) )
  * HLC/3 ( left ( frac{High + Low + Close}{3} right ) )
  * HLCC/4 ( left ( frac{High + Low + Close + Close}{4} right ) )
  * OHLC/4 ( left ( frac{Open + High + Low + Close}{4} right ) )
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

[COG = frac{-sum P\_{n}times left ( n+1 right )}{sum P\_{n}}]

←[Previous PostBalance of Power](balance-of-power.md)

[Next PostChaikin Money Flow (CMF)](chaikin-money-flow-cmf.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/center-of-gravity.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/center-of-gravity-1.png
