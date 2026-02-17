import discord
from discord.ext import commands
from config import OWNER_ID

class AntiGuildUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        async for entry in after.audit_logs(limit=1, action=discord.AuditLogAction.guild_update):
            if entry.user.id != OWNER_ID:
                await after.edit(
                    name=before.name,
                    icon=before.icon,
                    banner=before.banner
                )
                await self.bot.security_manager.punish(after, entry.user)

async def setup(bot):
    await bot.add_cog(AntiGuildUpdate(bot))
