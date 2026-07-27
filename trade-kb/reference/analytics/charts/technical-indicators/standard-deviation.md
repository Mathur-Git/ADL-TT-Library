---
title: Standard Deviation
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/standard-deviation/
---

# Standard Deviation

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/standard-deviation/)

The Standard Deviation indicator is a statistical calculation used to measure the variability. In trading this value is known as volatility. A low standard deviation indicates that the data points tend to be very close to the mean, whereas high standard deviation indicates that the data points are spread out over a large range of values.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/standard-deviation.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/standard-deviation-1.png)

* **Period**: Number of bars to use in the calculations.
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

* **Standard Deviations**: TBD
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

\[ s = \sqrt \frac{\sum (X -\bar X)^2}{(N-1)} \]

where:

* s = Standard deviation
* X = Each value in the sample
* X = Mean of the values
* N = Number of values (sample size)

←[Previous PostRSI](rsi.md)

[Next PostStochastic Oscillator (STOCH)](stochastic-oscillator-stoch.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/standard-deviation.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/standard-deviation-1.png
