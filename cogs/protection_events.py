import discord
from discord.ext import commands

class ProtectionEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.bot.anti_token_manager.scan_message(message)

async def setup(bot):
    await bot.add_cog(ProtectionEvents(bot))
