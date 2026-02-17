import discord
from config import OWNER_ID

class AuditAnalyzer:
    def __init__(self, bot):
        self.bot = bot

    async def get_responsible(self, guild, action_type):
        async for entry in guild.audit_logs(limit=5, action=action_type):
            if entry.user.id != OWNER_ID:
                return entry.user
        return None

    async def analyze_and_punish(self, guild, action_type, reason):
        user = await self.get_responsible(guild, action_type)
        if user:
            await self.bot.security_manager.punish(guild, user, reason)
