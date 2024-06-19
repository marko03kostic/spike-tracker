from typing import TypedDict, List, Union, Optional

from src.backend.exchange_stream_api.enums import (OP,
                                               BettingType,
                                               Field,
                                               ChangeType,
                                               SegmentType,
                                               StreamStatus,
                                               MarketStatus,
                                               Side,
                                               OrderStatus,
                                               PersistenceType,
                                               OrderType,
                                               LapseStatusReasonCode,
                                               StatusCode,
                                               ErrorCode)

class BetfairResponseMessage(TypedDict):
    op: OP
    id: int


class BetfairRequestMessage(TypedDict):
    op: OP
    id: int


class BetfairAuthenticationMessage(BetfairRequestMessage):
    appKey: str
    session: str


class BetfairConnectionMessage(BetfairResponseMessage):
    connectionId: str


class BetfairSubscriptionMessage(BetfairRequestMessage, total=False):
    segmentationEnabled: bool | None = None
    conflateMs: int | None = None
    heartbeatMs: int | None = None
    initialClk: str | None = None
    clk: str | None = None


class BetfairMarketFilter(TypedDict, total=False):
    countryCodes: List[str]
    bettingTypes: List[BettingType]
    turnInPlayEnabled: bool | None = None
    marketTypes: List[str]
    venues: List[str]
    marketIds: List[str]
    eventTypeIds: List[str]
    eventIds: List[str]
    bspMarket: bool | None = None
    raceTypes: List[str]


class BetfairMarketDataFilter(TypedDict, total=False):
    ladderLevels: int | None = None
    fields: List[Field] | None = None


class BetfairOrderFilter(TypedDict, total=False):
    includeOverallPosition: bool | None = None
    accountIds: List[int] | None = None
    customerStrategyRefs: List[str] | None = None
    partitionMatchedByStrategyRef: bool | None = None


class BetfairMarketSubscriptionMessage(BetfairSubscriptionMessage, total=False):
    marketFilter: BetfairMarketFilter
    marketDataFilter: BetfairMarketDataFilter


class BetfairOrderSubscriptionMessage(BetfairSubscriptionMessage, total=False):
    orderFilter: BetfairOrderFilter


class BetfairChangeMessage(BetfairResponseMessage, total=False):
    ct: ChangeType
    segmentType: SegmentType
    conflateMs: int | None = None
    status: StreamStatus 
    heartbeatMs: int
    pt: int
    initialClk: str
    clk: str


class BetfairMarketDefinition(TypedDict, total=False):
    Id: str
    Venue: str
    bspMarket: bool
    turnInPlayEnabled: bool
    persistenceEnabled: bool
    marketBaseRate: float
    eventId: str
    eventTypeId: str
    numberOfWinners: int
    bettingType: BettingType
    marketType: str
    marketTime: str
    suspendTime: str
    bspReconciled: bool
    complete: bool
    inPLay: bool
    crossMatching: bool
    runnersVoidable: bool
    numberOfActiveRunners: int
    betDelay: int
    status: MarketStatus
    regulators: str
    discountAllowed: bool
    timezone: str


class BetfairRunnerChange(TypedDict):
    id: int
    con: bool
    tv: Union[int, float]
    ltp: Union[int, float]
    spn: Union[int, float]
    spf: Union[int, float]

    batb: List[List[Union[int, float]]]
    batl: List[List[Union[int, float]]]
    bdatb: List[List[Union[int, float]]]
    bdatl: List[List[Union[int, float]]]

    atb: List[List[Union[int, float]]]
    atl: List[List[Union[int, float]]]
    spb: List[List[Union[int, float]]]
    spl: List[List[Union[int, float]]]
    trd: List[List[Union[int, float]]]

    hc: float


class BetfairMarketChange(TypedDict):
    rc: List[BetfairRunnerChange]
    img: bool
    tv: float
    marketDefinition: BetfairMarketDefinition
    id: str


class BetfairUnmatchedOrder(TypedDict, total=False):
    id: str
    p: Union[int, float]
    s: Union[int, float]
    bsp: Union[int, float]
    side: Side
    status: OrderStatus
    pt: PersistenceType
    ot: OrderType
    pd: int
    md: int
    cd: int
    ld: int
    lsrc: LapseStatusReasonCode
    avp: Union[int, float]
    sm: Union[int, float]
    sr: Union[int, float]
    sl: Union[int, float]
    sc: Union[int, float]
    sv: Union[int, float]
    rac: str
    rc: str
    rfo: str
    rfs: str



class BetfairOrderChange(TypedDict, total=False):
    fullimage: bool
    id: str
    hc: str | None = None
    uo: List[BetfairUnmatchedOrder]
    mb: List[List[float]]
    ml: List[List[float]]



class BetfairOrderAccountChange(TypedDict, total=False):
    closed: bool
    id: str
    fullimage: bool
    orc: List[BetfairOrderChange]



class BetfairMarketChangeMessage(BetfairChangeMessage, total=False):
    mc: List[BetfairMarketChange]


class BetfairOrderChangeMessage(BetfairChangeMessage, total=False):
    oc: List[BetfairOrderAccountChange]


BetfairMessage = Union[
    BetfairAuthenticationMessage, BetfairMarketSubscriptionMessage, BetfairOrderSubscriptionMessage,
]


class BetfairStatusMessage(BetfairResponseMessage, total=False):
    statusCode: StatusCode
    connectionClosed: bool
    errorCode: ErrorCode | None = None
    errorMessage: str | None = None
    connectionsAvailable: int