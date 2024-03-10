"""Module to create response objects for XTB API."""

from pydantic import Field

from xtb_sdk.base_classes import DataModel


class SymbolRecord(DataModel):
    """SymbolRecord model."""

    ask: float
    bid: float
    category_name: str
    contract_size: float
    currency: str
    currency_pair: bool
    currency_profit: str
    description: str
    expiration: str | None
    group_name: str
    high: float
    initial_margin: float
    instant_max_volume: float
    leverage: float
    long_only: bool
    lot_max: float
    lot_min: float
    lot_step: float
    low: float
    margin_hedged: float
    margin_hedged_strong: bool
    margin_maintenance: float
    margin_mode: float
    percentage: float
    pips_precision: int
    precision: int
    profit_mode: float
    quote_id: int
    short_selling: bool
    spread_raw: float
    spread_table: float
    starting: str | None
    step_rule_id: int
    stops_level: float
    swap_rollover3days: float
    swap_enable: bool
    swap_long: float
    swap_short: float
    swap_type: float
    symbol: str
    tick_size: float
    tick_value: float
    time: int
    time_string: str
    trailing_enabled: bool
    type_: int = Field(alias="type")


TEST_LIST = [
    {
        "ask": 14.63,
        "bid": 14.61,
        "categoryName": "STC",
        "contractSize": 1,
        "currency": "USD",
        "currencyPair": False,
        "currencyProfit": "USD",
        "description": "TEGNA Inc",
        "exemode": 1,
        "expiration": None,
        "groupName": "US",
        "high": 14.89,
        "initialMargin": 0,
        "instantMaxVolume": 2147483647,
        "leverage": 100.0,
        "longOnly": True,
        "lotMax": 1000000.0,
        "lotMin": 1.0,
        "lotStep": 1.0,
        "low": 14.57,
        "marginHedged": 0,
        "marginHedgedStrong": False,
        "marginMaintenance": 0,
        "marginMode": 104,
        "percentage": 100.0,
        "pipsPrecision": 2,
        "precision": 2,
        "profitMode": 6,
        "quoteId": 6,
        "quoteIdCross": 15,
        "shortSelling": False,
        "spreadRaw": 0.02,
        "spreadTable": 2.0,
        "starting": None,
        "stepRuleId": 12,
        "stopsLevel": 0,
        "swapEnable": True,
        "swapLong": 0.0,
        "swapShort": 0.0,
        "swapType": 2,
        "swap_rollover3days": 0,
        "symbol": "TGNA.US_9",
        "tickSize": 0.01,
        "tickValue": 0.01,
        "time": 1709931563963,
        "timeString": "Fri Mar 08 21:59:23 CET 2024",
        "trailingEnabled": False,
        "type": 2436,
    },
    {
        "ask": 4.17,
        "bid": 4.15,
        "categoryName": "STC",
        "contractSize": 1,
        "currency": "USD",
        "currencyPair": False,
        "currencyProfit": "USD",
        "description": "Sirius XM Holdings Inc",
        "exemode": 1,
        "expiration": None,
        "groupName": "US",
        "high": 4.22,
        "initialMargin": 0,
        "instantMaxVolume": 2147483647,
        "leverage": 100.0,
        "longOnly": True,
        "lotMax": 1000000.0,
        "lotMin": 1.0,
        "lotStep": 1.0,
        "low": 4.11,
        "marginHedged": 0,
        "marginHedgedStrong": False,
        "marginMaintenance": 0,
        "marginMode": 104,
        "percentage": 100.0,
        "pipsPrecision": 2,
        "precision": 2,
        "profitMode": 6,
        "quoteId": 6,
        "quoteIdCross": 15,
        "shortSelling": False,
        "spreadRaw": 0.02,
        "spreadTable": 2.0,
        "starting": None,
        "stepRuleId": 12,
        "stopsLevel": 0,
        "swapEnable": True,
        "swapLong": 0.0,
        "swapShort": 0.0,
        "swapType": 2,
        "swap_rollover3days": 0,
        "symbol": "SIRI.US_9",
        "tickSize": 0.01,
        "tickValue": 0.01,
        "time": 1709931006408,
        "timeString": "Fri Mar 08 21:50:06 CET 2024",
        "trailingEnabled": False,
        "type": 2436,
    },
]

if __name__ == "__main__":

    symbols = [
        SymbolRecord.model_validate(test_dict) for test_dict in SymbolRecord.TEST_LIST
    ]
    from pprint import pprint

    pprint(symbols)
