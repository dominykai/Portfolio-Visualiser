from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_crud import get_db_api_key, create_db_api_key
from backend.src.database.db import get_db
from backend.src.database.models.user_model import User
from backend.src.schema.models.api_key_schema import ApiKeySchema, ApiKeyCreate
from backend.src.services.auth.auth_service import get_current_active_user

api_key_router = APIRouter(
    prefix="/api_keys",
    tags=["API Keys"]
)

@api_key_router.get("/{broker_name}", response_model=ApiKeySchema)
def route_get_api_key(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return get_db_api_key(db, current_user.id, broker_name)

@api_key_router.post("/{broker_name}")
def route_post_api_key(
        broker_name: str,
        api_key: ApiKeyCreate,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return create_db_api_key(db, current_user.id, broker_name, api_key)