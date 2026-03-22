from telethon import events
from config import OWNER_ID, get_prefix
from __main__ import client
import re


def cmd(name):

    def decorator(func):

        async def wrapper(event):

            if event.sender_id != OWNER_ID:
                return

            prefix = get_prefix()

            pattern = rf"^{re.escape(prefix)}{name}(?:\s|$)"

            if not re.match(pattern, event.raw_text):
                return

            await func(event)

        client.add_event_handler(
            wrapper,
            events.NewMessage(incoming=True)
        )

        return wrapper

    return decorator
