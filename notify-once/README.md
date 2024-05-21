# Notify once fragmented text

Auto snoozes subsequent messages from the same sender within a certain time window (e.g. 1 minute).

TBD

The general idea is to use a generic throttle mechanism.
Memory cache with items expiring after x sec
whenever a message comes you check if the sender_id is already in the cache
-> if yes, update the timestamp to now -> DO NOT NOTIFY (mark it as read?)
-> if no, add it with timestamp -> NOTIFY (do nothing?)

## Closest feature

**Smart Notifications** in *groups* only!

1. Open group
2. *Notifications*, click *Customize*
3. *Smart Notifications*

## References

- [expiringdict](https://github.com/mailgun/expiringdict): dictionary with auto-expiring values for caching purposes.