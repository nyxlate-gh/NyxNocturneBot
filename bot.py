from twitchio.ext import commands

from config import ACCESS_TOKEN, CHANNEL_NAME

from utils.drop_manager import try_drop
from utils.chat_rewards import try_chat_reward


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

    async def event_message(self, message):
        if message.echo:
            return
        # Process commands first
        await self.handle_commands(message)

        # Background systems
        await try_drop(message)
        await try_chat_reward(message)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong! 🌙")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}! 🌙")


bot = NocturneBot()

bot.load_module("commands.inventory")
bot.load_module("commands.items")
bot.load_module("commands.economy")

bot.run()