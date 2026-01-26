from bcrypt import hashpw, gensalt, checkpw
from cryptography.fernet import Fernet

from backend.src.core.config_loader import settings


def get_password_hash(password: str) -> str:
    """Return a password hash with bcrypt."""
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password_hash(plain_password: str, hashed_password: str) -> bool:
    """Verify a password and its hash matches."""
    try:
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False

def encrypt_api_key(data: str) -> str:
    """Encrypt an API key using Fernet Encryption."""
    return Fernet(settings.SYMMETRIC_ENCRYPTION_KEY).encrypt(data.encode("utf-8")).decode("utf-8")

def decrypt_api_key(data: str) -> str:
    """Decrypt an API key using Fernet Decryption."""
    return Fernet(settings.SYMMETRIC_ENCRYPTION_KEY).decrypt(data.encode("utf-8")).decode("utf-8")

if __name__ == "__main__":
    print("Generated Fernet key: ", Fernet.generate_key().decode("utf-8"))
