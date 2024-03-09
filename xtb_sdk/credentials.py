from pathlib import Path
from typing import Optional

import yaml
from pydantic import StrictStr

from xtb_sdk.base_classes import XtbModel

__CREDENTIALS_PATH = ".xtb"
__CREDENTIALS_FILE = "credentials.yaml"


class Credentials(XtbModel):
    user_id: int
    password: StrictStr


def get_credentials(path: Optional[str] = None) -> Credentials:
    """
    Function to retrieve credentials from a specified path or default location. 
    If no path is provided, the default location is used. 
    Raises FileNotFoundError if the specified path is not found. 
    Returns a Credentials object.
    """
    if not path:
        path = str(Path.home() / __CREDENTIALS_PATH / __CREDENTIALS_FILE)

    try:
        with open(path, "r") as stream:
            config = yaml.safe_load(stream)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    return Credentials(**config)


if __name__ == "__main__":
    config = get_credentials()
    print(config.dict(by_alias=True))
