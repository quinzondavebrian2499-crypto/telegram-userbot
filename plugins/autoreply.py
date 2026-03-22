from telethon import events
from command import cmd
from __main__ import client
import time

REPLIES = {}
LAST_REPLY = {}


# ======================
# ADD REPLY
# ======================

@cmd("setreply")
async def setreply(event):

    try:
        _, key, value = event.text.split(" ", 2)
        REPLIES[key.lower()] = value
        await event.reply(f"✅ Reply added for: {key}")
    except:
        await event.reply("Usage: .setreply hi Hello!")


# ======================
# DELETE REPLY
# ======================

@cmd("delreply")
async def delreply(event):

    try:
        _, key = event.text.split(" ", 1)
        REPLIES.pop(key.lower(), None)
        await event.reply(f"❌ Reply removed: {key}")
    except:
        await event.reply("Usage: .delreply hi")


# ======================
# LIST REPLIES
# ======================

@cmd("replies")
async def list_replies(event):

    if not REPLIES:
        await event.reply("No auto replies set.")
        return

    text = "📌 Auto Replies:\n\n"

    for k, v in REPLIES.items():
        text += f"{k} → {v}\n"

    await event.reply(text)


# ======================
# AUTO REPLY LISTENER
# ======================

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):

    # ignore your own messages
    me = await client.get_me()
    if event.sender_id == me.id:
        return

    msg = event.raw_text
    if not msg:
        return

    msg = msg.lower()

    for key, value in REPLIES.items():

        if key in msg:

            user = event.sender_id
            now = time.time()

            # cooldown (15 seconds)
            if user in LAST_REPLY:
                if now - LAST_REPLY[user] < 15:
                    return

            LAST_REPLY[user] = now

            await event.reply(value)
            break
