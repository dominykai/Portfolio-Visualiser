from typing import Optional

from sqlalchemy.orm import Session

from backend.src.database.models.api_key_model import ApiKey
from backend.src.schema.models.api_key_schema import ApiKeyCreate
from backend.src.utils.auth_utils import encrypt_api_key, decrypt_api_key


def get_db_api_key(db: Session, user_id: int, broker_name: str) -> Optional[ApiKey]:
    """Return an API key from the database by user_id and broker_name."""
    db_api_key: Optional[ApiKey] = db.query(ApiKey).filter_by(users_id=user_id, brokers_name=broker_name).first()
    if db_api_key is None:
        return None

    # Create a clone as models are mutable
    db_api_key_clone = ApiKey(
        users_id=user_id,
        brokers_name=broker_name,
        api_key=db_api_key.api_key,
        private_key=db_api_key.private_key,
    )

    db_api_key_clone.api_key = decrypt_api_key(db_api_key_clone.api_key)

    if db_api_key_clone.private_key:
        db_api_key_clone.private_key = decrypt_api_key(db_api_key_clone.private_key)

    return db_api_key_clone


def create_db_api_key(db: Session, user_id: int, broker_name: str, api_key: ApiKeyCreate) -> ApiKey:
    """Create an API key entry into the database."""
    db_api_key = ApiKey(
        users_id=user_id,
        brokers_name=broker_name,
        api_key=encrypt_api_key(api_key.api_key),
        private_key=encrypt_api_key(api_key.private_key) if api_key.private_key else None,
    )
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key