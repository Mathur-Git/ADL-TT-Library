---
title: Algo dashboard panes
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-panes/
---

# Algo dashboard panes

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-panes/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Algo Dashboard vs Autotrader](../../../../guides/algo-ops.md#algo-dashboard-vs-autotrader) · [Algo Ops: Dashboard, Autotrader & Excel § Monitoring a running algo](../../../../guides/algo-ops.md#monitoring-a-running-algo)

The Algo Dashboard is divided into three separate panes. Located on the left side is the **Algo Explorer** pane where you can search for and select private or shared algos. When selected, the algo variables display in the center Algo Orders pane where you can edit and start the algo. Any changes made to variables can be saved as a template for future use. After an algo has been started, you can monitor and manage its progress in the **Algo Variables** pane.

## Algo Explorer pane

The **Algo Explorer** pane allows you to quickly locate and manage algos within a tree structure. The top level of the tree is split into two branches: **My Algos** and **Shared with me**. The **My Algos** branch contains all algos that have been deployed with your TT ID.  The **Shared with me** branch contains algos that have been published by TT or shared with you by other algo developers.

![Algo Explorer Pane](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-explorer.png)

**Note:** The list includes only ADL algos and Order Ticket Algos (OTAs) you have permission to run.

When you select an algo, the Algo Explorer shows the algo details and variables, as shown.

![Algo Launch Pane](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-launch.png)

1. **Template selection**: Lets you choose a specific [algo template](algo-templates.md), if available.
2. **Algo-specific variables**: Lets you verify or change the input variables for the algo before launching it.
3. **Common algo variables**: Lets you specify values for common algo variables.

### Split panel view

The Algo Explorer split panel view lets you show both the algo list and a selected algo’s parameters by selecting **Switch to split panel** from the Algo Explorer’s context menu. The two panels are placed side-by-side in the same space as the Algo Explorer pane, but you an resize one or both the split panels. With the split panel view, you can quickly select and modify algo or template parameters before launching.

![Algo Explorer split view](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-split-view.png)

Selecting **Switch to single panel** from the split panel context menu, restores the standard Algo Explorer pane view.

## Algo Orders pane

Located on the center of the Algo Dashboard is the **Algo Orders** pane. At the top of the pane is the Algo Dashboard toolbar, which allows you to cancel, pause, or resume algos. Directly below the toolbar is the Algo order grid, which contains algos that you started.

![Algo Orders Pane](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-orders.png)

**Note:** Algo orders can also be managed from the [Order Book](../../../order-management/order-book/description-order-book/order-book-overview.md) widget.

## Algo Variables pane

The **Algo Variable** pane is located on the right side of the Algo Dashboard and allows you to modify user-defined algo variables. It contains two tabs:

* The **Variables** tab shows two types of variables: algo-specific and standard. Algo-specific variables are added within ADL® (Algo Design Lab) and can include such things as order quantity or offsets. The standard variables listed below the algo-specific variables include unchangeable variables, such as **Co-location** and **Client Disconnect Action**.
* The **Exports** tab shows the names and values of [exported variables](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/export-block-output-values.md) defined for the algo in ADL.

![Algo Variables Pane](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-variables.png)

1. A gray background indicates that you cannot change the variable value.
2. A white background indicates you can double-click a value to modify it.
3. Exported variables defined in the algo.
4. Algo controls.

**Note:** All user-defined input and output variables for the algo are also shown in the **Algo Orders** pane.

## Minimizing the Algo Dashboard panes

You can minimize the Algo Explorer (left) and Algo Parameters (right) panes via the right-click context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-explorer-minimize.png)

Once minimized, the panes can be restored with a left-click on the thin vertical bar.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-explorer-minimize-2.png)

←[Previous PostAlgo Dashboard overview](algo-dashboard-overview.md)

[Next PostAlgo templates](algo-templates.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-explorer.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-launch.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-split-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-pane-variables.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-explorer-minimize.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-explorer-minimize-2.png
