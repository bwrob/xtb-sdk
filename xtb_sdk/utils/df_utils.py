"""Utility functions."""

from io import StringIO

import pandas as pd

from xtb_sdk.utils.logging import get_logger

logger = get_logger()


def inspect_dataframe(
    data: pd.DataFrame,
) -> None:
    """Inspect the given DataFrame by printing its head, summary, and descriptive
    statistics.

    Args:
        data (pd.DataFrame): The DataFrame to inspect.

    """
    # info prints to sys.stdout, provide buffer to capture output
    buffer = StringIO()
    data.info(buf=buffer)
    info_string = buffer.getvalue()

    inspect_msg = (
        f"Dataframe head: \n {data.head()} \n"
        f"Dataframe summary: \n {info_string} \n"
        f"Dataframe descriptive statistics: \n {data.describe()}\n"
    )
    logger.info(inspect_msg)
