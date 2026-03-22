from telethon import events
from config import PREFIX, OWNER_ID
from __main__ import client


def cmd(name):

    pattern = rf"^{PREFIX}{name}(?:\s|$)"

    def decorator(func):

        async def wrapper(event):

            # OWNER ONLY
            if event.sender_id != OWNER_ID:
                return

            await func(event)

        client.add_event_handler(
            wrapper,
            events.NewMessage(pattern=pattern)
        )

        return wrapper

    return decorator
