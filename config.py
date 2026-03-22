import os
import database

# Telegram API
API_ID = 2127709
API_HASH = "5b7a6b1e4ff43ac9437114de58cef95a"

# Owner
OWNER_ID = 1327719064  # your Telegram ID


# ======================
# PREFIX SYSTEM
# ======================

def get_prefix():
    return database.get("prefix", ".")


def set_prefix(p):
    database.set("prefix", p)
