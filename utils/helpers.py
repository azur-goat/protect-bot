import discord
from config import OWNER_ID

class Helpers:

    @staticmethod
    def is_owner(user_id: int) -> bool:
        return user_id == OWNER_ID

    @staticmethod
    async def safe_delete(obj):
        try:
            await obj.delete()
        except:
            pass

    @staticmethod
    async def safe_ban(guild, user, reason="Security"):
        try:
            await guild.ban(user, reason=reason)
        except:
            pass

    @staticmethod
    async def safe_edit(obj, **kwargs):
        try:
            await obj.edit(**kwargs)
        except:
            pass

    @staticmethod
    def format_user(user: discord.User):
        return f"{user} ({user.id})"
