from telethon import events
from config import OPENAI_API_KEY, OWNER_ID
from __main__ import client
from command import cmd
from openai import OpenAI

client_ai = OpenAI(api_key=OPENAI_API_KEY)

AI_ENABLED = True


# 🤖 AUTO REPLY
@client.on(events.NewMessage(incoming=True))
async def ai_autoreply(event):

    if not AI_ENABLED:
        return

    if event.sender_id == OWNER_ID:
        return

    if not event.is_private:
        return

    try:
        user_message = event.raw_text

        if not user_message:
            return

        response = client_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Telegram assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        await event.reply(reply)

    except Exception as e:
        print("AI ERROR:", e)


# 🔘 COMMAND CONTROL
@cmd("ai")
async def toggle_ai(event):
    global AI_ENABLED

    args = event.raw_text.split()

    if len(args) < 2:
        await event.reply("Usage: .ai on / .ai off")
        return

    if args[1] == "on":
        AI_ENABLED = True
        await event.reply("🤖 AI AutoReply Enabled")
    elif args[1] == "off":
        AI_ENABLED = False
        await event.reply("❌ AI AutoReply Disabled")
        print("AI TRIGGERED:", event.raw_text)
