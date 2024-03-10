"""Get all symbols."""

import logging

import pandas as pd

from xtb_sdk.api_client import APIClient
from xtb_sdk.consts import LOGGER_NAME
from xtb_sdk.credentials import get_credentials
from xtb_sdk.exceptions import ResponseErrorException
from xtb_sdk.request import Command, Request

logger = logging.getLogger(LOGGER_NAME)
FORMAT = "[%(asctime)-15s][%(funcName)s:%(lineno)d] %(message)s"
logging.basicConfig(format=FORMAT)


def get_symbols():
    """Run main."""
    # enter your login credentials here
    credentials = get_credentials()

    # create & connect to RR socket
    client = APIClient(credentials)
    with client.connection() as conn:
        symbols_response = conn.execute(Request(command=Command.GET_ALL_SYMBOLS))

    if not symbols_response.status:
        raise ResponseErrorException(
            f"Symbols retrieval failed. Error code: {symbols_response.error_code}"
        )

    print(
        f"Symbols retrieval successful. "
        f"Retrived {len(symbols_response.return_data)} symbols."
    )
    symbols = pd.DataFrame([item.dict() for item in symbols_response.return_data])
    symbols.to_csv("all_symbols.csv", sep=";")


if __name__ == "__main__":
    get_symbols()
