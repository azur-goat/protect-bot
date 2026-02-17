class FreezeManager:
    def __init__(self, bot):
        self.bot = bot
        self.frozen_guilds = set()

    async def freeze(self, guild):
        self.frozen_guilds.add(guild.id)

        for role in guild.roles:
            if role.permissions.administrator:
                await role.edit(permissions=role.permissions.none())

    async def unfreeze(self, guild):
        self.frozen_guilds.discard(guild.id)
