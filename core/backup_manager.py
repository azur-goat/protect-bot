import json
import os

class BackupManager:
    def __init__(self, bot):
        self.bot = bot
        os.makedirs("database/backups", exist_ok=True)

    async def create_backup(self, guild):
        data = {
            "name": guild.name,
            "roles": [],
            "channels": []
        }

        for role in guild.roles:
            data["roles"].append({
                "name": role.name,
                "permissions": role.permissions.value,
                "color": role.color.value,
                "position": role.position
            })

        for channel in guild.channels:
            data["channels"].append({
                "name": channel.name,
                "type": str(channel.type),
                "category": channel.category.name if channel.category else None,
                "position": channel.position
            })

        with open(f"database/backups/{guild.id}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
