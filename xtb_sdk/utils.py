"""Utility functions."""

from io import StringIO
from typing import Callable

import pandas as pd

DEFAULT_STREAMER = print


def inspect_dataframe(
    data: pd.DataFrame,
    stream: Callable[[str], None] = DEFAULT_STREAMER,
) -> None:
    """
    Inspect the given DataFrame by printing its head, summary, and descriptive
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
    stream(inspect_msg)
