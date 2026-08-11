---
title: Creating Uptick and Downtick Counters
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-uptick-and-downtick-counters/
---

# Creating Uptick and Downtick Counters

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-uptick-and-downtick-counters/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Market data, bars and indicators](../../../../guides/design-patterns.md#market-data-bars-and-indicators)

This is a possible way to use ADL to take a specific Instrument and pull out the Bid Price for that instrument…. and then create a counter that uses a User Defined Uptick/Downtick variable and monitors the market data. Then when the User Defined number of Uptick or Downticks in the market is reached…. this then outputs a TRUE boolean value which can then be used as a trigger condition within an algos logic.

**Note**: The 2 different State Blocks #1 and #2 both use the same internal formulas as shown in the screen shots. But make sure to change the reference VE (Value Extractor block) to either VE block Bid Price 1 or VE block Bid Price 2 in order to make sure you are referencing the correct values. State Blocks #2 should reference VE block Bid Price 2 , and State Block #1 should reference VE block Bid Price 1.

Below you will see 2 screen shots of logic. They are very similar in construction, but they differ with the internal State Block conditional logic in order to perform UPTICK logic or DOWNTICK Logic
Internal conditional logic for State Blocks #1 and #2:

#### Uptick Counter

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-uptick-downtick-counters-1.jpg)

State Block 1…….Condition 1: Bid Price > VE Bid Prc 1 Condition 2: Bid Price

State Block 2…….Condition 1: Bid Price > VE Bid Prc 2 Condition 2: Bid Price

#### Downtick Counter

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-uptick-downtick-counters-2.jpg)

State Block 1…….Condition 1: Bid Price VE Bid Prc 1

State Block 2…….Condition 1: Bid Price VE Bid Prc 2

←[Previous PostSubmit Iceberg with Random Quantity and Delay](submit-iceberg-with-random-quantity-and-delay.md)

[Next PostTime Series Bars for OHLC and VWAP Values](time-series-bars-for-ohlc-and-vwap-values.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-uptick-downtick-counters-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-uptick-downtick-counters-2.jpg
