from typing import Optional

from sqlalchemy.orm import Session

from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.schema.models.portfolio_cash_schema import PortfolioCashBase


def get_db_portfolio_cash(db: Session, user_id: int, broker_name: str) -> Optional[PortfolioCashBase]:
    """Fetch a portfolio cash record for a given user and broker."""
    return db.query(PortfolioCash).filter_by(users_id=user_id, brokers_name=broker_name).first()

def create_db_portfolio_cash(
        db: Session,
        portfolio_cash: PortfolioCashBase,
        user_id: int,
        broker_name: str,
):
    """Create a new portfolio cash record for a given user and broker."""
    db_portfolio_cash = PortfolioCash(
        users_id=user_id,
        brokers_name=broker_name,
        current_value=portfolio_cash.current_value,
        realised_profit_loss=portfolio_cash.realised_profit_loss,
        total_cost=portfolio_cash.total_cost,
        unrealised_profit_loss=portfolio_cash.unrealised_profit_loss,
        total_value=portfolio_cash.total_value
    )
    db.add(db_portfolio_cash)
    db.commit()
    db.refresh(db_portfolio_cash)
    return db_portfolio_cash