"""Get all symbols."""

import pandas as pd

from xtb_sdk.clients import APIClient
from xtb_sdk.credentials import get_credentials
from xtb_sdk.exceptions import ResponseErrorException
from xtb_sdk.request import Command, Request


def get_symbols():
    """Run main."""
    # enter your login credentials here
    credentials = get_credentials()

    # create & connect to RR socket
    client = APIClient(credentials=credentials)
    with client.connection() as conn:
        symbols_response = conn.execute(Request(command=Command.GET_ALL_SYMBOLS))

    if not symbols_response.status:
        raise ResponseErrorException(
            f"Symbols retrieval failed. Error code: {symbols_response.errorCode}"
        )

    print(
        f"Symbols retrieval successful. "
        f"Retrived {len(symbols_response.return_data)} symbols."
    )
    symbols = pd.DataFrame([item.dict() for item in symbols_response.return_data])
    symbols.to_csv("all_symbols.csv", sep=";")


if __name__ == "__main__":
    get_symbols()
