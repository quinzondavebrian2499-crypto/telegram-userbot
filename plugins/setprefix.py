from telethon import events
from __main__ import client
import database
import prefix


@client.on(events.NewMessage(pattern=r"\.setprefix (.+)"))
async def setprefix(event):

    new_prefix = event.pattern_match.group(1)

    database.set("prefix", new_prefix)

    prefix.PREFIX = new_prefix

    await event.reply(f"✅ Prefix changed to: {new_prefix}")
