# plugin: Ping | command: ping | desc: Check bot response speed

from command import cmd
import time

@cmd("ping")
async def ping(event):

    start = time.time()

    msg = await event.reply("🏓 Pinging...")

    end = time.time()

    ping_ms = round((end - start) * 1000, 2)

    await msg.edit(f"🏓 Pong!\nSpeed: {ping_ms} ms")