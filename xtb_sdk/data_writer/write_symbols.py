"""Writer for symbols."""

from xtb_sdk.data_models.credentials import CredentialsSource
from xtb_sdk.data_requester.requester import DataRequester
from xtb_sdk.utils.df_utils import inspect_dataframe
from xtb_sdk.utils.logging import get_logger

logger = get_logger()


def write_symbols(credentials_source: CredentialsSource = None) -> None:
    """
    Writes symbol data to a CSV file.

    Args:
        credentials_source: The source of credentials (default is None).

    Returns:
        None

    """

    with DataRequester(credentials_source) as requester:
        symbols = requester.get_symbols()

    inspect_dataframe(symbols)
    symbols.to_csv("all_symbols.csv", sep=";")


if __name__ == "__main__":
    write_symbols()
