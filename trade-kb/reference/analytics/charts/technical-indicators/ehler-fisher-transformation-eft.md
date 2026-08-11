---
title: Ehler Fisher Transformation (EFT)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/ehler-fisher-transformation-eft/
---

# Ehler Fisher Transformation (EFT)

> Category: **Analytics** · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/ehler-fisher-transformation-eft/)
>
> **Interpreted in:** [Charts & Analytics § Technical indicators](../../../../guides/charts-and-analytics.md#technical-indicators)

Ehler Fisher Transformation indicator tries to identify significant price reversals by normalizing
prices over a user-specified number of periods. A reversal signal is suggested when the two lines cross.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ehler-fisher-transformation.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ehler-fisher-transformation-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

[MidPoint = MP = frac{High – Low)}{2}]

[Intermediate = I = 2 times frac{MP –
LowestLow\_{n-periods}}{HighestHigh\_{n-periods}-LowestLow\_{n-periods}}]

The intermediate term I is then smoothed by a 5-period exponential moving average (EMA) then
transformed to a log form (fisher transform) before a final 3-period exponential moving average (EMA) smoothing:

[I\_{smoothed} = EMA\_{5-period};of;I]

[EFT = EMA\_{3-period};of;log left ( frac{1+I\_{smoothed}}{1-I\_{smoothed}} right )]

←[Previous PostEase of Movement (EOM)](ease-of-movement-eom.md)

[Next PostElder Force Index (EFI)](elder-force-index-efi.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ehler-fisher-transformation.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ehler-fisher-transformation-1.png
