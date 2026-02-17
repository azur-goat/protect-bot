import discord
from discord.ext import commands
from config import OWNER_ID

class AntiBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            async for entry in member.guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                if entry.user.id != OWNER_ID:
                    await member.guild.ban(entry.user, reason="Unauthorized bot add")
                    await member.ban(reason="Unauthorized bot")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.id == self.bot.user.id:
            print("⚠️ Tentative suppression du bot détectée.")

async def setup(bot):
    await bot.add_cog(AntiBot(bot))
