"""Custom exceptions for the XTB API."""


class ResponseError(Exception):
    """Error response XTB API."""


class LoginError(Exception):
    """Login error response XTB API."""


class SocketError(Exception):
    """Socket error response XTB API."""


class UnknownResponseError(Exception):
    """Unknown error response XTB API."""
