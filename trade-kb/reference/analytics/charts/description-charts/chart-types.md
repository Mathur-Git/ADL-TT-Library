---
title: Chart types
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/description-charts/chart-types/
---

# Chart types

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/description-charts/chart-types/)

TT offers a variety of chart types to help you display chart data in several different formats. Chart types can be accessed from the **Chart Types** menu and from **Search**, as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-types-menu.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-types-selection.png)

TT offers the following chart types:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bar.png)

#### Bar

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-bar.png)

#### Colored Bar

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/baseline-delta.png)

#### Baseline Delta

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/baseline-delta-mountain.png)

#### Baseline Delta Mountain

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/candle.png)

#### Candle

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hollow-candle.png)

#### Hollow Candle

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hlc.png)

#### HLC

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-hlc.png)

#### Colored HLC

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/line.png)

#### Line

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-line.png)

#### Colored Line

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/constant-volume-bar.png)

#### Constant Volume

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/heikin-ashi.png)

#### Heikin Ashi

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/histogram.png)

#### Histogram

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mountain.png)

#### Mountain

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-distribution.png)

#### Price Distribution

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/step.png)

#### Step

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-step.png)

#### Colored Step

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/scatterplot.png)

#### Scatterplot

---

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/volume-candle.png)

#### Volume Candle

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wave.png)

#### Wave

## Interpreting charts

For Candle, Bar, Colored Bar, and Hollow Candle charts:

* Green shows the close price was higher than the open.
* Red shows the close price was lower.
* A line extending from the body indicates a High or Low different from the open or close.
* Line with no candlestick indicates the same open and close with a different high or low.
* Dash with no line indicates no movement.
* A tail extending from the body indicates a High or Low different from the open or close.

In addition, the color of the bar determines how the chart is read:

* If the period is green: the top represents the Close (and High if there is no extending tail). The bottom is the Open (and Low if there is no extending tail).
* If the period is red: the top represents the Open (and High if there is no extending tail). The bottom is the Close (and Low if there is no extending tail).

## Continuation Charts

A continuation chart splices together several consecutive expiry months to form a seamless chart.

![Continuation Chart example](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-type-continuation-scaled.png)

The rollover from one expiry to the next is illustrated by an alternating colored line at the bottom of the chart as well as dotted lines along the y-axis.

You can create and configure a Continuation Chart by right-clicking in a chart and selecting **Settings: Chart…**

![Continuation Chart settings](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-type-continuation-chart-settings.png)

To create a continuation chart you select one of the roll-over options from the contract roll drop-down in the **Continuation** section of Chart Settings. This section provides a number of options for defining how you would like the chart to display the roll between expiries.

### Contract Roll Settings

* **No Continuation**: (Default) Do not display continuation data.
* **Standard At Expiration**: The instrument rolls to the next expiration the day after the most current instrument expires.
* **Adjust By N Days**: Select a number of trading days from the expiration date on which to roll from one instrument to the next.
* **Roll By Day Of Month**: Select the day Of month during the expiration month on which to roll from one instrument to the next.

### Additional Settings

* **Selected Months**: Choose which months to include in the continuation chart.
* **Equalize Closes**: Equalize the close of the day of the roll by using the old most active or lead month’s closing price and subtracting it from the new most active or lead month’s closing price. The result is then added to the open, high, low, and closing price of all historical bars.
* **Most Active**: Set the lead month to the most active instrument.

## Price Distribution charts

The Price Distribution chart displays the distribution of price over time. It includes the Initial Balance Range, opening price, a current price marker, the Time Price Area (TPA letters) value area, and the Tick Volume Distribution.

![Add-PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-price-dist-annotation.png)

### Interpreting the Price Distribution chart

The Time Price Area (TPA) provides a summary of the [letters](#tpa-letters) in the chart.

![TPA area](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa.png)

The Time Price Area (TPA) letter summary provides the following information about the [letters](#tpa-letters) in the chart.

1. The number of [letters](#tpa-letters) within the Time Price Area (TPA)
2. The number of letters at the point of control (POC)
3. The number of letters above the point of control
4. The number of letters below the point of control

The main part of the chart provides the following information about the price distribution during a trading day.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-nums.png)

1. The [letters](#tpa-letters) represent the consecutive 30-minute slices of the trading day.
2. The arrow pointing to the right identifies the open. The price is the first actual traded price, not the last session’s close.
3. The dark orange shading indicates the Initial Balance Range, which represents the first two TPA letters of the day.
4. The arrow pointing left identifies the last traded price (LTP) of the distribution.
5. The dark blue and red letter shading indicates the buy and sell volumes in the Volume Value Area.
6. The TPA Value Area indicates where [70%](#value-area-calculation) of the TPA letters occurred.
7. The light orange shading in the TPA and in the TPA Value area identifies the point of control, which is the largest number of TPA letters for the distribution.
8. The Volume Value Area indicates where [70%](#value-area-calculation) of the volume distribution occurred.
9. The small block in the Volume Value Area represents the volume point of control.

### Splitting TPAs on Price Distribution charts

On a Price Distribution chart, you can separate a TPA into columns for a clearer view of the distributions and breaks. To separate a TPA, right-click on the distribution and select **Split All** from the context menu.

![TPA area](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa-split.png)

To return the TPA back to its original position, right-click on the distribution and select **Remove All Splits**.

![TPA area](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa-split-remove.png)

### Time Price Area letters

Time Price Area (TPA) letters are assigned in 30 minute periods. They are plotted using the letter that is in progress at the beginning of each 30 minute period.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 08:00 | I | 12:00 | R | 16:00 | a | 20:00 | i | 24:00 | r | 04:00 |
| B | 08:30 | J | 12:30 | S | 16:30 | b | 20:30 | j | 00:30 | s | 04:30 |
| C | 09:00 | K | 13:00 | T | 17:00 | c | 21:00 | k | 01:00 | t | 05:00 |
| D | 09:30 | L | 13:30 | V | 17:30 | d | 21:30 | l | 01:30 | v | 05:30 |
| E | 10:00 | M | 14:00 | W | 18:00 | e | 22:00 | m | 02:00 | w | 06:00 |
| F | 10:30 | N | 14:30 | X | 18:30 | f | 22:30 | n | 02:30 | x | 06:30 |
| G | 11:00 | P | 15:00 | Y | 19:00 | g | 23:00 | p | 03:00 | y | 07:00 |
| H | 11:30 | Q | 15:30 | Z | 19:30 | h | 23:30 | q | 03:30 | z | 07:30 |

### Value area calculation

The value area is calculated by first identifying the price with the greatest volume. Using this, the volume of the two adjacent prices above are summed and the volume of the two adjacent prices below are summed. These totaled volumes are then compared and the larger of the two is added to the value area. This process continues until 70 percent of the volume is contained within the value area. Value area can be calculated using either the actual volume at price numbers or approximated by using TPA letter counts at price levels.

**Note**: You can change the percentage to use for calculations in the [Chart settings](../reference-charts/chart-settings.md).

←[Previous PostChart Overview](chart-overview.md)

[Next PostChart trading](chart-trading.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-types-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-types-selection.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bar.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-bar.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/baseline-delta.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/baseline-delta-mountain.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/candle.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hollow-candle.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hlc.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-hlc.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/line.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-line.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/constant-volume-bar.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/heikin-ashi.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/histogram.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mountain.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/price-distribution.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/step.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/colored-step.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/scatterplot.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/volume-candle.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wave.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-type-continuation-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-chart-type-continuation-chart-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-price-dist-annotation.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-nums.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa-split.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chart-type-tpa-split-remove.png
