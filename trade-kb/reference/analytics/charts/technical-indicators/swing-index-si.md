---
title: Swing Index (SI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/swing-index-si/
---

# Swing Index (SI)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/swing-index-si/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Swing Index (SI) indicator is an oscillator that is used as part of the Accumulative Swing Index for determining price trends for an instrument. Typically, an indication to buy is when the SI curve crosses above the zero line, and an indication to sell is when the SI curve crosses below the
zero line.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/swing-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/swing-index-1.png)

* **Limit Move Value**: Value of a limit move in one direction
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

[ SI = 50 times left ( frac{(C\_{y} – C\_{t}) + (0.5 \* (C\_{y} – O\_{y}) + (0.25 \* (C\_{t} – O\_{t})}{R} right ) times frac{K}{T} ]

where:

* Oy = Yesterday’s Open
* Ot = Today’s Open
* Hy = Yesterday’s High
* Ht = Today’s High
* Ly = Yesterday’s Low
* Lt = Today’s Low
* Cy = Yesterday’s Close
* Ct = Today’s Close
* K = largest of:
  * Ht – Cy
  * Lt – Cy
* R is based on the largest of:
  1. Ht – Cy
  2. Lt – Cy
  3. Ht – LtIf (1) is the largest, R = (Ht – Cy) – .5(Lt –
  Cy) + .25(Cy – Oy)  
  If (2) is the largest, R = (Lt – Cy) – .5(H2 –
  Cy) + .25(Cy – Oy)  
  If (3) is the largest, R = (Ht – Lt) + .25(Cy –
* T = Limit Move Value

←[Previous PostRelative Vigor Index](relative-vigor-index.md)

[Next PostTime Series Forecast (TSF)](time-series-forecast-tsf.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/swing-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/swing-index-1.png
