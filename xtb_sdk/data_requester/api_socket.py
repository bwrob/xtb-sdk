"""RR Socket class."""

import json
import logging
import socket
import ssl
import time

from xtb_sdk.consts import API_MAX_CONN_TRIES, API_SEND_TIMEOUT, LOGGER_NAME
from xtb_sdk.data_model.request import Request

logger = logging.getLogger(LOGGER_NAME)


class Socket:
    """RR Socket class."""

    def __init__(self, address, port, encrypt=True):
        """Constructor."""
        self._ssl = encrypt
        if not self._ssl:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket = ssl.wrap_socket(sock)  # pylint: disable=W4902
        self.conn = self.socket
        self._timeout = None
        self._address = address
        self._port = port
        self._decoder = json.JSONDecoder()
        self._received_data = ""

    def _connect(self):
        """Connect to RR socket."""
        for _ in range(API_MAX_CONN_TRIES):
            try:
                self.socket.connect((self._address, self._port))
            except socket.error as msg:
                logger.error("SockThread Error: %s", msg)
                time.sleep(0.25)
                continue
            logger.info("Socket connected")
            return True
        return False

    def _send_request(self, request: Request):
        """Send a request to RR socket."""
        msg = request.json(exclude_none=True)
        self._waiting_send(msg)

    def _waiting_send(self, msg):
        """Send a message to RR socket."""
        if self.socket:
            sent = 0
            msg = msg.encode("utf-8")
            while sent < len(msg):
                sent += self.conn.send(msg[sent:])
                logger.info("Sent: %s", msg)
                time.sleep(API_SEND_TIMEOUT / 1000)

    def _read(self, bytes_size=4096):
        if not self.socket:
            raise RuntimeError("Socket connection broken.")
        while True:
            char = self.conn.recv(bytes_size).decode()
            self._received_data += char
            try:
                (resp, size) = self._decoder.raw_decode(self._received_data)
                if size == len(self._received_data):
                    self._received_data = ""
                    break
                if size < len(self._received_data):
                    self._received_data = self._received_data[size:].strip()
                    break
            except ValueError:
                continue
        logger.info("Received: %s", resp)
        return resp

    def _close(self):
        logger.debug("Closing socket.")
        self.socket.close()
        if self.socket is not self.conn:
            logger.debug("Closing connection socket.")
            self.conn.close()
