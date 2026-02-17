import discord
from discord.ext import commands
from config import OWNER_ID

class AntiWebhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        webhooks = await channel.webhooks()
        for webhook in webhooks:
            async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create):
                if entry.user.id != OWNER_ID:
                    await webhook.delete()
                    await self.bot.security_manager.punish(channel.guild, entry.user)

async def setup(bot):
    await bot.add_cog(AntiWebhook(bot))
