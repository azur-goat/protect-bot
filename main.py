import os
import asyncio
import discord
from discord.ext import commands
from config import TOKEN, OWNER_ID
from core.bot import ProtectBot

intents = discord.Intents.all()

class UltimateProtection(ProtectBot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        for folder in ["cogs"]:
            for filename in os.listdir(f"./{folder}"):
                if filename.endswith(".py"):
                    await self.load_extension(f"{folder}.{filename[:-3]}")

    async def on_ready(self):
        print(f" Connect as : {self.user}")
        print(f" OWNER : {OWNER_ID}")

    async def on_guild_join(self, guild):
        print(f"J'ai rejoint : {guild.name}")
        await self.security_manager.initialize_guild(guild)

async def main():
    bot = UltimateProtection()

    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
