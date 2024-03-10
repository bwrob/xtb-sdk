"""Get all symbols."""

from pprint import pprint

import pandas as pd

from xtb_sdk.clients import APIClient
from xtb_sdk.credentials import get_credentials
from xtb_sdk.request import Command, Request


def main():
    """Run main."""
    # enter your login credentials here
    credentials = get_credentials()

    # create & connect to RR socket
    client = APIClient()

    # connect to RR socket, login
    login_response = client.execute(
        Request(command=Command.LOGIN, arguments=credentials)
    )
    print(login_response)

    resp = client.execute(Request(command=Command.GET_ALL_SYMBOLS))

    for item in resp.return_data[:3]:
        print("\n")
        pprint(item.dict())

    df = pd.DataFrame([item.dict() for item in resp.return_data])
    df.to_csv("all_symbols.csv", sep=";")

    # gracefully close RR socket
    client.disconnect()


if __name__ == "__main__":
    main()
