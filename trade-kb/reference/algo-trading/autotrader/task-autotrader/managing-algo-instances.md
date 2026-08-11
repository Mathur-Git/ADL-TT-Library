---
title: Managing algo instances
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/managing-algo-instances/
---

# Managing algo instances

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/managing-algo-instances/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Algo Dashboard vs Autotrader](../../../../guides/algo-ops.md#algo-dashboard-vs-autotrader) · [Algo Ops: Dashboard, Autotrader & Excel § Monitoring a running algo](../../../../guides/algo-ops.md#monitoring-a-running-algo)

Autotrader lets you manage algo instances individually or in groups. You can:

* Pause and stop algos
* Pin and unpin algo instances
* Create new tabs for currently running algos

## Pausing and stopping algos

Autotrader lets you pause and stop running algos.

* Pause: suspends the algo’s execution and then deletes all child orders with “Leave Order On Pause” = False.
* Stop: cancels the algo and deletes all child orders with “Leave Order On Cancel” = False.

**Note**: You can also pause and stop algos using the [inline action buttons](#inline).

To pause algos:

1. Select the algo or algos you want to pause.
2. Click the pause icon to pause the selected algos.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pause-algo.png)

You can also select **Pause All** from the **Pause** drop-down to pause all running algos. You can also show a **Pause All** control button by [customizing the control button visibiity](#control-buttons) from the context menu.

To stop algos:

1. Select the algo or algos you want to pause.
2. Click the Stop icon to pause the selected algos.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-stop-algo.png)

   The selected algos are stopped and their statuses are reset to Staging.

You can also select **Stop All** from the **Stop** drop-down to stop all running algos. If you stop an unpinned algo, the algo instance is also deleted.

To pause or stop algos using the inline action buttons:

1. Right-click a column heading and select **Edit Columns…**.
2. Enable the **Run** and **Stop** columns and click **OK**.
3. Click the toggle button in the **Run** column to pause and run the algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pause-inline.png)
4. Click the button in the **Stop** column to cancel the algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-stop-inline.png)

## Pinning and unpinning rows

Autotrader lets you pin rows to the widget so they remain in the view after the algos complete.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-rows-intro.png)

The following is displayed when pinning and unpinning rows:

1. Pinned rows
2. Unpinned rows
3. Dividing line

Note the following effects of pinning and unpinning rows:

* All instances are pinned by default.
* Staging algo instances cannot be unpinned.
* Unpinning an algo moves it below the dividing line.
* All running algos can be modified, whether pinned or not.
* Stopping a pinned running algo stops the algo and puts it in staging state.
* Stopping an unpinned algo stops the algo and deletes the instance/row.
* If a workspace is saved, algo tabs and all their instances are saved in their respective states. So pinned algos in any status are shown above the line and unpinned running or paused algos are listed below the line.

To unpin a row, select the pinned algo instance row or rows you want to unpin and click **Unpin rows**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-unpin-row-1.png)

The unpinned rows move below the dividing line.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-unpin-row-2.png)

To pin a row, select the unpinned algo instance row or rows you want to pin and click **Pin rows**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-row-1.png)

The unpinned rows move below the dividing line.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-row-2.png)

## Filtering Columns

To filter a column:

1. Hover over the the right side of the column header and select the down caret to filter on the desired selection.
2. The column header then appears in yellow, indicating that the column is filtered.

To remove a filter:

1. Click the filter icon in the header.
2. Click **Clear Filter**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-filter-column.png)

## Creating tabs for running algos

If you have algos running that are not shown in one of the Autotrader tabs, such as Order Ticket Algos (OTAs) or Order Management Algos (OMAs), you can automatically open the related algos in new tabs. In this way, you can use Autotrader to manage those algos in addition to the algos launched from Autotrader.

To open running algos in new tabs, right-click anywhere in the widget and select **Auto-create tabs for all running algos** from the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-tabs-1.png)

If another algo was running, such as Randomized Volume Slicer, a new tab for that algo would be added.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-tabs-2.png)

**Note**: Once a tab is created in Autotrader for algo, any future instances of the algo will be added to the tab, even if they are started outside of Autotrader.

## Customizing control button visibility

To hide and display control buttons:

1. Select **Edit control buttons** from the right-click context menu.The control button selection dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-control-buttons.png)
2. Select the buttons you want to display and click **OK**.

←[Previous PostLaunching an algo in Autotrader](launching-an-algo-in-autotrader.md)

[Next PostModifying algo variables in working orders](modifying-algo-variables-in-working-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pause-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-stop-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pause-inline.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-stop-inline.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-rows-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-unpin-row-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-unpin-row-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-row-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-pin-row-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-filter-column.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-tabs-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-tabs-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-control-buttons.png
