"""Utility functions."""

from collections.abc import Callable

import pandas as pd
from rich import print as rich_print

DEFAULT_STREAMER = rich_print


def inspect_dataframe(
    data: pd.DataFrame,
    stream: Callable[[str], None] = DEFAULT_STREAMER,
) -> None:
    """Inspect the given DataFrame.

    It will print its head, summary, and descriptive statistics.

    Args:
    ----
        data (pd.DataFrame):
            The DataFrame to inspect.
        stream (Callable[[str], None], optional):
            The stream function to use. Defaults to rich_print.

    """
    inspect_msg = (
        f"Dataframe head: \n {data.head()} \n"
        f"Dataframe summary: \n {data.info()} \n"
        f"Dataframe descriptive statistics: \n {data.describe()}\n"
    )
    stream(inspect_msg)
