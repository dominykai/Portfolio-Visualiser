from bcrypt import hashpw, gensalt, checkpw


def get_password_hash(password: str) -> str:
    """Return a password hash with bcrypt."""
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

def verify_password_hash(plain_password: str, hashed_password: str) -> bool:
    """Verify a password and its hash matches."""
    try:
        return checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False