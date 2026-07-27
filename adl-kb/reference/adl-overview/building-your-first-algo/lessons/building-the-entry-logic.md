---
title: Building the entry logic
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/building-the-entry-logic/
---

# Building the entry logic

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/building-the-entry-logic/)

The first part of building the Scalper algo is to define the entry order. This portion of your algo places a buy
order for a specified quantity at the best bid of the defined instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-highlighted.png)

### Starting an entry order with the Order block

The **Order** block enters orders into the market. Place an [Order](../../../trading-blocks/order-block.md)
block on the **Canvas** to be used to submit the entry order:

1. From the **Blocks** panel, click and drag the [Order](../../../trading-blocks/order-block.md) block on
   to the ADL canvas.![Add pic](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-1.png)
   Once placed, the Order block will be highlighted yellow to indicate that it is the currently selected block.
   In the **Block Properties** panel, you can view and edit the properties for the highlighted
   block.
2. In the **Blocks Properties** panel, specify the following properties.
   * Specify a **Name** of **Entry Order** to make it easier to identify the
     block.
   * Set **Type** to **Limit**
   * Set **Side** is **Buy**
   * Set **TIF** is **Day**.![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-2.png)You should see the block name appear under the Order block in the canvas.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-3.png)
Note the messages in the **Problems** tab of the **Information Panel** indicating that
the Order block you just placed is missing input connections. As you add more blocks and connect them to the
Order block, these messages will disappear.

### Selecting an instrument with the Instrument block

Now that you have an order block, you need to select an instrument you want to trade. The [Instrument](../../../trading-blocks/instrument-block.md) block lets you select the instrument you want to use. In this
algo, you will select a default contract, the front-month e-Mini S&P on CME, but will also allow a user to
choose a different contract when launching the algo.

To define the instrument for our entry order:

1. From the **Blocks** panel, double-click the [Instrument](../../../trading-blocks/instrument-block.md)
   block and then arrange it within the ADL canvas.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-1.png)
2. In the **Block Properties** panel, specify the following [properties](../../../trading-blocks/instrument-block.md#settings).
   * Give the block a **Name** of **Instrument**.
   * In the **Instrument** field, specify the default instrument for the algo. In this
     example, you want to use CME’s front-month e-Mini S&P contract.
   * For the **Type** property, select **User-defined** which will allow the
     user to choose a different contract when launching the algo.
   * Select an **Account** in the SIM environment which has:
     + Been assigned to your login.
     + User permissions to run in ADL.
     + Account permissions to run in ADL.![Instrument block properties panel](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-2.png)You can now see the selected **Instrument** displayed next to the blue instrument
     output port.
     ![Instrument block properties panel](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-3.png)
   * To set the instrument for the entry order, connect the Instrument block to the **Entry
     Order** block by clicking and dragging the left mouse button from the Instrument block’s
     output port to the **Entry Order** block’s **inst** input port.
     ![Instrument block properties panel](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-4.png)Notice that the first problem message regarding an invalid instrument is now gone, leaving two
     remaining problems.

### Setting the order price with the Field block

Next, set the price of the entry order at the best bid for the selected instrument. This algo uses a [Field](../../../trading-blocks/field-block.md) block to receive instrument data from the **Instrument**
block, continuously extract the Best Bid price of the instrument, and provide that value to the
**price** port of our **Entry Order** block.

To place the Field block and make the necessary connections:

1. You can use the Search feature to simplify the process of locating and pre-populating blocks.
   From the **Blocks** panel Search field, type “**bid**“.Notice how the list of blocks in the panel includes only those blocks whose names or properties that contain
   the string, “bid.”
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-1.png)
2. From the **Blocks** panel, click and drag the [Field
   (bidPrice)](../../../trading-blocks/field-block.md) block on to the ADL canvas.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-2.png)Notice that a new problem was added to the **Problems** tab of the Information Panel,
   indicating an issue needs to be resolved.
3. In the **Blocks Properties** panel, specify the following properties.
   * Notice that the **Field Name** drop-down is already selected as the result of block
     search.
   * Set **Name** to **Best Bid**.
   * Ensure that the **Lookup Type** is **Best**.![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-3.png)
4. To use Edge Finder to more easily connect blocks, press and hold the **Shift** key to display
   dashed lines for suggested connections from the Instrument block to the **Field** block and
   from the **Field** block to the **price** port of the **Order**
   block.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-4.png)
5. While holding the **Shift** key, either left-click each of the two dashed lines to make the
   connections, or right click one of the dotted lines to create both edges at once.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-5.png)

### Setting the order quantity with the Number block

To define the entry order quantity, the algo uses a [Number](../../../basic-blocks/number-block.md) block. You will set
a default value of 5, but allow the user to specify different quantities when running the algo.

To place the Number block and make the necessary connections:

1. From the **Blocks** panel **Search** field, type **5**.Notice how the panel automatically shows a Number block with its value already set to 5.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-1.png)
2. Click and drag the [Number](../../../basic-blocks/number-block.md) block on to the ADL canvas.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-2.png)
3. In the **Blocks Properties** panel, specify the following properties.
   * Notice that the **Default Value** drop-down is already set to 5, as the result of block
     search.
   * Set **Name** to **Entry Order Qty**.
   * Set **Variable Type** to **User Defined** which will allow the user to
     provide an order quantity other than the default of 5.
   * If desired, you could also use **Max Value** and **Min Value** to prevent
     users from accidentally submitting unreasonable order quantities.![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-3.png)
4. Connect the Number block to the **qty** input port of the Order block.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-4.png)After connecting the blocks, you have addressed the last of the problem issues, so the
   **Problems** tab is now blank.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-5.png)
5. While pressing the Shift key, click the dashed line to make the connection.
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-entry-order-number-4.png)

You have now finished the entry order portion of your algo which will place a 5-lot order at the best bid for the
instrument defined by the Instrument block. The next step is to test this portion your algo.

[Next PostTesting the entry logic](testing-the-entry-logic.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-highlighted.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-entry-ob-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-ib-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fb-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-nb-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-entry-order-number-4.png
