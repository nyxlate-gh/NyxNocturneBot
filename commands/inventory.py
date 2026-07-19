from twitchio.ext import commands

from utils.storage import get_user
from utils.items import get_item


RARITY_ICONS = {
    "Common": "⚪",
    "Uncommon": "🟢",
    "Rare": "🔵",
    "Epic": "🟣",
    "Legendary": "🟠"
}

RARITY_LEVELS = [
    "Common",
    "Uncommon",
    "Rare",
    "Epic",
    "Legendary"
]

RARITY_ORDER = {
    rarity: index
    for index, rarity in enumerate(RARITY_LEVELS)
}


class Inventory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inventory(self, ctx):
        user = get_user(ctx.author.name)

        inventory = user["inventory"]

        if not inventory:
            await ctx.send(
                f"🎒 {ctx.author.name}'s Backpack | "
                "It's empty... Perhaps the night has yet to bless you."
            )
            return

        items = []
        total_items = 0

        for item_id, amount in inventory.items():
            item = get_item(item_id)

            if item is None:
                continue

            rarity = item["rarity"]

            items.append((
                RARITY_ORDER.get(rarity, 999),
                f"{item['emoji']} {item['name']} ×{amount} "
                f"{RARITY_ICONS.get(rarity, '❔')}"
            ))

            total_items += amount

        items.sort(key=lambda x: x[0])

        display = [item[1] for item in items]

        await ctx.send(
            f"🎒 {ctx.author.name}'s Backpack | "
            + " • ".join(display)
            + f" | Unique: {len(display)} | Total: {total_items}"
        )


def prepare(bot):
    bot.add_cog(Inventory(bot))