from telethon import TelegramClient
import os
import importlib

api_id = 2127709
api_hash = "5b7a6b1e4ff43ac9437114de58cef95a"

client = TelegramClient("userbot", api_id, api_hash)

# load plugins
for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        importlib.import_module(f"plugins.{file[:-3]}")

client.start()
print("Userbot running with plugins...")

client.run_until_disconnected()