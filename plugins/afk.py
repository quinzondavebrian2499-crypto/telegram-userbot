# plugin: AFK | command: afk | desc: Set AFK status

from command import cmd

AFK = False


@cmd("afk")
async def afk(event):

    global AFK

    AFK = True

    await event.reply("😴 AFK Enabled")
