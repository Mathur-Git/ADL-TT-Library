---
title: General Preferences
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/general-preferences/
---

# General Preferences

> Category: **Overview** · [Source](https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/general-preferences/)
>
> **Interpreted in:** [Platform & Workspace § Preferences](../../../../guides/platform-and-workspace.md#preferences)

![General preferences](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-general.png)

### Display

Click each preference in the **Display** section to see a list of options.

| Preference | Description |
| --- | --- |
| Color Theme | Sets the color theme for each widget you open in your workspaces. |
| Language | Sets the language for your workspaces. |
| Background | Sets the background theme and color for your workspaces. |
| Context help | Enables tooltips for widgets. Select one of the following options:  * None — Do not show tooltips. * Simple — Display tooltips as short descriptions of a widget, where available. |
| Product Symbology | Determines which type of product symbol to display in your workspace. Select one of the following:   * **Exchange** — Sets your workspace to show only the exchange symbol for products (e.g., “CL” for CME Crude Oil Futures products). * **Exchange (Bloomberg)** — Sets the exchange symbol as primary. Products are displayed with the exchange symbol first and the Bloomberg symbol in parentheses (e.g., “CL (CL1)” for CME Crude Oil Futures products). * **Bloomberg (Exchange)** — Sets the Bloomberg symbol as primary. Products are displayed with the Bloomberg symbol first and the exchange symbol in parentheses (e.g., “C01 (BRN)” for ICE Brent Crude Futures products).   **Note:**   * To use this setting, Bloomberg symbology must be enabled for your company by TT. Contact your Customer Success Manager to enable this functionality. * You must reload your workspace for this setting to take effect. |
| Display Spread/Strategy legs instead of Alias | Sets whether to display the commonly used alias name, or to display all legs of the instrument, including expiries, strikes, and quantities of individual legs. |
| Show titlebar clock | Sets whether to show the clock in the workspace menu bar. |
| Show scrollbars on workspaces | Shows/hides workspace window scroll bars. When this preference is checked (enabled), scroll bars are visible within the workspace. When this preference is unchecked (disabled), scroll bars are not visible and widgets will automatically move to remain visible within the workspace if you resize the workspace window to make it smaller. This preference is checked by default and scroll bars are visible. |
| Support high resolution displays | Sets whether to improve text display in grid-based widgets for very high-resolution monitors or displays, such as a MacBook Retina display. Note that the preference has no affect on other types of displays. |

### Prices and Quantities

| Preference | Description |
| --- | --- |
| Display spread/strategy positions | Sets whether to display positions in exchange-listed spreads in addition to the positions of the spread legs. **Note:** To display the spread position as a spread SOD, the **Create SOD records for Spread/Strategy Positions** preference on your account must be enabled in the Setup application. |
| Show implied prices or quantities in pre-open | Sets whether to display implied prices and quantities when a contract is in a pre-open state. |
| Show decimal prices for fractional prices/ticks | Shows prices as decimals for instruments with fractional ticking and apostrophe price display. **Note:** If you change this setting, you must reload the workspace to see the changed display. |
| Increase/decrease prices and quantities with right/left mouse clicks | Sets whether the price and quantity controls adjust their values when left/right clicking your mouse buttons in the edit box.   This feature defaults to **checked** meaning that the price and quantity values decrease when left-clicked and increase when right-clicked. |
| Average price rounding | Sets the rounding precision when displaying average fill prices. Select one of the following:  * **Nearest Tick** to round to the nearest tick * **Decimal places** to display the selected number (1-8) of decimals |
| Crypto quantity display decimal places | Sets the preferred number of decimal digits to show for fractional quantities. You can set 0-8 decimal digits to display. If additional quantity is available, a “+” is shown to indicate the additional digits. |
| Quantity display thousands separator | Displays a comma or period thousands separator within large numeric quantity values. This setting does not apply to price values. |
| RFQ Quantity | Sets the default seeded quantity that appears when using the **Submit RFQ Quantity** context menu option. You can set a different value when using this functionality in the widget.   **Note:** This only affects widgets that support **Submit with RFQ** functionality. |
| Market depth level | Defines the number of depth levels that workspace widgets will subscribe to. Select one of the following:  * **5** * **10** * **15** * **20** * **<Default>** — The value set in the TT Product Database for each instrument. |

### Energy Quantities

| Preference | Description |
| --- | --- |
| Contracts | Represents trading quantities for energy products as the entire delivery amount. |
| Flow | Represents trading quantities for energy products as the amount to be delivered in each delivery period. |

### Data Caching

| Preference | Description |
| --- | --- |
| Cache instrument data locally | Sets whether to cache the instrument information downloaded when starting the Trade application. The setting is enabled by default to reduce bandwidth and improve performance, as most instrument definitions do not change frequently.  **Note:** You can update an instrument definition manually, if needed, from the [MD Trader](../../../basic-order-entry/md-trader/reference-md-trader/md-trader-reference.md) or [Spread Matrix](../../../order-management/fills/reference-fills/fills-reference.md) context menus. |

←[Previous PostPreferences Overview](preferences-overview.md)

[Next PostAccounts Preferences](accounts-preferences.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-general.png
