from twitchio.ext import commands

from utils.storage import get_user


class Inventory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inventory(self, ctx):
        user = get_user(ctx.author.name)

        inventory = user["inventory"]

        if not inventory:
            await ctx.send(
                f"🌙 {ctx.author.name}, your backpack is empty... "
                "Perhaps the night has yet to bless you."
            )
            return

        items = []

        for item, amount in inventory.items():
            items.append(f"{item} x{amount}")

        await ctx.send(
            f"🎒 {ctx.author.name}'s Backpack | " + ", ".join(items)
        )


def prepare(bot):
    bot.add_cog(Inventory(bot))