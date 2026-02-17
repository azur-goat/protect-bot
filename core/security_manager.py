import discord
from config import OWNER_ID

class SecurityManager:
    def __init__(self, bot):
        self.bot = bot

    async def initialize_guild(self, guild):
        await self.bot.backup_manager.create_backup(guild)

    async def punish(self, guild, user, reason="Unauthorized action"):
        if user.id == OWNER_ID:
            return

        try:
            await guild.ban(user, reason=reason)
        except:
            pass
