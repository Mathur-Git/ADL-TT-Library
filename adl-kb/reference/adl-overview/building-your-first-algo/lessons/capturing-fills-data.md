---
title: Capturing fills data
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/capturing-fills-data/
---

# Capturing fills data

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/lessons/capturing-fills-data/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Testing](../../../../guides/design-patterns.md#testing) · [Order Management & Risk § See also (ADL side)](../../../../../trade-kb/guides/order-management-and-risk.md#see-also-adl-side)

In this section, you will create the logic to extract data from your entry order fills and use the data to calculate your running average open price. The average open price will later be used to calculate the exit price of our Scalper algo.

![Add-PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fills-highlighted.png)

This section covers:

* The difference between continuous and discrete messages.
* Using ADL’s Formula Editor.
* Using the math blocks to perform calculations.

### Messages in ADL: Continuous Messages vs Discrete Messages

Data passed between blocks in ADL are referred to as messages. The two types of messages in ADL are:

* [Continuous Messages](../../adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages.md): a continuous input of specified data.
* [Discrete Messages](../../adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages.md): an individual message sent at a specific point in time, triggered by an event, storing details about the event in fields.

Thus far, the blocks of the Scapler algo use continuous messages:

* The [Instrument](../../../trading-blocks/instrument-block.md) block outputs a continuous feed of instrument data.
* The [Field](../../../trading-blocks/field-block.md) block continuously outputs the Best Bid price for the selected instrument.
* The [Number](../../../basic-blocks/number-block.md) block provides a continuous output of 5.

Next, you will use [discrete event messages](../../adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages.md) such as those emitted through the **Entry Order** block’s fills output port which outputs an individual discrete message for each fill that occurs using the orders placed by this block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-dm.png)

The fills discrete message contains fields that capture information about the fill, such as the fill price and fill quantity.

### Calculating the average open price

The Scalper algo will calculate the average open price of all executed entry orders. This will later be used to calculate the exit price. To calculate the average open price:

* Calculate value at risk which is the cost of your position.
* Total the fill quantities of all entry orders.
* Divide the value at risk by the total fill quantities to determine the average open price.

#### Calculating the value at risk

As fills are received from your entry order, the total cost of those fills can be calculated by multiplying the price by the quantity of each fill. The [ValueAccumulator](../../../discrete-blocks/value-accumulator-block.md) block lets you perform this calculation for each fill and then accumulates a running total of each result. The block uses the provided formula to calculate a new value to accumulate each time a discrete message enters the block.

To calculate the value at risk from your order fills:

1. From the **Blocks** panel, locate the [ValueAccumulator](../../../discrete-blocks/value-accumulator-block.md) block and place it on the canvas to the right of the **Entry Order** block.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-1.png)
2. Connect the **fills** output port of the Entry Order block to the top input port of the ValueAccumulator block.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-2.png)  
    Notice that the edge displays differently to provide a visual indication that this edge passes discrete messages.
3. In the **Block Properties** panel, set the **Name** to **VAR**.
4. Define the formula for the block to use in its calculations by clicking the **edit** link in the **Formula** field.  
      
    The [Formula Editor](../../advanced-concepts/description/formula-editor.md) for the block appears.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-3.png)
5. In the **Formula Builder**, you will create a formula to multiply the fill price and the fill quantity to determine the cost of the incoming fill.  
      
    To access discrete message fields sent into the block, you type #, followed by the name of the value you want to use. The editor displays the available message fields as you type.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-4.png)
   * Type **#** and select fillPrice from the list to add the **fillPrice** field to the formula.  
      ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-5.png)
   * Type **\*** for multiplication and then select the **fillQuantity** field to complete the formula.  
      ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-6.png)
   * Click **Save**.  
        
      Notice the Formula field of the Block Properties now shows the block formula.  
      ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-7.png)

#### Tracking the total filled quantities

To determine the average price of all fills received for your order, you need to keep track of quantities of all fills. In a similar manner used to calculate the value at risk, you will use the [ValueAccumulator](../../../discrete-blocks/value-accumulator-block.md) block to keep a running total of the fill quantities.

To track the total filled quantities:

1. Drag another ValueAccumlator block to the canvas beneath the **VAR** block and connect it to the **Entry Order** fills output port.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-qty-1.png)
2. In the **Block Properties** panel, set the **Name** to **Fill Qty**.
3. Open the Formula Editor and type # to add the fillQty field to the formula.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-qty-2.png)
4. Click **Save**.

#### Calculate the average open price

Finally, you need to use the values from the VAR and Fill Qty blocks to determine the average open price. You will use the Divide block to perform this calculation.

To determine the average open price:

1. From the Blocks panel, drag a [Divide](../../../arithmetic-blocks/divide-block.md) block to the canvas. Rename it to **Average Open Price**.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-price-1.png)
2. Connect the top numeric output port of the **VAR** block to the top input port of the **Average Open Price** block.
3. Connect the top numeric output port of the **Fill Qty** block to the bottom input port of the **Average Open Price** block.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-price-2.png)

### Testing your logic

Before continuing with the algo, it is a good idea to test your fills logic to make sure it is functioning as intended.

To test your logic, using the same setup as before:

1. In the **Values** tab, enter a larger order quantity so you can verify each fill updates the blocks values properly.
2. Play the **algo and watch the numeric outputs of the **VAR**, **Fill Qty** and Average Open Price** blocks to ensure they are updating as expected.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-test.png)
3. Stop the algo.

You have successfully completed capturing data from your fills and performing calculations with the data. Now you are ready to use these values to determine the price and quantity for your exit order.

←[Previous PostTesting the entry logic](testing-the-entry-logic.md)

[Next PostCreating the exit order](creating-the-exit-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-fills-highlighted.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-dm.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-var-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-qty-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-qty-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-price-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-price-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-fiils-test.png
