---
title: Creating OHLC and VWAP Time Bars
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-ohlc-and-vwap-time-bars/
---

# Creating OHLC and VWAP Time Bars

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-ohlc-and-vwap-time-bars/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Market data, bars and indicators](../../../../guides/design-patterns.md#market-data-bars-and-indicators)

### How to create Open, High, Low, Close, VWAP logic

In the below screen shots you will see Open, High, Low, Close (OHLC) is simple to create using the Time and Sales Block. Then using the extracted Trade Price value, you use this to create the various needed Value Calculations.

Please note:

* The Value Bucket Blocks are simply set for LAST with the internal “mode” selection. The internal “storeKey” formula is referencing TradeCounter block output. The “storeVal” is referencing TradePrc block output.
* The Min and Max for the TradePrc block output will give you the HIGH and LOW values.
* Volume is from the Value Accumulator block to give you the VWAP value for each designated Time Bar created.

#### Time Bars

This example leverages the Generator Block set to a User Defined Variable setting for time frame. We have it set for 60 seconds or 1 minute Time Bar creations. You also see below that there is 2 sets of OHLC and VWAP value outputs. This is to show you the current Time Bar and the previous one. This again is strictly for showing an example of one way to build this kind of logic.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-creating-ohlc-vwap-time-bars.jpg)

←[Previous PostTime Series Bars for OHLC and VWAP Values](time-series-bars-for-ohlc-and-vwap-values.md)

[Next PostStacked Q Holder Example](stacked-q-holder-example.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-creating-ohlc-vwap-time-bars.jpg
