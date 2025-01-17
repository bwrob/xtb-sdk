"""Module for the XTB API client."""

from types import TracebackType
from typing import TYPE_CHECKING, Self

import pandas as pd

from xtb_sdk.data_models.credentials import (
    Credentials,
    CredentialsSource,
    resolve_credentials,
)
from xtb_sdk.data_models.request import Command, Request
from xtb_sdk.data_models.response import ResponseError
from xtb_sdk.data_requester.api_client import APIClient
from xtb_sdk.utils.df_utils import inspect_dataframe
from xtb_sdk.utils.exceptions import ResponseErrorException
from xtb_sdk.utils.logging import get_logger

if TYPE_CHECKING:
    from xtb_sdk.data_requester.api_streaming_client import APIStreamClient

logger = get_logger()


class DataRequester:
    """Data requester for the XTB API."""

    def __init__(
        self,
        credentials_source: CredentialsSource = None,
    ) -> None:
        """Constructor for the API client.

        Args:
            credentials: Credentials object
            address: IP address
            port: Port
            encrypt: Whether to use SSL
            debug: Whether to print debug messages

        """
        self._credentials_source: CredentialsSource = credentials_source
        self._credentials: Credentials | None = None
        self._client: APIClient | None = None
        self._client_streaming: APIStreamClient | None = None
        self._stream_session_id: int | None = None

    def __enter__(self) -> Self:
        """Context manager for the API client."""
        credentials = resolve_credentials(self._credentials_source)
        logger.info("Credentials resoloved.")

        # create & connect to RR socket
        self._client = APIClient()
        self._stream_session_id = self.client.connect(credentials)
        return self

    def __exit__(
        self,
        exc_type: type,
        exc_value: BaseException,
        traceback: TracebackType,
    ) -> None:
        """Exit context manager for the API client.

        Args:
            exc_type: Type of the exception that caused the context manager to exit
            exc_value: The exception instance
            traceback: Traceback object

        Returns:
            None

        """
        self.client.close()

    @property
    def stream_session_id(self):
        """Get the stream session id."""
        if self._stream_session_id is None:
            logger.error(
                "Stream session id is only avaliable"
                "inside DataRequester context manager."
            )
        return self._stream_session_id

    @property
    def client(self):
        """Get the client."""
        if self._client is None:
            logger.error(
                "Client is only avaliable inside DataRequester context manager."
            )
        return self._client

    def get_symbols(self):
        """Run main."""
        # enter your login credentials here

        symbols_response = self.client.execute(
            Request(command=Command.GET_ALL_SYMBOLS)
        )

        if isinstance(symbols_response, ResponseError):
            msg = f"Symbols retrieval failed. Error code: {symbols_response.error_code}"
            raise ResponseErrorException(msg)

        logger.info(
            "Symbols retrieval successful.\n Retrived %s symbols.",
            len(symbols_response.return_data),
        )

        symbols = pd.DataFrame(
            [item.dict() for item in symbols_response.return_data]
        )
        inspect_dataframe(symbols)
        return symbols
