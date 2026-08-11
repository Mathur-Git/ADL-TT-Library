---
title: Alert block
category: miscellaneous-blocks
source: https://library.tradingtechnologies.com/adl/miscellaneous-blocks/alert-block/
---

# Alert block

> Category: **Miscellaneous Blocks** · [Source](https://library.tradingtechnologies.com/adl/miscellaneous-blocks/alert-block/)
>
> **Interpreted in:** [Core Semantics § Termination blocks](../../guides/core-semantics.md#termination-blocks) · [Design Patterns & Recipe Index § Risk](../../guides/design-patterns.md#risk) · [Formula Editor Reference § Blocks that take formulas](../../guides/formula-reference.md#blocks-that-take-formulas) · [Formula Editor Reference § Syntax](../../guides/formula-reference.md#syntax) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

### Alert block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-alert-block.png)

**STILL IN DEVELOPMENT**

The Alert block allows you to add a message to the Audit Trail and play a sound when certain conditions occur.  An alert can be triggered in one of two ways:

* When it receives a TRUE value through its Boolean input port
* When it receives a message through is discrete event message port

**Example:** **The Alert block is configured to play a sound and send a message to the Audit Trail when the [Formula](../arithmetic-blocks/formula-block.md) block sends a TRUE value to the Alert block’s Boolean input port, indicating that the trader’s P&L is withing ten percent of the maximum allowed.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-alert-block-example.png)

When an algorithm is executed from the ADL Designer canvas in client-side simulation, an Alert block will not generate an actual audit trail message. Instead, the Alert block will generate the specified text in the Alert Tab of the Information Panel. However, if Sound is selected as the method of alert, the Alert block will generate the specified sound.

**Note:** Only the user who launched the algo will be able to hear the sound alert configured from the Alert Block. Any users with an account share will not have the ability to hear this sound alert, but only the Audit Trail message will be visible.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formula | Equation used to generate the alert message    You can output text by enclosing the text in quotation marks. You can also use the + operator to combine text strings and algo values, as follows.  If not yet defined, the field displays a **Click to edit formula** link that opens the [Formula Builder](../adl-overview/advanced-concepts/description/formula-editor.md).  **Note:** The **Alert** block does not currently support the IF operator in the **Formula Builder**. |
| Actions | Actions to take when the alert is triggered. You can select any number of the following actions:  * **Sound** to play the specified sound * **Audit Trail** to write the message to the Audit Trail |
| Frequency | (For Boolean alerts only) Number of seconds to wait before firing the same alert again, as long as the Alert block input is TRUE. |
| Color | Background color for the text in the Audit Trail message. |
| Sound | Sound to play then the Alert is triggered. |

←[Previous PostLoop block](loop-block.md)

[Next PostPnl block](pnl-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-alert-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-alert-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-alert-block-message-forumla.png
