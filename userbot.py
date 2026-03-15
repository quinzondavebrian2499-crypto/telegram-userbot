from telethon import TelegramClient, events
import os
import importlib

# =========================
# TELEGRAM API
# =========================

api_id = 2127709
api_hash = "5b7a6b1e4ff43ac9437114de58cef95a"

client = TelegramClient("userbot", api_id, api_hash)

# =========================
# OWNER ID
# =========================

OWNER_ID = 1327719064   # <-- PUT YOUR TELEGRAM ID HERE

# =========================
# GLOBAL COMMAND FIREWALL
# =========================

@client.on(events.NewMessage(incoming=True))
async def command_firewall(event):

    # allow owner commands
    if event.sender_id == OWNER_ID:
        return

    text = event.raw_text

    if not text:
        return

    # block command prefixes
    if text.startswith(".") or text.startswith("!") or text.startswith("/"):

        raise events.StopPropagation


# =========================
# LOAD PLUGINS
# =========================

for file in os.listdir("./plugins"):
    if file.endswith(".py"):
        importlib.import_module(f"plugins.{file[:-3]}")


# =========================
# START BOT
# =========================

client.start()

print("Userbot running with plugins...")

client.run_until_disconnected()
