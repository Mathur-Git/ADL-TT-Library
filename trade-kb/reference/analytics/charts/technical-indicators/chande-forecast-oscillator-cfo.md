---
title: Chande Forecast Oscillator (CFO)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chande-forecast-oscillator-cfo/
---

# Chande Forecast Oscillator (CFO)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chande-forecast-oscillator-cfo/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Chande Forecast Oscillator plots the percentage difference between the closing price and the n-period linear regression forecasted price. The oscillator is above zero when the forecast price is greater than the closing price and less than zero if it is below.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-forecast-oscillator.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-forecast-oscillator-1.png)

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

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[CFO\_{i} = \frac{(Close\_{i} – Linear\;Regression)\times 100}{Close\_{i}} \]

where linear regresion is calcualted as

\[slope\;=\;m\;=\;\frac{\sum\_{i=1}^{n}(x\_{i} – \bar{x})(y\_{i} – \bar{y})}{\sum\_{i=1}^{n}(x\_{i} – \bar{x})^{2}}\]

\[intercept\;=\;b\;=\;\bar{y} – m\bar{x}\]

←[Previous PostChaikin Volatility (CV)](chaikin-volatility-cv.md)

[Next PostChande Momentum Oscillator (CMO)](chande-momentum-oscillator-cmo.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-forecast-oscillator.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-forecast-oscillator-1.png
