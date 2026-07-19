from twitchio.ext import commands

from utils.storage import get_user


class Economy(commands.Cog):
    """Commands related to Nyxium and the economy."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="balance", aliases=("bal",))
    async def balance(self, ctx):
        """Display a player's Nyxium balance."""

        profile = get_user(ctx.author.name)
        nyxium = profile.get("nyxium", 0)

        await ctx.send(
            f"🌙 {ctx.author.name}'s Balance | ✨ Nyxium: {nyxium}"
        )


def prepare(bot):
    bot.add_cog(Economy(bot))