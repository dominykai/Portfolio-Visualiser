from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.db import Base


class PortfolioCash(Base):
    __tablename__ = "portfolio_cash"

    current_value: Mapped[float] = mapped_column(Float)
    realised_profit_loss: Mapped[float] = mapped_column(Float)
    total_cost: Mapped[float] = mapped_column(Float)
    unrealised_profit_loss: Mapped[float] = mapped_column(Float)
    total_value: Mapped[float] = mapped_column(Float)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    brokers_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), primary_key=True)