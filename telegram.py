from telethon import TelegramClient, events

api_id = '23145072'
api_hash = '538ca0bba8c2d266bb559256c2b211ea'
phone_number = '9005443726392'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    sender_name = sender.username or f'{sender.first_name} {sender.last_name or ""}'

    message_text = event.message.message

    print(f'New message from {sender_name}: {message_text}')

async def main():
    await client.start(phone_number)

    print("Listening for incoming messages...")

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
