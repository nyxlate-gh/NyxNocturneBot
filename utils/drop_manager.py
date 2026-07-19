import random
import time

from utils.drops import get_random_item, give_item
from utils.items import get_item

DROP_COOLDOWN = 120      # seconds
DROP_CHANCE = 0.15       # 15%

last_drop_time = 0


async def try_drop(message):
    global last_drop_time

    now = time.time()

    # Ignore commands
    if message.content.startswith("!"):
        return

    # Ignore the bot itself
    if message.echo:
        return

    # Cooldown
    if now - last_drop_time < DROP_COOLDOWN:
        return

    # Roll chance
    if random.random() > DROP_CHANCE:
        return

    last_drop_time = now

    item_id = get_random_item()
    give_item(message.author.name, item_id)

    item = get_item(item_id)

    await message.channel.send(
        f"🌙 The night whispers... "
        f"{message.author.name} found "
        f"{item['emoji']} {item['name']}!"
    )