from typing import Optional

from sqlalchemy.orm import Session

from backend.src.database.models.user_model import User


def get_db_user_by_email(db: Session, email: str) -> Optional[User]:
    """Return a user in the database by email."""
    return db.query(User).filter(User.email == email).first()