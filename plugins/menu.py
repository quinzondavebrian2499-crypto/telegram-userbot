from telethon import events, Button
from __main__ import client


@client.on(events.NewMessage(pattern=r".menu"))
async def menu(event):

    buttons = [
        [Button.inline("📦 Plugins", b"plugins")],
        [Button.inline("⚙ Settings", b"settings")],
        [Button.inline("🛠 Utilities", b"utilities")],
        [Button.inline("❌ Close", b"close")]
    ]

    await event.respond(
        "🤖 **Userbot Menu**\nChoose an option:",
        buttons=buttons
    )


@client.on(events.CallbackQuery)
async def callbacks(event):

    data = event.data.decode("utf-8")

    if data == "plugins":

        await event.edit(
            "📦 **Installed Plugins**\n\nUse `.plugins` to see plugin list.",
            buttons=[[Button.inline("⬅ Back", b"back")]]
        )

    elif data == "settings":

        await event.edit(
            "⚙ **Userbot Settings**\n\nCommands:\n.setprefix\n.afk\n.autoreply",
            buttons=[[Button.inline("⬅ Back", b"back")]]
        )

    elif data == "utilities":

        await event.edit(
            "🛠 **Utilities**\n\nCommands:\n.calc\n.translate\n.img\n.remind",
            buttons=[[Button.inline("⬅ Back", b"back")]]
        )

    elif data == "back":

        buttons = [
            [Button.inline("📦 Plugins", b"plugins")],
            [Button.inline("⚙ Settings", b"settings")],
            [Button.inline("🛠 Utilities", b"utilities")],
            [Button.inline("❌ Close", b"close")]
        ]

        await event.edit(
            "🤖 **Userbot Menu**\nChoose an option:",
            buttons=buttons
        )

    elif data == "close":

        await event.delete()