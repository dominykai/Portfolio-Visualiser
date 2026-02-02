from datetime import timedelta, timezone, datetime
from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session
from starlette import status
from starlette.exceptions import HTTPException

from backend.src.core.config_loader import settings
from backend.src.database.crud.user_crud import get_db_user_by_email
from backend.src.database.db import get_db
from backend.src.database.models.user_model import User
from backend.src.schema.auth.token_schema import TokenData
from backend.src.utils.auth_utils import verify_password_hash

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
JWT_ACCESS_TOKEN_EXPIRY = settings.JWT_ACCESS_TOKEN_EXPIRY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def authenticate_user(email: str, password: str, db: Session = Depends(get_db)):
    """
    Check if the user is valid by comparing email and password.

    :param email: The user's email.
    :param password: The inputted password.
    :param db: The database session.
    :return: A user if authenticated, False otherwise.
    """
    user = get_db_user_by_email(db, email)

    if not user:
        return False
    if not verify_password_hash(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create an encoded JWT token of the given data."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRY)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    """Retrieve the user row from a database corresponding to the given access token.

    Use `get_current_active_user` instead for more rigorous checks."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)

    except InvalidTokenError:
        raise credentials_exception

    user = get_db_user_by_email(db, token_data.email)

    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """Retrieve the current user data with more checks."""
    return current_user