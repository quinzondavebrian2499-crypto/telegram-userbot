import prefix
from telethon import events
from __main__ import client

def cmd(name):

    pattern = rf"^{prefix.PREFIX}{name}"

    def decorator(func):

        client.add_event_handler(
            func,
            events.NewMessage(pattern=pattern)
        )

        return func

    return decorator
