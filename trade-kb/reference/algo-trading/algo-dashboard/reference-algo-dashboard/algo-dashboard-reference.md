---
title: Algo Dashboard Reference
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/reference-algo-dashboard/algo-dashboard-reference/
---

# Algo Dashboard Reference

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/reference-algo-dashboard/algo-dashboard-reference/)

## Available settings

These “Order Book” settings affect only the selected Algo Orders pane in the Algo Dashboard widget. To update the default settings with these values for newly-opened Order Book widgets or to apply them to existing opened Order Book widgets, click **Defaults**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-algo.png)

#### Display

| Setting | Description |
| --- | --- |
| Colors | Allows you to [customize or change the cell and column colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md#colors) available in the widget. There are separate settings for text and background colors. |
| Grid font size | Adjust the font size to suit your preferences and use bold text, if desired. |
| Bold font | Sets the use of bold text in the widget. |
| Row numbers | Displays the row numbers column. |
|
| Row checkbox column | Shows/Hides the checkbox selection column. |
| Italic font for fills | Sets italic font on all fill rows. |
| Ignore global Account List broadcasts | Configures the widget to ignore account selections made in an Account List. When checked (enabled), the widget ignores account selections broadcast by an Account List widget. |
| Highlight new and filled orders (seconds) | Highlights new and filled order rows. The highlight color displays for the set number of seconds. Setting the value to zero (0) seconds retains the highlight color until you select the right-click menu option **Mark all as seen**. |
| Persist algo columns | Preserves columns shown in the Algo Orders pane in the Algo Dashboard widget. When this setting is enabled, algo variable and export columns remain movable via drag-n-drop, are visible/editable in the “Edit Columns” menu, and can be saved in the workspace. |
| Include orders from previous sessions | Set whether to display orders from only the current session or whether to include orders from previous sessions as well. |
| Include deleted orders | Set whether to display deleted orders from only the current session or from previous sessions as well. To include deleted orders from previous sessions, also check the “Include orders from previous sessions” checkbox. |
| Flatten orders in “Filled” view mode | Enables filled child orders to be displayed in the order in which they were filled when using “Filled” view mode. When this setting is unchecked, filled child orders are displayed as nested underneath their parent order. Unchecked by default. |
| Launch floating order entry on left click on price or quantity | Enables the floating order entry preference to be launched when clicking on price and quantity cells in the grid. |
| Italic font for staged orders | Displays staged orders in italics in the Order Book. |
| Show tabs | Set whether to display the tab bar at the bottom of the widget |
| Set Order Book columns | Select the [columns](#ob-col-desc) you want shown in the Order Book. |
| Set Order Toolbar buttons | Select the [buttons](#ob-buttons-desc) you want shown in the Order Book. |

### Algo status

An algo can be in one of the following states.

Status | Order condition | Ends when… || Starting | An algo that a trader launched is initializing and performing risk checks. | The algo finishes the initialization process. |
| Working | An algo order that is currently running. | The algo is paused or canceled, or there is a change in Algo server status (e.g., server cycled). |
| Paused | An algo order that a trader has paused. | The algo either resumes working or gets canceled, or there is a change in Algo server status. |
| Deleting | An algo order that has been deleted displays in the Deleting state while the Algo server performs the delete action. | The Algo server completes deletion of child orders. |
| Failed | The algo order stops working. | The Algo server attempts to delete child orders if its **Leave Orders on Cancel** parameter is disabled during normal server shutdown.  The Algo server puts the parent order in the Failed state if it cannot delete all of the child orders.  **Note**: All TT Algos are automatically deleted when the Algo server shuts down, as TT Algos do not support the **Leave Orders on** setting. |

### Supported changes to algos

The Algo Server supports the following changes to parent algo orders.

| Change | Applies to… | Result |
| --- | --- | --- |
| Cancel | Applies to parent orders in the **Working** or **Paused** state. | Follows the behavior specified in the algo’s **Leave Orders on** setting. |
| Pause | Applies to parent orders in the **Working** state. | Follows the behavior specified in the algo’s **Leave Orders on** setting. |
| Resume | Applies to parent orders in the **Paused** state. | Starts working the paused order. |
| Modify the quantity | Applies to parent orders in the **Working** or **Paused** state. | Depending upon the algo, you may be able to modify the quantity using the **Algo Variable** pane.  If the algo is in the **Paused** state, the change will take effect when the algo is resumed. |
 Modify the price | Applies to parent orders in the **Working** or **Paused** state. | Depending upon the algo, you may be able to modify the price using the **Algo Variable** pane.  If the algo is in the **Paused** state, the change will take effect when the algo is resumed. |

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-algo.png
