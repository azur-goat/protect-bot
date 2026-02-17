import time
from collections import defaultdict
from config import OWNER_ID

class ThresholdSystem:
    def __init__(self, limit=3, window=10):
        self.limit = limit
        self.window = window
        self.actions = defaultdict(list)

    def register_action(self, user_id):
        now = time.time()
        self.actions[user_id].append(now)

        # Nettoyage
        self.actions[user_id] = [
            t for t in self.actions[user_id]
            if now - t < self.window
        ]

        return len(self.actions[user_id]) >= self.limit

    def reset_user(self, user_id):
        if user_id in self.actions:
            del self.actions[user_id]
