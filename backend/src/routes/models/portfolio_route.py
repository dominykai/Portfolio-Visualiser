from fastapi import APIRouter

from backend.src.schema.models.portfolio_cash_schema import PortfolioCashBase

portfolio_router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)

