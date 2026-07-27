---
title: Price Volume Trend (PVT)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/price-volume-trend-pvt/
---

# Price Volume Trend (PVT)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/price-volume-trend-pvt/)

The Price Volume Trend (PVT) study attempts to quantify the amount of volume flowing into or out of an instrument by identifying the close of the period in relation to the previous period’s close. The volume for the period is then added to a running continuous total.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-volume-trend.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-volume-trend-1.png)

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

\[ PVT = \left ( \frac{Close\_{current} – Close\_{previous}}{Close\_{previous}} \right ) + PVT\_{previous}\]

←[Previous PostPrice Rate of Change](price-rate-of-change.md)

[Next PostPring’s Know Sure Thing (KST)](prings-know-sure-thing-kst.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-volume-trend.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-volume-trend-1.png
