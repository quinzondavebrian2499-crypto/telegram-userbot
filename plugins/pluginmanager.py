from telethon import events
from __main__ import client
import importlib
import os
import sys

PLUGINS = "plugins"


@client.on(events.NewMessage(pattern=r".plugins"))
async def list_plugins(event):

    files = os.listdir(PLUGINS)

    plugins = [f.replace(".py","") for f in files if f.endswith(".py")]

    text = "📦 Loaded Plugins:\n\n"

    for p in plugins:
        text += f"• {p}\n"

    await event.reply(text)


@client.on(events.NewMessage(pattern=r".reload (.*)"))
async def reload_plugin(event):

    plugin = event.pattern_match.group(1)

    try:
        importlib.reload(sys.modules[f"{PLUGINS}.{plugin}"])

        await event.reply(f"🔄 Reloaded plugin: {plugin}")

    except Exception as e:
        await event.reply(f"Error: {e}")


@client.on(events.NewMessage(pattern=r".unload (.*)"))
async def unload_plugin(event):

    plugin = event.pattern_match.group(1)

    try:
        del sys.modules[f"{PLUGINS}.{plugin}"]

        await event.reply(f"❌ Unloaded plugin: {plugin}")

    except Exception as e:
        await event.reply(f"Error: {e}")


@client.on(events.NewMessage(pattern=r".load (.*)"))
async def load_plugin(event):

    plugin = event.pattern_match.group(1)

    try:
        importlib.import_module(f"{PLUGINS}.{plugin}")

        await event.reply(f"✅ Loaded plugin: {plugin}")

    except Exception as e:
        await event.reply(f"Error: {e}")
