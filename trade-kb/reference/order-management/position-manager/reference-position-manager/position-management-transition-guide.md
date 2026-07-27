---
title: Position Management Transition Guide
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/position-manager/reference-position-manager/position-management-transition-guide/
---

# Position Management Transition Guide

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/position-manager/reference-position-manager/position-management-transition-guide/)

This guide directs you to the Trade widgets that deliver the same position management functionality and data that is available in Monitor.

## Positions

The position management functionality available within the **Positions** tab of Monitor is available in the [Positions](../../positions/description-positions/positions-overview.md) widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-positions.png)

Using the Position widget, you can:

* [Group open positions and P/L](../../positions/task-positions/displaying-positions-by-group.md).
* [Customize the data displayed](../../../overview/widgets/task-widgets/organizing-the-widgets-menu.md#choosing-columns) by choosing which columns you want to see and arranging the order in which the columns appear. The following [Positions widget columns](../../../basic-order-entry/trading-crypto-on-tt/reference-trading-crypto-on-tt/crypto-reference.md) were also displayed in Monitor:
  * WrkBuy
  * WrkSell
  * BalanceUsed %
  * BalanceType
  * Margin
  * SOD Price
  * SOD PriceType
  * AutoLiq %
  * CurrLiq %
  * BalToLiq
  * P/L
  * P/L Open
  * P/L Realized
  * P/L Price
  * P/L PriceType

Similar to the Account List in Monitor, you can click the **Account** column in the Positions widget to search for and select an account.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-search.png)

Using the Positions widget, you can also export data to a comma-separated values (CSV) file for all rows or selected rows in the Positions widget. Use Shift-click to select multiple rows. You can export either a grouped or flat view of positions in the widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-export.png)

## Order Book

The **Orders** tab in Monitor provides you the ability to view or cancel working orders, as well as cancel stale orders. Trade provides these capabilities and more using the [Order Book](../../order-book/description-order-book/order-book-overview.md) widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-order-book.png)

Using the Order Book widget, you can:

* Apply [filters](../../order-book/reference-order-book/order-book-reference.md#ob-reference-filter-columns) and sort your order book columns by account, contract, exchange and more.
* [Customize the data displayed](../../../overview/widgets/task-widgets/organizing-the-widgets-menu.md#choosing-columns) by choosing which columns you want to see and arranging the order in which the columns appear.

## Deleting an order using Force Cancel

If you have administrator permissions in your firm, you can use the Force Cancel functionality to delete an order from the Order Book. Force Cancel sends a cancel message to the exchange and then removes the order from the TT system without waiting for an exchange acknowledgment. Force Cancel is typically used for removing stale orders no longer working at the exchange.

**Tip**: You can use Force Cancel instead of Monitor to remove stale orders from a user’s Order Book.

To delete an order using Force Cancel:

1. Select one or more orders in the Order Book.
2. Right-click and select **Force Cancel** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-force-cancel-orders-1.png)
3. Confirm that you want to force cancel the selected order and click **Cancel Orders** in the dialog box.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-force-cancel-confirm-1.png)

## Position Manager

With the addition of the [Position Manager](../description-position-manager/position-manager-overview.md) widget, you have access to the manual fills and start-of-day (SOD) records capabilities available in Monitor from within TT’s fully customizable workspace.

### Manual Fills

Using Position Manager, you can create manual fills using essentially the same manual fills
functionality as Monitor.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-manual-fills.png)

To create a manual fill:

1. In the workspace menu bar, click **Widgets** | **Miscellaneous** | **Position Manager**.

   **Tip**: You can also open Positions Manager by clicking **Create Manual Fill** from the context menu when selecting a row in the Positions widget.
2. Select [Admin Fills](../description-position-manager/position-manager-overview.md#admin) or [Local Fills](../description-position-manager/position-manager-overview.md#local) as the manual fill mode and click **+ Add Row**.
3. Enable the following optional settings as needed:
   * **Price off tick** — If checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.

     **Note**: Off-tick prices can be entered for instruments that tick in fractions (displayed with an apostrophe). For example: ZB Jun25 with a price of 116’26.

     Enable the ‘Price off tick’ checkbox to switch the price input control to accept decimal prices (such as 115.12345678) and create the fill with up to eight (8) digits of decimal precision.
   * **Create leg fills** — If checked, this setting auto-creates leg fills in addition to the spread fill when creating a manual fill on an exchange-listed spread contract.
4. In the manual fill row, click a cell in each of the following columns to enter or select a value:
   * **Contract** — Select a contract by using the product search or market explorer. The settlement price for the selected contract appears in the **Price** column.
   * **Account** — Select an account for the manual fill. All accounts available to you are displayed. An account is required for a manual fill.
   * **User** — Optionally, select a user for the manual fill. Only users assigned to the account are displayed in the dropdown menu.
   * **Side** — Select which side of the trade to apply the manual fill. Click “B” for Buy or “S” for Sell.
   * **Quantity** — Enter a quantity for the manual fill.
   * **Price** — Enter a price for the manual fill or use the default settlement price for the selected contract.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-add-1-1.png)

   Before the manual fill is published, the **Status** column displays as “Staged”. To delete a manual fill before it’s published, click the “x” in the manual fill row.
5. To create additional manual fills, click **+ Add Row** and repeat the previous Step.
6. Review each manual fill and click **Publish**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-add-2-1.png)

   The position in the account is modified in the Positions widget, and the fill appears in the Fills widget for each user sharing the account.

   **Tip**: To quickly offset a manual fill, right-click the published fill in Position Manager and select **Clone selected rows**. In the new row that appears, click the **B/S** button to flip the side and click
   **Publish**.

### Start-of-Day records

You can also create and modify SODs using the Position Manager widget, which includes basically the same SOD functionality as Monitor.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-sod.png)

To create an SOD:

1. In the workspace menu bar, click **Widgets** | **Miscellaneous** | **Position Manager**.

   The Position Manager widget opens.
2. Select the **Admin SOD** tab.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-1-1.png)
3. Click **+ Add Row** to create a new SOD record.

   A new SOD row is displayed and highlighted yellow in the Position Manager.
4. Enable the following optional setting as needed:

   **Price off tick** — If checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.

   **Note**: Off-tick prices cannot be entered for instruments that tick in fractions (displayed with an apostrophe). For example: ZB Sep18 with a price of 145’23.
5. In the SOD row, click each cell in the following columns to add or select a value:
   * **Contract** — Use the product search or market explorer to find and select a contract. The settlement price for the selected contract appears in the **Price** column.
**Account** — Select an account for the manual fill.

**Note:** An account is required to manually add an SOD record.

6. **SOD** — Add an SOD position. Positive values represent a long position, and negative values represent a short position.
7. **Use Settle** — Select whether to use the current settlement price for the contract.
8. **Price** — Enter a price for the SOD or use the default settlement price for the selected contract.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-2-1.png)

Before the SOD is published, the **Status** column displays a status of “Staged”.

9. To create additional SOD records, click **+ Add Row** and repeat the previous Step.
10. Review the SOD record and click **Publish**.

    The new SOD position is displayed in the Positions widget.

    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-3-pos-1.png)

### Modifying an SOD

A Start of Day (SOD) record for an account can be modified manually on a per contract basis.

To modify an SOD:

1. In the SOD row, click the following fields to modify as needed:
   * **SOD** — Modify the SOD position.
   * **Use Settle** — Select whether to use the current settlement price for the contract.
   * **Price** — Enter a price for the SOD or use the default settlement price for the selected contract.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-modify-3-1.png)

   **Note**: You can also open Positions Manager by clicking
   **Modify SOD** from the context menu when selecting a contract in the
   Positions widget.

   **Tip**: Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-icon-reset-1.png) to clear the modifications without saving as needed.
2. Review the SOD record and click **Publish**.

   The new SOD position is displayed in the Positions widget.

## Audit Trail

The Audit Trail widget provides more filtering options than Monitor. The “forever” [Audit Trail](../../audit-trail/description-audit-trail/audit-trail-overview.md) in Trade gives you the ability to [filter data by message and execution report types](../../audit-trail/task-audit-trail/filtering-the-contents-of-the-audit-trail.md), as well as [view historical data](../../audit-trail/task-audit-trail/viewing-historical-data.md) for the account used for trading.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-audit-trail.png)

←[Previous PostPosition Manager reference](position-manager-reference.md)

[Next PostCSV file format for uploading fills](csv-file-format-for-uploading-fills.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-positions.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-search.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-export.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-order-book.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-force-cancel-orders-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-force-cancel-confirm-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-manual-fills.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-add-1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-add-2-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-sod.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-2-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-3-pos-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-modify-3-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-icon-reset-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-transition-audit-trail.png
