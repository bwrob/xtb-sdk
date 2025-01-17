"""Module to create request objects for XTB API."""

from enum import StrEnum

from xtb_sdk.data_models.base_classes import DataModel
from xtb_sdk.data_models.credentials import Credentials


class Command(StrEnum):
    """Enum representing all XTB commands.

    Each command has a string value representing its name.

    """

    GET_ALL_SYMBOLS = "getAllSymbols"
    LOGIN = "login"


class Request(DataModel):
    """Request object for XTB API.

    Args:
        command: XtBCommand

    """

    command: Command
    arguments: Credentials | None = None


if __name__ == "__main__":
    # test Request object creation
    request = Request(command=Command.GET_ALL_SYMBOLS)
