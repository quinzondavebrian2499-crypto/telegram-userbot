from telethon import TelegramClient
import importlib
import os
from config import API_ID, API_HASH

client = TelegramClient("userbot", API_ID, API_HASH)

# load plugins
for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        importlib.import_module(f"plugins.{file[:-3]}")

client.start()

print("🔥 Clean Userbot Running...")

client.run_until_disconnected()
