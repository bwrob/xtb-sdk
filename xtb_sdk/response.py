"""Module to create response objects for XTB API."""

from xtb_sdk.base_classes import DataModel
from xtb_sdk.return_data_records import TEST_LIST, SymbolRecord


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


if __name__ == "__main__":
    test_dict = {
        "status": True,
        "returnData": TEST_LIST,
    }

    test_response = Response.model_validate(test_dict)
    test_succes = ResponseSuccess.model_validate(test_dict)
    from pprint import pprint

    pprint(test_response)
    pprint(test_succes)