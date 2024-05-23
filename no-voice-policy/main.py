import logging
import os
import time
from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaDocument

EXTRA_NAME = 'telegram-extras-no-voice-policy'
EXTRA_VAR_TG_API_ID = 'TG_API_ID'
EXTRA_VAR_TG_API_HASH = 'TG_API_HASH'
EXTRA_VAR_LANG = 'REPLY_LANG'

LANG = os.environ.get(EXTRA_VAR_LANG, 'en_US')

# basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(EXTRA_NAME)

# telegram client
api_id = os.environ[EXTRA_VAR_TG_API_ID]
api_hash = os.environ[EXTRA_VAR_TG_API_HASH]
client = TelegramClient(EXTRA_NAME, api_id, api_hash)
logger.info('Telegram client created.')

# reply message
reply_msg_filename = f'{os.path.join(os.path.realpath(os.path.dirname(__file__)), LANG)}.txt'
with open(reply_msg_filename, 'r') as file:
    message = file.read()
logger.info('The following reply message will be used:')
logger.info(message)

def main():

    # connecting telegram
    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        
        if event.is_private and isinstance(event.media, MessageMediaDocument) and event.media.voice:
            time.sleep(1)  
            await client.send_message(event.sender_id, message)
            logger.info(f'Message sent to ID {event.sender_id}.')
    
    client.run_until_disconnected()


if __name__ == '__main__':
    main()