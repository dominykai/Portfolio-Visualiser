from starlette.exceptions import HTTPException

from backend.src.services.external.brokers.abstract_broker import AbstractBroker


class Trading212Service(AbstractBroker):
    BASE_URL = "https://live.trading212.com"

    # Accounts
    def _get_account_summary(self) -> dict:
        """Provides a breakdown of your account's cash and investment metrics, including available funds,
         invested capital, and total account value."""
        return self.send_request("GET", "/api/v0/equity/account/summary")
