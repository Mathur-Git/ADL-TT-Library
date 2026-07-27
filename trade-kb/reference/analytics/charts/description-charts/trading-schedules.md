---
title: Trading Schedules
category: Analytics
source: https://library.tradingtechnologies.com/trade/analytics/charts/description-charts/trading-schedules/
---

# Trading Schedules

> Category: **Analytics** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/analytics/charts/description-charts/trading-schedules/)

The Trading Schedules widget gives you the ability to view and modify trading schedules on a per product basis.
Trading and clearing session times are set per product by the exchange, and traders can view the trading hours of
each instrument in the Trading Schedule widget.

The widget also gives you the ability to create, copy, and save product level custom trading schedules. You can apply
the exchange’s schedules or your own custom schedule to a product in an open Chart widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules.png)




To open Trading Schedules, click **Edit** | **Trading Schedules** in the workspace menu bar.

## Trading Schedules Display

The following image shows the basic components of the Trading Schedule widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-display.png)

The widget includes:

1. **Custom schedules pane** — Shows the list of saved custom schedules. Use the search box to quickly
   find a schedule. Saved schedules are also listed in the Chart widget when [applying a trading
   schedule](#apply) to an instrument.
2. **Schedule and Product Mappings tabs** — The **Schedule** tab shows the default exchange schedule
   and allows you to modify time ranges, sessions active, and days active. The **Product Mapping** tab allows
   you to apply the same custom schedule to additional products.
3. **Schedule name** — The name of the selected exchange product schedule or custom schedule.
4. **Timezone** — Shows the timezone for the exchange sessions. The “Days active indicators” and “Time
   Range” columns in the widget reflect the selected timezone.
5. **Trading Schedule columns** — The following columns are shown:
   * **checkboxes**: Indicate if historical data for the session is displayed in the Chart widget. When a
     checkbox is checked, the session is “active” and data is displayed. Click the checkbox to add/remove
     trading session data from the Chart widget. At least one session must be active.
   * **Color**: The color shown for the session in the “Days active indicator” at the bottom of the
     widget.
   * **Name**: The name of the exchange session or event.
   * **Time Range**: The trading hours for the session. The minus sign “-” next to the time (e.g.,
     -15:00:00) indicates that the trading session began the previous day.
   * **Days of the Week**: Indicates which days are reflected in the Chart widget and the “Days active
     indicator” for each trading session.
6. **Days active indicator** — Shows a visual display of the days and times a session was active. Each
   time range for the session is color-coded as indicated by the “Color” column. The “Days active indicator”
   changes based on which exchange sessions are marked “active” and which timezone is selected.
7. **Delete Schedule** — Deletes the selected custom schedule.
8. **Add Time Range** — Adds a custom time range to the schedule. The button is available when modifying a
   schedule (e.g., when you click “Edit Schedule” in the lower right corner.)
9. **Edit Schedule**/**Save to Custom Schedules**/**Cancel** — The “Edit Schedule” button allows you
   to edit a saved custom schedule selected in the schedules pane. The “Save to Custom Schedules” is displayed when
   a new instrument is added to the widget or when a saved custom schedule has been modified. The “Cancel” button
   deletes changes without saving.

## Creating and modifying a custom trading schedule

To create a custom trading schedule:

1. Click **Edit | Trading Schedules** in the workspace menu bar to open the widget.
2. Click the search icon in the widget to find and select an instrument.

   The exchange trading schedule is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step1.png)

   **Note**: The “default” exchange trading schedule can also be saved in the widget.
3. Customize the time range, sessions, and name for the schedule as needed and click **Save to Custom
   Schedules**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step2.png)

   The schedule appears in the custom schedules pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step3.png)

To modify a custom trading schedule, select a schedule in the custom schedules pane and click **Edit Schedule**.
After modifying the schedule, click **Save to Custom Schedules**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-edit.png)

## Trading Schedules Product Mapping

The **Product Mappings** tab gives you the ability to apply your custom schedule to other products. When you open
a Chart for a product that is mapped to a custom schedule, the Chart shows trading data based on the custom schedule
by default instead of the exchange schedule for that product.

To map products to a custom schedule, click the **Product Mappings** tab and click the “+” button to search for
and select a product. After adding the product(s), click the **Save** button.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-map.png)

To remove a product mapping, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-delete-icon.png) next to the mapping and
click “Save”. When the product mapping is deleted, the Chart automatically shows the trading data for the product
based on the exchange schedule.

**Note**: Autospreader instruments cannot be mapped as a product to a custom schedule. A [custom
schedule can be applied](#apply) to an Autospreader instrument when it’s displayed in an open Chart widget.

## Applying exchange and custom schedules

To apply an exchange or custom schedule to an instrument, [open the
menu](chart-overview.md#chart-menu) in the Chart widget and click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-schedules-1.png) to select the schedule.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-apply.png)



In the Chart, schedules can be applied to all exchange-traded instruments as well as synthetic Autospreader and
Aggregator instruments. When you apply an exchange schedule or custom schedule to an instrument in the Chart widget,
the chart shows the historical trading data for the instrument based on the sessions and days active in the
schedule.

To reapply the default exchange or custom schedule for the product, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-schedules-2.png) and
select “Default”.

**Note**: Custom schedules do not apply to continuation charts.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-apply-default.png)

←[Previous PostChart trading](chart-trading.md)

[Next PostTechnical Indicators](technical-indicators.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-add-step3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-map.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-delete-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-schedules-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-apply.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-schedules-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/chrt-trading-schedules-apply-default.png
