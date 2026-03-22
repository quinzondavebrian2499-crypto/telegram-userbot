from command import cmd
import os
import importlib

PLUGINS_DIR = "plugins"


def load_plugins():

    data = {}

    for file in os.listdir(PLUGINS_DIR):

        if file.endswith(".py"):

            name = file[:-3]

            try:
                module = importlib.import_module(f"{PLUGINS_DIR}.{name}")

                if hasattr(module, "HELP"):
                    data[name] = module.HELP

            except:
                continue

    return data


# ======================
# HELP SYSTEM (FIXED)
# ======================

@cmd("help")
async def help_menu(event):

    args = event.text.split(" ", 1)
    plugins = load_plugins()

    # 👉 SPECIFIC HELP
    if len(args) > 1:
        query = args[1].lower()

        if query not in plugins:
            await event.reply("❌ Plugin not found")
            return

        info = plugins[query]

        text = f"**{info['name']}**\n\n"
        text += f"{info['description']}\n\n"
        text += f"Usage: `{info['usage']}`"

        await event.reply(text)
        return

    # 👉 FULL MENU
    text = "🤖 **Userbot Help Menu**\n\n"

    for name, info in plugins.items():
        text += f"**{info['name']}**\n"
        text += f"{info['description']}\n"
        text += f"Usage: `{info['usage']}`\n\n"

    await event.reply(text)
