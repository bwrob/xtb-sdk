"""Module for the XTB API client."""

import json

from pydantic import ValidationError

from xtb_sdk.data_models.credentials import Credentials
from xtb_sdk.data_models.request import Command, Request
from xtb_sdk.data_models.response import (
    ResponseError,
    ResponseStreamSession,
    ResponseSuccess,
    ResponseType,
)
from xtb_sdk.data_requester.api_socket import Socket, StreamSessionId
from xtb_sdk.utils.consts import ENCODING, FILE_WRITE
from xtb_sdk.utils.exceptions import (
    LoginErrorException,
    UnexpectedResponseError,
    UnknownResponseError,
)
from xtb_sdk.utils.logging import get_logger

logger = get_logger()


UNKNOWN_RESPONSE_PATH = "unknown_response.json"


class APIClient(Socket):
    """Client for the XTB API."""

    def execute(
        self,
        request: Request,
    ) -> ResponseType:
        """
        Execute a request.

        Args:
            request: Request object

        """
        self._send_request(request)
        resp = self._read()
        logger.debug(resp)
        try:
            if request.command == Command.LOGIN:
                return ResponseStreamSession.model_validate(resp)
            return ResponseSuccess.model_validate(resp)
        except ValidationError:
            # if response is not a success, validate error response
            try:
                return ResponseError.model_validate(resp)
            except ValidationError as e:
                # if we don't know what the response is, save the response to file
                with open(UNKNOWN_RESPONSE_PATH, FILE_WRITE, encoding=ENCODING) as f:
                    f.write(json.dumps(resp))
                raise UnknownResponseError(
                    f"Unknown response, saved to {UNKNOWN_RESPONSE_PATH}"
                ) from e

    def connect(self, credentials: Credentials) -> StreamSessionId:
        """
        Context manager for the API client.

        Args:
            credentials: Credentials object

        """
        # connect to RR socket
        if not self._connect():
            raise ConnectionError(f"Cannot connect to {self._address} : {self._port}.")

        logger.info("Socket connected")

        # login to RR socket
        login_response = self.execute(
            Request(command=Command.LOGIN, arguments=credentials)
        )

        if isinstance(login_response, ResponseError):
            logger.error("Login failed - %s", login_response)
            raise LoginErrorException(
                f"Login failed. Error code: {login_response.error_code}"
            )

        if isinstance(login_response, ResponseStreamSession):
            logger.info("Login successful - %s", login_response)
            return login_response.stream_session_id

        raise UnexpectedResponseError(
            f"Unexpected bahaviour recived response - {login_response}"
        )

    def close(self) -> None:
        """Closes the connection and logs the closure of the connection to the RR
        socket."""
        self._close()
        logger.info("Connection to RR socket closed.")
