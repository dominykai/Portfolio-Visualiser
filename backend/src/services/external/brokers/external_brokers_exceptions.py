
class BadAPIKeyException(Exception):
    """
    Exception raised when the external broker returns a 401 error response, indicating
    that the API key supplied is invalid.
    """

class InsufficientAPIKeyPermissionsException(Exception):
    """
    Exception raised when the external broker returns a 403 error response, indicating
    that the API key does not have the sufficient permissions to perform the request.
    """

class TimedOutRequestException(Exception):
    """
    Exception raised when the external broker returns a 408 error response, indicating
    that the request timed-out.
    """

class ResponseRateLimitedException(Exception):
    """
    Exception raised when the external broker returns a 429 error response, indicating
    that the rate limit has been exceeded.
    """