---
title: Stacked Q Holder Example
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/stacked-q-holder-example/
---

# Stacked Q Holder Example

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/stacked-q-holder-example/)

### How to Build a Stacked Q Holder type logic

This example is a very basic type logic build that will stack the book for both the BUY and SELL side of the contracts market based on a UDV “Initial BASE Price”. This BASE Price will be entered in by the user; and then allow the user to set the Stack Depth based on a number of Price Increments away from each subsequently placed order.

* The Initial BASE Price in the TT platform is a User Defined Variable (UDV). One thing to note here is that you have to set this price as a whole number and not in decimal format. Please test in SIM to make sure your Pricing number is placing to the exact specified price.
* Stack Depth is the calculation that sets how many orders are to be placed up or down the market from your UDV “Initial BASE Price”. The Stack Depth calculation is the Interval in between each order based on Repetitions/Loop UDV x Interval UDV.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-1.jpg)

**Note**: This example is a very basic ENTRY ONLY type of algo. This example will simply place NEW Entry child orders at the back of the Stack Q based on LAST FILL Price. Also, the reason there is order qty’s of 2 in the above screen shot from the workspace is due to running an algo from the ADL Design Canvas as well as from the Algo Dashboard. This was done so as to help show how the values update throughout the algo logic as seen on the canvas.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-2.jpg)

Inside Stacking Order Block group block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-3.jpg)

Inside the Sell Side and Buy Side virtualized group blocks

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-4.jpg)
  
![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-5.jpg)

#### Explanations for internal formulas of various blocks in the algo

* LAST FILL: set to extract the FILL Price from the incoming discrete messages.
* Initial BASE Price Inject: set to inject a FILL PRICE based on the UDV
* Counter Buy and Counter Sell: sets a counter equal to 1
* Buy Price Maker: (Stacking Order Block: If Then Filled Price) – (Stacking Order Block: Loop index x Tick Size x Interval)
* Sell Price Maker: (Stacking Order Block: Loop index x Tick Size x Interval) + (Stacking Order Block: If Then Filled Price)
* SELL DOB: Price [ IF (Stacking Order Block Counter Sell)
* BUY DOB: Price [ IF (Stacking Order Block Counter Buy)

←[Previous PostCreating OHLC and VWAP Time Bars](creating-ohlc-and-vwap-time-bars.md)

[Next PostSmartberg Algo](smartberg-algo.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-2.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-3.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-4.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-stacked-q-holder-5.jpg
