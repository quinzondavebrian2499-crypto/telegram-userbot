from telethon import events
from command import cmd
from __main__ import client
import time
import database

HELP = {
    "name": "AFK",
    "description": "Set AFK status",
    "usage": ".afk <reason> / .afk off"
}

LAST_REPLY = {}


def set_afk(status, reason=""):
    database.set("afk", {"status": status, "reason": reason})


def get_afk():
    return database.get("afk", {"status": False, "reason": ""})


# ======================
# AFK COMMAND
# ======================

@cmd("afk")
async def afk(event):

    args = event.text.split(" ", 1)

    if len(args) > 1 and args[1].lower() == "off":
        set_afk(False)
        await event.reply("✅ AFK Disabled")
        return

    reason = args[1] if len(args) > 1 else "I'm AFK"

    set_afk(True, reason)

    await event.reply(f"😴 AFK Enabled\nReason: {reason}")


# ======================
# AUTO AFK REPLY
# ======================

@client.on(events.NewMessage(incoming=True))
async def auto_afk(event):

    afk = get_afk()

    if not afk["status"]:
        return

    me = await client.get_me()

    if event.sender_id == me.id:
        return

    user = event.sender_id
    now = time.time()

    if user in LAST_REPLY:
        if now - LAST_REPLY[user] < 30:
            return

    LAST_REPLY[user] = now

    await event.reply(f"😴 I'm AFK\nReason: {afk['reason']}")
