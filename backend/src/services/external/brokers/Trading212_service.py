from backend.src.schema.models.portfolio_cash_schema import PortfolioCashBase
from backend.src.services.external.brokers.abstract_broker import AbstractBroker


class Trading212Service(AbstractBroker):
    BASE_URL = "https://live.trading212.com"

    def get_cash_information(self) -> PortfolioCashBase:
        get_account_summary = self._get_account_summary()

        return PortfolioCashBase(
            current_value=get_account_summary["investments"]["currentValue"],
            realised_profit_loss=get_account_summary["investments"]["realizedProfitLoss"],
            total_cost=get_account_summary["investments"]["totalCost"],
            unrealised_profit_loss=get_account_summary["investments"]["unrealizedProfitLoss"],
            total_value=get_account_summary["totalValue"],
        )

    # Accounts
    def _get_account_summary(self) -> dict:
        """Provides a breakdown of your account's cash and investment metrics, including available funds,
         invested capital, and total account value."""
        return self.send_request("GET", "/api/v0/equity/account/summary")
