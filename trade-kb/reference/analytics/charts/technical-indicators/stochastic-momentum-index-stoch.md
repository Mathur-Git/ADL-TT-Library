---
title: Stochastic Momentum Index (STOCH)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/stochastic-momentum-index-stoch/
---

# Stochastic Momentum Index (STOCH)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/stochastic-momentum-index-stoch/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Stochastic Momentum Index (Stoch) normalizes price as a percentage between 0 and 100. Normally two lines are plotted, the %K line and a moving average of the %K which is called %D. A slow stochastic can be created by initially smoothing the %K line with a moving average before it is displayed. The length of this smoothing is set in the Slow K Period. Without the initial smoothing ( i.e., setting the Slow K Period to a value of 1 ) the %K becomes the ‘Raw %K’ value, and is also known as a fast stochastic.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stochastic-momentum-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stochastic-momentum-index-1.png)

* **%K Periods**: TBD
* **%K Smoothing Periods**: TBD
* **%K Double Smoothing Periods**: TBD
* **%D Periods**: TBD
* **%D Moving Average Type**: TBD
* **Color Selectors**: Colors to use for graph elements.
* **Over Zones Enabled**: Whether to shade the area between the plot and the horizontal overbought and oversold levels.
* **Over Bought**: Overbought quantity
* **Over Sold**: Oversold quantity
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[
\text{Fast } \%K = 100 \times \mathrm{SMA}\left(
\frac{Close – Low}{High – Low},
\text{Time Period}
\right)
\]

\[
\text{Slow } \%K = \mathrm{SMA}(\text{Fast } \%K, K\_{ma})
\]

\[
\text{Slow } \%D = \mathrm{SMA}(\text{Slow } \%K, D\_{ma})
\]

where:

* Close = the current closing price
* Low = the lowest low in the past n periods
* High = the highest high in the past n periods
* Kma = Period of Moving Average used to smooth the Fast %K Values
* Dma = Period of Moving Average used to smooth the Slow %K Values

←[Previous PostKlinger Volume Oscillator (KVO)](klinger-volume-oscillator-kvo.md)

[Next PostLinear Regression Forecast (LRF)](linear-regression-forecast-lrf.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stochastic-momentum-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stochastic-momentum-index-1.png
