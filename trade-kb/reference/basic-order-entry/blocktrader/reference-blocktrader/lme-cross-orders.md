---
title: LME Cross Orders
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/lme-cross-orders/
---

# LME Cross Orders

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/lme-cross-orders/)

The TT® platform supports LME Cross orders using the TT Blocktrader widget. You can submit the following orders on LME:

* Cross

## Blocktrader display for LME

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/05/blk-lme-display-17.png)

The components are:

1. **Exchange** — Lists the exchanges with OTC trade reporting supported on TT.
2. **Trade Type** — Lists the OTC trade types supported for the selected exchange. Currently for LME, this can only be “Cross”.
3. **Price** — Sets the price for the Cross trade. You can also use the up and down arrows to set the price.
4. **Quantity** — The total trade quantity.
5. **Deal Time** — The exact time for the deal.
6. **Instrument** — Allows you to search for and select the instrument being traded. For LME, this can be a futures instrument or a spread instrument defined by the exchange.
7. [LME block trade fields](#common-lme-blocktrader-trade-fields) — Allows you to complete the fields required by the exchange.
8. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking **Confirm** will allow the user to check the details of the trade before clicking **Submit**.

## Common LME Blocktrader Trade Fields

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/05/blk-lme-trade-fields-16.png)

The following list shows the Blocktrader fields that are common when submitting block orders on LME.

1. **Side** — Sets the Buyer or Seller. Select “Buyer” or “Seller” to set each side of the trade. The side chosen on the left hand side should be the prioritized side of the order.
2. **Customer Profile** — A drop-down list of available order profiles. This is an optional field. Only customers with order profiles defined in Setup appear in the **Customer Profile** list.
3. **TT Account** — Sets an optional account for the Buyer or Seller. This account will be used for the Buyer or Seller instead of the one set in the **Account** drop-down. All accounts assigned to the user are listed in the drop-down menu.   
     
   **Note:** The exchange does not allow the \* and % characters to be used as part of the account number.
4. **Text A** — Any text that a user intends to send to the exchange can be added here.
5. **Text TT** — Free text field.  
     
   **Note**: This field is meant for TT internal purposes only and is not sent to LME.
6. **Guaranteed** **Cross**
   * If the flag is checked, the trade will be filled at the cross price or can get an improvement from liquidity on LMEselect. If the market moves away during the crossing period, the trade will still be filled at the cross price.
   * If the flag is not checked, it will be Un-Guaranteed cross – the trade will be at the cross price or can get an improvement from liquidity on LMEselect. If the market moves away during the crossing period, the trade will be rejected.

## Submitting Cross Orders on LME

Before submitting a trade, the user should have access to submit Block orders. Refer to [User Account Permissions](https://library.tradingtechnologies.com/setup/company-administration/users/description-users/user-account-permissions/) for more information.

1. Open the **Blocktrader** widget and select “LME\_NTP” from the **Exchange** drop-down.
2. Select the trade type from the **Trade Type** drop-down.

   * Cross
3. Use the **Instrument** drop-down at the top of the widget to select the instrument.
4. Under the **Trade Type** drop-down, set the **Quantity** and **Price** for the trade.
5. Set the [LME block trade fields](#common-lme-blocktrader-trade-fields) in the center of the widget:

   * Determine if the Buy side should be prioritized or the Sell Side. The prioritized side should be on the left side.
   * Select the **Customer Profile** for both sides. If no profile is selected, the default profile is used.
   * Select the **TT Account** for both sides for executing the trade.
   * Enter the values as needed by trader on **Text A**.
   * Enter the values as needed by trader on **Text TT**.
   * If the trader wants a guaranteed trade, they should select the checkbox for **Guaranteed**.  
       
     **Note**: This field is meant for TT internal purposes only and is not sent to LME.
6. Click **Confirm**.
7. Review your selections for accuracy.
8. Click **Submit**.

## LME – TT Audit Trail Field Mappings

xml encoding="utf-8" ?

| **LME Cross Order Parameter** | **TT Audit Trail Column Name** | **Notes** |
| --- | --- | --- |
| CrossID | ExchExecID | Unique ID for each LME Cross Order |
| OrigCrossID | ExchExecID | For RFC Cancellation messages |
| CrossType | Type | “Guaranteed” or “Non-Guaranteed” |
| CrossPrioritisation | Text C | “Buy\_Side\_Prioritised” or “Sell\_side\_prioritised” |
| VenueType | Text B | “Onbook” or “Off Book “ |
| Aggressor Indicator | P/A | “P” for Passive or “A” for “Aggressive” |

←[Previous PostJPX J-Net Trades](jpx-j-net-trades.md)

[Next PostMEFF Cross Trades](meff-cross-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2026/05/blk-lme-display-17.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/05/blk-lme-trade-fields-16.png
