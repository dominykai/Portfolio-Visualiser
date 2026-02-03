from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.src.database.db import get_db
from backend.src.database.models.user_model import User
from backend.src.schema.models.portfolio_cash_schema import PortfolioCashBase
from backend.src.services.auth.auth_service import get_current_active_user
from backend.src.services.models.portfolio_service import fetch_portfolio_cash

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@portfolio_router.get("/{broker_name}", response_model=PortfolioCashBase)
def route_get_portfolio_cash(
        broker_name: str,
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
):
    return fetch_portfolio_cash(db, current_user.id, broker_name)