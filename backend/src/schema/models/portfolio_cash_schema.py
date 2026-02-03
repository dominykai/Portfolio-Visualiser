from pydantic import BaseModel

class PortfolioCashBase(BaseModel):
    current_value: float # Current value of all investments
    realised_profit_loss: float # The all-time realised profit loss from all the trades executed
    total_cost: float # The cost basis of your current investments
    unrealised_profit_loss: float # The potential profit loss of all your current investments
    total_value: float # Investments value

