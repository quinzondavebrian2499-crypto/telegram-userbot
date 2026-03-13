from telethon import events
from __main__ import client

@client.on(events.NewMessage(pattern=".calc (.*)"))
async def calc(event):
    expr = event.pattern_match.group(1)

    try:
        result = eval(expr)
        await event.reply(f"🧮 Result: {result}")
    except:
        await event.reply("Invalid calculation.")
