---
title: Autotrader reference
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/autotrader/reference-autotrader/autotrader-reference/
---

# Autotrader reference

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/autotrader/reference-autotrader/autotrader-reference/)

## Algo status

An algo can be in one of the following states.

Status | Order condition | Ends when… || Starting | An algo that a trader launched is initializing. | The algo finishes the initialization process. |
| Working | An algo order that is currently running. | The algo is paused or canceled, or there is a change in Algo server status (e.g., server cycled). |
| Paused | An algo order that paused itself or was paused by other means. | The algo either resumes working or gets canceled. |
| Deleting | An algo order that has been deleted displays in the Deleting state while the Algo server performs the delete action. | The Algo server completes deletion of orders. Child orders might not get deleted |
| Failed | The algo order stops working. |  |

## Supported changes to algos

The Algo Server supports the following changes to parent algo orders.

| Change | Applies to… | Result |
| --- | --- | --- |
| Cancel | Applies to parent orders in the **Working**, **Paused** or **Failed** state. | For child orders, follows the behavior specified in the algo’s **Leave Orders on Cancel** setting. |
| Pause | Applies to parent orders in the **Working** state. | For child orders, follows the behavior specified in the algo’s **Leave Orders on Pause** setting. |
| Resume | Applies to parent orders in the **Paused** state. | Starts working the paused order. |
| Modify the quantity | Applies to parent orders in the **Working** or **Paused** state. | Depending upon the algo, you may be able to modify the quantity using the **Algo Variable** pane.  If the algo is in the **Paused** state, the change will take effect when the algo is resumed. |
 Modify the price | Applies to parent orders in the **Working** or **Paused** state. | Depending upon the algo, you may be able to modify the price using the **Algo Variable** pane.  If the algo is in the **Paused** state, the change will take effect when the algo is resumed. |

## Context menu options

The right-click context menu contains the following options:

* **Fit all columns to content**: Resizes all column widths to match the width of their content.
* **Edit columns**: Lets you display and order columns in the grid.
* **Edit control buttons**: Hides or shows buttons to control algo execution and updates.
* **Hide (Show) unpinned rows**: Sets whether to show only rows for algos that were launched from the active tab.
* **Auto-create tabs for all running algos**: Add all running algos to the tab, including Order Ticket Algos (OTAs) and Order Management Algos (OMAs).
* **Zoom**: Zooms the view of the selected widget.

## Autotrader toolbar buttons

| Button | Description |
| --- | --- |
|  | Adds a row for a new instance of the algo |
|  | Pauses the selected, or all, running algos. |
|  | Starts or resumes the selected, or all, algos. |
|  | Stops the selected, or all, running algos. |
|  | Pins the selected rows so they remain in view after their corresponding algos complete |
|  | Unpins the selected algos, moving them below the dividing line |
|  | Duplicates the selected rows, including their parameter values. |
|  | Deletes the selected, or all, rows from Autotrader |
|  | Discards any edits you have made to an algo’s parameters |
|  | Updates the algo parameter values you changed. |

## Autotrader columns

| Column | Description |
| --- | --- |
| Current User | TT user name of the trader associated with the transaction or owns a staged order. |
| Originator | TT User ID of the person who submitted the order or staged order. |

[Next PostAlgo Server limitations](algo-server-limitations.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-add-row.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-pause.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-play.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-stop.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-pin-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-unpin-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-clone-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-delete-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-discard.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-btn-submit.png
