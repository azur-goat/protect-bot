import discord
from datetime import datetime, timezone, timedelta
from config import OWNER_ID

class AntiAlt:
    def __init__(self, bot, min_account_age_days=7):
        self.bot = bot
        self.min_age = timedelta(days=min_account_age_days)

    def is_suspicious(self, member: discord.Member):
        if member.id == OWNER_ID:
            return False

        account_age = datetime.now(timezone.utc) - member.created_at
        return account_age < self.min_age

    async def check_member(self, member: discord.Member):
        if self.is_suspicious(member):
            await self.bot.security_manager.punish(
                member.guild,
                member,
                "Alt account detected (account too recent)"
            )
