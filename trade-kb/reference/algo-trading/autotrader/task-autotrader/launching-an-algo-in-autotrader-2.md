---
title: Launching an algo in Autotrader
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader-2/
---

# Launching an algo in Autotrader

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader-2/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Algo Dashboard vs Autotrader](../../../../guides/algo-ops.md#algo-dashboard-vs-autotrader) · [Algo Ops: Dashboard, Autotrader & Excel § From Autotrader](../../../../guides/algo-ops.md#from-autotrader)

Autotrader allows you to run multiple algos and multiple instances of each algo from within a single widget. Users
who run large numbers of algo instances simultaneously should check the [Algo Server
limitations](../reference-autotrader/algo-server-limitations.md).

## Opening an algo and adding algo instances

To set up and launch an algo in Autotrader:

1. Do either of the following:
   * To open an algo in a new Autotrader widget, from the **Widgets** menu, select **Autotrader**.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-1.png)
   * To add an algo to an existing Autotrader widget, click + to open a new tab.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-1a.png)
2. Click **Pick Algo**, and select the desired algo from the list of deployed algos.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-2.png)

   **Note**: The list includes only ADL algos and Order Ticket Algos (OTAs) you have permission to run.A new Autotrader widget for the selected algo is opened, seeded with the algo name. The columns vary based on the
   inputs and variables defined as part of the algo. The green columns indicate user-defined (algo input) variables in
   the algo itself. Any exported (algo output) variables will appear as orange columns in Autotrader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-3.png)
3. Click **Add row** to add one instance of the algo.Each row represents an algo instance. Note that creating a row does not start the algo—each row must be
   launched for the corresponding algo instance to become active.

## Configuring and starting algo instances

After you open an algo in Autotrader, you can create several instances of the algo that let you reuse an algo with
different sets of parameters. For example, you could open a market-making algo and use different instances to run the
algo in different markets.

To configure and start a single algo instance:

1. Open an algo, if necessary.
2. Click ![Add row](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-icon-add-row.png) to add an instance of the algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-1.png)
3. Click each cell whose value you want to change and specify the desired value.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-2.png)
4. Select the algo instance by clicking its checkbox.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-3.png)
5. Click ![Play icon](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-at2-play-1.png).The algo instance Status changes to **Starting**…

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-4.png)

   …and then progresses to the next status (**Running**, in this case).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-5.png)

To configure and start multiple algo instances:

1. Open an algo, if necessary.
2. Click ![Add row](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-icon-add-row-1.png) to add the desired number of algo instances.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-1.png)
3. Do any of the following:
   * Click each cell whose value you want to change and specify the desired value.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2.png)
   * Select consecutive cells in a column or row and change the value of the last selected cell to use the same
     value for all of the selected cells.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2a.png)

     The new value is applied to all selected cells in the column.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2a-edit.png)
   * Select a region of cells to change the values of all cells in the region to the same value.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2b.png)

     The new is applied to all selected cells.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2b-edit.png)
4. Select the algos you want to start; then click ![Play icon](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-at2-play-2.png)

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-3.png)

   The Status of all of the selected algo instances changes to Starting and then progresses to the next status.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-4.png)

## Converting from existing Autotrader algos to Autotrader

If you have saved Autotrader configurations, you can easily convert them to Autotrader. All custom templates are also
converted, so you do not need to recreate them.

To convert existing Autotrader algos to Autotrader:

1. Open an algo in the Autotrader widget.
2. From the right-click context menu, select **Convert to new Autotrader**.The algo opens in the Autotrader widget.

## Configuring your algos with data from Microsoft Excel

After you open an algo in Autotrader, you can create several instances of the algo that let you reuse an algo with
different sets of parameters. For example, you could open a market-making algo and use different instances to run the
algo in different markets.

To configure and start algo instances:

1. Enter the algo input variables for the instances you want to launch.You can manually click each cell and specify a value, or you can use data you have stored in an Excel spreadsheet.
   The remainder of the steps assume you have the data stored in an open Excel spreadsheet.
2. Modify or create your Excel spreadsheet.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-1.png)
3. In the Excel spreadsheet, select the values you want to seed in the algo instances in Autotrader and copy them.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-2.png)

   When you copy and paste the values from Excel, the values are static and not linked dynamically. You can also [link the values from Excel](../../excel-integration-with-tt/description-excel-integration-with-tt/excel-linking-overview.md) so that they update in Autotrader if you
   change them in Excel.
4. In the Autotrader grid, select the cells corresponding to those you copied from Excel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-3.png)
5. Paste the values by typing **Ctrl-V**.The corresponding cells update with the copied values.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-4.png)

   The new variable values appear in each row of the algo in Autotrader. Note that the algos are not yet launched.
6. Select the algo instances you want to launch, and click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-open-algo-2.png).You can launch an instance by clicking the launch button associated with the instance, or you can select the the
   checkbox for one or more instances and click the launch button in the toolbar.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-5.png)

   The selected algos’ **Status** changes to **Starting** as the algo instances are launched.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-6.png)

   After the algos launch successfully, the **Status** field changes to **Working**.

←[Previous PostModifying an algo variable in a working order](modifying-an-algo-variable-in-a-working-order.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-1a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-launch-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-icon-add-row.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-at2-play-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-inst-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-icon-add-row-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2a-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2b.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-2b-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-at2-play-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-multi-inst-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-open-algo-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at2-config-excel-6.png
