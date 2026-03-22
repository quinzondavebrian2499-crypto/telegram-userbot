from command import cmd

@cmd("alive")
async def alive(event):

    await event.reply("✅ Userbot is alive!")
