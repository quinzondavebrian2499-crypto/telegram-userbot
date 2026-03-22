from command import cmd

HELP = {
    "name": "Alive",
    "description": "Check if bot is running",
    "usage": ".alive"
}

@cmd("alive")
async def alive(event):

    await event.reply("✅ Userbot is alive!")
