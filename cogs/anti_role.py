import discord
from discord.ext import commands
from config import OWNER_ID

class AntiRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def punish_if_needed(self, guild):
        async for entry in guild.audit_logs(limit=1):
            if entry.user.id != OWNER_ID:
                await self.bot.security_manager.punish(guild, entry.user)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        await role.delete()
        await self.punish_if_needed(role.guild)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        await self.bot.restore_manager.restore_guild(role.guild)
        await self.punish_if_needed(role.guild)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        await after.edit(
            name=before.name,
            permissions=before.permissions,
            colour=before.colour
        )
        await self.punish_if_needed(after.guild)

async def setup(bot):
    await bot.add_cog(AntiRole(bot))
