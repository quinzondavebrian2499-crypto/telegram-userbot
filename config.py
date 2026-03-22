import database

OWNER_ID = 1327719064  # your Telegram ID

def get_prefix():
    return database.get("prefix", ".")

def set_prefix(p):
    database.set("prefix", p)
