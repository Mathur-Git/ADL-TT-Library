---
title: Accumulative Swing Index (ASI)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/accumulative-swing-index-asi/
---

# Accumulative Swing Index (ASI)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/accumulative-swing-index-asi/)

The Accumulative Swing Index created by Welles Wilder attempts to find the swing line within the bar. Originally created to apply to daily bars, as there is a market or user defined value of the maximum price change that can occur during the trading session. Using the study on intra-day bar data will require the user to specify a limit value for the given bar interval.

Welles Wilder created this indicator based on the below important reference points:

1. Today’s close is higher (lower) than the prior close
2. Today’s close is higher (lower) than today’s open
3. Today’s high (low) is greater (less) than the prior close
4. Today’s low (high) is greater (less) than the prior close
5. The prior close was above (below) the prior open.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulative-swing-index.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulative-swing-index-1.png)

* **Limit Move Value:** Maximum price change during a trading session
* **Result:** Color of the technical indicator
* **Display Axis Label:** Check to show the axis label

## Formula

\[ASI\_{t} = ASI\_{t-1} + SI\_{t}\]

where \(SI\_{t}\) is the current bar’s swing index calculated by the formula:

\[SI\_{t} = 50 \times \left ( \frac{Close\_{t} – Close\_{t-1}+0.5\times(Close\_{t}-Open\_{t})+0.25 \times (Close\_{t-1}-Open\_{t-1})}{R} \right ) \times \frac{K}{T}\]

where

\[K = max\left ( High\_{t} – Close\_{t-1}\;,\;Close\_{t-1} – Low\_{t} \right )\]

\(T\) is a user defined value which means the maximum price change during a trading session.

\(R\) is a value calculated on the base of the relationship between current close price and previous high and low prices. The formula is:

\[R = TR – 0.5 \times ER + 0.25 \times SH\]

where

\[TR = max(High\_{t} – Close\_{t-1} , Close\_{t-1} – Low\_{t} , High\_{t} – Low\_{t})\]
\[ER = \left\{\begin{matrix} High\_{t} – Close\_{t-1} & if Close\_{t-1} > High\_{t} \\ 0 & if Low\_{t} \leq Close\_{t-1} \leq High\_{t} \\ Close\_{t-1} – Low\_{t} & if Close\_{t-1} < Low\_{t} \end{matrix}\right.\]
\[SH = Close\_{t-1} – Open\_{t-1}\]

←[Previous PostAccumulation Distribution (ACC Dist)](accumulation-distribution-acc-dist.md)

[Next PostADX/DMS](adx-dms.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulative-swing-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/accumulative-swing-index-1.png
