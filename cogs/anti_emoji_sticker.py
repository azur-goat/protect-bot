import discord
from discord.ext import commands
from config import OWNER_ID

class AntiEmojiSticker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def punish(self, guild):
        async for entry in guild.audit_logs(limit=1):
            if entry.user.id != OWNER_ID:
                await self.bot.security_manager.punish(guild, entry.user)

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        await self.punish(guild)

    @commands.Cog.listener()
    async def on_guild_stickers_update(self, guild, before, after):
        await self.punish(guild)

async def setup(bot):
    await bot.add_cog(AntiEmojiSticker(bot))
