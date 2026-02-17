import discord
from discord.ext import commands
from config import OWNER_ID

class AntiBanKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if entry.user.id != OWNER_ID:
                await guild.ban(entry.user, reason="Unauthorized ban")

async def setup(bot):
    await bot.add_cog(AntiBanKick(bot))
