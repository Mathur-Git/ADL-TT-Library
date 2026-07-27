---
title: Subscribing to Products in the Market Grid
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/task-market-grid/subscribing-to-products-in-the-market-grid/
---

# Subscribing to Products in the Market Grid

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/task-market-grid/subscribing-to-products-in-the-market-grid/)

You can create a tab that includes all available instruments for a specific product. This method allows the expired
contracts to automatically roll into the next contract and will automatically add new instruments to the tab as they
come available.

## Creating a Product Subscription

To subscribe to a product:

1. [Add a
   new tab](using-tabs-in-the-market-grid.md#add-tabs) to the
   Market Grid using the **From a Product** selector. Enter the product name and click the
   **OK** button.

All available instruments for the product appear in the tab.

2. The market grid displays all instrument names in ***italics***.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-italic-instr-1.png)

The italicized contract name means that the market grid has an active product subscription. The market grid will
automatically roll expired contracts into the next available contract and add new contracts as they become
available.

**Warning:** Deleting a row with italics cancels the product subscription for all instruments in the tab.

The remaining instruments appear without italics revert to the regular behavior as if each row was [added
individually](adding-instruments-to-the-market-grid.md).

## Showing and Hiding Rows

The Market Grid allows two ways to hide instrument rows within a tab:

* **Using the Contract Filter** This method preserves the product subscription behavior while also
  allowing you to clear
  the tab of instruments you do not want to view.
* **Using the Remove option in the right-click context menu** This method completely removes the
  instrument from the
  tab. However, removing one or more rows from a group of instruments added as a product subscription will
  lose the
  benefits of subscribing at the product level.

**Note:**
TT strongly recommends using the contract filter to hide rows in the Market Grid.

To filter contracts:

1. Simply hover over the **Contract** column header and select the down caret to open the list of all
   currently
   subscribed instruments.

![alt](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-filter-contracts.png)

2. Use the check boxes to select only the contracts you want to view.

![alt](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-select-filtered-contracts.png)

3. The **Contract** column header now appears in yellow, showing that rows are currently hidden from
   view. The contracts
   names continue to appear in italics showing that the product subscription remains active.

![alt](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-filtered-rows.png)

4. To remove the filter and show all of the instruments, click the filter icon in the **Contract**
   header, then click
   **Clear Filter**.
   ![Clear Filters](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-clear-contract-filter.png)

By using the filter feature, you can be sure that any configured product subscriptions will remain active.

←[Previous PostUsing Tabs in the Market Grid](using-tabs-in-the-market-grid.md)

[Next PostConfiguring the Market Grid display](configuring-the-market-grid-display.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-italic-instr-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-filter-contracts.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-select-filtered-contracts.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-filtered-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-clear-contract-filter.png
