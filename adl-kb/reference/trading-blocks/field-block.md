---
title: Field block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/field-block/
---

# Field block

> Category: **Trading Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/field-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block.png)

The Field block is a trading block that retrieves market data, such as AskQty or Volume, for a connected [Instrument](instrument-block.md) block. You can use these values as inputs to other blocks, such as an [Order](order-block.md) block or a logical block.

The following example gets the Ask and Open prices for the CL Sep17 instrument and feeds their outputs to a Greater Than block to determine whether the market moved up since the opening.

**Example:** **Two Field blocks receive instrument data. Each extracts and outputs their designated price field data.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-example.png)

### Market data fields

The Field block allows you to select which type of market data to monitor.

| Field Name | Description |
| --- | --- |
| Ask Market Quantity | Total quantity of resting Sell Market orders. |
| Ask Order Count | Number of ask orders at the specified market depth including the user’s offers (ask orders at the best ask price if depth is not provided)  **Note:** The Field block will output a zero value if this field is unsupported by the exchange or when the market is empty. TT or the exchange can verify if a particular field is supported. |
| Ask Price | Ask price at the specified index level (best ask price if depth is not specified) |
| Ask Quantity | Ask quantity at the specified market depth including the user’s offers (ask quantity at the best ask price if depth is not specified |
| Bid Market Quantity | Total quantity of resting Buy Market orders. |
| Bid Order Count | Number of bid orders at the specified market depth including the user’s orders (bid orders at the best bid price if depth is not provided)  **Note:** The Instrument Field block will output a zero value if this field is unsupported by the exchange or when the market is empty. TT or the exchange can verify if this field is supported. |
| Bid Price | Bid price at the specified index level (best bid price if depth is not specified) |
| Bid Quantity | Bid quantity at the specified market depth including the user’s bids (bid quantity at the best bid price if depth is not specified) |
| Close Price | Price at market close |
| Direct Ask Price | Ask price at the specified index level, taking into account only the levels where there is at least one non-implied offer (if depth is not specified: lowest ask price where there is a non-implied offer) |
| Direct Ask Quantity | Non-implied ask quantity at the specified market depth (if market depth is not provided: non-implied ask quantity at the lowest ask price where there is at least one non-implied bid) |
| Direct Bid Price | Bid price at the specified index level, taking into account only the levels where there is at least one non-implied bid (if depth is not specified: highest bid price where there is a non-implied bid) |
| Direct Bid Quantity | Non-implied bid quantity at the specified market depth (if market depth is not provided: non-implied bid quantity at the highest bid price where there is at least one non-implied bid) |
| High Price | Highest traded price during the current trading session |
| Implied Ask Quantity | Quantity available at the implied ask price |
| Implied Bid Quantity | Quantity available at the implied bid price |
| Last Trade Price | Last traded price |
| Last Trade Quantity | Either accumulated or the last quantity traded at the last traded price (depending on the user’s Gateway settings) |
| Low Price | Lowest traded price during the current trading session |
| Min Price Increment | Minimum tradable increment for the specified instrument |
| Min Tick Increment | Minimum achievable tick increment for the specified instrument  **Note:** A single instrument could have differing Minimum Price Increment and Minimum Tick Increment. For example, an outright S&P 500 E-mini contract has a Minimum Price Increment of 25 (because it trades in an increment of 25), but it has a Minimum Tick Increment of 5 (because an E-mini spread trades in an increment of 5). |
| Open Price | Price at market open |
| Round Lot Quantity | Size of the quantity multiples valid for trading (e.g. quantities must be a multiple of 5) |
| Settle Price | Settled price from the previous trading session |
| Settle Price Unit | Per unit settlement price. **Note:** B3 exchange only. |
| Volume | Volume traded during the current trading session |
| Working Days to Expiry | Number of weekdays until the contract expires. **Note:** B3 exchange only. |
| Workup Price | Trade price based on the BrokerTec workup matching algorithm |

### Lookup types

Several market data fields will inevitably vary at different depths of the market (e.g., bid quantity). For these fields, you can specify a market depth to retrieve the attribute at that price level. The **LookupType** block setting allows you to choose a method of specifying a market depth for applicable attributes:

* **Best**. The block returns the value at the inside market.
* **Index**. The Field block exposes an additional port, as shown in the following illustration. You can connect a numeric value into this port to specify a price level.

  **Example:** **Index lookup type**

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-index.png)

  **Note:** The **Index** count does not take into account the price levels where the selected attribute is zero. For instance, the following illustration shows the first three index levels of the Bid quantity for the ZB Sep16 contract. In addition, when the provided index is negative or goes beyond the existing market depth, the block will output a zero for quantity-related attributes and a NaN (Not A Number) for price-related attributes

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trading-block-instr-index.png)
* **Price**. When this option is selected, the Field block exposes an additional port, as shown in the illustration below. The user may feed a numeric value into this port to specify an index level. The index level is defined as the number of “ticks” away from the best bid/offer, taking into account only the price levels where the selected attribute is non-zero.

  **Example:** **Price lookup type**

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-price-lookup.png)

### Flip for Sell Order functionality

The **Order Side** variable will appear automatically for any algorithm containing a block with the Flip For Sell Order functionality enabled, and the user must set this variable before launching the algorithm.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-order-side-var.png)

When this functionality is enabled, the following pairs of attributes will alternate depending on the user’s selection of the **Order Side** variable.

* Bid Price / Ask Price
* Bid Qty / Ask Qty
* High / Low
* Direct Bid Qty / Direct Ask Qty
* Bid Orders Qty / Ask Orders Qty
* Direct Bid Price / Direct Ask Price

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Field Name | Market data [field value](#md-fields) to extract |
| Lookup Type | Price level to use for the value  The following [lookup types](#lookup-types) allow you indicate a market depth to use:   * **Best**: Inside market. * **Index**: Number of price levels away from the inside market (max=20). * **Price**: Specific price at which to retrieve the value. When selected, a **price** input port is added to the block.   **Note:** The selected Field Name determines which, if any, of these lookup types are available. |
| Flip for Sell Order | Whether to enable a single algorithm to act either as buy or sell side routine as needed  See [Flip For Sell Order Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information. |

←[Previous PostInstrument block](instrument-block.md)

[Next PostMarket State block](market-state-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trading-block-instr-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-price-lookup.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-field-block-order-side-var.png
