---
title: Trade Volume Index (TVI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/trade-volume-index-tvi/
---

# Trade Volume Index (TVI)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/trade-volume-index-tvi/)

The Trade Volume Index (TVI) leverages intraday market data to show whether a security is being accumulated (purchased) or distributed (sold). The Trade Volume Index assumes that higher prices represent buy orders while lower prices are sell orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-volume-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-volume-index-1.png)

* **Min Tick Value**: Minimum price movement required to include in the calculation.
* **Field**: Price or combination of prices to use as the base for average calculations. Possible values include:

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

\[EMA1 = EMA1\_\text{n-1} + \left ((\frac{2}{(n + 1)}) \* (P\_n – EMA1\_\text{n-1}) \right)\]

\[EMA2 = EMA2\_\text{n-1} + \left ((\frac{2}{(n + 1)}) \* (EMA1\_n – EMA2\_\text{n-1}) \right)\]

\[EMA3 = EMA3\_\text{n-1} + \left ((\frac{2}{(n + 1)}) \* (EMA2\_n – EMA3\_\text{n-1}) \right)\]

\[ TRIX = \frac{(EMA3\_n – EMA3\_\text{n-1})}{EMA3\_\text{n-1}} \]

where:

* P*n* =the current price.
* EMA1*n*-1 = the exponential moving average value of *n* periods back
* EMA2*n*-1 = the exponential moving average value of *n* periods back
* EMA3*n*-1 = the exponential moving average value of *n* periods back

←[Previous PostTime Series Forecast (TSF)](time-series-forecast-tsf.md)

[Next PostTrend Intensity Index](trend-intensity-index.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-volume-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-volume-index-1.png
