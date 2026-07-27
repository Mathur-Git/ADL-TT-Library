---
title: Chande Momentum Oscillator (CMO)
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chande-momentum-oscillator-cmo/
---

# Chande Momentum Oscillator (CMO)

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/technical-indicators/chande-momentum-oscillator-cmo/)

The Chande Momentum Oscillator (CMO) attempts to capture the momentum of the instrument.
The indicator oscillates between -100 and 100 with overbought level
of 50 and oversold level of -50.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-momentum-oscillator.png)

## Configuration Options

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-momentum-oscillator-1.png)

* **Period**: Number of bars to use in the calculations.
* **Color Selectors**: Colors to use for graph elements.
* **Over Zones Enabled**: Whether to shade the area between the plot and the horizontal overbought and oversold levels.
* **Over Bought**: Overbought quantity
* **Over Sold**: Oversold quantity
* **Display Axis Label**: Whether to display the most recent value on the Y axis.

## Formula

[CMO = left (frac{PosSum – NegSum}{PosSum + NegSum} right )times 100]

where:

[PosSum = sum (Close\_{current};-;Close\_{previous});when;(Close\_{current};-;Close\_{previous}) > 0]

[NegSum = sum left | (Close\_{current};-;Close\_{previous}) right |;when;(Close\_{current};-;Close\_{previous})

←[Previous PostChande Forecast Oscillator (CFO)](chande-forecast-oscillator-cfo.md)

[Next PostMoney Flow Index (MFI)](money-flow-index-mfi.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-momentum-oscillator.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chande-momentum-oscillator-1.png
