---
title: Donchian Channel
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/donchian-channel/
---

# Donchian Channel

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/donchian-channel/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

The Dochian Channel indicator creates a channel between the highest high price and lowest low price for the previous user-defined number of bars. The width of the channel helps visualize the volatility of the market price. If the price fluctuates a lot, the channel will be wider. Converely, when the price moves less, the channel will be narrower. The center line tracks the midpoint between the bands.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/donchian-channel.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/donchian-channel-1.png)

* **High Period**: Number of bars to use for the highest high price.
* **Low Period**: Number of bars to use for the lowest low price.
* **Channel Fill**: Whether to shade the region between the upper and lower bands.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.
* **Include In Auto Scale**

## Formula

The Donchian Channel uses the following formulas:

* \( DC\_{upper} = High\_{n-periods} \)
* \( DC\_{lower} = Low\_{n-periods} \)
* \( DC\_{middle} = \frac {DC\_{upper} + DC\_{lower}}{2} \)

←[Previous PostDisparity Index](disparity-index.md)

[Next PostDonchian Width](donchian-width.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/donchian-channel.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/donchian-channel-1.png
