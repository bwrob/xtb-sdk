# pylint: skip-file


import logging
from threading import Thread

from xtb_sdk.api_socket import Socket
from xtb_sdk.consts import (
    API_MAX_CONN_TRIES,
    DEFAULT_XAPI_ADDRESS,
    DEFUALT_XAPI_STREAMING_PORT,
    LOGGER_NAME,
)

logger = logging.getLogger(LOGGER_NAME)


class APIStreamClient(Socket):
    def __init__(
        self,
        address=DEFAULT_XAPI_ADDRESS,
        port=DEFUALT_XAPI_STREAMING_PORT,
        encrypt=True,
        ssId=None,
        tickFun=None,
        tradeFun=None,
        balanceFun=None,
        tradeStatusFun=None,
        profitFun=None,
        newsFun=None,
    ) -> None:
        super().__init__(address, port, encrypt)
        self._ss_id = ssId

        self._tickFun = tickFun
        self._tradeFun = tradeFun
        self._balanceFun = balanceFun
        self._tradeStatusFun = tradeStatusFun
        self._profitFun = profitFun
        self._newsFun = newsFun

        if not self._connect():
            raise Exception(
                "Cannot connect to streaming on "
                + address
                + ":"
                + str(port)
                + " after "
                + str(API_MAX_CONN_TRIES)
                + " retries",
            )

        self._running = True
        self._t = Thread(target=self._readStream, args=())
        self._t.setDaemon(True)
        self._t.start()

    def _readStream(self) -> None:
        while self._running:
            msg = self._read()
            logger.info("Stream received: " + str(msg))
            if msg["command"] == "tickPrices":
                self._tickFun(msg)
            elif msg["command"] == "trade":
                self._tradeFun(msg)
            elif msg["command"] == "balance":
                self._balanceFun(msg)
            elif msg["command"] == "tradeStatus":
                self._tradeStatusFun(msg)
            elif msg["command"] == "profit":
                self._profitFun(msg)
            elif msg["command"] == "news":
                self._newsFun(msg)

    def disconnect(self) -> None:
        self._running = False
        self._t.join()
        self.close()

    def execute(self, dictionary) -> None:
        self._send_request(dictionary)

    def subscribe_price(self, symbol) -> None:
        self.execute(
            {
                "command": "getTickPrices",
                "symbol": symbol,
                "streamSessionId": self._ss_id,
            },
        )

    def subscribe_prices(self, symbols) -> None:
        for symbolX in symbols:
            self.subscribePrice(symbolX)

    def subscribe_trades(self) -> None:
        self.execute({"command": "getTrades", "streamSessionId": self._ss_id})

    def subscribe_balance(self) -> None:
        self.execute({"command": "getBalance", "streamSessionId": self._ss_id})

    def subscribe_trade_status(self) -> None:
        self.execute({"command": "getTradeStatus", "streamSessionId": self._ss_id})

    def subscribe_profits(self) -> None:
        self.execute({"command": "getProfits", "streamSessionId": self._ss_id})

    def subscribe_news(self) -> None:
        self.execute({"command": "getNews", "streamSessionId": self._ss_id})

    def unsubscribe_price(self, symbol: str) -> None:
        self.execute(
            {
                "command": "stopTickPrices",
                "symbol": symbol,
                "streamSessionId": self._ss_id,
            },
        )

    def unsubscribe_prices(self, symbols) -> None:
        for symbol in symbols:
            self.unsubscribe_price(symbol)

    def unsubscribe_trades(self) -> None:
        self.execute({"command": "stopTrades", "streamSessionId": self._ss_id})

    def unsubscribe_balance(self) -> None:
        self.execute({"command": "stopBalance", "streamSessionId": self._ss_id})

    def unsubscribe_trade_status(self) -> None:
        self.execute({"command": "stopTradeStatus", "streamSessionId": self._ss_id})

    def unsubscribe_profits(self) -> None:
        self.execute({"command": "stopProfits", "streamSessionId": self._ss_id})

    def unsubscribe_news(self) -> None:
        self.execute({"command": "stopNews", "streamSessionId": self._ss_id})
