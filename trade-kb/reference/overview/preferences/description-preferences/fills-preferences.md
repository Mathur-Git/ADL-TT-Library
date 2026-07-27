---
title: Fills Preferences
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/fills-preferences/
---

# Fills Preferences

> Category: **Overview** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/fills-preferences/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-fills.png)

| Preference | Description |
| --- | --- |
| Display Fill Alert widget on new fills | Display a Fill Alerts widget when new fills are received. |
| Desktop notification on full fills | Display notifications of only full fills on the screen on top of all applications, even when the TT application is behind other applications or even minimized. |
| Desktop notification on partial fills | Display notifications of partial fills on the screen on top of all applications, even when the TT application is behind other applications or even minimized. |
| Conflate partial fills (ms) | Partial fills for each order will be independently conflated at the configured millisecond threshold. The partial fill alert will be held until the millisecond threshold expires, or the order is fully filled. If the order is fully filled within the conflation period, no partial fill alert will display. |
| Consider child order full fill as partial fill | This setting indicates how to handle child orders of a TT Order Type that receive partial fills, and only editable when **Desktop Notification on full fills** is ticked. Enabled by default.   When enabled (the box is ticked), **Partial Fill** of a child order is considered as a full fill and fill alert will display (e.g. a 1-lot fill of a 5-lot child order would trigger the alert).   When disabled (the box is unticked), fill alert will only display upon **Full Fill** of a child order. |
| Only notify on fills where I am the CurrentUser | When enabled, you would receive fill notification only if you are the CurrentUser of that order. |

←[Previous PostOptions Preferences](options-preferences.md)

[Next PostAlgos & Autospreader Preferences](algos-autospreader-preferences.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-fills.png
