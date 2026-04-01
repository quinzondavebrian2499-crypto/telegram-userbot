from telethon import TelegramClient
import importlib
import os
from config import API_ID, API_HASH

client = TelegramClient("userbot", API_ID, API_HASH)

# ===== LOAD PLUGINS (WITH ERROR LOGGING) =====
for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        try:
            print(f"🔄 Loading {file}...")
            importlib.import_module(f"plugins.{file[:-3]}")
        except Exception as e:
            print(f"❌ Failed to load {file}: {e}")

client.start()

print("🔥 Clean Userbot Running...")

client.run_until_disconnected()
