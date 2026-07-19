import random
import time

from utils.drops import get_random_item, give_item
from utils.items import get_item

# ==============================
# Drop Settings
# ==============================

DROP_COOLDOWN = 120      # seconds
DROP_CHANCE = 0.15       # 15%

last_drop_time = 0

# ==============================
# Drop Messages
# ==============================

DROP_MESSAGES = [
     "🌙 The night whispers...",
    "🍃 The wind carries something your way...",
    "🦉 A raven lands nearby...",
    "✨ Moonlight reveals something hidden...",
    "🌌 The stars shimmer for a moment...",
    "🌠 A shooting star leaves something behind...",
    "🌸 A Night Bloom blooms in the darkness...",
    "🌑 Shadows part for a brief moment...",
    "🌙 A mysterious glow catches your eye...",
    "✨ The moon smiles upon you..."
]

# ==============================
# Rarity Icons
# ==============================

RARITY_EMOJIS = {
    "Common": "⚪",
    "Uncommon": "🟢",
    "Rare": "🔵",
    "Epic": "🟣",
    "Legendary": "🟠"
}


# ==============================
# Drop Logic
# ==============================

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

    # Random chance
    if random.random() > DROP_CHANCE:
        return

    last_drop_time = now

    # Give random item
    item_id = get_random_item()
    give_item(message.author.name, item_id)

    item = get_item(item_id)

    rarity = item["rarity"]
    rarity_icon = RARITY_EMOJIS.get(rarity, "❔")

    announcement = random.choice(DROP_MESSAGES)
    rarity = item["rarity"]
    rarity_icon = RARITY_EMOJIS.get(rarity, "❔")

    await message.channel.send(
        f"{announcement} "
        f"🎁 {message.author.name} obtained "
        f"{item['emoji']} {item['name']} "
        f"{rarity_icon} {rarity}!"
)