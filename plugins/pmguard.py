# plugin: PMGuard | command: pmguard | desc: Protect private messages

from telethon import events
from command import cmd
from __main__ import client

APPROVED_USERS = set()
PM_GUARD = True


@cmd("pmguard")
async def pmguard_toggle(event):

    global PM_GUARD

    text = event.text.split()

    if len(text) < 2:
        await event.reply("Usage: pmguard on/off")
        return

    if text[1] == "on":
        PM_GUARD = True
        await event.reply("✅ PM Guard Enabled")

    elif text[1] == "off":
        PM_GUARD = False
        await event.reply("❌ PM Guard Disabled")


@cmd("approve")
async def approve(event):

    if not event.is_private:
        return

    user = event.chat_id

    APPROVED_USERS.add(user)

    await event.reply("✅ User approved")


@cmd("disapprove")
async def disapprove(event):

    if not event.is_private:
        return

    user = event.chat_id

    APPROVED_USERS.discard(user)

    await event.reply("❌ User disapproved")


@cmd("block")
async def block(event):

    if not event.is_private:
        return

    user = event.chat_id

    await client.block(user)

    await event.reply("🚫 User blocked")


@client.on(events.NewMessage(incoming=True))
async def pm_guard(event):

    if not PM_GUARD:
        return

    if not event.is_private:
        return

    user = event.sender_id

    if user in APPROVED_USERS:
        return

    if user == (await client.get_me()).id:
        return

    await event.reply(
        "⚠️ You are not approved to PM.\nWait until I approve you."
    )
