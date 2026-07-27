---
title: Uploading Routing Rules
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/task-routing-rules/uploading-routing-rules/
---

# Uploading Routing Rules

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/task-routing-rules/uploading-routing-rules/)

You can use the Routing Rules widget to upload one or more custom routing rules into the TT platform.

When uploading routing rules into TT, the .csv file must adhere to the following rules:

* Files must be saved as plain text format.
* The filename must use a .csv file extension.
* Data fields must be comma delimited.
* Spaces after commas (for readability) are allowed.
* The .csv file can contain a maximum of 1000 order rows, as follows:
* Row 1 must be the header fields, as follows:
  * The row must contain columns for all fields used by any of the orders.
  * The header column names must exactly match the field names, including capitalization.
  * The field columns can be arranged in any order, but the data within a column must match the value expected by the column header.
  * Must have all relevant routing rule fields as a column header.

To upload Routing Rules to TT:

1. Click **Edit** at the bottom of the Routing Rules rules panel.  
     
   The widget is now in edit mode and additional buttons are displayed.
2. Click **Import**.  
   The **Upload Routing Rules** dialog appears.

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules.png)

3. Click **Select files** to locate the **.csv** file or drag and drop it into the dialog box.

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules-select-files.png)

4. In the **Routing Rules Import** utility that appears, review the data in the **IMPORT PREVIEW** pane to verify that the imported columns are mapped to Routing Rules columns.  
     
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules-import-preview.png)  
   If a column from the .csv file did not map to a routing rules column, double-click the empty cell in **Imported Columns** to select one.  
     
   **Tip**: You can also drag-and-drop columns from **Unused Columns** to **Imported Columns**.
5. Click **Confirm** in the **Routing Rules Import** utility to add the routing rule.
6. Click **Save Changes**.

←[Previous PostApplying a routing rule in TT](applying-a-routing-rule-in-tt.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules-select-files.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/07/rr-upload-routing-rules-import-preview.png
