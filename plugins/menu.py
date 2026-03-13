from telethon import events
from __main__ import client

@client.on(events.NewMessage(pattern=r".menu"))
async def menu(event):

    text = """
🤖 **Userbot Menu**

📦 Plugins
.plugins

⚙ Settings
.settings

🛠 Utilities
.utilities
"""

    await event.reply(text)


@client.on(events.NewMessage(pattern=r".settings"))
async def settings(event):

    text = """
⚙ **Settings**

.setprefix
.afk
.autoreply
"""

    await event.reply(text)


@client.on(events.NewMessage(pattern=r".utilities"))
async def utilities(event):

    text = """
🛠 **Utilities**

.calc
.translate
.img
.remind
"""

    await event.reply(text)
