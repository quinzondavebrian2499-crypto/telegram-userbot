from telethon import events
from config import OPENAI_API_KEY, OWNER_ID
from __main__ import client
import openai

openai.api_key = OPENAI_API_KEY

AI_ENABLED = True


@client.on(events.NewMessage(incoming=True))
async def ai_autoreply(event):
    
    if not AI_ENABLED:
        return

    # ignore yourself
    if event.sender_id == OWNER_ID:
        return

    # only reply in private chats
    if not event.is_private:
        return

    try:
        user_message = event.raw_text

        if not user_message:
            return

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Telegram assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message["content"]

        await event.reply(reply)

    except Exception as e:
        print("AI ERROR:", e)
