import discord
from discord.ext import commands
from config import OWNER_ID

class AntiMemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.roles != after.roles:
            async for entry in after.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
                if entry.user.id != OWNER_ID:
                    await after.edit(roles=before.roles)
                    await self.bot.security_manager.punish(after.guild, entry.user)

async def setup(bot):
    await bot.add_cog(AntiMemberUpdate(bot))
