---
title: Formula Editor
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/formula-editor/
---

# Formula Editor

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/formula-editor/)
>
> **Interpreted in:** [Formula Editor Reference](../../../../guides/formula-reference.md) · [Gotchas, Hard Limits & Platform Constraints § Hard numeric limits](../../../../guides/gotchas-and-limits.md#hard-numeric-limits)

Many of the ADL blocks allow you to define formulas to calculate output values for the blocks. For such blocks, you can open the Formula Editor from their respective **Block Properties** panel.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-edit-link.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-launch.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-blank.png)

The Formula Editor shows the types of values and operations you can use in a formula, including:

* Arithmetic operators (i.e. +, -, %)
* Misc symbols to define the order of operations, such as parentheses
* Comparison operators (i.e. <, >=, ==, !=)
* Logical operators (i.e. IF, AND, OR, !**Note:** The IF operator is not currently supported in the [Alert](../../../miscellaneous-blocks/alert-block.md) block.
* Numbers and Boolean values
* [Variables](#adl-ac-variables), including values from other ADL block output connectors and values from the discrete event message entering the block
  + Block connectors let you use the output from another block in a formula.
  + Message fields let a formula use information from the incoming discrete event message.

The Formula Editor provides an auto-complete feature that lets you easily refer to information already available in your algo. When type one of the special characters (@ or #), the editor display a list of items that you can insert as variables into the formula. Also, typing characters after the symbol filters the list to items beginning with those characters.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-show-variables.png)

|  |  |
| --- | --- |
|  | Typing # displays a list of all fields available in an an incoming discrete event message. |
|  | Typing @ displays a list of blocks on the canvas that contain one or more continuous output ports. |

### Sample formulas

The following samples illustrate some basic formula types.

#### Boolean formula

The following formula simply outputs a Boolean value of TRUE, which can then be used by other downstream blocks.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-boolean-algo.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-boolean.png)

#### Arithmetic formula

The following formula for the **ExitPrice** [Value Extractor](../../../discrete-blocks/value-extractor-block.md) block calculates the price two ticks higher than the fill price, which you could use to submit an exit Sell order two ticks higher than the price of the Buy order fill.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-arithmetic-algo.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-arithmetic-2.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-fillprice.png)

|  |  |
| --- | --- |
|  | To access the value of the **fillPrice** message field, we type # and select the field. |
|  | To access the value of the **TickSize** [Field](../../../trading-blocks/field-block.md) block, we type @ and select the desired block. |

#### Conditional formula

The following formula outputs a TRUE/FALSE value based on whether the current opposite inside market is two ticks higher than the price of a fill.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-conditional-algo.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-conditional-2.png)

1. The IF condition uses the **>=** operator to compare the value of the **BestAsk** Field block (the available quantity at the Best Ask price) with the price two ticks away from the fill price (from the previous formula).
2. If the condition is TRUE, the formula outputs the Boolean value TRUE.
3. Otherwise, the formula outputs the Boolean value FALSE.

### Variable fields

The Formula Editor includes drop-down menus that allow you to add values that update dynamically as the algo runs.

* **connectors**: Lets you reference the value of a continuous output port from any other block in the algorithm. You can also type the connector in the form, **[*block.connector*]**.

  The following connector within the Formula Editor displays the continuous output ports from the Analytics block, named **Analytics0** within the algorithm.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formlua-editor-continuos-output.png)

  **Notes:**
  + Within the example above, you can type **@Analytics0**, or **@Analytics0-** (with a dash) to search the output port on a granular level.
  + The Formula Editor can only display a maximum of 100 continuous output ports from any other block in the algorithm.
* **messages**: Lets you extract any of the following information embedded within a discrete event message. You can also type the connector in the form, **{*fieldName*}**.

  + **limitPrice**: Price of an new order
  + **orderQuantity**: Total order quantity
  + **workingQuantity**: Working quantity of an order
  + **fillPrice**: Price of a fill
  + **fillQuantity**: Quantity of a fill
  + **cumQuantity**: Sum of fill quantities
  + **disclosedQuantity**: Quantity of a disclosed order visible in the market
  + **deletedQuantity**: Canceled quantity of a deleted order
  + **tradeQuantity**: Quantity of the last trade for a specified instrument
  + **tradePrice**: Price of the last trade for a specified instrument
  + **stopTrigger**: Price at which the respective stop order is activated
  + **isBuy**: Whether a fill was a buy side execution
  + **isQuotingOrder**: Whether the message was generated by a submitted quote order (valid only for Autospreader order blocks)
  + **isHedgeOrder**: Whether the message was generated by a submitted hedge order (valid only for Autospreader order blocks
  + **isExternalEvent**: Whether the message was generated from a source outside of the algorithm
  + **isTriggered**: Whether an order resulted from a trigger condition
  + **instrument**: Instrument associated with the message
  + **userField*N***: One of four empty fields that can be populated by a [Value Injector](../../../discrete-blocks/value-injector-block.md) and then accessed by a [Value Extractor](../../../discrete-blocks/value-extractor-block.md)
* “*string*“: ([Alert](../../../miscellaneous-blocks/alert-block.md) block only) Lets you add customized text to a message string.

### Blocks that use the Formula Editor

The following ADL blocks allow you to create custom formulas.

* Trading blocks

  + [Discrete Order block](../../../trading-blocks/discrete-order-block.md)
* Discrete blocks

  + [Branch](../../../discrete-blocks/branch-block.md)
  + [Discrete Max](../../../discrete-blocks/discrete-min-max-blocks.md)
  + [Discrete Min](../../../discrete-blocks/discrete-min-max-blocks.md)
  + [Moving Average](../../../discrete-blocks/moving-average-block.md)
  + [State](../../../discrete-blocks/state-block.md)
  + [Value Accumulator](../../../discrete-blocks/value-accumulator-block.md)
  + [Value Bucket](../../../discrete-blocks/value-bucket-block.md)
  + [Value Extractor](../../../discrete-blocks/value-extractor-block.md)
  + [Value Injector](../../../discrete-blocks/value-injector-block.md)
* Misc blocks

  + [Alert](../../../miscellaneous-blocks/alert-block.md)
  + [Formula](../../../arithmetic-blocks/formula-block.md)
  + [Stopwatch](../../../miscellaneous-blocks/stopwatch-block.md)

←[Previous PostOrder of discrete event message propagation](order-of-discrete-event-message-propagation.md)

[Next PostLinking Excel Data to the Algo Dashboard](linking-excel-data-to-the-algo-dashboard.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-edit-link.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-launch.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-editor-blank.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-show-variables.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-bubble-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-bubble-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-boolean-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-boolean.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-arithmetic-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-arithmetic-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-fillprice.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-bubble-1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-bubble-2-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-conditional-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formula-sample-conditional-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-formlua-editor-continuos-output.png
