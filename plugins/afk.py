from telethon import events
from command import cmd
from __main__ import client
import time

AFK = False
AFK_REASON = ""
LAST_REPLY = {}


# ======================
# AFK COMMAND
# ======================

@cmd("afk")
async def afk(event):

    global AFK, AFK_REASON

    args = event.text.split(" ", 1)

    if len(args) > 1 and args[1].lower() == "off":
        AFK = False
        AFK_REASON = ""
        await event.reply("✅ AFK Disabled")
        return

    AFK = True
    AFK_REASON = args[1] if len(args) > 1 else "I'm AFK"

    await event.reply(f"😴 AFK Enabled\nReason: {AFK_REASON}")


# ======================
# AUTO REPLY WHEN AFK
# ======================

@client.on(events.NewMessage(incoming=True))
async def auto_afk(event):

    if not AFK:
        return

    # ignore your own messages
    me = await client.get_me()
    if event.sender_id == me.id:
        return

    user = event.sender_id
    now = time.time()

    # cooldown (no spam)
    if user in LAST_REPLY:
        if now - LAST_REPLY[user] < 30:
            return

    LAST_REPLY[user] = now

    await event.reply(f"😴 I'm AFK\nReason: {AFK_REASON}")
