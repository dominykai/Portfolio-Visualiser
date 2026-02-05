from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.db import Base


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True)

    api_keys: Mapped[List["ApiKey"]] = relationship()
    portfolio_cash: Mapped[List["PortfolioCash"]] = relationship(back_populates="broker")