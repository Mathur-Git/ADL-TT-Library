---
title: Time & Sales reference
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference/
---

# Time & Sales reference

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference/)

## Available settings

These settings affect only the selected Time & Sales widget. To update the default settings with these value for newly-opened Time & Sales widgets, or to apply them to existing opened widgets, click **Defaults**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-settings.png)

* **Grid font size**: Adjust the font size to suit your preferences and use bold text, if desired.
* **Colors**: Allows you to [customize or change the cell and column colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md#colors) available in the widget.
* **Highlight quantities >=**: Highlight the row when a transaction quantity equals or exceeds this value.
* **Show milliseconds**: Check to show millisecond accuracy in the Time column. When checked, you have the option to set **Show microseconds** to display microseconds in the Time column.
* **Launch floating order entry on left click on price or quantity.**: Check to open the [default floating order entry widget](../../../overview/preferences/description-preferences/orders-preferences.md) when a user clicks on a price or quantity.
* **Accumulate trades by time (1 sec)**: Check to accumulate individual traded quantities at the same price level and buy/sell direction into an total traded quantity within the past 1 second interval. Uncheck to display all individual trades as they occur.
  * **Accumulate instruments individually** — Consolidates trades per instrument within the one (1) second aggregation time window. When enabled, a trade occurring in a different instrument within the time
    frame does not end the aggregation of the current instrument and each instrument aggregates
    separately. Can only be enabled when **Accumulate trades by time (1 sec)** is enabled. This setting is
    disabled by default.
  * **Highlight aggregated quantity cells** — Highlights quantities that consist of multiple trades consolidated within the one second accumulation time frame. Disabled by default.
* **Historical Data**: Check to include or exclude historical data.
  **Note**: For options and strategies products, only new Time & Sales prints are populated going forward once the widget is open.
* **SetTime and Sales columns**: Select the [columns](#ts-col-desc) you want shown in Time & Sales.

### Time & Sales column descriptions

| Column | Description |
| --- | --- |
| Date | Date the event took place, based on the current date set on the local workstation. |
| Time | Time the event took place, based on the current time set on the local workstation. |
| Contract | Name of the contract. |
| OptionStyle | * **American** — may be exercised on *any* business day until the expiration date. * **European** — may be exercised *only* on the expiration date. * **Asian** — may be exercised at the average price instead of the spot price. * **One Time** — is exercised *automatically* at a single reference price on the last trading day. |
| Price | Buy/Sell price of the product. |
| Product | Name of the product being traded. |
| Quantity | Quantity of the product that was bought/sold. |
| Term | Shows the contract month for a strategy. If all contracts in a strategy are in the same month, that month is listed in the Term column. If not, then just the front month of the strategy is listed. |
| Type | Order type (i.e., Vole, Block, Basis). A unique identifier for OTC trade types is displayed to help differentiate between the different OTC order types. |

### Trade Sounds

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-trade-sounds.png)

The **Trade Sounds** section allows you to play sounds for trades that meet or exceed a
user-defined range of quantities. To enable this functionality, check the **Enable trade sounds** checkbox.

When checked, the **Add Rule** button is displayed. Click this button to add one or more rules for which sound to play for trades that meet or exceed the range of trade quantities. Double-click a cell in the following columns to add or select a value for each rule:

* **Trade Qty Min** — Enter the minimum trade quantity.
* **Trade Qty Max** — Enter the maximum trade quantity. When a trade meets or exceeds this range, the selected sound is played.
* **Side** — Select which side of the trade to apply the sound. The table row will be shaded blue for “Buy” or red for “Sell” based on which side is selected. If the cell is blank, the sound plays for both sides of the trade.
* **Sound** — Select which sound to play when the trade quantity meets or exceeds your trade quantity range.

The following controls are available for each rule:

* **Use** — Check this checkbox in each row to activate a rule.
* **Play** — Click to preview the selected sound.
* **Del** — Click the “x” to remove a rule.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-trade-sounds.png
