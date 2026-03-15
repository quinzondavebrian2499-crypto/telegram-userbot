import prefix
import owner
from telethon import events
from __main__ import client


def cmd(name):

    pattern = rf"^{prefix.PREFIX}{name}"

    def decorator(func):

        async def wrapper(event):

            # only allow owner commands
            if event.sender_id != owner.OWNER_ID:
                return

            await func(event)

        client.add_event_handler(
            wrapper,
            events.NewMessage(pattern=pattern)
        )

        return wrapper

    return decorator
