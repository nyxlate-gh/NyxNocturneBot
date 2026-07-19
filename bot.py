from twitchio.ext import commands

from config import ACCESS_TOKEN, CHANNEL_NAME


class NocturneBot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=ACCESS_TOKEN,
            prefix="!",
            initial_channels=[CHANNEL_NAME],
        )

    async def event_ready(self):
        print("=" * 40)
        print("🌙 NocturneBot is online!")
        print(f"Logged in as: {self.nick}")
        print(f"User ID: {self.user_id}")
        print("=" * 40)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! 🌙")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}! 🌙")


bot = NocturneBot()

bot.load_module("commands.inventory")

bot.run()