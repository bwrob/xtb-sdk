"""Logging utilities."""

import logging

LOGGING_FORMAT = "[%(asctime)-15s][%(funcName)s:%(lineno)d] %(message)s"
LOGGER_NAME = "xtb_logger"


def get_logger() -> logging.Logger:
    """Provides a default logger for use in the package."""
    logger = logging.getLogger(LOGGER_NAME)
    logging.basicConfig(format=LOGGING_FORMAT)
    return logger
