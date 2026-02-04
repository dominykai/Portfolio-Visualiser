from starlette.exceptions import HTTPException

from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.services.external.brokers.abstract_broker import AbstractBroker


class Trading212Service(AbstractBroker):
    BASE_URL = "https://live.trading212.com"

    def get_cash_information(self) -> PortfolioCash:
        portfolio_cash = PortfolioCash()


        return portfolio_cash_model

    # Accounts
    def _get_account_summary(self) -> dict:
        """Provides a breakdown of your account's cash and investment metrics, including available funds,
         invested capital, and total account value."""
        return self.send_request("GET", "/api/v0/equity/account/summary")
