import json
import discord

class RestoreManager:
    def __init__(self, bot):
        self.bot = bot

    async def restore_guild(self, guild):
        try:
            with open(f"database/backups/{guild.id}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            return

        # Restore roles
        existing_roles = [r.name for r in guild.roles]
        for role_data in data["roles"]:
            if role_data["name"] not in existing_roles:
                await guild.create_role(
                    name=role_data["name"],
                    permissions=discord.Permissions(role_data["permissions"]),
                    colour=discord.Colour(role_data["color"])
                )

        # Restore channels
        existing_channels = [c.name for c in guild.channels]
        for channel_data in data["channels"]:
            if channel_data["name"] not in existing_channels:
                if "text" in channel_data["type"]:
                    await guild.create_text_channel(channel_data["name"])
                elif "voice" in channel_data["type"]:
                    await guild.create_voice_channel(channel_data["name"])
