# Notify only once for multiple messages

(event.sender_id??)

cache with items expiring after x sec
whenever a message comes you check if the sender_id is already in the cache
-> if yes, update the timestamp to now -> DO NOT NOTIFY (mark it as read?)
-> if no, add it with timestamp -> NOTIFY (do nothing?)