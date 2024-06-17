from enum import Enum


class OP(Enum):
    authentication = "authentication"
    connection = "connection"
    status = "status"
    heartbeat = 'heartbeat'   
    marketSubscription = "marketSubscription"
    orderSubscription = "orderSubscription"
    mcm = 'mcm'
    ocm = 'ocm'


class Field(Enum):
    EX_BEST_OFFERS_DISP = "EX_BEST_OFFERS_DISP"
    EX_BEST_OFFERS = "EX_BEST_OFFERS"
    EX_ALL_OFFERS = "EX_ALL_OFFERS"
    EX_TRADED = "EX_TRADED"
    EX_TRADED_VOL = "EX_TRADED_VOL"
    EX_LTP = "EX_LTP"
    EX_MARKET_DEF = "EX_MARKET_DEF"
    SP_TRADED = "SP_TRADED"
    SP_PROJECTED = "SP_PROJECTED"


class BettingType(Enum):
    ODDS = "ODDS"
    LINE = "LINE"
    RANGE = "RANGE"
    ASIAN_HANDICAP_DOUBLE_LINE = "ASIAN_HANDICAP_DOUBLE_LINE"
    ASIAN_HANDICAP_SINGLE_LINE = "ASIAN_HANDICAP_SINGLE_LINE"


class ChangeType(Enum):
    SUB_IMAGE = 'SUB_IMAGE'
    RESUB_DELTA = 'RESUB_DELTA'
    HEARTBEAT = 'HEARTBEAT'


class OrderType(Enum):
    L = "LIMIT"
    LOC = "LIMIT_ON_CLOSE"
    MOC = "MARKET_ON_CLOSE"
    LIMIT = "LIMIT"
    LIMIT_ON_CLOSE = "LIMIT_ON_CLOSE"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"


class LapseStatusReasonCode(Enum):
    MKT_UNKNOWN = 'MKT_UNKNOWN'
    MKT_INVALID = 'MKT_INVALID'
    RNR_UNKNOWN = 'RNR_UNKNOWN'
    TIME_ELAPSED = 'TIME_ELAPSED'
    CURRENCY_UNKNOWN = 'CURRENCY_UNKNOWN'
    PRICE_INVALID = 'PRICE_INVALID'
    MKT_SUSPENDED = 'MKT_SUSPENDED'
    MKT_VERSION = 'MKT_VERSION'
    LINE_TARGET = 'LINE_TARGET'
    LINE_SP = 'LINE_SP'
    SP_IN_PLAY = 'SP_IN_PLAY'
    SMALL_STAKE = 'SMALL_STAKE'
    PRICE_IMP_TOO_LARGE = 'PRICE_IMP_TOO_LARGE'


class PersistenceType(Enum):
    L = "LAPSE"
    P = "PERSIST"
    MOC = "MARKET_ON_CHANGE"
    LAPSE = "LAPSE"
    PERSIST = "PERSIST"
    MARKET_ON_CLOSE = "MARKET_ON_CHANGE"


class OrderStatus(Enum):
    E = "EXECUTABLE"
    EC = "EXECUTION_COMPLETE"
    EXECUTABLE = "EXECUTABLE"
    EXECUTION_COMPLETE = "EXECUTION_COMPLETE"


class MarketStatus(Enum):
    INACTIVE = "INACTIVE"
    OPEN = "OPEN"
    SUSPENDED = "SUSPENDED"
    CLOSED = "CLOSED"
    

class Side(Enum):
    B = "BACK"
    L = "LAY"
    BACK = "BACK"
    LAY = "LAY"


class SegmentType(Enum):
    SEG_START = 'SEG_START'
    SEG = 'SEG'
    SEG_END = 'SEG_END'


class StreamStatus(Enum):
    UP_TO_DATE = (None, "The exchange stream data is up to date.")
    SERVICE_LATENCY = (503, "The downstream services are experiencing latency.")

    def __init__(self, code, description):
        self.code = code
        self.description = description


class StatusCode(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ErrorCode(Enum):
    NO_APP_KEY = "NO_APP_KEY"
    INVALID_APP_KEY = "INVALID_APP_KEY"
    NO_SESSION = "NO_SESSION"
    INVALID_SESSION_INFORMATION = "INVALID_SESSION_INFORMATION"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    INVALID_INPUT = "INVALID_INPUT"
    INVALID_CLOCK = "INVALID_CLOCK"
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"
    TIMEOUT = "TIMEOUT"
    SUBSCRIPTION_LIMIT_EXCEEDED = "SUBSCRIPTION_LIMIT_EXCEEDED"
    INVALID_REQUEST = "INVALID_REQUEST"
    CONNECTION_FAILED = "CONNECTION_FAILED"
    MAX_CONNECTION_LIMIT_EXCEEDED = "MAX_CONNECTION_LIMIT_EXCEEDED"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"