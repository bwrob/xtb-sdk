"""Module to retrieve credentials from a specified path or default location."""

from os import PathLike
from pathlib import Path

import yaml
from pydantic import StrictStr

from xtb_sdk.data_models.base_classes import DataModel

__CREDENTIALS_PATH = ".xtb"
__CREDENTIALS_FILE = "credentials.yaml"


class Credentials(DataModel):
    """Model to store credentials."""

    user_id: int
    password: StrictStr


CredentialsSource = Credentials | str | PathLike | None


def resolve_credentials(source: CredentialsSource) -> Credentials:
    """
    Function to retrieve credentials from a specified path or default location. If no
    path is provided, the default location is used.

    Args:
        path: Optional[str]

    Returns:
        Credentials

    """
    if not source:
        path = str(Path.home() / __CREDENTIALS_PATH / __CREDENTIALS_FILE)

    try:
        with open(path, "r", encoding="utf-8") as stream:
            config = yaml.safe_load(stream)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {path}") from exc

    return Credentials(**config)
