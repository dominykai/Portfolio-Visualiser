from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.src.database.crud.api_key_crud import get_db_api_key
from backend.src.database.crud.portfolio_crud import get_db_portfolio_cash, create_db_portfolio_cash
from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.services.external.brokers import BROKER_CLASS_MAP


def is_portfolio_cash_valid(portfolio_cash: PortfolioCash) -> bool:
    """Return a boolean indicating whether the given portfolio_cash model is valid for use.
    """
    if portfolio_cash is None:
        return False
    return True

def update_db_portfolio_cash(db: Session, user_id: int, brokers_name: str) -> PortfolioCash:
    """Update the user's portfolio_cash db instance."""

    db_api_keys = get_db_api_key(db, user_id, brokers_name)
    if db_api_keys is None:
        raise HTTPException(status_code=404, detail="User does not have API Keys for requested Broker.")

    broker_class = BROKER_CLASS_MAP[brokers_name]
    broker_instance = broker_class(db_api_keys.api_key, db_api_keys.private_key)

    updated_portfolio_cash = create_db_portfolio_cash(
        db,
        broker_instance.get_cash_information(),
        user_id,
        brokers_name,
    )
    return updated_portfolio_cash

def fetch_portfolio_cash(db: Session, user_id: int, brokers_name: str) -> PortfolioCash:
    """Get the most up-to-date portfolio_cash model of a user's account."""

    db_portfolio_cash = get_db_portfolio_cash(db, user_id, brokers_name)

    if is_portfolio_cash_valid(db_portfolio_cash):
        return db_portfolio_cash

    # user's portfolio_cash is outdated and needs to be updated.
    return update_db_portfolio_cash()