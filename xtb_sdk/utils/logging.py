"""Logging utilities."""

import logging

__LOGGING_FORMAT = "[%(asctime)-15s][%(funcName)s:%(lineno)d] %(message)s"
__LOGGER_NAME = "xtb"
__LOGGER_NAME_WEBSOCKETS_CLIENT = "websockets.client"
__LOGGER_NAME_WEBSOCKETS_SERVER = "websockets.server"
__LOGGER_LEVEL = logging.INFO

logging.basicConfig(format=__LOGGING_FORMAT, level=__LOGGER_LEVEL)


def get_logger() -> logging.Logger:
    """Provides a default logger for use in the package."""
    logger = logging.getLogger(__LOGGER_NAME)
    logging.basicConfig(format=__LOGGING_FORMAT, level=logging.DEBUG)
    return logger


def enable_debug_mode() -> None:
    """Enable debug mode."""
    for name in (
        __LOGGER_NAME,
        __LOGGER_NAME_WEBSOCKETS_CLIENT,
        __LOGGER_NAME_WEBSOCKETS_SERVER,
    ):
        logging.getLogger(name).setLevel(logging.DEBUG)
