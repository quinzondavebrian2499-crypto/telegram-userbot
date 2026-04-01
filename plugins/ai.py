from telethon import events
from openai import OpenAI
import os

# ===== SETTINGS =====
AI_ENABLED = True
OWNER_ID = 123456789  # <-- replace with your Telegram user ID

# ===== OPENAI CLIENT =====
client_ai = OpenAI(
    api_key="sk-REPLACE_THIS_WITH_YOUR_KEY"
)

# ===== AUTO REPLY =====
@client.on(events.NewMessage(incoming=True))
async def ai_autoreply(event):
    print("🔥 EVENT DETECTED:", event.raw_text)

    if not AI_ENABLED:
        print("❌ AI OFF")
        return

    if event.sender_id == OWNER_ID:
        print("❌ OWNER MESSAGE IGNORED")
        return

    if not event.is_private:
        print("❌ NOT PRIVATE")
        return

    try:
        print("✅ PASSED FILTERS")

        user_message = event.raw_text

        response = client_ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Telegram assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        print("✅ AI RESPONSE:", reply)

        await event.reply(reply)

    except Exception as e:
        print("🚨 AI ERROR:", e)
