import time

from twitchio.ext import commands

from utils.storage import get_user, update_user

# Economy constants
DAILY_REWARD = 100
DAILY_COOLDOWN = 60 * 60 * 24  # 24 hours


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

    @commands.command()
    async def daily(self, ctx):
        """Claim the daily Nyxium reward."""

        profile = get_user(ctx.author.name)

        current_time = int(time.time())
        last_claim = profile.get("last_daily", 0)

        elapsed = current_time - last_claim

        if elapsed < DAILY_COOLDOWN:
            remaining = DAILY_COOLDOWN - elapsed

            hours = remaining // 3600
            minutes = (remaining % 3600) // 60

            await ctx.send(
                f"🌑 The night has already blessed you today. "
                f"Try again in {hours}h {minutes}m."
            )
            return

        profile["nyxium"] += DAILY_REWARD
        profile["last_daily"] = current_time

        update_user(ctx.author.name, profile)

        await ctx.send(
            f"🌙 The night blesses {ctx.author.name}...\n"
            f"✨ +{DAILY_REWARD} Nyxium!"
        )


def prepare(bot):
    bot.add_cog(Economy(bot))