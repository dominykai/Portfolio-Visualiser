from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.user_crud import create_db_user
from backend.src.database.db import get_db
from backend.src.database.models.user_model import User
from backend.src.schema.models.user_schema import UserSchema, UserCreate
from backend.src.services.auth.auth_service import get_current_active_user

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/", response_model=UserSchema)
def route_get_user(current_user: User = Depends(get_current_active_user)):
    return current_user

@user_router.post("/", response_model=UserSchema)
def route_post_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_db_user(db, user)