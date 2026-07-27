---
title: Time and Timers in TT ADL
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl/
---

# Time and Timers in TT ADL

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl/)

### Time and Timers in TT ADL

There are a number of scenarios where TT ADL developers may need to use time and timers in their algos. ADL provides this functionality via several blocks and mechanisms. Some of these are new in TT ADL. The following describes the use case for each.

#### Use Case 1: An algo needs to institute a time delay in the logical path of a discrete event.

The Stopwatch block allows users to set a time delay for a discrete event in milliseconds. The number of milliseconds is specified as an output of the associated Green Canvas so it can vary based on the logical conditions within.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-1.png)

One example where this may be useful is to set a delay between a fill and an additional order entry. In the algo below, the fill message is delayed 10 seconds before the quantity being fed to the Order block is increased.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-2.png)

#### Use Case 2: An algo needs to perform an action on a specific date at a specific time.

The new “AtStartTime” mode in the Generator block allows you to specify a date / time at which to signal a notification. When in the “AtStartTime” mode, you would display both the “UTCDate” and “UTCTime” connectors, which are comprised of “year”, “month”, “day”, “hour”, “minute”, “second”, and “millisecond”. When the specified UTC date and time have been reached, a discrete event will propagate from the output port.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-3.png)

One example where this may be useful is to update the “on/off” input port of an Order block at a specific date and time. In the algo below, the Order block is enabled until July 14, 2017 15:00:00.000 UTC.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-4.png)

#### Use Case 3: An algo needs to perform an action at a specific time every day.

The new “AtStartTime” mode in the Generator block allows you to specify a daily time at which to signal a notification. When in the “AtStartTime” mode, you would display only the “UTCTime” connectors, which is comprised of “hour”, “minute”, “second”, and “millisecond”. When the specified UTC time has been reached, a discrete event will propagate from the output port. Note that this will repeat daily.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-5.png)

One example where this may be useful is to update the “on/off” input port of an Order block at a specific time. In the algo below, the Order block is enabled at 3:00:00.000 UTC.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-6.png)

#### Use Case 4: An algo needs an optionally repeating discrete message notification at a given time interval.

The enhanced “TimeInterval” mode in the Generator block allows you to specify that a discrete message notification be signaled when the specified time interval has passed. When in this mode, input ports for “enabled”, “repeating”, and “periodMs” will be exposed. The “enabled” port allows the timer to be enabled / disabled, and the “repeating” port allows the event to be repeated The “periodMs” port allows the time period to be defined in milliseconds. All of these can be dynamically set.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-7.png)

One example where this may be useful is to update the “price” port of an Order block at specific time intervals. In the algo below, the order is repriced every 500ms to be equal to the bid.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-8.png)

#### Use Case 5: An algo needs to know the date and time at which a given discrete event has occurred.

The new MsgInfo Extractor block allows you to expose the date and time at which an event has occurred. Specifically, you would expose the “year”, “month”, “day”, “hour”, “minute”, “second”, and “millisecond” output ports. These will update every time a discrete event enters the MsgInfo Extractor block. The date / time stamp will represent the point in time that the block receives the message.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-9.png)

One example where this may be useful is to ensure that an Order block is enabled only if the algo is started between specific times. In the algo below, the Order block is enabled only if the algo is started between 10:00:00.000 UTC and 14:00:00.000 UTC.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-10.png)

**Note**: The Clock block available in the X\_TRADER version of ADL is not part of the TT version of ADL. Although you can technically create the same mechanism in TT ADL, TT strongly advises against this as it may result in serious degradation in the performance of your algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-11.png)

So if you need to use time and timers in your algos, TT ADL provides several blocks and mechanisms to facilitate your implementation.

←[Previous PostClip Size Reload Functionality](clip-size-reload-functionality.md)

[Next PostADL and TT Mobile](adl-and-tt-mobile.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-9.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-10.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-time-and-timers-11.png
