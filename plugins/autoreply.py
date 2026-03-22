from telethon import events
from command import cmd
from __main__ import client
import time
import database

LAST_REPLY = {}


def get_replies():
    return database.get("replies", {})


def save_replies(data):
    database.set("replies", data)


# ======================
# ADD REPLY
# ======================

@cmd("setreply")
async def setreply(event):

    try:
        _, key, value = event.text.split(" ", 2)

        replies = get_replies()
        replies[key.lower()] = value

        save_replies(replies)

        await event.reply(f"✅ Reply saved: {key}")

    except:
        await event.reply("Usage: .setreply hi Hello!")


# ======================
# DELETE REPLY
# ======================

@cmd("delreply")
async def delreply(event):

    try:
        _, key = event.text.split(" ", 1)

        replies = get_replies()
        replies.pop(key.lower(), None)

        save_replies(replies)

        await event.reply(f"❌ Removed: {key}")

    except:
        await event.reply("Usage: .delreply hi")


# ======================
# LIST REPLIES
# ======================

@cmd("replies")
async def list_replies(event):

    replies = get_replies()

    if not replies:
        await event.reply("No replies saved.")
        return

    text = "📌 Auto Replies:\n\n"

    for k, v in replies.items():
        text += f"{k} → {v}\n"

    await event.reply(text)


# ======================
# AUTO REPLY LISTENER
# ======================

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):

    me = await client.get_me()

    if event.sender_id == me.id:
        return

    msg = event.raw_text
    if not msg:
        return

    msg = msg.lower()

    replies = get_replies()

    for key, value in replies.items():

        if key in msg:

            user = event.sender_id
            now = time.time()

            if user in LAST_REPLY:
                if now - LAST_REPLY[user] < 15:
                    return

            LAST_REPLY[user] = now

            await event.reply(value)
            break
