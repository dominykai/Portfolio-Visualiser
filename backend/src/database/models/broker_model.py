from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.db import Base


class Broker(Base):
    __tablename__ = "brokers"

    name: Mapped[str] = mapped_column(String, primary_key=True)