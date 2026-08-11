---
title: Displaying positions by group
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/positions/task-positions/displaying-positions-by-group/
---

# Displaying positions by group

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/positions/task-positions/displaying-positions-by-group/)
>
> **Interpreted in:** [Order Management & Risk § Position tracking (Positions, Position Manager)](../../../../guides/order-management-and-risk.md#position-tracking-positions-position-manager)

You can configure the Positions widget to display your open positions and P/L by risk group, account, exchange, product, or contract by using the **Grouping** option in the context menu or the local **Settings: Positions** menu. The widget is in “aggregate” view mode by default.

To group positions, right-click in the widget and select **Grouping…**. For example, we can group our positions by account.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ghf-positions-group-by.png)

When grouping positions, you can also select **Top-level summary row** to display a summary at the top of the widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-summary1.png)

The summary row shows your overall position based on your grouping.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-summary2.png)

**Note**: When grouping by account, parent account positions also include their child account positions, so only the parent account net position is added to the total in the summary row.

To change the grouping, click an option in the **Grouping…** menu (e.g., **Exchange**).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ghf-positions-group-by-exchange.png)

By clicking **Grouping…** | **None**, you can disable grouping to display the positions in a flattened form as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-flattened.png)

## Displaying positions by risk group

Risk groups allow your administrator to set risk limits for managed users or accounts from different companies in TT. When displaying positions by risk group, the **P/L**, **Margin**, and credit balance columns (e.g., **Balance**) are calculated independently of the accounts assigned to the group.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-risk-group.png)

## Displaying OTC trade positions

The Positions widget displays OTC trade positions when enabling a global checkbox Preference on the Positions page labeled “Display OTC trade positions”. The preference defaults to OFF (unchecked). When enabled, the positions from OTC trades will be displayed the same as all other positions. For example, if the account position is 100 from non-OTC trades, and a 1,000 lot Block trade is executed in the same account, the position will display as 1,100 with no designation of the non-OTC portion from the OTC portion.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-display-otc-positions.png)

[Next PostDisplaying positions by product group](displaying-positions-by-product-group.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ghf-positions-group-by.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-summary1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-summary2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ghf-positions-group-by-exchange.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-flattened.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-risk-group.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/positions-display-otc-positions.png
