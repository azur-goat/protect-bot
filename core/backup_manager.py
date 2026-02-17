import json
import os
from datetime import datetime

class BackupManager:
    def __init__(self, bot):
        self.bot = bot
        os.makedirs("database/backups", exist_ok=True)

    async def create_backup(self, guild):
        data = {
            "guild_name": guild.name,
            "created_at": datetime.utcnow().isoformat(),
            "roles": [],
            "categories": [],
            "channels": []
        }

        # Roles
        for role in guild.roles:
            if role.is_default():
                continue

            data["roles"].append({
                "name": role.name,
                "permissions": role.permissions.value,
                "color": role.color.value,
                "position": role.position,
                "hoist": role.hoist,
                "mentionable": role.mentionable
            })

        # Categories
        for category in guild.categories:
            data["categories"].append({
                "name": category.name,
                "position": category.position
            })

        # Channels
        for channel in guild.channels:
            data["channels"].append({
                "name": channel.name,
                "type": str(channel.type),
                "category": channel.category.name if channel.category else None,
                "position": channel.position
            })

        with open(f"database/backups/{guild.id}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
