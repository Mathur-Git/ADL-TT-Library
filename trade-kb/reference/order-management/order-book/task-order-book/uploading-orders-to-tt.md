---
title: Uploading orders to TT
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/uploading-orders-to-tt/
---

# Uploading orders to TT

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/uploading-orders-to-tt/)

You can use the Order Upload feature to submit orders into the TT platform using a comma-separated
(**.csv**) file.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-intro.png)

## Prerequisites

Before uploading orders, the .csv files must be properly formatted. The [Order
upload .csv file format](../reference-order-book/order-upload-csv-file-format.md) help describes the format of the order upload file and the supported order
parameters.

Additionally, you must be authorized in Setup to trade with all accounts provided in the upload file.

Note For Order Uploads, TT supports native order types and all TT Order Types, including Order Management Algos (OMAs), Order Ticket Algos (OTAs), and ADL algos with all parameters. TT Premium Order Types and Bank algos are supported with all parameters as well.

## Uploading an orders file

To upload orders from a orders **.csv** file:

1. In the Order Book, select **Upload orders** from the context menu.The **Upload Orders** dialog appears.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-dialog.png)
2. In the **Upload Orders** dialog, either **Select files** to locate the desired
   **.csv** files or drag them to the dialog; then click **Close**.The **Order Book Import** Column Mapper appears. It shows the columns that could be automatically
   mapped from your input file, along with columns that either could not be mapped automatically or have no values
   for one or more of the orders.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-col-mapper-dialog.png)
3. Map the **Unused Columns** to their corresponding **Import Load Columns** either by
   dragging an unused column to its corresponding import column or by clicking or by clicking a blank column and
   selecting the desired column from the drop-down list.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-col-mapper.png)

   The **IMPORT PREVIEW** panel presents a preview of the information for the orders defined in the
   uploaded **.csv** files. The panel displays only the first ten orders; all of the orders are
   imported, however.
4. When you have finished mapping the columns, click **Confirm**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-grid.png)

   **Note**: You do not have to map all columns. Data for unmapped columns will be ignored during the
   import.

## Submitting uploaded orders

To submit the uploaded orders:

1. For each order, verify the order parameters.
2. If you need to update an order parameter, such as changing a price that is no longer valid or changing the order
   TIF, you can click in the field and change the value.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-modify.png)
3. Select one or more orders and click the following buttons as needed:
   * **Submit to Exchange** — Sends the selected order(s) directly to the exchange.
   * **Submit as Held** — Submits orders into the TT system as “held” orders that can be
     sent to the exchange.**Note**: TT Order Type orders (i.e. TT Stop, TT Iceberg, etc.) cannot be submitted as held
     orders.
   * **Stage** — Submits the selected orders as staged orders that can be claimed and managed in the
     Order Book.After the orders are submitted, they are deactivated in the Order Upload preview widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-submit-error.png)

   To give you visual cues for orders successfully submitted:
   * The row text is changed to italics.
   * The checkbox is removed.
   * A yellow gear icon is displayed in the row for orders submitted as Held; a green check mark is displayed
     for orders that were successfully submitted to the exchange.If an error occurs when submitting an order, a red triangle indicates the order needs correction.

## Correcting errors in uploaded orders

If the uploaded file contains errors, such as missing or invalid values, the corresponding order rows are disabled
and problematic order parameter values are highlighted.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-intro.png)

1. Error indicator icon
2. Order parameters that need correction

To correct errors:

1. Hover over the error icon to display the errors related to an order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-message.png)
2. In each of the highlighted fields for the order, click in the cell and correct the value.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-correction.png)

   **Note**: When you correct all errors for an order, the error icon is removed and the checkbox is
   enabled so you can submit the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-fixed.png)
3. When the errors are corrected, submit the orders by clicking **Submit as Held** or **Submit
   to Exchange**.

### A special note about the Contract field

In row 8 of the previous example, the **Contract** field for the order (**ZB Dec18**)
is highlighted as an error with error message “Contract: Missing instrument data”, even though the contract name
looks correct. This error commonly occurs when using the wrong contract name. In this case, the .csv file contained
the following entry for the last order.

```
S, 10, CME, ZB Dec18, 151'14, Day, Limit, , , 12345,,
```

As described in the [Order upload .csv file format](../reference-order-book/order-upload-csv-file-format.md) help, all contracts must be
specified using the exhange-provided “short” contract name, which is listed in the Instrument Data dialog
(**Type Shift-Ctrl-X** in MD Trader or Market Grid row).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-instr-data.png)

Because the order entry in the .csv file identified the contract by specifying “ZB Dec18” instead of “ZBZ8”, the
upload identified the contract name as an error.

←[Previous PostInquiring and accepting EEX and Eurex block trades](inquiring-and-accepting-eex-and-eurex-block-trades.md)

[Next PostReviewing and approving orders](reviewing-and-approving-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-col-mapper-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-col-mapper.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-grid.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-modify.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-submit-error.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-message.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-correction.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-error-fixed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-upload-orders-instr-data.png
