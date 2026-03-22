from command import cmd
from config import set_prefix, get_prefix

HELP = {
    "name": "Prefix",
    "description": "Change command prefix",
    "usage": ".setprefix !"
}


@cmd("setprefix")
async def prefix(event):

    try:
        new = event.text.split(" ", 1)[1]

        if len(new) > 2:
            await event.reply("❌ Prefix too long")
            return

        set_prefix(new)

        await event.reply(f"✅ Prefix changed to: {new}")

    except:
        await event.reply("Usage: .setprefix !")


@cmd("prefix")
async def show_prefix(event):

    await event.reply(f"Current prefix: {get_prefix()}")
