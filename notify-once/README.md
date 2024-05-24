# Notify once fragmented text

Auto snoozes subsequent messages from the same sender within a certain time window (e.g. 1 minute).

This feature help you to avoid multiple annoying notifications for people writing fragmented text. In the following example, instead of receiving three notifications you will receive only the first one.

`[10:00:00] hey`

`[10:00:10] how are you?`

`[10:00:20] all good?`

Additionally, you could set the following environment variables:
* **TIME_WINDOW_SECONDS**, time window in seconds (by default, `60`)


Internally the feature is implemented with a kind of throttling mechanism based on **expiringdict** library.

## Closest feature

**Smart Notifications** in *groups* only!

1. Open group
2. *Notifications*, click *Customize*
3. *Smart Notifications*

## References

- [expiringdict](https://github.com/mailgun/expiringdict): dictionary with auto-expiring values for caching purposes.