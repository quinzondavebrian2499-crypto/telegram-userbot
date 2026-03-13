from telethon import events
from __main__ import client
import prefix

@client.on(events.NewMessage(pattern=r"\.setprefix (.+)"))
async def set_prefix(event):
    new_prefix = event.pattern_match.group(1)

    prefix.PREFIX = new_prefix

    await event.reply(f"✅ Command prefix changed to: {new_prefix}")
