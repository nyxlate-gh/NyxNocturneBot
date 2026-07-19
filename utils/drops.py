import random

from utils.items import load_items


def get_random_item():
    """Return a random item ID using weighted probabilities."""

    items = load_items()

    item_ids = list(items.keys())
    weights = [item["weight"] for item in items.values()]

    return random.choices(item_ids, weights=weights, k=1)[0]

from utils.storage import get_user, update_user


def give_item(username, item_id):
    """Give an item to a player."""

    user = get_user(username)

    inventory = user["inventory"]

    inventory[item_id] = inventory.get(item_id, 0) + 1

    update_user(username, user)