import discord

class PermissionUtils:

    @staticmethod
    def has_admin(member: discord.Member) -> bool:
        return member.guild_permissions.administrator

    @staticmethod
    def strip_admin(role: discord.Role):
        perms = role.permissions
        if perms.administrator:
            perms.administrator = False
        return perms

    @staticmethod
    def copy_role_permissions(role: discord.Role):
        return discord.Permissions(role.permissions.value)

    @staticmethod
    def lock_channel(channel: discord.abc.GuildChannel):
        overwrites = channel.overwrites
        for target, overwrite in overwrites.items():
            overwrite.send_messages = False
            overwrite.connect = False
        return overwrites
