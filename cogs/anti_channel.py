import discord
from discord.ext import commands
from config import OWNER_ID

class AntiChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def punish(self, guild):
        async for entry in guild.audit_logs(limit=1):
            if entry.user.id != OWNER_ID:
                await self.bot.security_manager.punish(guild, entry.user)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        await channel.delete()
        await self.punish(channel.guild)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        await self.bot.restore_manager.restore_guild(channel.guild)
        await self.punish(channel.guild)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        await after.edit(name=before.name)
        await self.punish(after.guild)

async def setup(bot):
    await bot.add_cog(AntiChannel(bot))
