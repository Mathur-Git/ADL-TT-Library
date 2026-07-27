---
title: Time Series Bars for OHLC and VWAP Values
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/time-series-bars-for-ohlc-and-vwap-values/
---

# Time Series Bars for OHLC and VWAP Values

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/time-series-bars-for-ohlc-and-vwap-values/)

ADL allows a number of ways to create [technical indicators](../../../miscellaneous-blocks/analytics-block.md#technical-indicators). In this article, we focus on creating time series bars for OHLC (Open, High, Low, Close) and VWAP (Volume Weighted Average Price indicators).

This first ADL Canvas leverages the [Analytics block](../../../miscellaneous-blocks/analytics-block.md) to update the time series bars at 1 Minute Time intervals.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-1.jpeg)

You can compare this method with creating the OHLC using the [Time and Sales block](../../../trading-blocks/time-and-sales-block.md) and having a boolean condition trigger for the various “Time Series” calculations.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-2.jpeg)
  
![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-3.jpeg)

In addition, the following code sample illustrates a method for building and storing 1 min OHLC values. In this example the past 4 bars are tracked as well as the current activity. The values are calculated off the [Time and Sales block](../../../trading-blocks/time-and-sales-block.md) with snapshots taken every minute so it takes 4 minutes for the bar data to be loaded. If there is a 1 min period where nothing trades, a snapshot for that period will not be taken. Also, block trades have been filtered out from the time and sales feed.

←[Previous PostCreating Uptick and Downtick Counters](creating-uptick-and-downtick-counters.md)

[Next PostCreating OHLC and VWAP Time Bars](creating-ohlc-and-vwap-time-bars.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-1.jpeg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-2.jpeg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-series-for-ohlc-vwap-3.jpeg
