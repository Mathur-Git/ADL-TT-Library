---
title: Random Walk Index
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/random-walk-index/
---

# Random Walk Index

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/random-walk-index/)

The Random Walk Index indicator determines if price movement is random or the result of a statistically significant trend over a specific time period.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/random-walk-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/random-walk-index-1.png)

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

* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[ RW\_{low} = \frac{High\_{1-n} – Low}{ATR\_{n} \* \sqrt n} \]

\[ RW\_{high} = \frac{High – Low\_{1-n}}{ATR\_{n} \* \sqrt n} \]

where ATR is the average true range over N periods preceding the current period.

←[Previous PostRainbow Oscillator](rainbow-oscillator.md)

[Next PostRAVI](ravi.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/random-walk-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/random-walk-index-1.png
