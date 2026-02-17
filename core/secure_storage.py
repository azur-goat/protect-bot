import os
from cryptography.fernet import Fernet

class SecureStorage:
    def __init__(self):
        os.makedirs("database/encrypted", exist_ok=True)
        self.key_path = "database/encrypted/master.key"

        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as f:
                f.write(key)

        with open(self.key_path, "rb") as f:
            self.key = f.read()

        self.cipher = Fernet(self.key)

    def encrypt(self, data: str):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, data: bytes):
        return self.cipher.decrypt(data).decode()
