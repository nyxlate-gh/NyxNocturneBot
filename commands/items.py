from twitchio.ext import commands

from utils.items import get_item


class Items(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inspect(self, ctx, *, item_id: str = None):

        if item_id is None:
            await ctx.send("Usage: !inspect <item>")
            return

        item = get_item(item_id.lower())

        if item is None:
            await ctx.send("🌙 That item doesn't exist.")
            return

        await ctx.send(
    f"{item['emoji']} {item['name']} • {item['rarity']} ✦ {item['description']}"
    
        )


def prepare(bot):
    bot.add_cog(Items(bot))