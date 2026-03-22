import os
import database

# Telegram API
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")


# Owner
OWNER_ID = 1327719064  # your Telegram ID


# ======================
# PREFIX SYSTEM
# ======================

def get_prefix():
    return database.get("prefix", ".")


def set_prefix(p):
    database.set("prefix", p)
