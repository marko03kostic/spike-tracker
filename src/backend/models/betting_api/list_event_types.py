from typing import TypedDict, List, Optional
from enum import Enum


class OrderStatus(Enum):
    PENDING = "PENDING"
    EXECUTION_COMPLETE = "EXECUTION_COMPLETE"
    EXECUTABLE = "EXECUTABLE"
    EXPIRED = "EXPIRED"


class TimeRange(TypedDict):
    from_: Optional[str]
    to: Optional[str]


class MarketBettingType(Enum):
    ODDS = "ODDS"
    LINE = "LINE"
    RANGE = "RANGE"
    ASIAN_HANDICAP_DOUBLE_LINE = "ASIAN_HANDICAP_DOUBLE_LINE"
    ASIAN_HANDICAP_SINGLE_LINE = "ASIAN_HANDICAP_SINGLE_LINE"
    FIXED_ODDS = "FIXED_ODDS"


class MarketFilter(TypedDict):
    textQuery: Optional[str]
    eventTypeIds: Optional[List[str]]
    eventIds: Optional[List[str]]
    competitionIds: Optional[List[str]]
    marketIds: Optional[List[str]]
    venues: Optional[List[str]]
    bspOnly: Optional[bool]
    turnInPlayEnabled: Optional[bool]
    inPlayOnly: Optional[bool]
    marketBettingTypes: Optional[List[MarketBettingType]]
    marketCountries: Optional[List[str]]
    marketTypeCodes: Optional[List[str]]
    marketStartTime: Optional[TimeRange]
    withOrders: Optional[List[OrderStatus]]
    raceTypes: Optional[List[str]]


class ListEventTypesParams(TypedDict):
    filter: MarketFilter
    locale: None = None #todo
