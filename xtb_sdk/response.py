"""
Module to create response objects for XTB API.
"""

from xtb_sdk.base_classes import XtbModel
from xtb_sdk.return_data_records import TEST_LIST, SymbolRecord


class XtbResponse(XtbModel):
    """
    Response object for XTB API.
    """

    status: bool


class XtbError(XtbResponse):
    """
    Error response object for XTB API.
    """

    error_code: str
    error_descr: str


class XtbSuccess(XtbResponse):
    """
    Success response object for XTB API.
    """

    return_data: list[SymbolRecord]


if __name__ == "__main__":
    test_dict = {
        "status": True,
        "returnData": TEST_LIST,
    }

    test_response = XtbResponse.model_validate(test_dict)
    test_succes = XtbSuccess.model_validate(test_dict)
    from pprint import pprint

    pprint(test_response)
    pprint(test_succes)
