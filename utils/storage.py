import json
from pathlib import Path

DATA_FILE = Path("data/users.json")


def load_users():
    """Load all users from users.json."""
    if not DATA_FILE.exists():
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_users(users):
    """Save all users to users.json."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def get_user(username):
    """
    Return a user's profile.
    Create one automatically if it doesn't exist.
    """

    username = username.lower()

    users = load_users()

    if username not in users:
        users[username] = {
            "inventory": {},
            "gold": 0,
            "xp": 0,
            "level": 1
        }

        save_users(users)

    return users[username]


def update_user(username, profile):
    users = load_users()
    users[username.lower()] = profile
    save_users(users)