"""
Module to create request objects for XTB API.
"""

from enum import StrEnum

from xtb_sdk.base_classes import XtbModel


class XtBCommand(StrEnum):
    """
    Enum representing all XTB commands.
    Each command has a string value representing its name.
    """

    GET_ALL_SYMBOLS = "getAllSymbols"


class XtbRequest(XtbModel):
    """
    Request object for XTB API.

    Args:
        command: XtBCommand
    """

    command: XtBCommand


if __name__ == "__main__":
    # test XtbRequest object creation
    request = XtbRequest(command=XtBCommand.GET_ALL_SYMBOLS)
    print(request.dict())
