---
title: Time & Sales Data
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data/
---

# Time & Sales Data

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data/)

The Time & Sales widget keeps a running record of trades for selected instruments displayed in reverse
chronological order. The widget will automatically remove contracts after they expire.

Users can access historical Time & Sales data by scrolling to the bottom of the widget screen. The Time &
Sales widget on TT maintains and displays a history of trade data from all of your sessions and not just for the
current session.

* Each new entry is added to the top of the list, causing the widget screen to auto-scroll downward.
* If you manually scroll through the list to review older data, auto-scroll turns off.
* A red line at the top of the widget screen indicates you can scroll up to view additional information.
* To return to auto-scrolling, scroll to the top of the widget screen.

The **Price** and **Qty** column filters give you the ability to display only trades with
prices or quantities that meet minimum and/or maximum values. For example, you can configure Time & Sales to show
only
ES contract trades with prices between 3900.00 and 3901.50.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-price-filter.png)

**Note**: Filter the widget by “Contract” before applying a filter to the **Price** column.

If you are viewing market data at the product level in Time & Sales, new instruments added by the
exchange for that product will automatically appear in the widget. For example, if you are viewing market
data for ES strategies at CME, user-defined strategies newly created and traded at the exchange for this product
will
automatically appear in Time & Sales.

## Time & Sales quantity filtering

The **Qty** column in the Time & Sales widget supports four levels of quantity filtering.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-filter-quantity1.png)

Filtering levels include:

1. **Global** — Applies the **Qty Filter** to both live *and* historical data
   for all products selected within the widget.
2. **Product** — Applies to live updates per *product*.
3. **Type** — Applies to live updates per *product type*.
4. **Instrument** — Applies to live updates per *instrument.*

Product level filters can be expanded to view available instruments. The filters are collapsed by default to easily
find the products added to the widget.

**Note**: A more specific filter will override a more general filter if both have values set. An instrument level
filter is the most specific.

Click each field to add or modify a minimum and maximum value as needed. To remove a value, click the “X” next to the
field.

## Time & Sales consolidated quantities

By enabling the **Highlight aggregated quantity cells** option in the Time & Sales settings, you can identify
quantities that consist of multiple trades consolidated within the one second accumulation time frame. The highlight
color can be customized using the **Colors** settings in the widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-hover.png)

Also when accumulating trades within the one second time frame, you can mouse hover on a consolidated quantity cell
to display a pop-up list of each individual trade quantity. The list shows up to 20 of the most recent trades that
comprise the aggregated quantity.

←[Previous PostTime & Sales Overview](time-sales-overview.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-price-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-filter-quantity1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ts-hover.png
