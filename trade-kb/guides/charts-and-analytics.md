# Charts & Analytics

[KB Home](../README.md) · [Full Index](../INDEX.md) · [Spread Trading / Autospreader](spread-trading-autospreader.md) ·
[Order Types & Execution](order-types-and-execution.md) · [Market Data & Depth](market-data-and-depth.md) ·
[Algo Ops](algo-ops.md) · [Order Management & Risk](order-management-and-risk.md) ·
[Platform & Workspace](platform-and-workspace.md) · Charts & Analytics (this page)

The Chart widget is TT's charting surface: historical bar/tick data blended with the same live price feed used by
MD Trader and the other order-entry widgets, with over 115 technical indicators, a full drawing-tools kit, and the
ability to trade directly from the chart. This guide catalogs chart types, settings, drawing tools, chart-trading
workflow, every technical indicator, and Trader Analytics — the platform-side complement to
[ADL's Analytics block](../../adl-kb/reference/miscellaneous-blocks/analytics-block.md), which computes several of
these same indicators (ATR, Bollinger, MACD, SMA/EMA/DEMA/TEMA/WMA, RSI, StdDev, Stochastic) server-side inside a
running algo.

---

## Chart types & basics

The Chart widget opens from instrument search, Market Explorer, the Widgets menu, or as a linked widget from a
Market Grid. Its **Chart menu** (top-left icon) is the hub for chart type, technical indicators, intervals, drawing
tools, the trading order pane, snapshot export, crosshair, Trading Schedules, comparisons, and settings — see
[Chart Overview](../reference/analytics/charts/description-charts/chart-overview.md).

TT offers the following chart types, described in
[Chart types](../reference/analytics/charts/description-charts/chart-types.md):

| Chart type | Notes |
|---|---|
| Bar / Colored Bar | OHLC bars; colored variant shades by up/down close |
| Candle / Hollow Candle | Standard candlesticks |
| HLC / Colored HLC | High-low-close bars without an open tick |
| Line / Colored Line | Close-price line |
| Baseline Delta / Baseline Delta Mountain | Shades area above/below a baseline |
| Mountain | Filled area under the close line |
| Constant Volume | Bars sized by a fixed volume increment rather than time |
| Heikin Ashi | Smoothed candles that filter noise to highlight trend |
| Histogram | Vertical bars per period |
| Step / Colored Step | Stair-step price line |
| Scatterplot | Discrete point plot |
| Volume Candle | Candle width scaled by volume |
| Wave | Smoothed continuous price curve |
| Price Distribution | Time Price Area (TPA) / volume distribution profile — see below |

**Continuation charts** splice consecutive expiry months into one seamless series, with configurable roll rules
(Standard At Expiration, Adjust By N Days, Roll By Day Of Month) and an Equalize Closes option — see
[Chart types § Continuation Charts](../reference/analytics/charts/description-charts/chart-types.md#continuation-charts).

**Price Distribution charts** show the Initial Balance Range, opening price, Time Price Area (TPA) letters in
30-minute slices, the point of control (POC), and the Volume/TPA Value Areas (default 70% — configurable in
[Chart Settings](../reference/analytics/charts/reference-charts/chart-settings.md)) — see
[Chart types § Price Distribution charts](../reference/analytics/charts/description-charts/chart-types.md#price-distribution-charts).

## Chart settings & drawing tools

All per-widget configuration — chart type, interval, colors, fonts, trading-pane behavior (Show Fills, Show Working
Orders, Enable Trading Mode, custom action buttons, max order quantity, Stop Limit payup), and the Price
Distribution-specific display toggles — lives in
[Chart Settings](../reference/analytics/charts/reference-charts/chart-settings.md) (right-click → **Settings**).

TT ships 30+ drawing tools, all documented with their configuration options in
[Drawing tools](../reference/analytics/charts/description-charts/drawing-tools.md): None, Annotation, Arrow,
Average, Callout, Channel, Check, Continuous, Crossline, Ellipse, Fibarc, Fibfan, Fibonacci, Fibprojection,
Fibtimezone, Focusarrow, Freeform, Gannfan, Gartley, Line, Pitchfork, Quadrant, Ray, Rectangle, Regression, Segment,
Speedarc, Speedline, Star, Timecycle, Tirone, Trendline, Vertical, Xcross, and Clear Drawings. Drawing tools are not
available on Price Distribution charts.

## Trading from a chart

Enabling trading on a chart adds an order pane (accounts, order type, TIF, quantity) plus clickable Bids/Asks
columns for one-click order entry, and can display fills and working orders overlaid on the price data — see
[Chart trading](../reference/analytics/charts/description-charts/chart-trading.md).

| Task | Reference |
|---|---|
| Add an instrument to a chart | [Adding an instrument to a chart](../reference/analytics/charts/task-charts/adding-an-instrument-to-a-chart.md) |
| Change chart type, interval, daily-value box, price axis, LTP spread formula | [Formatting charts](../reference/analytics/charts/task-charts/formatting-charts.md) |
| Add/remove/edit a technical indicator, or stack one indicator on another (study-on-a-study) | [Using technical indicators](../reference/analytics/charts/task-charts/using-technical-indicators.md) |
| Overlay another instrument's data for comparison | [Adding a comparison](../reference/analytics/charts/task-charts/adding-a-comparison.md) |
| Add up to two more instruments as independent-axis line series | [Adding a series](../reference/analytics/charts/task-charts/adding-a-series.md) |
| Enter orders by clicking Bids/Asks cells; customize quantity buttons | [Entering orders on a chart](../reference/analytics/charts/task-charts/entering-orders-on-a-chart.md) |
| Show fills (grouped by interval or by position) and working orders | [Displaying fills and working orders](../reference/analytics/charts/task-charts/displaying-fills-and-working-orders.md) |
| Reprice/delete working orders directly on the chart; group with MD Trader | [Modifying working orders in a chart](../reference/analytics/charts/task-charts/modifying-working-orders-in-a-chart.md) |
| Cancel one order, all buys, all sells, or all working orders | [Canceling orders on a chart](../reference/analytics/charts/task-charts/canceling-orders-on-a-chart.md) |
| Add custom order-type / TIF / algo-template buttons to the order pane | [Adding a custom action button](../reference/analytics/charts/task-charts/adding-an-custom-action-button.md) |
| Export bar + indicator data to CSV | [Exporting Chart Data](../reference/analytics/charts/task-charts/exporting-chart-data.md) |

**Trading Schedules**: view/modify per-product exchange session times, or build and save custom trading schedules
and map them to other products, then apply an exchange or custom schedule to any chart (including Autospreader and
Aggregator instruments) — see
[Trading Schedules](../reference/analytics/charts/description-charts/trading-schedules.md).

## Technical indicators

The Chart's **Technical Indicators** menu holds 117 studies, each with its own configuration options (period, price
field, moving-average type, overbought/oversold zones, etc.) and a documented formula. Add one from the chart menu
or by searching its name; indicators can also be layered on top of each other (study-on-a-study) — see
[Technical Indicators (overview)](../reference/analytics/charts/description-charts/technical-indicators.md) and
[Using technical indicators](../reference/analytics/charts/task-charts/using-technical-indicators.md).

**Connection to ADL**: [ADL's Analytics block](../../adl-kb/reference/miscellaneous-blocks/analytics-block.md)
computes a subset of these indicators (ATR, Bollinger Bands, MACD, Simple/Exponential/Double-Exponential/
Triple-Exponential/Weighted Moving Average, RSI, Standard Deviation, Stochastic Oscillator) server-side, inside a
running algo, from its own rolling bar array — using the identical formulas documented on the Chart pages below. A
common validation workflow is to eyeball the indicator on a Chart first (visually confirm the signal you intend to
trade), then wire the equivalent Analytics-block indicator into the algo with matching period/field/MA-type
settings.

| Indicator | What it measures | Reference |
|---|---|---|
| Absolute Price Oscillator | Difference between two moving averages, unsmoothed (MACD without a signal line) | [reference](../reference/analytics/charts/technical-indicators/absolute-price-oscillator.md) |
| Accumulation Distribution (ACC Dist) | Volume-weighted line tracking buying/selling pressure from where the close sits in the day's range | [reference](../reference/analytics/charts/technical-indicators/accumulation-distribution-acc-dist.md) |
| Accumulative Swing Index (ASI) | Cumulative running total of the Swing Index, tracking longer-term price-swing momentum | [reference](../reference/analytics/charts/technical-indicators/accumulative-swing-index-asi.md) |
| ADX/DMS | Average Directional Movement Index — quantifies trend strength (not direction) from the Directional Movement system | [reference](../reference/analytics/charts/technical-indicators/adx-dms.md) |
| Alligator | Three smoothed, offset moving averages (jaw/teeth/lips) distinguishing trending from ranging markets | [reference](../reference/analytics/charts/technical-indicators/alligator.md) |
| Aroon (AR) | Time elapsed since the most recent high/low, to gauge trend presence and direction | [reference](../reference/analytics/charts/technical-indicators/aroon-ar.md) |
| Aroon Oscillator (ARO) | Difference between Aroon Up and Aroon Down as a single oscillating line | [reference](../reference/analytics/charts/technical-indicators/aroon-oscillator-aro.md) |
| ATR Bands | Bands plotted above/below price, offset by a multiple of Average True Range | [reference](../reference/analytics/charts/technical-indicators/atr-bands.md) |
| ATR Trailing Stops | Trailing stop levels derived from Average True Range | [reference](../reference/analytics/charts/technical-indicators/atr-trailing-stops.md) |
| Average True Range (ATR) | Size of the period's range, including any gap from the prior close | [reference](../reference/analytics/charts/technical-indicators/average-true-range-atr.md) |
| Awesome Oscillator | Difference between 5- and 34-period SMAs of the bar midpoint — a momentum gauge | [reference](../reference/analytics/charts/technical-indicators/awesome-oscillator.md) |
| Balance of Power | Buying vs. selling pressure from where the close falls within the bar's range | [reference](../reference/analytics/charts/technical-indicators/balance-of-power.md) |
| Boll %B | Where price sits relative to the Bollinger Bands, expressed as a percentage | [reference](../reference/analytics/charts/technical-indicators/boll-b.md) |
| Bollinger Bands (BBANDS) | Upper/lower volatility envelope: a moving average ± a multiple of standard deviation | [reference](../reference/analytics/charts/technical-indicators/bollinger-bands.md) |
| Bollinger Bandwidth | Width of the Bollinger Bands, as a standalone volatility measure | [reference](../reference/analytics/charts/technical-indicators/bollinger-bandwidth.md) |
| Center of Gravity (COG) | Low-lag oscillator built from a weighted moving average, aimed at identifying turning points early | [reference](../reference/analytics/charts/technical-indicators/center-of-gravity-cog.md) |
| Chaikin Money Flow (CMF) | Volume-weighted average of the Accumulation/Distribution line over a period | [reference](../reference/analytics/charts/technical-indicators/chaikin-money-flow-cmf.md) |
| Chaikin Volatility (CV) | Rate of change of the high-low trading range, as a volatility measure | [reference](../reference/analytics/charts/technical-indicators/chaikin-volatility-cv.md) |
| Chande Forecast Oscillator (CFO) | Percentage difference between price and its time-series-forecast value | [reference](../reference/analytics/charts/technical-indicators/chande-forecast-oscillator-cfo.md) |
| Chande Momentum Oscillator (CMO) | Momentum oscillator from the sum of gains vs. losses over a period | [reference](../reference/analytics/charts/technical-indicators/chande-momentum-oscillator-cmo.md) |
| Choppiness Index | Whether the market is trending or moving sideways/choppy | [reference](../reference/analytics/charts/technical-indicators/choppiness-index.md) |
| Commodity Channel Index (CCI) | Current typical price vs. its moving average, scaled by mean deviation | [reference](../reference/analytics/charts/technical-indicators/commodity-channel-index-cci.md) |
| Coppock Curve (CC) | Long-term momentum indicator from a weighted MA of rate-of-change, historically a buy-signal tool | [reference](../reference/analytics/charts/technical-indicators/coppock-curve-cc.md) |
| Correlation Coefficient | Statistical correlation between two price series | [reference](../reference/analytics/charts/technical-indicators/correlation-coefficient.md) |
| Darvas Box | Breakout boxes built from recent high/low ranges | [reference](../reference/analytics/charts/technical-indicators/darvas-box.md) |
| Detrended Price Oscillator (DPO) | Removes the trend component from price to expose shorter cycles | [reference](../reference/analytics/charts/technical-indicators/detrended-price-oscillator-dpo.md) |
| Directional Movement Index (DMI) | +DI / -DI lines quantifying directional price movement (feeds ADX) | [reference](../reference/analytics/charts/technical-indicators/directional-movement-index-dmi.md) |
| Disparity Index | Percentage difference between price and a moving average | [reference](../reference/analytics/charts/technical-indicators/disparity-index.md) |
| Donchian Channel | Channel between the highest high and lowest low over n bars | [reference](../reference/analytics/charts/technical-indicators/donchian-channel.md) |
| Donchian Width | Width of the Donchian Channel, as a volatility measure | [reference](../reference/analytics/charts/technical-indicators/donchian-width.md) |
| Ease of Movement (EOM) | Relates price change to volume to show how "easily" price is moving | [reference](../reference/analytics/charts/technical-indicators/ease-of-movement-eom.md) |
| Ehler Fisher Transformation (EFT) | Transforms price into a near-Gaussian distribution to sharpen turning-point signals | [reference](../reference/analytics/charts/technical-indicators/ehler-fisher-transformation-eft.md) |
| Elder Force Index (EFI) | Combines price change, direction, and volume into a single "force" reading | [reference](../reference/analytics/charts/technical-indicators/elder-force-index-efi.md) |
| Elder Impulse System | Colors bars from EMA trend + MACD-histogram momentum alignment | [reference](../reference/analytics/charts/technical-indicators/elder-impulse-system.md) |
| Elder Ray Index | Bull Power / Bear Power — buying/selling pressure relative to an EMA | [reference](../reference/analytics/charts/technical-indicators/elder-ray-index.md) |
| Fractal Chaos Bands (FCB) | Bands from fractal highs/lows, flagging potential trend changes | [reference](../reference/analytics/charts/technical-indicators/fractal-chaos-bands-fcb.md) |
| Fractal Chaos Oscillator (FCO) | Oscillator derived from fractal chaos theory, highlighting trend changes | [reference](../reference/analytics/charts/technical-indicators/fractal-chaos-oscillator-fco.md) |
| Gator Oscillator | Histogram of convergence/divergence between the Alligator lines | [reference](../reference/analytics/charts/technical-indicators/gator-oscillator.md) |
| Gopalakrishnan Range Index (GAPO) | Compares a period's range to prior ranges — a volatility measure | [reference](../reference/analytics/charts/technical-indicators/gopalakrishnan-range-index-gapo.md) |
| High Low Bands (HLB) | Bands built from moving averages of the high and low prices | [reference](../reference/analytics/charts/technical-indicators/high-low-bands-hlb.md) |
| High Minus Low (H-L) | Simple difference between a bar's high and low | [reference](../reference/analytics/charts/technical-indicators/high-minus-low-h-l.md) |
| Highest High Value (HH) | Highest high over the past n periods | [reference](../reference/analytics/charts/technical-indicators/highest-high-value-hh.md) |
| Historical Volatility (HV) | Standard deviation of price returns, as a statistical volatility measure | [reference](../reference/analytics/charts/technical-indicators/historical-volatility-hv.md) |
| Ichimoku Clouds (ICH) | Trend-following system of shifted mid-point lines forming a support/resistance "cloud" | [reference](../reference/analytics/charts/technical-indicators/ichimoku-clouds-ich.md) |
| Intraday Momentum Index (IMI) | RSI-style momentum measure adapted for intraday candlestick relationships | [reference](../reference/analytics/charts/technical-indicators/intraday-momentum-index-imi.md) |
| Keltner Channel (KC) | ATR-based bands plotted around a moving average of typical price | [reference](../reference/analytics/charts/technical-indicators/keltner-channel-kc.md) |
| Klinger Volume Oscillator (KVO) | Volume-based oscillator aimed at anticipating longer-term money-flow reversals | [reference](../reference/analytics/charts/technical-indicators/klinger-volume-oscillator-kvo.md) |
| Linear Regression Forecast (LRF) | Projected next value of the linear-regression trendline | [reference](../reference/analytics/charts/technical-indicators/linear-regression-forecast-lrf.md) |
| Linear Regression Intercept (LRI) | Intercept value of the linear-regression trendline | [reference](../reference/analytics/charts/technical-indicators/linear-regression-intercept-lri.md) |
| Linear Regression R2 (R2) | R-squared goodness-of-fit of the regression trendline | [reference](../reference/analytics/charts/technical-indicators/linear-regression-slope-r2-r2.md) |
| Linear Regression Slope (LRS) | Slope of the linear-regression trendline — trend direction/strength | [reference](../reference/analytics/charts/technical-indicators/linear-regression-slope-lrs.md) |
| Lowest Low Value (LL) | Lowest low over the past n periods | [reference](../reference/analytics/charts/technical-indicators/lowest-low-value-ll.md) |
| MACD | Fast-MA minus slow-MA, with a signal line and histogram of their difference | [reference](../reference/analytics/charts/technical-indicators/macd.md) |
| Market Facilitation Index | Relates a bar's price range to its volume, gauging market efficiency | [reference](../reference/analytics/charts/technical-indicators/market-facilitation-index.md) |
| Mass Index (MI) | High-low range expansion/contraction used to flag potential trend reversals | [reference](../reference/analytics/charts/technical-indicators/mass-index-mi.md) |
| Median Price (MP) | Midpoint of a bar's high and low | [reference](../reference/analytics/charts/technical-indicators/median-price-mp.md) |
| Momentum Indicator | Rate of change of price over n periods | [reference](../reference/analytics/charts/technical-indicators/momentum-indicator.md) |
| Money Flow Index (MFI) | Volume-weighted RSI — buying/selling pressure including volume | [reference](../reference/analytics/charts/technical-indicators/money-flow-index-mfi.md) |
| Moving Average (MA) | Rolling average of price over n periods (Simple/Exponential/Weighted/etc. variants) | [reference](../reference/analytics/charts/technical-indicators/moving-average-ma.md) |
| Moving Average Deviation | Amount/percentage price deviates from its own moving average | [reference](../reference/analytics/charts/technical-indicators/moving-average-deviation.md) |
| Moving Average Envelope (MAE) | Bands plotted a fixed percentage above/below a moving average | [reference](../reference/analytics/charts/technical-indicators/moving-average-envelope-mae.md) |
| Negative Volume Index | Cumulative index that only updates on days volume declines | [reference](../reference/analytics/charts/technical-indicators/negative-volume-index.md) |
| On Balance Volume (OBV) | Cumulative running total of volume on up periods minus volume on down periods | [reference](../reference/analytics/charts/technical-indicators/on-balance-volume-obv.md) |
| Parabolic Sar (SAR) | Trailing stop-and-reverse price points for trend-following positions | [reference](../reference/analytics/charts/technical-indicators/parabolic-sar-sar.md) |
| Performance Index | Normalized index of price performance relative to a starting point | [reference](../reference/analytics/charts/technical-indicators/performance-index.md) |
| Pivot Points | Support/resistance levels computed from the prior period's high/low/close | [reference](../reference/analytics/charts/technical-indicators/pivot-points.md) |
| Positive Volume Index | Cumulative index that only updates on days volume rises | [reference](../reference/analytics/charts/technical-indicators/positive-volume-index-pvi.md) |
| Pretty Good Oscillator | Price's deviation from its SMA, scaled by ATR | [reference](../reference/analytics/charts/technical-indicators/pretty-good-oscillator.md) |
| Price Momentum Oscillator | Double-smoothed rate-of-change oscillator | [reference](../reference/analytics/charts/technical-indicators/price-momentum-oscillator.md) |
| Price Rate of Change (PROC) | Percentage change in price over n periods | [reference](../reference/analytics/charts/technical-indicators/price-rate-of-change.md) |
| Price Volume Trend (PVT) | Cumulative volume adjusted by the percentage price change each period | [reference](../reference/analytics/charts/technical-indicators/price-volume-trend-pvt.md) |
| Prime Number Bands | Bands plotted at the nearest prime-number price levels | [reference](../reference/analytics/charts/technical-indicators/prime-number-bands.md) |
| Prime Number Oscillator | Oscillator based on price's distance from the nearest prime number | [reference](../reference/analytics/charts/technical-indicators/prime-number-oscillator.md) |
| Pring's Know Sure Thing (KST) | Momentum oscillator combining four smoothed rate-of-change curves | [reference](../reference/analytics/charts/technical-indicators/prings-know-sure-thing-kst.md) |
| Pring's Special K | Long-horizon composite of KST curves for major trend turning points | [reference](../reference/analytics/charts/technical-indicators/prings-special-k.md) |
| Psychological Line | Percentage of up periods over n periods — a sentiment gauge | [reference](../reference/analytics/charts/technical-indicators/psychological-line.md) |
| QStick | Moving average of (close − open), gauging candle sentiment over time | [reference](../reference/analytics/charts/technical-indicators/qstick.md) |
| Rainbow Moving Average | Series of successively smoothed moving averages plotted together to visualize trend strength | [reference](../reference/analytics/charts/technical-indicators/rainbow-moving-average.md) |
| Rainbow Oscillator | Oscillator derived from the spread between the Rainbow Moving Average bands | [reference](../reference/analytics/charts/technical-indicators/rainbow-oscillator.md) |
| Random Walk Index | Compares actual price range to a random-walk expectation, testing whether a trend is statistically significant | [reference](../reference/analytics/charts/technical-indicators/random-walk-index.md) |
| RAVI | Range Action Verification Index — trending vs. range-bound market from two moving averages | [reference](../reference/analytics/charts/technical-indicators/ravi.md) |
| Relative Vigor Index | Close's position within the trading range, smoothed like a stochastic | [reference](../reference/analytics/charts/technical-indicators/relative-vigor-index.md) |
| Relative Volatility | Standard-deviation-based variant of RSI, showing direction of volatility | [reference](../reference/analytics/charts/technical-indicators/relative-volatility.md) |
| RSI | Relative Strength Index — normalizes up/down closes into a 0–100 momentum oscillator | [reference](../reference/analytics/charts/technical-indicators/rsi.md) |
| Schaff Trend Cycle (STC) | Combines MACD and Stochastic logic for a faster trend-cycle signal | [reference](../reference/analytics/charts/technical-indicators/schaff-trend-cycle-stc.md) |
| Shinohara Intensity Ratio | Compares buying/selling ratios to gauge market strength | [reference](../reference/analytics/charts/technical-indicators/shinohara-intensity-ratio.md) |
| Standard Deviation | Statistical variability of price — the basis of "volatility" in many other studies | [reference](../reference/analytics/charts/technical-indicators/standard-deviation.md) |
| STARC Bands | Stoller Average Range Channel — ATR-based bands around a SMA | [reference](../reference/analytics/charts/technical-indicators/starc-bands.md) |
| Stochastic Momentum Index (STOCH) | Refined stochastic measuring close relative to the midpoint of the high-low range | [reference](../reference/analytics/charts/technical-indicators/stochastic-momentum-index-stoch.md) |
| Stochastic Oscillator (STOCH) | %K/%D lines normalizing close relative to the high-low range over n periods | [reference](../reference/analytics/charts/technical-indicators/stochastic-oscillator-stoch.md) |
| Supertrend | ATR-based trend-following overlay that flips above/below price | [reference](../reference/analytics/charts/technical-indicators/supertrend.md) |
| Swing Index (SI) | Wilder's index measuring the swing in price, accounting for gaps | [reference](../reference/analytics/charts/technical-indicators/swing-index-si.md) |
| Time Series Forecast (TSF) | Linear-regression-based forecast of the next price value | [reference](../reference/analytics/charts/technical-indicators/time-series-forecast-tsf.md) |
| Trade Volume Index (TVI) | Cumulative volume index flagging accumulation/distribution from tick direction | [reference](../reference/analytics/charts/technical-indicators/trade-volume-index-tvi.md) |
| Trend Intensity Index | Strength of the current trend from deviations off a moving average | [reference](../reference/analytics/charts/technical-indicators/trend-intensity-index.md) |
| TRIX | Triple-smoothed EMA rate of change, filtering out short-term noise | [reference](../reference/analytics/charts/technical-indicators/trix.md) |
| True Range | Greatest of high−low, high−prior close, prior close−low; the basis of ATR | [reference](../reference/analytics/charts/technical-indicators/true-range.md) |
| TT Cumulative Volume Delta (TT_CVD) | Running total of bid vs. ask transaction volume (buying vs. selling pressure) | [reference](../reference/analytics/charts/technical-indicators/tt-cumulative-volume-delta-tt_cvd.md) |
| Twiggs Money Flow | Volume-weighted accumulation/distribution measure, similar to Chaikin Money Flow with added smoothing | [reference](../reference/analytics/charts/technical-indicators/twiggs-money-flow.md) |
| Typical Price | Average of a bar's high, low, and close | [reference](../reference/analytics/charts/technical-indicators/typical-price.md) |
| Ulcer Index | Depth and duration of price drawdowns — a downside-volatility measure | [reference](../reference/analytics/charts/technical-indicators/ulcer-index.md) |
| Ultimate Oscillator (ULTOSC) | Combines three timeframes of buying pressure to reduce false divergence signals | [reference](../reference/analytics/charts/technical-indicators/ultimate-oscillator-ultosc.md) |
| Valuation Lines | Horizontal reference lines marking a session's value area | [reference](../reference/analytics/charts/technical-indicators/valuation-lines.md) |
| Vertical Horizontal Filter | Trend strength independent of trend direction | [reference](../reference/analytics/charts/technical-indicators/vertical-horizontal-filter.md) |
| Volume | Total traded volume per bar, color-coded by up/down close | [reference](../reference/analytics/charts/technical-indicators/volume.md) |
| Volume At Price (VAP) | Histogram of volume traded at each price level | [reference](../reference/analytics/charts/technical-indicators/volume-at-price-vap.md) |
| Volume Delta | Net difference between buy-side and sell-side volume for a period | [reference](../reference/analytics/charts/technical-indicators/volume-delta.md) |
| Volume on the Ask (AVol) | Volume traded at the ask price | [reference](../reference/analytics/charts/technical-indicators/volume-on-the-ask-avol.md) |
| Volume on the Bid (BVol) | Volume traded at the bid price | [reference](../reference/analytics/charts/technical-indicators/volume-on-the-bid-bvol.md) |
| Volume Oscillator | Difference between two volume moving averages | [reference](../reference/analytics/charts/technical-indicators/volume-oscillator.md) |
| Volume Rate of Change | Percentage change in volume over n periods | [reference](../reference/analytics/charts/technical-indicators/volume-rate-of-change.md) |
| Volume Underlay | Displays volume as a shaded region behind the price chart | [reference](../reference/analytics/charts/technical-indicators/volume-underlay.md) |
| Vortex Indicator | Identifies trend direction/reversals from positive vs. negative directional movement | [reference](../reference/analytics/charts/technical-indicators/vortex-indicator.md) |
| VWAP | Volume-weighted average price for the session, with optional standard-deviation bands | [reference](../reference/analytics/charts/technical-indicators/vwap.md) |
| Weighted Close | (High + Low + 2×Close) / 4 — a close-weighted average price | [reference](../reference/analytics/charts/technical-indicators/weighted-close.md) |
| Williams % R (WillR) | Inverted stochastic — close's position within the high-low range over n periods | [reference](../reference/analytics/charts/technical-indicators/williams-r-willr.md) |
| ZigZag | Filters minor price noise to show only reversals beyond a defined percentage threshold | [reference](../reference/analytics/charts/technical-indicators/zigzag.md) |

## Trader Analytics

Trader Analytics is a separate widget (not the Chart) for post-trade performance review: pick a time interval,
account(s), and instrument(s), then calculate a statistics report (Closed P/L, win/loss counts and averages, Profit
Index, hold times, time-between-trades, etc.), broken out by Total / Long / Short — see
[Trader Analytics Overview](../reference/analytics/trader-analytics/description-trader-analytics/trader-analytics-overview.md),
[Trader Analytics Display](../reference/analytics/trader-analytics/description-trader-analytics/trader-analytics-display.md),
[Trader Analytics Reference](../reference/analytics/trader-analytics/reference-trader-analytics/trader-analytics-reference.md)
(full row/column definitions), and
[Calculating trader performance statistics](../reference/analytics/trader-analytics/task-trader-analytics/calculating-trader-performance-statistics.md).
