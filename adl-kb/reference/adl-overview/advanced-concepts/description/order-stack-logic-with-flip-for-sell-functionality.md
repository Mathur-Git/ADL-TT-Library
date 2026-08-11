---
title: Order Stack Logic with Flip for Sell functionality
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-stack-logic-with-flip-for-sell-functionality/
---

# Order Stack Logic with Flip for Sell functionality

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-stack-logic-with-flip-for-sell-functionality/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry) · [Design Patterns & Recipe Index § Bi-directional algos](../../../../guides/design-patterns.md#bi-directional-algos)

### Building Basic Queue Holder Functionality

Users often need to place several order “up or down the book”
. To achieve this, we will build basic Queue Holder functionality. The following examples show the basic entry-side of the logic for these types of order entry.

#### Example 1: Order Stack with Discrete Order block and Flip 4 Sell Functionality

This example uses the following algo variables:

* BUY Side for order entry
* Set for 2 price ticks below best bid price
* Order Qty of 5 for each order
* Total of 5 Price Increments to be entered “down the book” from the set 2 Offset Price ticks

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-1.jpg)

The following screen shots show how to assemble the logic. This first screen shot sets up the variables.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-2.jpg)

This part creates the original stack of orders. It uses a loop block to set the depth of the stack and takes the Index Number off the Loop Block and adds that to any offset the user designates to figure out the exact price each original order should be placed at. Each of these will be a virtual instance. The DOB references “START PRICE” as the original order, and Order QTY. Also, the DOB is set for Flip for Sell functionality.

To help with the internal referencing of some of the blocks seen below:

* The Green SUM block is counting FILL Qty. The other SUM block is using the number value of 1 to count the levels.
* Original Price Maker….. (offset for Inside Mkt – 1 + Stacking Order Block Loop Block index) \* Tick
* Fixed Stack Depth input references the Stack Depth
* DOB Price input is Start Price…QTY input is Order QTY

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-3.jpg)

This screen shot shows the inside logic of the virtualized “Individual Virtual Order Managers” group block.

To help with the internal referencing of some of the blocks seen below:

* Starting Price input is Limit Price
* Are We Buying input is IsBuy
* Net Decrement Calculation Piece 1 input is Fill QTY

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-4.jpg)

This screenshot shows a larger view of the logic inside the Virtualized Group Block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-5.jpg)

And this screen shot shows the logic responsible for the Order Price Movement.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-6.jpg)

←[Previous PostFlip for Sell Order functionality](flip-for-sell-order-functionality.md)

[Next PostVirtualization](virtualization.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-2.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-3.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-4.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-5.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-order-stack-logic-flip-4-sell-6.jpg
