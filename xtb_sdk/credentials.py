"""Module to retrieve credentials from a specified path or default location."""

from pathlib import Path

import yaml
from pydantic import StrictStr

from xtb_sdk.base_classes import DataModel
from xtb_sdk.consts import ENCODING

__CREDENTIALS_PATH = ".xtb"
__CREDENTIALS_FILE = "credentials.yaml"


class Credentials(DataModel):
    """Model to store credentials."""

    user_id: int
    password: StrictStr


def get_credentials(path: str | None = None) -> Credentials:
    """Retrieve credentials from a specified path or default location.

    If no path is provided, the default location is used.

    Args:
    ----
        path: Optional[str]

    """
    if not path:
        path = str(Path.home() / __CREDENTIALS_PATH / __CREDENTIALS_FILE)

    try:
        with Path(path).open(encoding=ENCODING) as stream:
            config: dict[str, str] = yaml.safe_load(stream)
    except FileNotFoundError as exc:
        msg = f"File not found: {path}"
        raise FileNotFoundError(msg) from exc

    user_id = int(config["user_id"])
    password = config["password"]
    return Credentials(user_id=user_id, password=password)


if __name__ == "__main__":
    cred = get_credentials()
