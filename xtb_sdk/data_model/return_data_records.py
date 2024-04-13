"""Module to create response objects for XTB API."""

from pydantic import Field

from xtb_sdk.data_model.base_classes import DataModel


class SymbolRecord(DataModel):
    """SymbolRecord model."""

    ask: float
    bid: float
    category_name: str
    contract_size: float
    currency: str
    currency_pair: bool
    currency_profit: str
    description: str | None
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
