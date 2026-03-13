from telethon import events
from __main__ import client
import os

PLUGIN_DIR = "plugins"

def read_plugin_info():

    plugins = []

    for file in os.listdir(PLUGIN_DIR):

        if file.endswith(".py"):

            path = os.path.join(PLUGIN_DIR, file)

            with open(path, "r") as f:

                first_line = f.readline()

                if first_line.startswith("# plugin:"):

                    parts = first_line.replace("# plugin:", "").split("|")

                    name = parts[0].strip()
                    command = parts[1].replace("command:", "").strip()
                    desc = parts[2].replace("desc:", "").strip()

                    plugins.append((name, command, desc))

    return plugins


@client.on(events.NewMessage(pattern=r".help"))
async def help_menu(event):

    plugins = read_plugin_info()

    text = "🤖 **Userbot Help Menu**\n\n"

    for name, cmd, desc in plugins:

        text += f"**{name}**\n"
        text += f"`{cmd}`\n"
        text += f"{desc}\n\n"

    await event.reply(text)
