---
title: Launching an algo from the Algo Dashboard
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/task-algo-dashboard/launching-an-algo-from-the-algo-dashboard/
---

# Launching an algo from the Algo Dashboard

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/algo-dashboard/task-algo-dashboard/launching-an-algo-from-the-algo-dashboard/)

Use the Algo Dashboard to launch algos one at a time and do the following:

* Start / Pause / Resume / Cancel algos.
* Modify parameters of running algos.
* Monitor various metadata of running algos, such as P/L and the number of working orders.

## Launching an algo

**Note**: Users who run large numbers of algo instances simultaneously should check the [Algo Server limitations](../../autotrader/reference-autotrader/algo-server-limitations.md).

To launch an algo from the Algo Dashboard…

1. Select **Algo Dashboard** from the **Widgets** menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-2.png)
2. Select the algo that you want to launch.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-3.png)
3. Configure the parameters as needed to run the algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-4a.png)

   **Note**: The **Co-location** drop down is seeded based on the market of the default instrument in the selected algo. It will also seed when multiple instruments are defined if all instruments are from the same market.
4. Specify an **Instance name**, if desired, to give this instance of the algo a [custom name](../description-algo-dashboard/algo-instance-names.md) that will appear in the **TextTT** column of the launch algo.
5. Select which action the algo should take if the client loses its connection to TT:
   * **Leave** to allow the algo to continue running normally.
   * **Pause** to suspend the algo until you manually restart it.
   * **Cancel** to delete the algo.**Note**: You can set the default Disconnect action in the [Preferences](../../../overview/preferences/description-preferences/algos-autospreader-preferences.md).
6. Click ![<strong>Launch algo</strong>](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-icon.png).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-4b.png)

   The algo is launched and added to the **Algo Orders Pane** with a **Starting** status. After the algo initializes successfully, its status changes to **Working**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-5.png)

### Using mulitple accounts for algos with Autospreader or Aggregator instruments

The Algo Explorer panel provides you with the ability to select separate accounts for routing the child orders of a parent [Autospreader](../../../spread-trading/autospreader/description-autospreader/introduction-to-autospreader.md) or [Aggregator](../../../spread-trading/aggregator/description-aggregator/aggregator-overview.md) algo order. For example, you can use separate accounts on different exchanges to submit orders for cross-exchange spreads, or split trading between separate accounts and different brokers.

To select different accounts for a spread or aggregator order while configuring an algo:

1. Specify either an Autospreader or Aggregator instrument.
2. In the **Account** dropdown, select **Multi…**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-multi-account-1.png)
3. For each leg, specify the desired account.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-multi-account-2.png)

## Launching an algo template

If you have defined [templates](../description-algo-dashboard/algo-templates.md) for your algos, they appear nested beneath their respective algos. Launching an algo template lets you start the algo order immediately with its pre-configured parameters, bypassing the parameter configuration.

**Note**: From the Algo Explorer context menu, you can choose to show or hide the algo templates.

To launch an an algo template:

1. Select **Algo Dashboard** from the **Widgets** menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-1.png)
2. Select one or more algo templates that you want to launch.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-2.png)
3. Click the **Launch algos** button to launch the selected algos.The selected templates launch their respective algos with their parameters and adds them to the **Algo Orders Pane** with a **Starting** status. After each algo initializes successfully, its status changes to **Working**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-3.png)

## Modifying a working algo

To modify the algo while it’s parent order is working in the market:

1. Click the order in the dashboard and change the settings in the **Algo Variables Pane**.**Note**: You can also click ![the Pause button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-pause-button.png) to pause the algo before modifying the parameters.When you select a parent order, the **Algo Variables Pane** (at the right edge of the widget) is auto-populated to show the parameters pertaining to the selected parent order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-1.png)
2. Change the desired values.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-2.png)

   After you change the value of a parameter, the cell background is highlighted to indicate that there is a change waiting to be committed.
3. Click ![the Submit button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-submit-button.png) button to commit the changes.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-3.png)

   The working parent order updates with the new values.

[Next PostManaging algo templates](managing-algo-templates.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-4a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-4b.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-launch-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-multi-account-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-multi-account-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/alg-launch-template-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-pause-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-submit-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/algo-dash-modify-3.png
