from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class EncryptionUtils:
    @staticmethod
    def generate_key_from_password(password: str, salt: bytes = b'static_salt') -> bytes:
        # Generating an encryption key from a password using PBKDF2 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    @staticmethod
    def encrypt_data(data: str, password: str) -> bytes:
        #Encrypting data using a password
        try:
            key = EncryptionUtils.generate_key_from_password(password)
            f = Fernet(key)
            encrypted_data = f.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            raise Exception(f"Encryption failed: {str(e)}")

    @staticmethod
    def decrypt_data(encrypted_data: bytes, password: str) -> str:
        #Decrypting data using a password
        try:
            key = EncryptionUtils.generate_key_from_password(password)
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data)
            return decrypted_data.decode()
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")