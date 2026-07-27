---
title: TFEX OTC Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/tfex-otc-trades/
---

# TFEX OTC Trades

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/tfex-otc-trades/)

The TT® platform supports [TFEX OTC Trades](https://www.tfex.co.th/tfex/index.html).
Using the Blocktrader widget, you can submit One Sided Orders. One Sided Orders are orders posted from one participant to another who is listed as the counterparty.
Once the counterparty submits a matching half to a *Buy* or *Sell* order the trade is reported.

### Blocktrader display for TFEX

The Blocktrader widget consists of the following components for submitting OTC trades on TFEX.

![Annotated TFEX Blocktrader Widget](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-contract-displayed.png "One sided trade fields")

The components are:

1. **Exchange Selector** –
   Lists all exchanges with OTC trade reporting supported on TT.
2. **Trade Type Selector** –
   Lists OTC trade type supported for the exchange: One Sided.
3. **Price** – maps to Tag 7 (`Price`)

Sets the price for **One-Sided** trades.
A price may be keyed-in or adjusted using the arrows.

1. **Quantity** – maps to TFEX Tag 6 (`orderQty`)

The total trade quantity

1. **Price off tick** —
   When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller
   than what is
   displayed.
2. **Import** –
   Allows the user to upload a CSV file containing multiple block trades.
   See the section on [uploading `.csv` files](#upload).
3. **Instrument Picker** – maps to TFEX Tag 5 (`OrderbookId`)

Allows you to search for an instrument and select it for trading.

1. [**TFEX Trade Fields**](#tfex-trade-fields) –
   Allows you to modify fields required by the exchange.
   Fields are displayed base on the selected trade type.
2. **Confirm Order and Submit** –
   Submits the order with the selected options.

When **Confirm Order** is checked, two clicks are required for submission.

* The first **Confirm** click locks in the options for the trader to review.
* The second **Submit** click sends the order.

### TFEX Trade Fields

![TFEX Trade Fields](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-fields.png "TFEX Trade Fields")

1. **Side** –
   Sets the *Buyer* or *Seller*.
2. **Customer Profile** *(optional)* –
   A drop-down list of available **Order Profiles** as defined in **Setup** under the
   **Customer Profile** list.
3. **Counterparty** – maps to TFEX Tag 11 (`counterpartyMember`).
   A drop-down list of counterparty participant codes as defined in **Setup**.
4. **TT Account** –
   Sets the account for executing the trade.
   The accounts assigned to the user, as a *Buyer* or *Seller*, are listed in the dropdown.
5. **Owner Type** *(default `<none>`)* – maps to Tag 18
   (`ownerType`).
   By default, **Owner Type** sends the **Order Tag Defaults** to the exchange as
   defined in **User Setup**. To
   override the default, an alternate value may be selected from the dropdown:

   * **Customer**
   * **Institution**
   * **Principal**
   * **Foreign**

1. **Member** – maps to TFEX Tag 9 (`member`).
   By default, **Member** sends the **Order Tag Defaults** to the exchange, as
   defined in **User Setup**. To override
   the default, an alternate value may entered into the text box.
2. **Open/Close** *(optional)* – maps to TFEX Tag 510 (`ownOpenClose`).
3. **Text C** *(optional)* – maps to TFEX Tag 20 (`ownInfoText`).
   By default, **Text C** sends the **Order Tag Defaults** to the exchange as defined
   in **User Setup**. To override
   the default, an alternate value may entered into the text box.
4. **Text TT** *(optional)* –
   Adds a note that is **not** sent to the exchange but remains in on the order in the TT System.
   By default, **Text TT** sends the **Order Tag Defaults** to the exchange as
   defined in **User Setup**. To override
   the default, an alternate value may entered into the text box.

## Submitting Trades on TFEX

To submit a trade on TFEX:

1. Open the **Blocktrader** widget and select TFEX from the [**Exchange
   Selector**](#display).
2. Select the trade type from the [**Trade Type Selector**](#display).
3. **One Sided**
4. Use the [**Instrument Picker**](#display) at the top of the widget to select the
   instrument.
5. Back under the **Trade Type Selector**, set the [**Quantity**](#display)
   and [**Price**](#display) for the trade.
6. Set the [**TFEX Trade Fields**](#display) in the center of the widget:
7. Select the **Customer Profile**.

If no profile is selected, the default profile is used.

* Select the **Counterparty**.

Other members of the exchange are listed in the dropdown.

* Select the **TT Account** for executing the trade.
* Type in the name of your firm that is a member of the Exchange.
* Select the **Owner Type** for transaction:
* **Customer**
* **Institution**
* **Principal**
* **Foreign**
* Indicate if this transaction is **Opening** or **Closing** the position.
* Make any notes regarding the transaction in **Text C** or **Text TT**.

1. The fields will be locked for review.

Click **Confirm**.

1. Review your selections for accuracy.

Click **Submit**.

## Matching One Sided Trades

Trades with two brokers are reported once both parties submit matching halves of an order, both *Buy* and
*Sell*, to
the exchange.
*Buy* and *Sell* requests can be submitted in any order.
The counterparty confirms the transaction by submitting the second half of the trade.

Matching trades must meet the following requirements:

* Both sides of the trade are set, both *Buy* and *Sell*.
* Each participant lists the other as the counterparty.
* Counterparty order details must match the first order by:
* **Trade Type**
* **Instrument**
* **Price**
* **Quantity**

## Importing Trades *(CSV Upload)*

Trades can be imported into Blocktrader by uploading CSV to TT.
This allows a trader to create order information in applications *outside* of TT.
The external application will produce a comma separated file.

![CSV Import File](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-csv-file.png "Sample CSV File")

**Note:**
A **C**omma **S**eparated **F**ile *(`.csv`)* is a simple
text-based format for tabular data.
It is **not** an Excel file *(`.xlsx`)*.

1. Go to the **Blocktrader** widget and set to **TFEX** as the exchange.

In the bottom left of the widget click the *Import* button.
A dialog box will appear.

1. Stage the `.csv` file for upload.

In the **Upload Orders** dialog, either:

* Use the **File Browser** to navigate to the file
  ![Upload dialog](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-upload-dialog.png "Upload dialog")

or:

* **Drag and drop** the file onto the dialog box.
  ![Upload drag](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-upload-drag.png "Upload drag")

The **Block Trader Import** widget will appear.
The widget displays the **Blocktrader columns** next to the **Imported Columns**.
![TFEX Import Mapping](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-import-mapping.png "Import Mapping")

**Note:**
When uploading a `.csv` file for the first time, you will need to map the columns to the TT fields.
Mapping can be done using the **dropdown** or by **drag and drop**.
Mappings are retained for future uploads as long as the file format remains the same.

1. Preview the order details.

Click **Confirm** to preview order details.
Each row contains one order.

1. Review and verify the order information.
   ![TFEX Order Upload](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-order-upload.png "Order Upload")

Imported orders are validated.
If a field cannot be successfully validated, the rows will be disabled in the preview.
Problematic cells are highlighted with a red border.
Orders can be corrected or adjusted in the preview.

1. Submit the report to the exchange.

Click **Submit to Exchange**.

←[Previous PostSGX Trades](sgx-trades.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-contract-displayed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-fields.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-csv-file.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-upload-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-upload-drag.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-import-mapping.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-tfex-order-upload.png
