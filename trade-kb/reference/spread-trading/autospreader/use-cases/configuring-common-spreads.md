---
title: Configuring Common Spreads
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/configuring-common-spreads/
---

# Configuring Common Spreads

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/use-cases/configuring-common-spreads/)

Below are listed parameters for configuring common synthetic spreads. These settings are intended for illustrative
purposes and may not be the only way to create these spreads. The performance of these synthetic instruments is
dependent on market conditions and are in no way guaranteed profitability.

The parameters displayed in the table are entered into the spread configuration fields where labeled in the image
below. Note that tick size is entered in the field labeled **Override** which requires activation of the
checkbox. For more information about spread parameters, refer to [Spread
Configuration](../description-autospreader/spread-configuration.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-usecase-editor.png)

#### Crush

**Formula:** Price Differential
**Tick Size:** 1/100

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1 | 2 | 3 |
| Contracts | ZS / CME | ZM / CME | ZL / CME |
| Ratio | -10.0 | 11.0 | 9.0 |
| Multiplier | -1.0 | 2.2 | 11.0 |

#### CRACK

**Formula:** Price Differential
**Tick Size:** 1/100

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1 | 2 | 3 |
| Contracts | CL / CME | RB / CME | HO / CME |
| Ratio | -3.0 | 2.0 | 1.0 |
| Multiplier | -1 | 28.0 | 14.0 |

#### ES/YM Ratio

**Formula:** Ratio
**Tick Size:** default

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ES / CME | YM / CME |
| Ratio | 5.0 | -6.0 |
| Multiplier | 50.0 | 5.0 |

#### TUT

**Formula:** Net Change
**Tick Size:** 1/8

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZT / CME | ZN / CME |
| Ratio | 2.0 | -1.0 |
| Multiplier | 1/8 | -1/8 |

#### TUF

**Formula:** Net Change
**Tick Size:** 1/8

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZT / CME | ZF / CME |
| Ratio | 4.0 | -3.0 |
| Multiplier | 1/8 | -3/32 |

#### TUB

**Formula:** Net Change
**Tick Size:** 1/8

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZT / CME | ZB / CME |
| Ratio | 6.0 | -1.0 |
| Multiplier | 1/8 | -1/12 |

#### FYT

**Formula:** Net Change
**Tick Size:** 1/4

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZF / CME | ZN / CME |
| Ratio | 3.0 | -2.0 |
| Multiplier | 1/4 | -1/3 |

#### FOB

**Formula:** Net Change
**Tick Size:** 1/4

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZF / CME | ZB / CME |
| Ratio | 5.0 | -1.0 |
| Multiplier | 1/4 | -1/5 |

#### NOB

**Formula:** Net Change
**Tick Size:** 1/2

|  |  |  |
| --- | --- | --- |
|  | 1 | 2 |
| Contracts | ZN / CME | ZB / CME |
| Ratio | 3.0 | -1.0 |
| Multiplier | 1/2 | -1/3 |

←[Previous PostUsing instruments as pricing components of a spread](using-instruments-as-pricing-components-of-a-spread.md)

[Next PostBasis Trading Metals and FX](basis-trading-metals-and-fx.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-usecase-editor.png
