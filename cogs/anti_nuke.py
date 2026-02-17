import discord
from discord.ext import commands
from collections import defaultdict
import asyncio
from config import OWNER_ID

class AntiNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.action_counter = defaultdict(int)

    async def log_action(self, guild, user):
        if user.id == OWNER_ID:
            return

        self.action_counter[user.id] += 1

        if self.action_counter[user.id] >= 3:
            await self.bot.security_manager.punish(guild, user, "Mass action detected")

        await asyncio.sleep(10)
        self.action_counter[user.id] -= 1

async def setup(bot):
    await bot.add_cog(AntiNuke(bot))
