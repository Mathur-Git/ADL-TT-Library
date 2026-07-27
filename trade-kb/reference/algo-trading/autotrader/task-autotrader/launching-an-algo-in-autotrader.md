---
title: Launching an algo in Autotrader
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader/
---

# Launching an algo in Autotrader

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader/)

To set up and launch an algo in Autotrader:

1. From the **Widgets** menu, select **Autotrader**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-1.png)
2. Click **Pick Algo**, and select the desired algo from the list of deployed algos.

   ![](https://library.tradingtechnologies.com/trade/Content/at-launch-2a.png)

   Note: The list includes only ADL algos and Order Ticket Algos (OTAs) you have permission to run.

   A new Autotrader widget for the selected algo is opened, seeded with the algo name. The columns vary based on
   the inputs and variables defined as part of the algo. The green columns indicate user-defined (algo input)
   variables in the algo itself. Any exported (algo output) variables will appear as orange columns in Autotrader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-3.png)
3. Click **New** to add one instance of the algo; or you can click the **New** dropdown to add multiple
   copies of an algo (as shown).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-4.png)

   The specified number of algo instances are added to the widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-5.png)

   Each row represents an algo instance. Note that creating a row does not start the algo—each row must be
   launched for the corresponding algo instance to become active.
4. Enter the algo input variables for the instances you want to launch.

   You can manually click each cell and specify a value, or you can use data you have stored in an Excel
   spreadsheet. The remainder of the steps assume you have the data stored in an open Excel spreadsheet.
5. Modify or create your Excel spreadsheet.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-6.png)
6. In the Excel spreadsheet, select the values you want to seed in the algo instances in Autotrader and copy them.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-7.png)

   When you copy and paste the values from Excel, the values are static and not linked dynamically. You can also
   [link the values from Excel](../../excel-integration-with-tt/description-excel-integration-with-tt/excel-linking-overview.md) so that they update in Autotrader if
   you change them in Excel.
7. In the Autotrader widget, select the cells corresponding to those you copied from Excel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-8.png)
8. Paste the values by typing **Ctrl-V**.

   The corresponding cells update with the copied values.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-9.png)

   The new variable values appear in each row of the algo in Autotrader. Note that the algos are not yet launched.
9. Select the algo instances you want to launch, and click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-open-algo.png)

   You can launch an instance by clicking the launch button associated with the instance, or you can select the
   checkbox for one or more instances and click the launch button in the toolbar.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-10.png)

   The selected algos’ **SynthStatus** changes to **Starting** as the algo instances are launched.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-11.png)

   After the algos launch successfully, the **SynthStatus** field changes to **Working**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-12.png)

[Next PostManaging algo instances](managing-algo-instances.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-1.png
- https://library.tradingtechnologies.com/trade/Content/at-launch-2a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-9.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-open-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-10.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-11.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/at-launch-12.png
