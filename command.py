from telethon import events
from config import OWNER_ID, get_prefix
from __main__ import client
import re


def cmd(name):

    def decorator(func):

        async def wrapper(event):

            # ONLY YOUR COMMANDS
            if event.sender_id != OWNER_ID:
                return

            prefix = get_prefix()

            text = event.raw_text
            if not text:
                return

            pattern = rf"^{re.escape(prefix)}{name}(?:\s|$)"

            if not re.match(pattern, text):
                return

            await func(event)

        client.add_event_handler(
            wrapper,
            events.NewMessage()  # ✅ LISTEN TO ALL (IMPORTANT)
        )

        return wrapper

    return decorator
