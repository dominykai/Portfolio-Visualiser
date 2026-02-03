from abc import ABC, abstractmethod
from requests import get, HTTPError
from starlette.exceptions import HTTPException

from backend.src.schema.models.portfolio_cash_schema import PortfolioCash


class AbstractBroker(ABC):
    BASE_URL: str = None

    def __init__(self, api_key: str, private_key: str):
        if self.BASE_URL is None:
            raise NotImplementedError(self.__class__.__name__ + " does not have a BASE_URL set")

        self.api_key = api_key
        self.private_key = private_key

    @abstractmethod
    def get_cash_information(self) -> PortfolioCash:
        """Create a PortfolioCash object given the Broker's external API."""
        raise NotImplementedError(self.__class__.__name__ + " does not have a get_cash_information method")

    def send_request(self, method: str, endpoint: str, params: dict = None) -> dict:
        """Send a request to a given API endpoint.

        :param method: The HTTP method to use.
        :param endpoint: The API Endpoint path.
        :param params: Optional request parameters.
        :return: Response object as a dict.
        """
        url = self.BASE_URL + endpoint
        method = method.upper()

        response = {}
        try:
            if method == "GET":
                response = get(url=url, params=params, auth=(self.api_key, self.private_key))

            response.raise_for_status()

        except HTTPError:
            # Wrap requests.HTTPError to FastAPI.HTTPException
            raise HTTPException(
                status_code=response.status_code,
            )

        return response.json()
