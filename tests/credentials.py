"""Tests for the credentials module."""

from xtb_sdk.data_models.credentials import resolve_credentials


def test_credentials():
    cred = resolve_credentials(None)
    print(cred.dict(by_alias=True))
