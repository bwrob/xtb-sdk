"""Utility functions."""

from collections.abc import Callable

import pandas as pd

DEFAULT_STREAMER = print


def inspect_dataframe(
    data: pd.DataFrame,
    stream: Callable[[str], None] = DEFAULT_STREAMER,
) -> None:
    """Inspect the given DataFrame by printing its head, summary, and descriptive
    statistics.

    Args:
        data (pd.DataFrame): The DataFrame to inspect.

    """
    inspect_msg = (
        f"Dataframe head: \n {data.head()} \n"
        f"Dataframe summary: \n {data.info()} \n"
        f"Dataframe descriptive statistics: \n {data.describe()}\n"
    )
    stream(inspect_msg)
