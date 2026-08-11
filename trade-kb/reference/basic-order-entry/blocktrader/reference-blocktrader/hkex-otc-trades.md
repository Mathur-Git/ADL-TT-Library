---
title: HKEx OTC Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/hkex-otc-trades/
---

# HKEx OTC Trades

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/hkex-otc-trades/)

The Blocktrader widget supports entering the following OTC trades on HKEX:

* T1: Internal Trade — Orders where a Buy-side participant and an Ask-side participant are set within the same order. Both sides of the order are then submitted as a cross order.
* T2: Combo (Internal Strategy) — A single order with multiple instrument legs. However, a user-defined strategy is not created at the exchange.
* T4: Interbank 1-Sided Trade — Orders that are only posted to the participant listed as the order’s counterparty. Interbank trades are only executed after the counterparty submits a matching order.

## Blocktrader display for HKEX Interbank 1-Sided and Internal trades

Blocktrader consists of the following components for submitting Interbank 1-Sided and Internal trades on HKEX.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-display.png)

The image shows the following:

1. **Exchange selector** — Lists exchanges with OTC/Wholesale trades supported on TT®
2. **Trade Type selector** — Lists the OTC/Wholesale trade types supported for the selected exchange.
3. **Account selector** — Sets the account used for submitting the trade for both the Buyer and Seller. The account or clearing account “override” in Setup is sent to the exchange API as ex\_client\_s.
4. **Price** — Used for entering a price for the transaction. You can also use the up and down arrows to set the price.
5. **Quantity** — Used for entering the Buy or Sell quantity of the trade. You can also use the up and down arrows to set the quantity.
6. **Price off tick** — When checked, allows you to enter an off tick for instruments that support tick sizes smaller than what is displayed.
7. **Use text for counterparty** — Allows counterpartys to be entered as text instead of selected from the dropdown list defined in Setup.
8. **Instrument search** — Allows you to search for and select the instrument being traded. The best Bid and Ask price are displayed for the selected instrument.

   **NOTE**: Only “Future” and “Option” product types are supported for OTC trades at HKEX. OTC trades submitted for “Spread” and “Strategy” products will be rejected by the exchange.
9. [HKEX OTC fields](#hkex_common) — Allows you to complete the fields required by the exchange. Fields are displayed based on the trade type.
10. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking **Confirm** allows you to check the details of the trade before clicking **Submit**.
11. **Message indicator** — Indicates if the trade was successfully sent to the exchange. Also shows if the order needs to be confirmed before submitting.

## Blocktrader display for HKEX Internal Strategy trades

Blocktrader consists of the following components for submitting Internal Strategy (combination) trades on HKEx.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-internal-strategy-display.png)

The image shows the following:

1. **Exchange selector** — Lists exchanges with OTC/Wholesale trades supported on TT®
2. **Trade Type selector** — Lists the OTC/Wholesale trade types supported for the selected exchange.
3. **Account selector** — Sets the account used for submitting the trade for both the Buyer and Seller. The account is sent to the exchange API as ex\_client\_s.
4. **Price** — Enter the price of a single instrument transaction. You can also use the up and down arrows to set the price.
5. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
6. **Templates** — Allows you to select a strategy template to configure and submit multi-leg strategy
   transactions. Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-save.png) to save your custom strategy as a template.
7. **Leg definition grid and instrument picker** — The instrument picker allows you to search for and select the instrument being traded. The grid allows you to set a price and quantity for each leg. For multi-leg strategies, the grid displays the net sum of the best Bid and Ask prices for each leg. Click “+” to add a leg or X” to remove a leg as needed.

   **NOTE**: Only “Future” and “Option” product types are supported for OTC trades at HKEX. OTC trades submitted for “Spread” and “Strategy” products will be rejected by the exchange.
8. [HKEx OTC fields](#hkex_common) — Allows you to complete the fields required by the exchange. Fields are displayed based on the trade type.
9. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking confirm will allow the user to check the details of the trade before clicking **Submit**.
10. **Message indicator** — Indicates if the trade was successfully sent to the exchange. Also shows if the order needs to be confirmed before submitting.

## Submitting HKEX Interbank 1-Sided and Internal Orders in Blocktrader

Interbank 1-Sided trades are only executed after both traders submit a matching order. The exchange checks the following to match an Interbank Trade:

* Both orders must match the same series, price, and quantity.
* One order must be a “Buy” and the other a “Sell”.
* Each participant must set the other participant as its counterparty.

**Note**: Prior to submitting an OTC trade, you should know the counterparty’s Participant
Code. For Interbank trades, you must verify that the counterparty enters a matching Interbank order.

To submit an HKEX Interbank 1-Sided or Internal Order in Blocktrader:

1. Select **HKEX** from the Exchange selector.
2. Search for and select the instrument being traded.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-explorer.png)

   **Note**: Only “Future” and “Option” product types are supported for OTC trades at HKEX. OTC trades submitted for “Spread” and “Strategy” products will be rejected by the exchange.
3. Select either **Interbank 1-Sided** or **Internal** in the Trade Type selector.
4. Set the price and quantity for the trade.
5. Complete the [common fields for Interbank and Internal trades](#hkex_common).

   **Note**:
   For an Internal trade, populate credentials for both the Buyer and Seller sides of the trade.
6. Click the **Submit** button.

   If **Confirm order** is checked, confirm the order before submitting it to the exchange.

## Submitting HKEX Internal Strategy Trades in Blocktrader

Note: For a list of supported strategies on the exchange, refer to [HKEX Tailor Made Combinations](https://www.hkex.com.hk/Services/Trading/Derivatives/Overview/Trading-Mechanism/Tailor-Made-Combinations?sc_lang=en).

To submit HKEX Internal Strategy Trades in Blocktrader:

1. Select **HKEX** from the Exchange selector.
2. Select **Internal Strategy** in the Trade Type selector.
3. Use the [instrument picker](../task-blocktrader/submitting-trades-in-blocktrader.md) to search for and select an instrument for each leg of the strategy.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-internal-strategy-instruments.png)

   **Note**: Only “Future” and “Option” product types are supported for OTC trades at HKEX. OTC trades submitted for “Spread” and “Strategy” products will be rejected by the exchange.
4. Select a quantity and price for each leg of the strategy.

   Blocktrader shows the net price differential for the legs of the strategy.
5. Complete the [common fields for Internal Strategy trades](#hkex_common).

   **Note**:
   For an Internal trade, populate credentials for both the Buyer and Seller sides of the trade.
6. Click the **Submit** button.

   If **Confirm order** is checked, confirm the order before submitting it to the exchange.

## Common Fields for HKEX Interbank 1-Sided, Internal, and Internal Strategy trades

| Blocktrader Field | Value(s) | Description |
| --- | --- | --- |
|  |  |  |
| --- | --- | --- |
| Side | Buy or Sell | Sets which side of the trade you are entering. |
| Customer Profile | A drop-down list of available Order Profiles. | Administrator-defined “Order Tag Defaults” and user-defined Order Profiles are listed. Order profiles uploaded to your workspace are also shown.  **Note**: The “Customer Information” value in Order Tag Defaults or the **User** | **Order Routing** tab is sent to the exchange in the “customer\_info\_s” API field and appears on the OTC order at the exchange for back office reconciliation.  This is an optional field.  When an order profile is selected, the TT Account field may be populated with the user’s account number. |
| Counterparty | A drop-down list of counterparty participant codes | Sets the counterparty for the trade and is forwarded to the exchange API as part of the *ex\_customer\_s field*.  **Note**: This is a required field for HKEX Interbank 1-Sided trades and Internal trades. |
| TT Account | A drop-down list of accounts assigned to the user | Sets a specific account for the Buyer or Seller. This account will be used for the Buyer or Seller instead of the account selected in the order panel. All accounts assigned to the user are listed in the drop-down menu. The TT Account value is sent to the exchange API as *ex\_client\_s*. This is an optional field. The default value is “none”.  **Note**: The exchange does not allow the \* and % characters to be used as part of the account number. |
| Account Type | A1-A4, G1-G2, M1-M3, P1-P3, U1-U2. | Account types are automatically mapped to HKEX account codes in TT based on the routing account settings. Sent to the exchange in the *ex\_client\_s* field. This field is grayed out in Blocktrader. |
| Open/Close | Open or Close | Sets whether the trade opens or closes a position. |
| Give Up | Carrying Participant Code | Sets the five-digit Carrying Participant Code provided by the securities code committee.  This field is a required field when submitting a Give Up order and is sent to the exchange API as part of the *ex\_customer\_s field*. |
| Text B *(optional)* | Free-form text field   * Max 15 characters * Alpha-numeric and special characters allowed | A user-defined text value, sent to HKEx in the *customer\_info\_s* field of the exchange API. Traders can use **Text B** to [associate legs of a trade to a single strategy](#matching_legs).  **Note:** Blocktrader ‘Text B’ can override the ‘Text B’ values set in **order tag defaults** or **order profiles**. |

### Associating Legs to a Strategy

Traders can use **Text B** to combine the legs of a trade that belong to a single strategy.
This allows a trader to accumulate enough volume to meet the minimum quantities for a block trade.

* **Matching** or **Corresponding** Fields — indicate legs that belong to the same strategy
* **Unmatched Fields** — are not associated with the strategy

Matching works the same way for both **Internal Trades** and **Interbank 1-Sided Trades**.
First, any leg with a ‘Buy’-side tag in the **Text B** field is a candidate for matching with other legs that have the same tag in the ‘Sell’-side.
If they match, the second leg’s ‘Buy’-side must also match the first leg’s ‘Sell’-side.
This correspondence between two legs allows for three successful combinations of **Text B** fields:

* All buy and sell side **Text B** tags are the same
* A tagged buy-side matches a tagged sell-side, the other **Text B** fields are blank
* A tagged buy-side matches a tagged sell-side, the other fields are not blank, but match each other

#### Examples

Below are examples of legs matched using **Text B**.

Both sides match



| Text B: | Buy | Sell |
| --- | --- | --- |
| Leg 1 | ABC &check; | ABC &check; |
| Leg 2 | ABC &check; | ABC &check; |

One sides matches, the other is blank



| Text B: | Buy | Sell |
| --- | --- | --- |
| Leg 1 | ABC &check; |  |
| Leg 2 |  | ABC &check; |

Buy & Sell Correspond



| Text B: | Buy | Sell |
| --- | --- | --- |
| Leg 1 | ABC &check; | 123 &check; |
| Leg 2 | 123 &check; | ABC &check; |

Unmatched, Leg 1 ‘Sell’ does not have a matching ‘Buy’ in any Leg



| Text B: | Buy | Sell |
| --- | --- | --- |
| Leg 1 | ABC | 456 ❌ |
| Leg 2 | ABC &check; | 123 &check; |
| Leg 3 | 123 &check; | ABC &check; |

←[Previous PostEuronext Wholesale Trades](euronext-wholesale-trades.md)

[Next PostICE and ICE_L OTC Trades](ice-and-ice_l-otc-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-internal-strategy-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-save.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-explorer.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-hkex-internal-strategy-instruments.png
