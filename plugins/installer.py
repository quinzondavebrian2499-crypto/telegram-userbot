from telethon import events
from __main__ import client
import requests
import os

PLUGIN_DIR = "plugins"

@client.on(events.NewMessage(pattern=r".install (.*)"))
async def install_plugin(event):

    url = event.pattern_match.group(1)

    try:
        r = requests.get(url)

        if r.status_code != 200:
            await event.reply("❌ Failed to download plugin.")
            return

        name = url.split("/")[-1]

        path = os.path.join(PLUGIN_DIR, name)

        with open(path, "wb") as f:
            f.write(r.content)

        await event.reply(f"✅ Plugin installed: {name}\nUse `.load {name.replace('.py','')}`")

    except Exception as e:
        await event.reply(f"Error: {e}")