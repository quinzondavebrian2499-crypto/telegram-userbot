from telethon import events
from openai import OpenAI
from userbot import client

print("🔥 AI PLUGIN LOADED")

client_ai = OpenAI(api_key="sk-REPLACE_THIS_WITH_YOUR_KEY")

@client.on(events.NewMessage(incoming=True))
async def ai_autoreply(event):
    print("🔥 EVENT DETECTED:", event.raw_text)
    await event.reply("IT WORKS 🔥")
