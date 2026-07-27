---
title: Linear Regression Intercept (LRI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/linear-regression-intercept-lri/
---

# Linear Regression Intercept (LRI)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/linear-regression-intercept-lri/)

Linear regression is a statistical tool used
to help predict future values from past values. It is commonly used
as a quantitative way to determine the underlying trend and when
prices are overextended. A linear regression trendline uses the
least squares method to plot a straight line through prices so as
to minimize the distances between the prices and the resulting trendline.
This linear regression intercept indicator plots the intercept for
the trendline for each data point.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/linear-regression-intercept.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/linear-regression-intercept-1.png)

* **Period**: Number of bars to use in the calculations.
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

The best fit line associated with the n points
(x1, y1), (x2, y2), . . . , (xn, yn) has the
form y = mx + b

[slope;=;m;=;frac{sum\_{i=1}^{n}(x\_{i} – bar{x})(y\_{i} – bar{y})}{sum\_{i=1}^{n}(x\_{i} – bar{x})^{2}}]

[intercept;=;b;=;bar{y} – mbar{x}]

←[Previous PostLinear Regression Forecast (LRF)](linear-regression-forecast-lrf.md)

[Next PostLinear Regression Slope R2 (R2)](linear-regression-slope-r2-r2.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/linear-regression-intercept.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/linear-regression-intercept-1.png
