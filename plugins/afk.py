from telethon import events
from __main__ import client

AFK = False
AFK_REASON = ""

@client.on(events.NewMessage(pattern=r".afk(?: (.*))?"))
async def set_afk(event):
    global AFK, AFK_REASON

    AFK = True
    AFK_REASON = event.pattern_match.group(1) or "AFK"

    await event.reply(f"😴 AFK Enabled\nReason: {AFK_REASON}")

@client.on(events.NewMessage(incoming=True))
async def afk_reply(event):
    global AFK

    if AFK and not event.out:
        await event.reply(f"😴 I am AFK\nReason: {AFK_REASON}")

@client.on(events.NewMessage(outgoing=True))
async def remove_afk(event):
    global AFK

    if AFK:
        AFK = False
        await event.reply("✅ AFK Disabled")