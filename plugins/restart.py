from command import cmd
import os
import sys

@cmd("restart")
async def restart(event):

    await event.reply("🔄 Restarting...")

    os.execv(sys.executable, [sys.executable] + sys.argv)
