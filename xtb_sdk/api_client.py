"""Module for the XTB API client."""

import logging
from contextlib import contextmanager

from pydantic import ValidationError

from xtb_sdk.api_socket import Socket
from xtb_sdk.consts import DEFAULT_XAPI_ADDRESS, DEFAULT_XAPI_PORT, LOGGER_NAME
from xtb_sdk.credentials import Credentials
from xtb_sdk.exceptions import LoginErrorException
from xtb_sdk.request import Command, Request
from xtb_sdk.response import ResponseError, ResponseStreamSession, ResponseSuccess

logger = logging.getLogger(LOGGER_NAME)


class APIClient(Socket):
    """Client for the XTB API."""

    def __init__(
        self,
        credentials: Credentials,
        *,
        address: str = DEFAULT_XAPI_ADDRESS,
        port: int = DEFAULT_XAPI_PORT,
        encrypt: bool = True,
    ):
        """
        Constructor for the API client.

        Args:
            credentials: Credentials object
            address: IP address
            port: Port
            encrypt: Whether to use SSL

        """
        super().__init__(address, port, encrypt)
        self.__stream_session_id = None
        self.__credentials = credentials

    @property
    def stream_session_id(self):
        """Get the stream session id."""
        if self.__stream_session_id is None:
            print("stream session id is not available")
        return self.__stream_session_id

    def execute(
        self,
        request: Request,
    ) -> ResponseSuccess | ResponseError | None:
        """
        Execute a request.

        Args:
            request: Request object

        """
        self._send_request(request)
        resp = self._read()
        try:
            if request.command == Command.LOGIN:
                return ResponseStreamSession.model_validate(resp)
            return ResponseSuccess.model_validate(resp)
        except ValidationError:
            return ResponseError.model_validate(resp)

    @contextmanager
    def connection(self):
        """Context manager for the API client."""
        # connect to RR socket
        if not self._connect():
            raise ConnectionError(f"Cannot connect to {self._address} : {self._port}.")

        # login to RR socket
        login_response = self.execute(
            Request(command=Command.LOGIN, arguments=self.__credentials)
        )
        if not login_response.status:
            raise LoginErrorException(
                f"Login failed. Error code: {login_response.error_code}"
            )
        self.__stream_session_id = login_response.stream_session_id
        print(f"Login successful - {login_response}")

        try:
            yield self
        finally:
            self._close()
