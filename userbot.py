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

import database

async def after_restart():
    data = database.get("restart")

    if not data:
        return

    try:
        msg = await client.get_messages(data["chat_id"], ids=data["msg_id"])
        await msg.edit("✅ Restarted successfully!")
    except:
        pass

    database.set("restart", None)


with client:
    client.loop.run_until_complete(after_restart())
    print("🔥 Clean Userbot Running...")
    client.run_until_disconnected()
