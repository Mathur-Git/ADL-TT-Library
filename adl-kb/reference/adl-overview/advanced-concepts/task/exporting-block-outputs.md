---
title: Exporting block outputs
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/exporting-block-outputs/
---

# Exporting block outputs

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/exporting-block-outputs/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § User-defined variables](../../../../guides/algo-types.md#user-defined-variables) · [Design Patterns & Recipe Index § Organisation and reuse](../../../../guides/design-patterns.md#organisation-and-reuse) · [Algo Ops: Dashboard, Autotrader & Excel § Driving algo variables from Excel (linking)](../../../../../trade-kb/guides/algo-ops.md#driving-algo-variables-from-excel-linking)

### Exporting block outputs

To export [block output values](../description/export-block-output-values.md):

1. In ADL, right-click on the output port of a block and select **Export value** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-export-values-step1.png)

   After selecting the port, the port is outlined with an orange border, as seen for the **fillPrice** port in the example.
2. Click the **Information** bar at the bottom of the canvas; then click the **Export Values** label to display the exported values.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-export-values-step2.png)
3. Deploy the algo.
4. Open the Algo Dashboard and launch the algo.

   Columns for the exported values will be visible at the far right, similar to the above example.

To stop exporting a value, right-click on the desired output port and select **Unexport value** from the context menu.

[Next PostManaging shared algos](managing-shared-algos.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-export-values-step1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-export-values-step2.png
