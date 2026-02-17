from discord.ext import commands
from core.security_manager import SecurityManager
from core.backup_manager import BackupManager
from core.restore_manager import RestoreManager
from core.freeze_manager import FreezeManager
from core.crypto_manager import CryptoManager
from core.anti_token_manager import AntiTokenManager

class ProtectBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.security_manager = SecurityManager(self)
        self.backup_manager = BackupManager(self)
        self.restore_manager = RestoreManager(self)
        self.freeze_manager = FreezeManager(self)
        self.crypto_manager = CryptoManager()
        self.anti_token_manager = AntiTokenManager(self)
