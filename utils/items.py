import json
from pathlib import Path

ITEMS_FILE = Path("data/items.json")


def load_items():
    with open(ITEMS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_item(item_id):
    items = load_items()
    return items.get(item_id)