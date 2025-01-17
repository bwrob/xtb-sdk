"""Tests for the credentials module."""

from xtb_sdk.data_models.credentials import resolve_credentials


def test_credentials() -> None:
    resolve_credentials(None)
