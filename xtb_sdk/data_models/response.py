"""Module to create response objects for XTB API."""

from xtb_sdk.data_models.base_classes import DataModel
from xtb_sdk.data_models.return_data_records import SymbolRecord


class Response(DataModel):
    """Response object for XTB API."""

    status: bool


class ResponseError(Response):
    """Error response object for XTB API."""

    error_code: str
    error_descr: str


class ResponseSuccess(Response):
    """Success response object for XTB API."""

    return_data: list[SymbolRecord]


class ResponseStreamSession(Response):
    """Stream session response object for XTB API."""

    stream_session_id: str


ResponseType = ResponseSuccess | ResponseError | ResponseStreamSession
