import json
import os

DB_FILE = "db.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get(key, default=None):
    db = load_db()
    return db.get(key, default)


def set(key, value):
    db = load_db()
    db[key] = value
    save_db(db)
