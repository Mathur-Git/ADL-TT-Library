---
title: Sounds Preferences
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/sounds-preferences/
---

# Sounds Preferences

> Category: **Overview** · [Source](https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/sounds-preferences/)
>
> **Interpreted in:** [Platform & Workspace § Preferences](../../../../guides/platform-and-workspace.md#preferences)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-sounds.png)

* **Enable Sounds**: Click the checkbox to enable your sound preferences. Uncheck to disable.
* **Only play sounds for my actions**: Click the checkbox to play sounds resulting only from your
  own actions.

### General

| Preference | Description |
| --- | --- |
| Disconnect | Plays a sound alert when the TT Platform connection is lost. |
| Reconnect | Plays a sound alert when the TT Platform connection is restored. |
| Exchange connection down | Plays a sound alert when TT receives notification that an exchange connection goes down. |
| Exchange connection up | Plays a sound alert when TT receives notification that an exchange connection comes back up. |

### Orders

| Preference | Description |
| --- | --- |
| New – manually submitted | Plays a sound alert only when a new manual (not automated) order is entered. |
| New – algo submitted | Plays a sound alert only when a new automated (Algo and Autospreader) order is entered. |
| Reject | Plays a sound alert when an order is rejected. |
| Staged order | Plays a sound alert when a care order is submitted. |
| Pass request | Plays a sound alert when you send an order passing request. |
| Pass reject | Plays a sound alert when you reject an order passing request. |
| Cancel order – manually | Plays a sound alert only when a manual order is canceled. |
| Cancel order – by algo | Plays a sound alert only when an automated (Algo and Autospreader) order is canceled. |
| RFQ received | Plays a sound alert when an RFQ is received. |
| OTC Trade | Plays a sound alert when an OTC trade is submitted. |
| Change | Plays a sound when making order changes from the Order Book using the “Change” button (Cxl/Rpl button does not trigger a sound) or from other widgets (e.g., MD Trader). |
| Staged Change Request | Plays a sound when receiving a care order change request. The sound is played for the user who claimed the order and not the care order originator. |
| Staged Cancel Request | Plays a sound when receiving a care order cancellation request. The sound is played for the user who claimed the order and not the care order originator. |
| Unfilled Hedge Order | Plays a sound alert when a missed hedge on an Autospreader leg order appears in the Hedge Manager widget. |

### Fills

| Preference | Description |
| --- | --- |
| Full Fill Buy | Plays a sound alert when a Buy order is fully filled. |
| Full Fill Sell | Plays a sound alert when a Sell order is fully filled. |
| Partial Fill Buy | Plays a sound alert when a Buy order is partially filled. |
| Partial Fill Sell | Plays a sound alert when a Sell order is partially filled. |
| Conflate partial fills (ms) | Plays whether to hold partial fill sounds per order for a configured time interval in milliseconds. When enabled, partial fill sounds are held until the interval expires or the order is fully filled. If the order is fully filled within the interval, no partial fill sound is played. |
| Consider child order full fill as partial fill | Plays a sound alert when a TT Order Type parent order is partially filled by a fully filled child order. Enabled by default.  When this setting and **Partial Fill Buy/Sell** sounds are enabled, a partial sound plays instead of the full fill sound when the child order is fully filled.  When this setting is enabled and only **Full Fill Buy/Sell** sounds are enabled, then sounds for child order fills will not play. In this instance, only the full fill sound plays when the parent is fully filled. |

### Algos

| Preference | Description |
| --- | --- |
| Failed algo | Plays a sound alert when an algo fails. |

### Custom Sounds

To add and use your own custom sound files:

1. Scroll to the bottom of the sound files and click **Add New** in the **Custom Sounds** section.
2. Click **Choose file** to select a sound file on your device and click **Upload**.

   **Note**: Sound files must be in the MP3 format (file extension .mp3).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-sounds1.png)

   The file is uploaded to your workspace and can be selected in each sound preference (e.g., Orders,
   Fills, etc.). To remove the file, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-delete.png).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-sounds2.png)

←[Previous PostAlgos & Autospreader Preferences](algos-autospreader-preferences.md)

[Next PostHotkeys Preferences](hotkeys-preferences.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-sounds.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-sounds1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-delete.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-sounds2.png
