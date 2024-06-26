import logging
import os
import time
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaDocument
from expiringdict import ExpiringDict

EXTRA_NAME = 'telegram-extras-notify-once'
EXTRA_VAR_TG_API_ID = 'TG_API_ID'
EXTRA_VAR_TG_API_HASH = 'TG_API_HASH'
EXTRA_VAR_TIME_WINDOW = 'TIME_WINDOW_SECONDS'

# basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(EXTRA_NAME)

# expiring dictionary
time_window = os.environ.get(EXTRA_VAR_TIME_WINDOW, 60)
cache = ExpiringDict(max_len=100, max_age_seconds=time_window)
logger.info(f'Cache for {time_window} seconds initiated.')

# telegram client
api_id = os.environ[EXTRA_VAR_TG_API_ID]
api_hash = os.environ[EXTRA_VAR_TG_API_HASH]
client = TelegramClient(EXTRA_NAME, api_id, api_hash)
logger.info('Telegram client created.')

def main():

    # connecting telegram
    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        
        msgs = cache.get(event.sender_id)
        if msgs is None:
            cache[event.sender_id] = 1
            logger.debug(f'First message in the interval by ID {event.sender_id}.')
        else:
            await event.message.mark_read();
            cache[event.sender_id] = msgs + 1
            logger.debug(f'Message snoozed by ID {event.sender_id} because is the occurrence no. {msgs}.')

    
    client.run_until_disconnected()


if __name__ == '__main__':
    main()