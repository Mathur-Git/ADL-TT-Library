---
title: Detrended Price Oscillator (DPO)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/detrended-price-oscillator-dpo/
---

# Detrended Price Oscillator (DPO)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/detrended-price-oscillator-dpo/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Detrended Price Oscillator, by Gerald Appel, attempts to eliminate the long-term trends in prices by using a displaced moving average so it does not react to the most current price action. This allows the indicator to show intermediate overbought and oversold levels effectively.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/detrended-price-oscillator.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/detrended-price-oscillator-1.png)

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

\[DPO = Close – MA\_{n}\;of\;\left ( \frac{n}{2}+1 \right )\;periods\;ago \]

←[Previous PostMoving Average Deviation](moving-average-deviation.md)

[Next PostDirectional Movement Index (DMI)](directional-movement-index-dmi.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/detrended-price-oscillator.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/detrended-price-oscillator-1.png
