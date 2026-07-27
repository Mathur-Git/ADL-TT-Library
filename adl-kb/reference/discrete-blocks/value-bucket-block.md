---
title: Value Bucket block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/value-bucket-block/
---

# Value Bucket block

> Category: **Discrete Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/value-bucket-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block.png)

The Value Bucket Block can be used to store multiple pairs of numeric values which can be retrieved as needed. Each
pair consists of a KEY which the user can use to locate a specific pair, and a VALUE which is the actual numeric value
of interest to the user. When triggered by an input discrete event message, the Value Bucket block evaluates its
formula for KEY to define the key portion of the entry and uses its formula for VALUE to determine the associated
value. The Value Bucket Keys must be unique. If a message would cause an entry to use an existing key, the block’s [Mode property](#mode-property) can resolve the conflict in one of three ways:

* Adding the value to the key’s existing entry.
* Replace the existing value with the average of the new value and existing values.
* Replace the existing value with the new value.

The Value Bucket block operates in the following manner:

1. A discrete event message received through the **store** port triggers the Value Bucket block.
2. When triggered, the Value Bucket block adds to its internal hash table (see: [Internal
   data collection](#data-collection) for more information about hash tables) a new entry consisting of a KEY and a VALUE.
3. After the addition of the new entry, the Value Bucket block will look at the input message, and search through
   its internal hash table to locate the entry whose key value matches the input **lookup** port.
4. Once it finds the correct entry, it outputs the entry’s value through the **val** output port.
5. Afterwards, it passes on the original message unchanged through its **out** port.
6. Optionally, you can also set up the Value Bucket block to empty its internal hash table and reset its value to a
   NaN (Not A Number) when a discrete event message triggers the **reset** port.

**Example:** **When the Value Bucket block is triggered by a discrete event
message from the MsgInfo Extractor block, it uses its internal formulas to use trade price as the KEY and the
quantity traded as the VALUE and adds these as a new entry in the Value Bucket block. It also receives the
**tradePrice** through its **lookup** port which the Value Bucket block will use to find
the entry with the KEY of **tradePrice**. The VALUE for this entry is output it through its
**val** port. It also passes the original discrete event message through its **out** port
to downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-intro-example.png)

**Example:** **This example uses the Value Bucket block to store price and
quantity every time a trade occurs. When a trade occurs, it also outputs the corresponding quantity from its
internal collection for every transaction with a trade price lower than the open price. The output is used in
downstream logic to respond when it crosses a threshold. The Value Bucket block also outputs the incoming message
for every trade to be handled by some downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-example.png)

The Value Bucket block uses its **Fields Formula Editor** to specify the tradePrice and tradeQuantity
values for its **storeKey** and **storeVal** fields, respectively.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-formula.png)

### Internal data collection

The Value Bucket block’s internal hash table can be conceptualized as a simple table with two columns: KEY and VALUE.
In the following example, suppose that the Value Bucket block is triggered by a discrete event message every time a
trade occurs in a given instrument. When triggered, the Value Bucket will extract and use the Trade Price as the KEY;
and the Trade Quantity as the VALUE of each new entry. A user might create such table to maintain and use the running
volume at different prices during a trading session.

1. Suppose that the Value Bucket block already has three entries in its internal hash table, as shown in the
   following illustration.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table1.png)
2. Suppose that a new trade occurs at Price 1290 25, for a Quantity of 3. A discrete event message containing this
   information will trigger the Value Bucket block. When triggered, the block will extract and add a new entry to its
   internal hash table using the Trade price and the Trade Quantity.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table2.png)
3. Suppose that the user specifies the **#bars** input as 1289 50. The block will search through its
   internal hash table to locate the entry whose KEY value matches the input **#bars** value.
   Afterwards, it will output the VALUE of the corresponding entry as 7.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table3.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Mode | Occasionally, two entries in the hash table will end up with the same KEYs. In this case, the Value Bucket will resolve the conflict through one of the three methods chosen by the user:   * Sum: Sum the values of the two conflicting entries and consolidate them into a single entry * Average: Take the average of the values of the two conflicting entries and consolidate them into a single   entry * Last: Retain the recent entry and discard the older one |
| Formulas | Equations used to calculate the value of the entry’s key and value pair  The **edit** link opens the [Fields Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostValue Extractor block](value-extractor-block.md)

[Next PostGenerator block](generator-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-intro-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-formula.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-bucket-block-table3.png
