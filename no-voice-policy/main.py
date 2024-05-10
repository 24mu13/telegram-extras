import logging
import os
import time
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaDocument

EXTRA_NAME = 'tgext-no-voice-policy'
LANG = 'it-IT'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(EXTRA_NAME)

api_id = 'yourid'
api_hash = 'yourhash'

client = TelegramClient(EXTRA_NAME, api_id, api_hash)
logger.info("Connected to Telegram.")

with open(f'{os.path.join(os.path.realpath(os.path.dirname(__file__)), LANG)}.txt', 'r') as file:
    message = file.read()

def main():

    client.start()
    
    @client.on(events.NewMessage)
    async def _(event):
        
        if event.is_private and isinstance(event.media, MessageMediaDocument) and event.media.voice:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.sender_id, message)
            logger.info(f'Message sent to {event.sender_id} .')
    
    client.run_until_disconnected()


if __name__ == '__main__':
    main()