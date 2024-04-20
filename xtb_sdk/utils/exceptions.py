"""Custom exceptions for the XTB API."""


class ResponseErrorException(Exception):
    """Error response XTB API."""


class LoginErrorException(Exception):
    """Login error response XTB API."""


class SocketErrorException(Exception):
    """Socket error response XTB API."""


class UnknownResponseError(Exception):
    """Unknown error response XTB API."""


class UnexpectedResponseError(Exception):
    """Unknown error response XTB API."""
