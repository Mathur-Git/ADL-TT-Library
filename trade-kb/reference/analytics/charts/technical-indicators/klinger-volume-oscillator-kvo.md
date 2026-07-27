---
title: Klinger Volume Oscillator (KVO)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/klinger-volume-oscillator-kvo/
---

# Klinger Volume Oscillator (KVO)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/klinger-volume-oscillator-kvo/)

Klinger Volume Oscillator, developed by Stephen Klinger, uses the key price compared to the prior bar’s key price to assign volume as positive or negative value.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/klinger-volume-oscillator.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/klinger-volume-oscillator-1.png)

* **Signal Periods**: TBD
* **Short Cycle**: Number of periods to include in the short cyle.
* **Long Cycle**: Number of periods to include in the long cycle.
* **Color Selectors**: Colors to use for graph elements.
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

\[Key\;Price\_{t} = \frac{High\_{t} + Low\_{t} + Close\_{t}}{3} \]

\[Key\;Price\_{t-1} = \frac{High\_{t-1} + Low\_{t-1} + Close\_{t-1}}{3} \]

\[
\text{Trend} =
\begin{pmatrix}
\text{if } \text{Key Price}\_t > \text{Key Price}\_{t-1}, \quad \text{Volume} \\
\text{if } \text{Key Price}\_t < \text{Key Price}\_{t-1}, \quad -\text{Volume}
\end{pmatrix}
\]

\[KVO = EMA\_{short-period}(Trend) – EMA\_{long-period}(Trend) \]

\[KVO\;Signal = EMA\_{signal}(KVO)\]

where

\[EMA = exponential\;moving\;average\;of\;user\;defined\;lengths\;of\;short-period,\;long-period,\;and\;signal.\]

←[Previous PostKeltner Channel (KC)](keltner-channel-kc.md)

[Next PostStochastic Momentum Index (STOCH)](stochastic-momentum-index-stoch.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/klinger-volume-oscillator.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/klinger-volume-oscillator-1.png
