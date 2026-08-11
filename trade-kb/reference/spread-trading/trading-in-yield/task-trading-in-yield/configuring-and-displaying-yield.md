---
title: Configuring and displaying yield
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/task-trading-in-yield/configuring-and-displaying-yield/
---

# Configuring and displaying yield

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/task-trading-in-yield/configuring-and-displaying-yield/)

Using the Yield widget, you can configure and display prices in yield for Futures or Treasury Bonds in TT. Yield configurations can also be created from Autospreader or MD Trader.

After a configuration is added, it appears in the Yield widget and the list of available yield configurations in [Autospreader](#as) and [MD Trader](#mdt). Yield prices are displayed based on which configuration is selected.

**Note**: For CME BrokerTec only, the Maturity Date and Settlement date will be auto-populated.

To configure yield using the Yield widget:

1. Click **Widgets** | **Automation** on the menu bar to open the **Yield** widget.
2. Click **Create**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-config-create.png)
3. In the **Edit Yield** dialog box that appears, configure the [yield conversion settings and options](../reference-trading-in-yield/yield-configuration-options.md).

   Based on the product type you select, different required fields are displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-gui.png)
4. Click **Save**.

   The yield configuration appears in the Yield widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-config-create-2.png)

## Configuring and displaying yield in Autospreader

Yield can also be applied in Autospreader by adding a yield configuration to each leg. When an Autospreader instrument is configured for yield, the Autospreader MD Trader only displays the spread price in yield and the price ladder is automatically inverted.

To configure and display yield in Autopsreader:

1. Click the **Yield** parameter to select an existing yield configuration or click **Configure Yield** to add a new one.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-spread-config.png)

   **Note**: To modify an existing yield configuration, you must edit it using the Yield widget.
2. In the **Edit Yield** dialog box, configure the [required fields](../reference-trading-in-yield/yield-configuration-options.md) for the instrument being traded.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-spread-config-gui.png)
3. Click **Save**.

   When the spread is launched, the Autospreader MD Trader only shows the price in yield.

## Configuring and displaying yield in MD Trader

To configure and display yield in MD Trader:

1. Right-click the price ladder to select **Yield** | **Show Yield** and click **Configure Yield…**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config.png)

   The “Yield” column is shown and the **Edit Yield** dialog box appears.

   **Note**: You can also select an existing configuration in MD Trader to display prices in yield. To modify an existing yield configuration, you must edit it using the Yield widget.
2. In the **Edit Yield** dialog box, configure the [required fields](../reference-trading-in-yield/yield-configuration-options.md) for the instrument being traded.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-gui-1.png)
3. Click **Save**.

   The **Yield** column displays the instrument price in yield. The “+” sign indicates the yield value is rounded. The added yield configuration is now available in the Yield widget, as well as MD Trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-display.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-config-create.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-gui.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-config-create-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-spread-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-spread-config-gui.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-gui-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-mdt-config-display.png
