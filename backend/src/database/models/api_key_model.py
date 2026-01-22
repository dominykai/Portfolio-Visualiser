from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.db import Base


class ApiKey(Base):
    __tablename__ = "api_keys"

    api_key: Mapped[str] = mapped_column(String, nullable=False)
    private_key: Mapped[str] = mapped_column(String)

    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    brokers_name: Mapped[str] = mapped_column(ForeignKey("brokers.name"), primary_key=True)