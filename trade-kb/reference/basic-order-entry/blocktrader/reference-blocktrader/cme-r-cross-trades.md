---
title: CME R-Cross Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/cme-r-cross-trades/
---

# CME R-Cross Trades

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/cme-r-cross-trades/)

The **Blocktrader** widget supports sending [a combined RFQ and RFC Cross (R-Cross) trade at CME](https://www.cmegroup.com/confluence/display/EPICSANDBOX/RFQ+and+RFC+Cross). The exchange requires that members send a “quote request for cross” (RFQ) message prior to performing a cross trade. Using the Blocktrader widget, you can manually submit an RFQ and then submit the R-Cross trade or submit the trade within a set time interval after the RFQ is submitted.

The quote request for cross message is broadcast to all market participants and is visible in the RFQ Viewer widget on TT. Once the cross trade is executed, you can view the fills and order status in the Order Book, Fills, and Audit Trail widgets.

## Blocktrader display for CME R-Cross Trades

Blocktrader consists of the following fields for submitting R-Cross trades on CME.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-display.png)

The widget includes:

1. **Exchange selector** — Lists the exchanges with trade reporting supported on TT®
2. **Trade type selector** — Lists the trade types supported for the selected exchange.
3. **Profile selector** — Sets the order profile for routing the trade to the exchange.
4. **Account selector** — Sets the account and connection used to route the trade to the exchange.
5. **TIF selector** — Sets the TIF restriction on the order. Select either “Day” or “IOC”.
6. **Price** — Used for entering a price for the transaction. You can also use the up and down arrows to set the price.
7. **Quantity** — Used for entering the buy or sell quantity for the trade. You can also use the up and down arrows to set the quantity.
8. **Deal Time** — Used for setting the time of the transaction.
9. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
10. **RFQ** — Sends a “Request for Quote Response” message for the cross trade to all market participants.

    **Note**: Ensure that you have selected an account for the specific exchange where you’ll be submitting the RFQ. Account selection for RFQs is set up in [Preferences | Accounts](../../../overview/preferences/description-preferences/accounts-preferences.md#rfq).
11. **Auto RFQ** — Sends a “Request for Quote Response” message for the cross trade, then automatically submits the trade after the set time interval is elapsed.

    **Note**: Ensure that you have selected an account for the specific exchange where you’ll be submitting the RFQ. Account selection for RFQs is set up in [Preferences | Accounts](../../../overview/preferences/description-preferences/accounts-preferences.md#rfq).
12. **Instrument picker**: Opens the Market explorer to search for or manually select an exchange, product, and instrument.
13. **Side** — Sets the Buyer or Seller. Click the Buyer or Seller cell to set each side of the trade.
14. **TT Account** — Sets the executing account number as agreed between the broker and clearing member firm. This account will be used for the Buyer or Seller instead of the account selected in the order panel. The accounts listed are assigned to your username in Setup.
15. **Confirm Order** and **Submit** — Allows you to confirm the trade before it’s submitted. The **Submit** button sends the trade to the exchange. Order confirmations are enabled by default.
16. **Message indicator** — Indicates if the trade was successfully sent to the exchange. Also shows if the order needs to be confirmed before submitting.

## Submitting a CME R-Cross Trade on TT

Before submitting a cross trade, consider the following:

* Ensure that wholesale trading is enabled for your account or username in Setup.
* Contact the exchange to ensure that your products are eligible for RFQ.
* If you plan to use **Auto RFQ** in Blocktrader to set your own time interval between RFQ and submitting the order (RFC), contact the exchange or [refer to the exchange rules](https://www.cmegroup.com/rulebook/files/cme-group-Rule-539.pdf) for the correct time interval for your product.

The following is an example of a cross trade configured and submitted in Blocktrader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-overview.png)

To submit a CME R-Cross Trade on TT:

1. Click **Widgets** in the workspace title bar and select **Miscellaneous** | **Blocktrader**.
2. Click the exchange selector in the Blocktrader widget and select “CME”.
3. Click the trade type selector and select “Request for Cross”.
4. Select a contract for each leg of the transaction using the [instrument picker](../task-blocktrader/submitting-trades-in-blocktrader.md#pick).
5. Select an account for routing the transaction to the exchange.
6. Set the **Price** and **Quantity** fields for the transaction.
7. Set the [transaction time](../task-blocktrader/submitting-trades-in-blocktrader.md#deal) for the trade.
8. For instruments that support tick sizes smaller than what is displayed, you can check **Price off tick** to enter an off tick price for the trade.
9. In the **Side** fields, click **Buyer** and **Seller** to determine the sides of the trade.
10. Click **TT Account** and select the executing account number as agreed upon by the broker and clearing member firm.
11. Click **RFQ** or click **Auto RFQ** and set a time interval.

    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-rfq.png)

    **Note**: CME requires you to send an RFQ first, wait for 5 – 30 seconds depending on the product, and than send an RFC.

    **Tip**: The **Elapsed** column in the RFQ Viewer widget shows how long the RFQ has been submitted.

    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-elapsed.png)
12. Click **Submit**.

    **Note**: Blocktrader prompts you to confirm orders by default. Confirm the order and click “Submit”. Uncheck **Confirm order** on the Blocktrader widget to disable order confirmations.

←[Previous PostBlocktrader Display](blocktrader-display.md)

[Next PostGFO-X Block Orders](gfo-x-block-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-overview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-rfq.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-cme-r-cross-elapsed.png
