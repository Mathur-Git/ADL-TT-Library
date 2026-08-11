---
title: Introduction to Autospreader
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/introduction-to-autospreader/
---

# Introduction to Autospreader

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/description-autospreader/introduction-to-autospreader/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § What AutoSpreader is](../../../../guides/spread-trading-autospreader.md#what-autospreader-is)

Use Autospreader® to create and trade your own synthetic calendar, inter-product, or inter-exchange spreads. You can define the legs of the spread, then preview the implied market for the spread based on the outright legs. When entering orders in the implied market, Autospreader works the legs to achieve the spread setting parameters.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-overview.png)

The Autospreader widget can be opened by:

* Clicking **Autospreader** in the widgets menu.
* Selecting a synthetic spread in the Explorer.

### How Autospreader Works

Autospreader constructs a synthetic spread market using settings established during the spread creation process. Synthetic spread orders are executed on the Autospreader Server, which is colocated with the exchange matching engine.

When you submit a synthetic spread order, Autospreader submits a quoting order in the designated quoting leg or legs based on the current bid or ask in the hedge leg and the available liquidity. Autospreader calculates a price level at which to place the quoting order where adequate liquidity is available to fill the order at the desired spread price. As the best bid or ask changes in the hedge leg, Autospreader automatically replaces the quote order.

### Autospreader widget functionality

When you open the **Autospreader** widget from the **Widgets** menu, it displays the list of spreads you’ve created and those that have been shared with you. You can launch, create, edit, and manage (copy, share, delete) all of your spreads from this widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-intro.png)

The Autospreader widget provides the following functions:

* **Create** — Opens an Autospreader configuration interface for creating a new spread.
* **Launch** — Launches a spread in your workspace using one of the selected options.
* **Edit (icon)** — Opens an Autospreader configuration interface for modifying an existing spread
* **Copy** — Allows you to select and copy an existing spread. The spread can then be modified and renamed as needed.
* **Delete** — Allows you to select and delete a spread.
* **Share** — Shares selected spread configurations with users in your company.
* **Filter list** — Allows you to enter a spread name, status, owner, or date and filter the list of spreads.

[Next PostAutospreader Configuration Interface](autospreader-configuration-interface.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-overview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-intro.png
