import json
import os
from datetime import datetime

class SecurityLogger:
    def __init__(self):
        os.makedirs("database/logs", exist_ok=True)
        self.file = "database/logs/security_logs.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def log(self, guild_id, user_id, action, reason):
        with open(self.file, "r", encoding="utf-8") as f:
            logs = json.load(f)

        logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "guild_id": guild_id,
            "user_id": user_id,
            "action": action,
            "reason": reason
        })

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)
