---
title: Opening Spread Matrix
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix/
---

# Opening Spread Matrix

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix/)

Use the **Exchange-listed** tab to open a spread matrix for an exchange-listed calendar spread.

1. Open the Spread Matrix widget.
2. Click the **Exchange-listed** tab in the **Add Tab** dialogue.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-tab2.png)
3. Enter a product in the **Search for products** box or click Explore to select a single product.
4. Click **Ok**.

## Opening an inter-product Spread Matrix

Use the **Autospreader** tab to open an existing inter-product spread that is managed by the Autospreader® widget. This includes any inter-product spreads you’ve created using the Spread Matrix.

1. Open the Spread Matrix widget.
2. Click the **Autospreader** tab in the **Add Tab** dialogue.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/spread-matrix-as.png)
3. Click the dropdown arrow in the **Select a spread** field and click on a spread.

   **Note**: The **Autospreader** tab only displays synthetic inter-product spreads. If there are no inter-product spreads created in Autospreader®, this dropdown will be empty.
4. click **OK**.

## Opening a custom inter-product Spread Matrix

To populate a Spread Matrix with two different products when there is not an existing Autospreader spread comprised of legs of the two different products, use the **Custom** tab.

1. Open the Spread Matrix widget.
2. Click the **Custom** tab from the **Add Tab** dialogue.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/spread-matrix-custom.png)
3. Click **Search for a product…** in the **Front leg product** and **Back leg product** fields to select products for the front and back legs of the spread.
4. Configure the following settings in the **Spread Settings** table:
   * **Ratio** — Indicates the quantity of each leg in relation to the others. A negative sign (-) before the number indicates a short leg. Values entered in the Ratio field do not affect the spread price.
   * **Multiplier** — Weights the value of the leg price to calculate the spread price when using the “Price Differential” formula:

     `(1 * Leg1.MergedPrice) - (1 * Leg2.MergedPrice)`

     **Note**: The multiplier can be a whole number, decimal number, or fraction. Fractional representation optimizes ticking accuracy.

     **Example**: A Spread Multiplier of 0.333333 displays as 1/3 in the
     **Tick Information** section.
5. Click **Ok**.

   The custom spread is launched in Spread Matrix.

[Next PostDisplaying market data in spread matrix](displaying-market-data-in-spread-matrix.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-tab2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/spread-matrix-as.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/spread-matrix-custom.png
