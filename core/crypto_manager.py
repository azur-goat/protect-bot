from cryptography.fernet import Fernet

class CryptoManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: str):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, token: bytes):
        return self.cipher.decrypt(token).decode()
