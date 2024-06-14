from typing import TypedDict, Set, List, Dict

from src.backend.betting_api.enums import (PriceData, MarketStatus,
                                       Side, OrderStatus,
                                       OrderType, MarketBettingType,
                                       ExecutionReportStatus,
                                       ExecutionReportErrorCode, PersistenceType, 
                                       InstructionReportStatus,
                                       InstructionReportErrorCode,
                                       RollupModel, TimeInForce,
                                       BetTargetType, PriceLadderType,
                                       ErrorCode, TimeGranularity, MarketProjection,
                                       OrderProjection, MatchProjection, MarketSort,
                                       OrderBy, SortDir, BetStatus, GroupBy)


class CancelInstruction(TypedDict):
    betId: str
    sizeReduction: float


class CancelInstructionReport(TypedDict):
    status: InstructionReportStatus
    errorCode: InstructionReportErrorCode
    instruction: CancelInstruction
    sizeCancelled: float
    cancelledDate: str


class UpdateInstruction(TypedDict):
    betId: str
    newPersistenceType: PersistenceType


class UpdateInstructionReport(TypedDict):
    status: InstructionReportStatus
    errorCode: InstructionReportErrorCode
    instruction: UpdateInstruction


class UpdateExecutionReport(TypedDict):
    customerRef: str
    status: ExecutionReportStatus
    errorCode: ExecutionReportErrorCode
    marketId: str
    instructionReports: List[UpdateInstructionReport]


class ExBestOffersOverrides(TypedDict):
    bestPricesDepth: int
    rollupModel: RollupModel
    rollupLimit: int
    rollupLiabilityThreshold: float
    rollupLiabilityFactor: int


class PriceProjection(TypedDict):
    priceData: Set[PriceData]
    exBestOffersOverrides: ExBestOffersOverrides
    virtualise: bool
    rolloverStakes: bool


class RunnerProfitAndLoss(TypedDict):
    selectionId: int
    ifWin: float
    ifLose: float
    ifPlace: float


class MarketProfitAndLoss(TypedDict):
    marketId: str
    commissionApplied: float
    profitAndLosses: List[RunnerProfitAndLoss]


class PriceLadderDescription(TypedDict):
    type: PriceLadderType


class KeyLineSelection(TypedDict):
    selectionId: int
    handicap: float


class KeyLineDescription(TypedDict):
    keyLine: List[KeyLineSelection]


class LimitOrder(TypedDict):
    size: float
    price: float
    persistenceType: PersistenceType
    timeInForce: TimeInForce
    minFillSize: float
    betTargetType: BetTargetType
    betTargetSize: float


class LimitOnCloseOrder(TypedDict):
    liability: float
    price: float


class MarketOnCloseOrder(TypedDict):
    liability: float


class PlaceInstruction(TypedDict):
    orderType: OrderType
    selectionId: int
    handicap: float
    side: Side
    limitOrder: LimitOrder
    limitOnCloseOrder: LimitOnCloseOrder
    marketOnCloseOrder: MarketOnCloseOrder
    customerOrderRef: str
    

class PlaceInstructionReport(TypedDict):
    status: InstructionReportStatus
    errorCode: InstructionReportErrorCode
    orderStatus: OrderStatus
    instruction: PlaceInstruction
    betId: str
    placedDate: str
    averagePriceMatched: float
    sizeMatched: float


class PlaceExecutionReport(TypedDict):
    customerRef: str
    status: ExecutionReportStatus
    errorCode: ExecutionReportErrorCode
    marketId: str
    instructionReports: List[PlaceInstructionReport]


class ReplaceInstructionReport(TypedDict):
    status: InstructionReportStatus
    errorCode: InstructionReportErrorCode
    cancelInstructionReport: CancelInstructionReport
    placeInstructionReport: PlaceInstructionReport


class CancelExecutionReport(TypedDict):
    customerRef: str
    status: ExecutionReportStatus
    errorCode: ExecutionReportErrorCode
    marketId: str
    instructionReports: List[CancelInstructionReport]


class ReplaceInstruction(TypedDict):
    betId: str
    newPrice: float


class ReplaceExecutionReport(TypedDict):
    customerRef: str
    status: ExecutionReportStatus
    errorCode: ExecutionReportErrorCode
    marketId: str
    instructionReports: List[ReplaceInstructionReport]


class ItemDescription(TypedDict):
    eventTypeDesc: str
    eventDesc: str
    marketDesc: str
    marketType: str
    marketStartTime: str
    runnerDesc: str
    numberOfWinners: int
    eachWayDivisor: float


class RunnerId(TypedDict):
    marketId: str
    selectionId: int
    handicap: float


class MarketVersion(TypedDict):
    version: int


class CurrentItemDescription(TypedDict):
    marketVersion: MarketVersion


class CurrentOrderSummary(TypedDict):
    betId: str
    marketId: str
    selectionId: int
    handicap: float
    priceSize: float
    bspLiability: float
    side: Side
    status: OrderStatus
    persistenceType: PersistenceType
    orderType: OrderType
    placedDate: str
    matchedDate: str
    averagePriceMatched: float
    sizeMatched: float
    sizeRemaining: float
    sizeLapsed: float
    sizeCancelled: float
    sizeVoided: float
    regulatorAuthCode: str
    regulatorCode: str
    customerOrderRef: str
    customerStrategyRef: str
    currentItemDescription: CurrentItemDescription


class CurrentOrderSummaryReport(TypedDict):
    currentOrders: List[CurrentOrderSummary]
    moreAvailable: bool


class MarketRates(TypedDict):
    marketBaseRate: float
    discountAllowed: bool


class MarketLicence(TypedDict):
    wallet: str
    rules: str
    rulesHasDate: bool
    clarifications: str


class MarketLineRangeInfo(TypedDict):
    maxUnitValue: float
    minUnitValue: float
    interval: float
    marketUnit: str


class PriceSize(TypedDict):
    price: float
    size: float


class ClearedOrderSummary(TypedDict):
    eventTypeId: str
    eventId: str
    marketId: str
    selectionId: int
    handicap: float
    betId: str
    placedDate: str
    persistenceType: PersistenceType
    orderType: OrderType
    side: Side
    itemDescription: ItemDescription
    betOutcome: str
    priceRequested: float
    settledDate: str
    lastMatchedDate: str
    betCount: int
    commission: float
    priceMatched: float
    priceReduced: bool
    sizeSettled: float
    profit: float
    sizeCancelled: float
    customerOrderRef: str
    customerStrategyRef: str


class ClearedOrderSummaryReport(TypedDict):
    clearedOrders: List[ClearedOrderSummary]
    moreAvailable: bool


class Order(TypedDict):
    betId: str
    orderType: OrderType
    status: OrderStatus
    persistenceType: PersistenceType
    side: Side
    price: float
    size: float
    bspLiability: float
    placedDate: str
    avgPriceMatched: float
    sizeMatched: float
    sizeRemaining: float
    sizeLapsed: float
    sizeCancelled: float
    sizeVoided: float
    customerOrderRef: str
    customerStrategyRef: str


class Match(TypedDict):
    betId: str
    matchId: str
    side: Side
    price: float
    size: float
    matchDate: str


class MarketDescription(TypedDict):
    persistenceEnabled: bool
    bspMarket: bool
    marketTime: str
    suspendTime: str
    settleTime: str
    bettingType: MarketBettingType
    turnInPlayEnabled: bool
    marketType: str
    regulator: str
    marketBaseRate: float
    discountAllowed: bool
    wallet: str
    rules: str
    rulesHasDate: bool
    eachWayDivisor: float
    clarifications: str
    lineRangeInfo: MarketLineRangeInfo
    raceType: str
    priceLadderDescription: PriceLadderDescription


class Competition(TypedDict):
    id: str
    name: str


class CompetitionResult(TypedDict):
    competition: Competition
    marketCount: int
    competitionRegion: str


class EventType(TypedDict):
    id: str
    name: str


class EventTypeResult(TypedDict):
    eventType: EventType
    marketCount: int


class MarketTypeResult(TypedDict):
    marketType: str
    marketCount: int


class CountryCodeResult(TypedDict):
    countryCode: str
    marketCount: int


class VenueResult(TypedDict):
    venue: str
    marketCount: int


class TimeRange(TypedDict):
    from_: str
    to: str


class TimeRangeResult(TypedDict):
    timeRange: TimeRange
    marketCount: int


class Event(TypedDict):
    id: str
    name: str
    countryCode: str
    timezone: str
    venue: str
    openDate: str


class EventResult(TypedDict):
    event: Event
    marketCount: int


class ExchangePrices(TypedDict):
    availableToBack: List[PriceSize]
    availableToLay: List[PriceSize]
    tradedVolume: List[PriceSize]


class StartingPrices(TypedDict):
    nearPrice: float
    farPrice: float
    backStakeTaken: List[PriceSize]
    layLiabilityTaken: List[PriceSize]
    actualSP: float


class Runner(TypedDict):
    selectionId: int
    handicap: float
    status: str
    adjustmentFactor: float
    lastPriceTraded: float
    totalMatched: float
    removalDate: str
    sp: StartingPrices
    ex: ExchangePrices
    orders: List[Order]
    matches: List[Match]
    matchesByStrategy: Dict[str, Match]


class RunnerCatalog(TypedDict):
    selectionId: int
    runnerName: str
    handicap: float
    sortPriority: int
    metadata: dict[str, str]


class MarketBook(TypedDict):
    marketId: str
    isMarketDataDelayed: bool
    status: MarketStatus
    betDelay: int
    bspReconciled: bool
    complete: bool
    inplay: bool
    numberOfWinners: int
    numberOfRunners: int
    numberOfActiveRunners: int
    lastMatchTime: str
    totalMatched: float
    totalAvailable: float
    crossMatching: bool
    runnersVoidable: bool
    version: int
    runners: List[Runner]
    keyLineDescription: KeyLineDescription


class MarketCatalogue(TypedDict):
    marketId: str
    marketName: str
    marketStartTime: str
    description: MarketDescription
    totalMatched: float
    runners: List[RunnerCatalog]
    eventType: EventType
    competition: Competition
    event: Event


class TimeRange(TypedDict):
    from_: str
    to: str


class MarketFilter(TypedDict):
    textQuery: str
    exchangeIds: Set[str]
    eventTypeIds: Set[str]
    eventIds: Set[str]
    competitionIds: Set[str]
    marketIds: Set[str]
    venues: Set[str]
    bspOnly: bool
    turnInPlayEnabled: bool
    inPlayOnly: bool
    marketBettingTypes: Set[MarketBettingType]
    marketCountries: Set[str]
    marketTypeCodes: Set[str]
    marketStartTime: TimeRange
    withOrders: Set[OrderStatus]
    raceTypes: Set[str]


class BettingAPIException(TypedDict):
    errorCode: ErrorCode
    errorDetails: str
    requestUUID: str


class ListEventTypes(TypedDict):
    filter: MarketFilter
    locale: str


class ListCompetitions(TypedDict):
    filter: MarketFilter
    locale: str


class ListTimeRanges(TypedDict):
    filter: MarketFilter
    granularity: TimeGranularity


class ListEvents(TypedDict):
    filter: MarketFilter
    locale: str


class ListMarketTypes(TypedDict):
    filter: MarketFilter
    locale: str


class ListCountries(TypedDict):
    filter: MarketFilter
    locale: str


class ListVenues(TypedDict):
    filter: MarketFilter
    locale: str


class ListMarketCatalogue(TypedDict):
    filter: MarketFilter
    marketProjection: Set[MarketProjection]
    sort: MarketSort
    maxResults: int
    locale: str


class ListMarketBook(TypedDict):
    marketIds: List[str]
    priceProjection: PriceProjection
    orderProjection: OrderProjection
    matchProjection: MatchProjection
    currencyCode: str
    locale: str
    matchedSince: str
    betIds: Set[str]


class ListRunnerBook(TypedDict):
    marketId: str
    selectionId: str
    handicap: float
    priceProjection: PriceProjection
    orderProjection: OrderProjection
    matchProjection: MatchProjection
    includeOverallPosition: bool
    partitionMatchedByStrategyRef: bool
    customerStrategyRefs: Set[str]
    currencyCode: str
    locale: str
    matchedSince: str
    betIds: Set[str]


class ListMarketProfitAndLoss(TypedDict):
    marketIds: Set[str]
    includeSettledBets: bool
    includeBspBets: bool
    netOfCommission: bool


class ListCurrentOrders(TypedDict):
    betIds: Set[str]
    marketIds: Set[str]
    orderProjection: OrderProjection
    placedDateRange: TimeRange
    orderBy: OrderBy
    sortDir: SortDir
    fromRecord: int
    recordCount: int


class ListClearedOrders(TypedDict):
    betStatus: BetStatus
    eventTypeIds: Set[str]
    eventIds: Set[str]
    marketIds: Set[str]
    runnerIds: Set[RunnerId]
    betIds: Set[str]
    side: Side
    settledDateRange: TimeRange
    groupBy: GroupBy
    includeItemDescription: bool
    locale: str
    fromRecord: int
    recordCount: int


class PlaceOrders(TypedDict):
    marketId: str
    instructions: List[PlaceInstruction]
    customerRef: str
    marketVersion: MarketVersion
    customerStrategyRef: str
    async_: bool


class CancelOrders(TypedDict):
    marketId: str
    instructions: List[CancelInstruction]
    customerRef: str


class ReplaceOrders(TypedDict):
    marketId: str
    instructions: List[ReplaceInstruction]
    customerRef: str
    marketVersion: MarketVersion
    async_: bool


class UpdateOrders(TypedDict):
    marketId: str
    instructions: List[UpdateInstruction]
    customerRef: str