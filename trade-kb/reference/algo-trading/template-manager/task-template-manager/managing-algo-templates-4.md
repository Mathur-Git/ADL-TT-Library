---
title: Managing algo templates
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/template-manager/task-template-manager/managing-algo-templates-4/
---

# Managing algo templates

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/template-manager/task-template-manager/managing-algo-templates-4/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Templates](../../../../guides/algo-ops.md#templates)

Using the Template Manager, you can easily create and manage templates that provide customized, preset values for an
algo. You can then launch these algos with their predefined values, or you can associate a template with a [custom action button](../../../basic-order-entry/md-trader/task-md-trader/configuring-md-trader.md) in MD Trader.

The Template Manager lets you:

* [Add](#add-template) templates for algos to create sets of algos with different preset values
* [Clone](#clone-template) existing templates
* [Set a default](#default-template) template for an algo.
* [Delete](#delete-template) templates

## Adding algo templates

You can add templates for one or more algos. A new template begins with the default parameter values configured for
each algo.

To add a template for an algo:

1. Select an algo name from the **Algo Explorer** pane.The default parameter values for the algo are displayed in the **Algo Parameters** pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-1.png)
2. Click ![the +Add Template button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-button.png).A new template is added beneath the selected algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-2.png)
3. Select the new algo template in the **Algo Explorer** pane.The template parameters are displayed in the **Algo Parameters** pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-3.png)
4. Change the algo parameter values as desired.If you want to change the name of the template, click **(edit)** by the algo name. Then enter a new
   name in the dialog and click **Save**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-4.png)
5. Click ![the Save template button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-save-template-button.png) to save the template.By default, the **Instance Name** matches the template name. If desired, you can also change it to
   a different value.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-5.png)

Note: You can also select multiple algos and create new templates for each them, all at once.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-multi-templates-2.png)

## Cloning algo templates

In addition to creating new templates for algos, you can also clone existing templates to create multiple sets of
preset values for an algo.

To clone algo templates:

1. Select one or more algo templates in the **Algo Explorer** pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone-template-1.png)
2. Click ![the Clone button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone2-button.png).Note that the button reflects the number of templates selected.A new copy of each of the selected templates is created beneath its original.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone-template-2.png)
3. Select and modify the cloned templates as desired.

## Setting a default algo template

A default algo template indicates which set of preset values to display when selecting an algo to launch, such as in
[Algo Dashboard](../../algo-dashboard/task-algo-dashboard/launching-an-algo-from-the-algo-dashboard.md). When you create
multiple templates for an algo, you must select a default template to use whenever you select an algo. The default
template is identified with a star (![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-yellow-star-1.png)), as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-intro.png)

To set a default template for an algo:

1. Hover the cursor over a template to display a clickable star.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-1.png)
2. Click the star to set the template as the default for the algo.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-2.png)

## Deleting algo templates

To delete algo templates:

1. Select one or more algo templates in the **Algo Explorer** pane.
2. Click ![the Delete button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-delete-button.png).Note that the button reflects the number of templates selected.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-save-template-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-template-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-add-multi-templates-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone-template-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone2-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-clone-template-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-yellow-star-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-default-template-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tm-delete-button.png
