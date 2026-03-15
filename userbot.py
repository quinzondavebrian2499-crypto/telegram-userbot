from telethon import TelegramClient
import os
import importlib

api_id = 2127709
api_hash = "5b7a6b1e4ff43ac9437114de58cef95a"

client = TelegramClient("userbot", api_id, api_hash)
from telethon import events
import security


@client.on(events.NewMessage(incoming=True))
async def command_firewall(event):

    # ignore our own messages
    if event.sender_id == security.OWNER_ID:
        return

    # check if message looks like a command
    text = event.raw_text

    if not text:
        return

    if text.startswith(".") or text.startswith("!") or text.startswith("/"):

        # stop the command
        event.stop_propagation()

# load plugins
for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        importlib.import_module(f"plugins.{file[:-3]}")

client.start()
print("Userbot running with plugins...")

client.run_until_disconnected()
