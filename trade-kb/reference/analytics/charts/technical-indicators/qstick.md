---
title: QStick
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/qstick/
---

# QStick

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/qstick/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The QStick indicator quantifies and identifies trends in candlestick charts. The indicator is a moving average calculation of the difference between the Open and Close prices over a specific period.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/qstick.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/qstick-1.png)

* **Period**: Number of bars to use in the calculations.
* **Moving Average Type**: Type of moving average to use in the calculations:
  * **Simple**: Mean (average) of the data.
  * **Exponential**: Newer data are weighted more heavily geometrically.
  * **Time Series**: Calculates a linear regression trendline using the “least squares fit” method.
  * **Triangular**: Weighted average where the middle data are given the most weight, decreasing linearly to the end points.
  * **Variable**: An exponential moving average with a volatility index factored into the smoothing formula. The Variable Moving average uses the Chande Momentum Oscillator as the volatility index.
  * **VIDYA**: An exponential moving average with a volatility index factored into the smoothing formula. The VIDYA moving average uses the Standard Deviation as the volatility index. (Volatility Index DYnamic Average).
  * **Weighted**: Newer data are weighted more heavily arithmetically.
  * **Welles Winder**:The standard exponential moving average formula converts the time period to a fraction using the formula EMA% = 2/(n + 1) where n is the number of days. For example, the EMA% for 14 days is 2/(14 days +1) = 13.3%. Wilder, however, uses an EMA% of 1/14 (1/n) which equals 7.1%. This equates to a 27-day exponential moving average using the standard formula.
  * **Hull**: The Hull Moving Average makes a moving average more responsive while maintaining a curve smoothness. The formula for calculating this average is as follows: HMA[i] = MA( (2\*MA(input, period/2) – MA(input, period)), SQRT(period)) where MA is a moving average and SQRT is square root.
  * **Double Exponential**: The Double Exponential moving average attempts to remove the inherent lag associated to Moving Averages by placing more weight on recent values.
  * **Triple Exponential**: TBD
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

[ qstick\_{t} = frac{1}{n} sum\_{i=0}^{n-1} left ( close\_{t-i} – open\_{t-i} right ) ]

←[Previous PostPsychological Line](psychological-line.md)

[Next PostRainbow Moving Average](rainbow-moving-average.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/qstick.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/qstick-1.png
