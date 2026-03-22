from command import cmd
import os
import sys
import database

HELP = {
    "name": "Restart",
    "description": "Restart the bot",
    "usage": ".restart"
}


@cmd("restart")
async def restart(event):

    # save message info
    database.set("restart", {
        "chat_id": event.chat_id,
        "msg_id": event.id
    })

    await event.reply("🔄 Restarting...")

    os.execv(sys.executable, [sys.executable] + sys.argv)
