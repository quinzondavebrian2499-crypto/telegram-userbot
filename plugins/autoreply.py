from telethon import events
from __main__ import client

AUTO_PRIVATE = False
AUTO_GROUP = False

@client.on(events.NewMessage(pattern=r".autoreply on"))
async def auto_all_on(event):
    global AUTO_PRIVATE, AUTO_GROUP
    AUTO_PRIVATE = True
    AUTO_GROUP = True
    await event.reply("🤖 Auto reply enabled for all chats.")

@client.on(events.NewMessage(pattern=r".autoreply off"))
async def auto_all_off(event):
    global AUTO_PRIVATE, AUTO_GROUP
    AUTO_PRIVATE = False
    AUTO_GROUP = False
    await event.reply("❌ Auto reply disabled.")

@client.on(events.NewMessage(pattern=r".autoreply private on"))
async def auto_private_on(event):
    global AUTO_PRIVATE
    AUTO_PRIVATE = True
    await event.reply("✅ Auto reply enabled for private chats.")

@client.on(events.NewMessage(pattern=r".autoreply private off"))
async def auto_private_off(event):
    global AUTO_PRIVATE
    AUTO_PRIVATE = False
    await event.reply("❌ Auto reply disabled for private chats.")

@client.on(events.NewMessage(pattern=r".autoreply group on"))
async def auto_group_on(event):
    global AUTO_GROUP
    AUTO_GROUP = True
    await event.reply("✅ Auto reply enabled for groups.")

@client.on(events.NewMessage(pattern=r".autoreply group off"))
async def auto_group_off(event):
    global AUTO_GROUP
    AUTO_GROUP = False
    await event.reply("❌ Auto reply disabled for groups.")

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):

    if event.out:
        return

    if event.is_private and AUTO_PRIVATE:
        await event.reply("Hello! I will respond later.")

    if event.is_group and AUTO_GROUP:
        await event.reply("Hello! I will respond later.")
