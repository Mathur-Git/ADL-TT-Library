---
title: Managing shared algos
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/managing-shared-algos/
---

# Managing shared algos

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/managing-shared-algos/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § Sharing](../../../../guides/algo-types.md#sharing)

### Sharing an algo

To share an algo with other users:

1. Open the algo you want to share in ADL.
2. [Deploy](../../adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md) the algo, if the algo is not already deployed.
3. From the **File** menu, select **Share/Unshare**.  
      
    The Sharing settings dialog appears.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-dialog.png)
4. Enter the comma-separated TTID email addresses of the users with whom you want to share the algo.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-emails.png)
5. Click either or both of the following [permissions](../description/algo-sharing.md): 
   * **View in ADL (but not edit)**: Allows the users to open the algo in ADL, but not alter it.**Launch**: Limits the user to running the algo from the Algo Dashboard.  
   **Note:** Selected permissions are applied to all users specified. If you want to assign different permissions to different users, you must share the algo separately for each users-permissions combination.
6. Click **OK**.  
      
   **Note**: If any of the emails are invalid, a message similar to the following is displayed and the permissions are not set for any of the specified email addresses.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-invalid-email.png)

### Revoking permissions for a shared algo

To revoke algo sharing permissions:

1. [Open](../../introduction-to-adl/task-introduction-to-adl/opening-adl.md) the algo you want to share in ADL.
2. From the **File** menu, select **Share/Unshare**.  
      
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-delete-dialog.png)
3. Click ![the X icon](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-sharing-delete.png) for the user whose permission you want to revoke.
4. Click **OK**.

### Changing permissions for a shared algo

To change user permissions for a shared algo:

1. [Open](../../introduction-to-adl/task-introduction-to-adl/opening-adl.md) the algo you want to share in ADL.
2. [Revoke](#revoke) algo sharing for the desired user.
3. [Re-share](#share) the algo with the user, selecting the new permissions.
4. Click **OK**.

### Algo sharing restrictions

TT imposes the following restrictions for shared algos:

* You must know the email address of each user with whom you want to share an algo.
* If the same email address is shared over different companies, whether active or inactive, then this will default to the first company this was set up. You will need to speak with the other company’s administrator to delete the user from within TT Setup before sharing the ADL algo to the same email address under the new company.
* If a user with whom you share an algo requires approval to run algos in Setup, that user will need to [request approval](../../adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md) to run the algo. In this situation, you will need to enable Read permission for that user.

←[Previous PostExporting block outputs](exporting-block-outputs.md)

[Next PostHandling External Events](handling-external-events.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-emails.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-invalid-email.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-algo-sharing-delete-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-sharing-delete.png
