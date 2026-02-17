import re

class AntiTokenManager:
    TOKEN_PATTERN = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}"

    def __init__(self, bot):
        self.bot = bot

    async def scan_message(self, message):
        if re.search(self.TOKEN_PATTERN, message.content):
            await message.delete()
            await message.channel.send("🚨 Token détecté et supprimé.")
