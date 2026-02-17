import time
from collections import defaultdict
from config import OWNER_ID

class AntiSelfbot:
    def __init__(self, bot, spam_threshold=5, interval=5):
        self.bot = bot
        self.spam_threshold = spam_threshold
        self.interval = interval
        self.user_messages = defaultdict(list)

    async def check_message(self, message):
        if message.author.bot:
            return

        if message.author.id == OWNER_ID:
            return

        now = time.time()
        self.user_messages[message.author.id].append(now)

        # Nettoyage ancien timestamps
        self.user_messages[message.author.id] = [
            t for t in self.user_messages[message.author.id]
            if now - t < self.interval
        ]

        if len(self.user_messages[message.author.id]) >= self.spam_threshold:
            await self.bot.security_manager.punish(
                message.guild,
                message.author,
                "Selfbot-like spam detected"
            )
