from command import cmd
from __main__ import client
import importlib
import sys
import os

LOADED = {}


# ======================
# LOAD PLUGIN
# ======================

@cmd("load")
async def load_plugin(event):

    try:
        name = event.text.split(" ", 1)[1]

        module = f"plugins.{name}"

        if module in sys.modules:
            await event.reply("⚠️ Plugin already loaded")
            return

        importlib.import_module(module)

        LOADED[name] = module

        await event.reply(f"✅ Loaded: {name}")

    except Exception as e:
        await event.reply(f"❌ Error:\n{e}")


# ======================
# UNLOAD PLUGIN
# ======================

@cmd("unload")
async def unload_plugin(event):

    try:
        name = event.text.split(" ", 1)[1]

        module = f"plugins.{name}"

        if module not in sys.modules:
            await event.reply("⚠️ Plugin not loaded")
            return

        del sys.modules[module]

        LOADED.pop(name, None)

        await event.reply(f"❌ Unloaded: {name}")

    except Exception as e:
        await event.reply(f"❌ Error:\n{e}")


# ======================
# RELOAD PLUGIN
# ======================

@cmd("reload")
async def reload_plugin(event):

    try:
        name = event.text.split(" ", 1)[1]

        module = f"plugins.{name}"

        if module not in sys.modules:
            await event.reply("⚠️ Plugin not loaded")
            return

        importlib.reload(sys.modules[module])

        await event.reply(f"🔄 Reloaded: {name}")

    except Exception as e:
        await event.reply(f"❌ Error:\n{e}")


# ======================
# LIST PLUGINS
# ======================

@cmd("plugins")
async def list_plugins(event):

    files = [f[:-3] for f in os.listdir("./plugins") if f.endswith(".py")]

    text = "📦 Plugins:\n\n"

    for f in files:
        text += f"• {f}\n"

    await event.reply(text)
