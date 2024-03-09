from pathlib import Path
from typing import Optional

import yaml
from pydantic import StrictStr

from xtb_sdk.base_classes import XtbModel

__CREDENTIALS_PATH = ".xtb"
__CREDENTIALS_FILE = "credentials.yaml"


class Credentials(XtbModel):
    """
    A class representing credentials.

    Attributes:
        user_id (int): The user ID.
        password (StrictStr): The password.

    """
    user_id: int
    password: StrictStr



def get_credentials(path: Optional[str] = None) -> Credentials:
    """Reads a YAML file containing credentials.

    Args:
        path (str, optional): The path to the YAML file containing the credentials. 
            If not provided, the default path will be used. (default: None)

    Returns:
        Credentials: An instance of the Credentials class with the values loaded from the YAML file.

    Raises:
        FileNotFoundError: If the file specified by the path does not exist.

    Extra instructions:
        - The default path is determined by combining the user's home directory, 
        the ".xtb" directory, and the "credentials.yaml" file.
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
