from abc import ABC, abstractmethod
from requests import get, HTTPError

from backend.src.database.models.portfolio_model import PortfolioCash
from backend.src.services.external.brokers.external_brokers_exceptions import *


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

        except HTTPError as http_err:
            match http_err.response.status_code:
                case 401:
                    raise BadAPIKeyException()
                case 403:
                    raise InsufficientAPIKeyPermissionsException()
                case 408:
                    raise TimedOutRequestException()
                case 429:
                    raise ResponseRateLimitedException()
                case _:
                    raise NotImplementedError(
                        f"""
                        Error code status {http_err.response.status_code} not implemented for external broker
                        {self.__class__.__name__} with response message {http_err.response.text}
                        """
                    )


        return response.json()
