"""Test function to validate a response object."""

import json
import os

from xtb_sdk.consts import ENCODING, FILE_READ
from xtb_sdk.response import ResponseSuccess

RESPONSE_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "responses")


def test_response(json_path: str) -> ResponseSuccess:
    """Test function to validate a response object."""
    with open(json_path, FILE_READ, encoding=ENCODING) as f:
        test_dict = json.load(f)
    return ResponseSuccess.model_validate(test_dict)


if __name__ == "__main__":
    print("Testing responses..." f"\nPath: {RESPONSE_DATA_PATH}")

    test_cases = os.listdir(RESPONSE_DATA_PATH)

    for test_case in test_cases:
        case_path = os.path.join(RESPONSE_DATA_PATH, test_case)
        validated_response = test_response(case_path)

    print("All tests passed!")
