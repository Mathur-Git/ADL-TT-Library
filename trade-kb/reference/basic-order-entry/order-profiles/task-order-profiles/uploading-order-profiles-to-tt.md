---
title: Uploading Order Profiles to TT
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/task-order-profiles/uploading-order-profiles-to-tt/
---

# Uploading Order Profiles to TT

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/task-order-profiles/uploading-order-profiles-to-tt/)

As a company administrator, you can use the Order Profiles widget to upload one or more custom order profiles into the TT platform. Uploaded profiles are environment specific, so you can upload and use different profiles in the Simulation and Live environments. For example, profiles verified in Simulation can then be uploaded to Live.

**Note**: Before uploading, ensure that the order profiles are in the [CSV file format](../../../viewing-market-data/depth/reference-depth/depth-reference.md#upload) and are properly formatted.

**Tip**: To upload order profiles as rules under existing Setup profiles created by an administrator, the profile names must match exactly, including case sensitivity.

To upload order profiles to TT:

1. Click **Edit** at the bottom of the Order Profiles rules panel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit.png)

   The widget is now in edit mode and additional buttons are displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit-buttons.png)
2. Click **Import**.

   The **Upload Order Profiles** dialog appears.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-upload-dialog.png)
3. Click **Select files** to locate the **.csv** file or drag and drop it into the dialog box.
4. In the **Order Profile Import** utility that appears, review the data in the **IMPORT PREVIEW** pane to verify that the imported columns are mapped to Order Profiles columns.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-preview.png)

   If a column from the .csv file did not map to an Order Profile column, double-click the empty cell in **Imported Columns** to select one.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-map-edit.png)

   **Tip**: You can also drag-and-drop columns from **Unused Columns** to **Imported Columns**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-map-edit2.png)
5. Click **Confirm** in the **Order Profile Import** utility to add the profile.
6. Optionally, rename the profile by double-clicking it in the **Profile pane** and entering a name.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-name1.png)

   **Tip**: To allow specific profiles to be visible to users, you can click the “eyeball” button (![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-5.png)) for each profile that you want to display in the profile list.
7. Click **Save Changes**.
8. Click **Publish**.

   The new profile is broadcast to all users in your company. Published profiles are stored locally on each user’s machine and are loaded upon login. If they are currently logged in, users will see the new profiles and rules in their open Order Profiles widgets.

   Uploaded profiles and rules are shaded green in Order Profiles.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-shaded.png)

   For more details about viewing uploaded profiles, refer to [Viewing uploaded order profiles](#view).

## Viewing uploaded order profiles

When a file is uploaded, saved, and published by an administrator, consider the following:

* All users and administrators in the same company and environment have the ability to see all profiles
* Profiles where the “User” field is blank are hidden.
* If the “User” field is populated, that user will automatically see that profile by default.
* A user can view “hidden” profiles by clicking the “eyeball” button in the Profiles panel while in edit mode.

To view uploaded order profiles:

1. Click the **Edit** button in the lower right corner of Order Profiles.
2. On the Profiles panel, click the gray “eyeball” button (![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-6.png)) in the upper left corner to select and enable all uploaded profiles.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-view.png)
3. Click **Save Changes**.

   All uploaded profiles are displayed.

←[Previous PostSoft Limits](soft-limits.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit-buttons.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-upload-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-preview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-map-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-map-edit2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-name1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-shaded.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profile-view.png
