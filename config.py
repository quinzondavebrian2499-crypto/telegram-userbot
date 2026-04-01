import os
import database

# Telegram API
API_ID = 2127709
API_HASH = "5b7a6b1e4ff43ac9437114de58cef95a"
OPENAI_API_KEY = "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"

# Owner
OWNER_ID = 1327719064  # your Telegram ID


# ======================
# PREFIX SYSTEM
# ======================

def get_prefix():
    return database.get("prefix", ".")


def set_prefix(p):
    database.set("prefix", p)
