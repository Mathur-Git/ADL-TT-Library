---
title: Keyboard trading in MD Trader
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/description-md-trader/keyboard-trading-in-md-trader/
---

# Keyboard trading in MD Trader

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/description-md-trader/keyboard-trading-in-md-trader/)

In addition to click-trading in MD Trader using a mouse, you can use the keyboard to make trades. Enabling
keyboard trading provides an alternative method for submitting orders and does not disable the mouse.

**Note**: The [hotkeys](../../../overview/preferences/description-preferences/hotkeys-preferences.md) functionality must be enabled in your workspace in order to use keyboard trading in MD Trader.

You can enable or disable keyboard trading for each MD Trader widget using the local settings: right-click in MD Trader, select **Settings: MD Trader**, check the **Keyboard trading** checkbox and click **Save**. You can enable keyboard trading for all MD Traders in your workspace or for all future MD Traders by using the **Defaults** page in the local settings.

When enabled, yellow (buy side) and
green (sell side) boxes appear as markers in the **Bids** and **Asks** columns.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-on.png)

When you hover on a marker, the cursor displays “Buy” or “Sell” based on which side of the market you’re on.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-cursor.png)

As you move the cursor to different **Bid** and **Ask** cells, the cursor displays a dotted line around each cell to indicate where the marker can be placed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-move.png)

If you hold down the **Ctrl** key, left clicks on **Bid** and **Ask** cells away from the markers do not submit orders, but instead move the buy/sell marker to that price level. An order is submitted at that price level by pressing the assigned hotkey to buy or sell, or by clicking again in the same cell.

**Note**: Mouse click actions to cancel orders in MD Trader are still executed while in keyboard trading mode.

## MD Trader keyboard commands

With focus on MD Trader, you can press hotkeys on your keyboard to execute trading commands.

**Note**: MD Trader keyboard hotkeys are the only TT Hotkey functions that can be assigned with single alpha keys. Each alpha key is shown in upper case to match the keyboard, but commands must be entered in lower case.

Refer to the following table to submit trading commands using the keyboard.

| **Action** | **Hotkey** |
| --- | --- |
| Increase buy side marker | **D** |
| Center buy side marker | **E** |
| Decrease buy side marker | **C** |
| Buy at buy side marker | **A** |
| Delete buy orders at buy side marker | **S** |
| Sweep buy up to buy side marker | **Ctrl+A** |
| Increase sell side marker | **K** |
| Center sell side marker | **I** |
| Decrease sell side marker | **M** |
| Sell at sell side marker | **;** |
| Sweep sell down to sell side marker | **Ctrl+;** |
| Center both buy/sell markers and the price ladder | **Ctrl+Space** |

←[Previous PostOrder Types](order-types-2.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-on.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-cursor.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-keyboard-move.png
