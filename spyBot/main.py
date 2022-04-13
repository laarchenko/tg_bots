from telethon import TelegramClient, events

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TARGET_ID = os.getenv("TARGET_ID")
STORE_ID = os.getenv("STORE_ID")

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage())
async def my_event_handler(event):
    if event.chat_id == TARGET_ID:
        await client.send_message(STORE_ID, event.raw_text)


client.start()
client.run_until_disconnected()
