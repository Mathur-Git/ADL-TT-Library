---
title: Moving Average Envelope (MAE)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/moving-average-envelope-mae/
---

# Moving Average Envelope (MAE)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/moving-average-envelope-mae/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Moving Average Envelope creates an envelope around a moving average to find overbought or oversold conditions, to smooth the price trend and as an indicator of price breakouts. The moving average envelope uses a moving average as the center line with a lower and upper bands added a percetnage above and below the center line.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/moving-average-envelope.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/moving-average-envelope-1.png)

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
* **Period**: Number of bars to use in the calculations.
* **Shift Type**: Type of offset (percent or points)
* **Shift**: Percentage or number of points to offset above or below the average.
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
* **Channel Fill**: Whether to shade the area between the top and bottom lines.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

Envelopes start with any moving average type (see Moving Averages for formulas) and then creates an offset x% above or below the average or an offset Y points above or below the average.

* For percentage envelopes:Upper band = moving average + x%(moving average)
    
  Lower band = moving average – x%(moving average)
* For points envelopes:Upper band = moving average + constant
    
  Lower band = moving average – constant

←[Previous PostMomentum Indicator](momentum-indicator.md)

[Next PostNegative Volume Index](negative-volume-index.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/moving-average-envelope.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/moving-average-envelope-1.png
