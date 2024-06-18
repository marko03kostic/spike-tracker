import requests
from typing import Set, List, Dict, Any, Optional

from src.main_application import MainApplication
from src.backend.betting_api.enums import (MarketProjection, MatchProjection,
                                       OrderProjection,TimeGranularity,
                                       Side, OrderBy, SortDir, MarketSort,
                                       GroupBy, BetStatus, MarketBettingType, OrderStatus,
                                       PriceData, RollupModel, OrderType, PersistenceType,
                                       TimeInForce, BetTargetType, Endpoint, ErrorCode)
from src.backend.betting_api.definitions import (MarketFilter, CompetitionResult,
                                             TimeRangeResult, EventResult,
                                             MarketTypeResult, CountryCodeResult,
                                             VenueResult, PriceProjection, MarketCatalogue,
                                             TimeRange, MarketProfitAndLoss, PlaceInstruction,
                                             MarketVersion, CancelInstruction, CancelExecutionReport,
                                             ReplaceInstruction, UpdateExecutionReport, 
                                             ReplaceExecutionReport, UpdateInstruction,
                                             PlaceExecutionReport, EventTypeResult,
                                             MarketBook, CurrentOrderSummaryReport,
                                             ClearedOrderSummaryReport, ExBestOffersOverrides,
                                             LimitOrder, LimitOnCloseOrder, MarketOnCloseOrder,
                                             ListEventTypes, ListCompetitions, ListTimeRanges, ListEvents,
                                                ListMarketTypes, ListCountries, ListVenues, ListMarketCatalogue,
                                                ListMarketBook, ListRunnerBook, ListMarketProfitAndLoss,
                                                ListCurrentOrders, ListClearedOrders, PlaceOrders, CancelOrders,
                                                ReplaceOrders, UpdateOrders)

class BettingAPIClient:

    def __init__(self) -> None:
        self.main_app: MainApplication = MainApplication.instance()
        self.BASE_URL = None
        self.timeout = None
        self.BASE_URL = "https://api.betfair.com/exchange/betting/rest/v1.0"
        self.timeout = 30

    @property
    def headers(self) -> dict:
        return {
            'X-Application': self.main_app.app_key,
            'X-Authentication': self.main_app.ssoid,
            'Content-type': 'application/json',
            'Accept-encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

    def _handle_api_specific_errors(self, response: requests.Response)  -> None:
        error_code = response.json().get('detail', {}).get('APINGException', {}).get('errorCode', None)
        if error_code:
            print(ErrorCode[error_code])

    def list_event_types(self,
                        text_query: Optional[str] = None,
                        exchange_ids: Optional[Set[str]] = None,
                        event_type_ids: Optional[Set[str]] = None,
                        event_ids: Optional[Set[str]] = None,
                        competition_ids: Optional[Set[str]] = None,
                        market_ids: Optional[Set[str]] = None,
                        venues: Optional[Set[str]] = None,
                        bsp_only: Optional[bool] = None,
                        turn_in_play_enabled: Optional[bool] = None,
                        in_play_only: Optional[bool] = None,
                        market_betting_types: Optional[Set[MarketBettingType]] = None,
                        market_countries: Optional[Set[str]] = None,
                        market_type_codes: Optional[Set[str]] = None,
                        from_: Optional[str] = None,
                        to: Optional[str] = None,
                        with_orders: Optional[Set[OrderStatus]] = None,
                        race_types: Optional[Set[str]] = None,
                        locale: Optional[str] = None) -> List[EventTypeResult]:
        
        market_start_time = TimeRange(from_=from_,
                                      to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListEventTypes(filter=filter,
                                   locale=locale)

        response = self.post(Endpoint.LIST_EVENT_TYPES.value, json_data=json_data)
        return [EventTypeResult(i) for i in response]
        
    def list_competitions(self,
                        text_query: Optional[str] = None,
                        exchange_ids: Optional[Set[str]] = None,
                        event_type_ids: Optional[Set[str]] = None,
                        event_ids: Optional[Set[str]] = None,
                        competition_ids: Optional[Set[str]] = None,
                        market_ids: Optional[Set[str]] = None,
                        venues: Optional[Set[str]] = None,
                        bsp_only: Optional[bool] = None,
                        turn_in_play_enabled: Optional[bool] = None,
                        in_play_only: Optional[bool] = None,
                        market_betting_types: Optional[Set[MarketBettingType]] = None,
                        market_countries: Optional[Set[str]] = None,
                        market_type_codes: Optional[Set[str]] = None,
                        from_: Optional[str] = None,
                        to: Optional[str] = None,
                        with_orders: Optional[Set[OrderStatus]] = None,
                        race_types: Optional[Set[str]] = None,
                        locale: Optional[str] = None) -> List[CompetitionResult]:
        
        #TODO
        market_start_time = TimeRange(from_=from_,
                                      to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListCompetitions(filter=filter,
                                     locale=locale)
        
        response = self.post(Endpoint.LIST_COMPETITIONS.value, json_data=json_data)
        return [CompetitionResult(i) for i in response]

    def list_time_ranges(self,
                        granularity: TimeGranularity,
                        text_query: Optional[str] = None,
                        exchange_ids: Optional[Set[str]] = None,
                        event_type_ids: Optional[Set[str]] = None,
                        event_ids: Optional[Set[str]] = None,
                        competition_ids: Optional[Set[str]] = None,
                        market_ids: Optional[Set[str]] = None,
                        venues: Optional[Set[str]] = None,
                        bsp_only: Optional[bool] = None,
                        turn_in_play_enabled: Optional[bool] = None,
                        in_play_only: Optional[bool] = None,
                        market_betting_types: Optional[Set[MarketBettingType]] = None,
                        market_countries: Optional[Set[str]] = None,
                        market_type_codes: Optional[Set[str]] = None,
                        from_: Optional[str] = None,
                        to: Optional[str] = None,
                        with_orders: Optional[Set[OrderStatus]] = None,
                        race_types: Optional[Set[str]] = None) -> List[TimeRangeResult]:

        market_start_time = TimeRange(from_=from_,
                                    to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)

        json_data = ListTimeRanges(filter=filter,
                                granularity=granularity)
        
        response = self.post(Endpoint.LIST_TIME_RANGES.value, json_data=json_data)
        return [TimeRangeResult(i) for i in response]

    def list_events(self,
                    text_query: Optional[str] = None,
                    exchange_ids: Optional[Set[str]] = None,
                    event_type_ids: Optional[Set[str]] = None,
                    event_ids: Optional[Set[str]] = None,
                    competition_ids: Optional[Set[str]] = None,
                    market_ids: Optional[Set[str]] = None,
                    venues: Optional[Set[str]] = None,
                    bsp_only: Optional[bool] = None,
                    turn_in_play_enabled: Optional[bool] = None,
                    in_play_only: Optional[bool] = None,
                    market_betting_types: Optional[Set[MarketBettingType]] = None,
                    market_countries: Optional[Set[str]] = None,
                    market_type_codes: Optional[Set[str]] = None,
                    from_: Optional[str] = None,
                    to: Optional[str] = None,
                    with_orders: Optional[Set[OrderStatus]] = None,
                    race_types: Optional[Set[str]] = None,
                    locale: Optional[str] = None) -> List[EventResult]:
        
        market_start_time = TimeRange(from_=from_,
                                    to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListEvents(filter=filter,
                                locale=locale)
        
        response = self.post(Endpoint.LIST_EVENTS.value, json_data=json_data)
        return [EventResult(i) for i in response]

    def list_market_types(self,
                        text_query: Optional[str] = None,
                        exchange_ids: Optional[Set[str]] = None,
                        event_type_ids: Optional[Set[str]] = None,
                        event_ids: Optional[Set[str]] = None,
                        competition_ids: Optional[Set[str]] = None,
                        market_ids: Optional[Set[str]] = None,
                        venues: Optional[Set[str]] = None,
                        bsp_only: Optional[bool] = None,
                        turn_in_play_enabled: Optional[bool] = None,
                        in_play_only: Optional[bool] = None,
                        market_betting_types: Optional[Set[MarketBettingType]] = None,
                        market_countries: Optional[Set[str]] = None,
                        market_type_codes: Optional[Set[str]] = None,
                        from_: Optional[str] = None,
                        to: Optional[str] = None,
                        with_orders: Optional[Set[OrderStatus]] = None,
                        race_types: Optional[Set[str]] = None,
                        locale: Optional[str] = None) -> List[MarketTypeResult]:
        
        market_start_time = TimeRange(from_=from_,
                                      to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListMarketTypes(filter=filter,
                                    locale=locale)
        
        response = self.post(Endpoint.LIST_MARKET_TYPES.value, json_data=json_data)
        return [MarketTypeResult(i) for i in response]

    def list_countries(self,
                    text_query: Optional[str] = None,
                    exchange_ids: Optional[Set[str]] = None,
                    event_type_ids: Optional[Set[str]] = None,
                    event_ids: Optional[Set[str]] = None,
                    competition_ids: Optional[Set[str]] = None,
                    market_ids: Optional[Set[str]] = None,
                    venues: Optional[Set[str]] = None,
                    bsp_only: Optional[bool] = None,
                    turn_in_play_enabled: Optional[bool] = None,
                    in_play_only: Optional[bool] = None,
                    market_betting_types: Optional[Set[MarketBettingType]] = None,
                    market_countries: Optional[Set[str]] = None,
                    market_type_codes: Optional[Set[str]] = None,
                    from_: Optional[str] = None,
                    to: Optional[str] = None,
                    with_orders: Optional[Set[OrderStatus]] = None,
                    race_types: Optional[Set[str]] = None,
                    locale: Optional[str] = None) -> List[CountryCodeResult]:
        
        market_start_time = TimeRange(from_=from_,
                                    to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListCountries(filter=filter,
                                  locale=locale)
        
        response = self.post(Endpoint.LIST_COUNTRIES.value, json_data=json_data)
        return [CountryCodeResult(i) for i in response]

    def list_venues(self,
                    text_query: Optional[str] = None,
                    exchange_ids: Optional[Set[str]] = None,
                    event_type_ids: Optional[Set[str]] = None,
                    event_ids: Optional[Set[str]] = None,
                    competition_ids: Optional[Set[str]] = None,
                    market_ids: Optional[Set[str]] = None,
                    venues: Optional[Set[str]] = None,
                    bsp_only: Optional[bool] = None,
                    turn_in_play_enabled: Optional[bool] = None,
                    in_play_only: Optional[bool] = None,
                    market_betting_types: Optional[Set[MarketBettingType]] = None,
                    market_countries: Optional[Set[str]] = None,
                    market_type_codes: Optional[Set[str]] = None,
                    from_: Optional[str] = None,
                    to: Optional[str] = None,
                    with_orders: Optional[Set[OrderStatus]] = None,
                    race_types: Optional[Set[str]] = None,
                    locale: Optional[str] = None) -> List[VenueResult]:
        
        market_start_time = TimeRange(from_=from_,
                                    to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListVenues(filter=filter,
                                locale=locale)
        
        response = self.post(Endpoint.LIST_VENUES.value, json_data=json_data)
        return [VenueResult(i) for i in response]

    def list_market_catalogue(self,
                            max_results: int,
                            text_query: Optional[str] = None,
                            exchange_ids: Optional[Set[str]] = None,
                            event_type_ids: Optional[Set[str]] = None,
                            event_ids: Optional[Set[str]] = None,
                            competition_ids: Optional[Set[str]] = None,
                            market_ids: Optional[Set[str]] = None,
                            venues: Optional[Set[str]] = None,
                            bsp_only: Optional[bool] = None,
                            turn_in_play_enabled: Optional[bool] = None,
                            in_play_only: Optional[bool] = None,
                            market_betting_types: Optional[Set[MarketBettingType]] = None,
                            market_countries: Optional[Set[str]] = None,
                            market_type_codes: Optional[Set[str]] = None,
                            from_: Optional[str] = None,
                            to: Optional[str] = None,
                            with_orders: Optional[Set[OrderStatus]] = None,
                            race_types: Optional[Set[str]] = None,
                            market_projection: Optional[Set[MarketProjection]] = None,
                            sort: Optional[MarketSort] = None,
                            locale: Optional[str] = None) -> List[MarketCatalogue]:
        
        market_start_time = TimeRange(from_=from_,
                                    to=to)

        filter = MarketFilter(textQuery=text_query,
                                exchangeIds=exchange_ids,
                                eventTypeIds=event_type_ids,
                                eventIds=event_ids,
                                competitionIds=competition_ids,
                                marketIds=market_ids,
                                venues=venues,
                                bspOnly=bsp_only,
                                turnInPlayEnabled=turn_in_play_enabled,
                                inPlayOnly=in_play_only,
                                marketBettingTypes=market_betting_types,
                                marketCountries=market_countries,
                                marketTypeCodes=market_type_codes,
                                marketStartTime=market_start_time,
                                withOrders=with_orders,
                                raceTypes=race_types)
        
        json_data = ListMarketCatalogue(filter=filter,
                                     marketProjection=market_projection,
                                     sort=sort,
                                     maxResults=max_results,
                                     locale=locale)
        
        response = self.post(Endpoint.LIST_MARKET_CATALOGUE.value, json_data=json_data)
        return [MarketCatalogue(i) for i in response]

    def list_market_book(self,
                        market_ids: List[str],
                        price_data: Optional[Set[PriceData]] = None,
                        best_prices_depth: Optional[int] = None,
                        rollup_model: Optional[RollupModel] = None,
                        rollup_limit: Optional[int] = None,
                        rollup_liability_threshold: Optional[float] = None,
                        rollup_liability_factor: Optional[int] = None,
                        virtualise: Optional[bool] = None,
                        rollover_stakes: Optional[bool] = None,
                        order_projection: Optional[OrderProjection] = None,
                        match_projection: Optional[MatchProjection] = None,
                        currency_code: Optional[str] = None,
                        locale: Optional[str] = None,
                        matched_since: Optional[str] = None,
                        bet_ids: Optional[Set[str]] = None) -> List[MarketBook]:
        
        ex_best_offers_overrides = ExBestOffersOverrides(
            bestPricesDepth=best_prices_depth,
            rollupModel=rollup_model,
            rollupLimit=rollup_limit,
            rollupLiabilityThreshold=rollup_liability_threshold,
            rollupLiabilityFactor=rollup_liability_factor
        )
        
        price_projection = PriceProjection(
            priceData=price_data,
            exBestOffersOverrides=ex_best_offers_overrides,
            virtualise=virtualise,
            rolloverStakes=rollover_stakes
        )

        json_data = ListMarketBook(marketIds=market_ids,
                                priceProjection=price_projection,
                                orderProjection=order_projection,
                                matchProjection=match_projection,
                                currencyCode=currency_code,
                                locale=locale,
                                matchedSince=matched_since,
                                betIds=bet_ids)
        
        response = self.post(Endpoint.LIST_MARKET_BOOK.value, json_data=json_data)
        return [MarketBook(i) for i in response]

    def list_runner_book(self,
                        market_id: str,
                        selection_id: str,
                        handicap: Optional[float] = None,
                        price_data: Optional[Set[PriceData]] = None,
                        best_prices_depth: Optional[int] = None,
                        rollup_model: Optional[RollupModel] = None,
                        rollup_limit: Optional[int] = None,
                        rollup_liability_threshold: Optional[float] = None,
                        rollup_liability_factor: Optional[int] = None,
                        virtualise: Optional[bool] = None,
                        rollover_stakes: Optional[bool] = None,
                        order_projection: Optional[OrderProjection] = None,
                        match_projection: Optional[MatchProjection] = None,
                        include_overall_position: Optional[bool] = None,
                        partition_matched_by_strategy_ref: Optional[bool] = None,
                        customer_strategy_refs: Optional[Set[str]] = None,
                        currency_code: Optional[str] = None,
                        locale: Optional[str] = None,
                        matched_since: Optional[str] = None,
                        bet_ids: Optional[Set[str]] = None) -> List[MarketBook]:
        
        ex_best_offers_overrides = ExBestOffersOverrides(
            bestPricesDepth=best_prices_depth,
            rollupModel=rollup_model,
            rollupLimit=rollup_limit,
            rollupLiabilityThreshold=rollup_liability_threshold,
            rollupLiabilityFactor=rollup_liability_factor
        )
        
        price_projection = PriceProjection(
            priceData=price_data,
            exBestOffersOverrides=ex_best_offers_overrides,
            virtualise=virtualise,
            rolloverStakes=rollover_stakes
        )

        json_data = ListRunnerBook(marketId=market_id,
                                handicap=handicap,
                                priceProjection=price_projection,
                                orderProjection=order_projection,
                                matchProjection=match_projection,
                                selectionId=selection_id,
                                includeOverallPosition=include_overall_position,
                                partitionMatchedByStrategyRef=partition_matched_by_strategy_ref,
                                customerStrategyRefs=customer_strategy_refs,
                                currencyCode=currency_code,
                                locale=locale,
                                matchedSince=matched_since,
                                betIds=bet_ids)
        
        response = self.post(Endpoint.LIST_RUNNER_BOOK.value, json_data=json_data)
        return [MarketBook(i) for i in response]

    def list_market_profit_and_loss(self,
                                    market_ids: Set[str],
                                    include_settled_bets: Optional[bool] = None,
                                    include_bsp_bets: Optional[bool] = None,
                                    net_of_commission: Optional[bool] = None) -> List[MarketProfitAndLoss]:
        
        json_data = ListMarketProfitAndLoss(marketIds=market_ids,
                                            includeSettledBets=include_settled_bets,
                                            includeBspBets=include_bsp_bets,
                                            netOfCommission=net_of_commission)
        
        response = self.post(Endpoint.LIST_MARKET_PROFIT_AND_LOSS.value, json_data=json_data)
        return [MarketProfitAndLoss(i) for i in response]

    def list_current_orders(self,
                            bet_ids: Optional[Set[str]] = None,
                            market_ids: Optional[Set[str]] = None,
                            order_projection: Optional[OrderProjection] = None,
                            from_: Optional[str] = None,
                            to: Optional[str] = None,
                            order_by: Optional[OrderBy] = None,
                            sort_dir: Optional[SortDir] = None,
                            from_record: Optional[int] = None,
                            record_count: Optional[int] = None) -> CurrentOrderSummaryReport:
        
        time_range = TimeRange(from_=from_,
                                    to=to)

        json_data = ListCurrentOrders(betIds=bet_ids,
                                      marketIds=market_ids,
                                      orderProjection=order_projection,
                                      placedDateRange=time_range,
                                      orderBy=order_by,
                                      sortDir=sort_dir,
                                      fromRecord=from_record,
                                      recordCount=record_count)
        
        response = self.post(Endpoint.LIST_CURRENT_ORDERS.value, json_data=json_data)
        return CurrentOrderSummaryReport(response)

    def list_cleared_orders(self,
                            bet_status: BetStatus,
                            event_type_ids: Optional[Set[str]] = None,
                            event_ids: Optional[Set[str]] = None,
                            market_ids: Optional[Set[str]] = None,
                            runner_ids: Optional[Set[str]] = None,
                            bet_ids: Optional[Set[str]] = None,
                            side: Optional[Side] = None,
                            from_: Optional[str] = None,
                            to: Optional[str] = None,
                            group_by: Optional[GroupBy] = None,
                            include_item_description: Optional[bool] = None,
                            locale: Optional[str] = None,
                            from_record: Optional[int] = None,
                            record_count: Optional[int] = None) -> ClearedOrderSummaryReport:
        
        time_range = TimeRange(from_=from_,
                                    to=to)
        
        json_data = ListClearedOrders(betStatus=bet_status,
                                        eventTypeIds=event_type_ids,
                                        eventIds=event_ids,
                                        marketIds=market_ids,
                                        runnerIds=runner_ids,
                                        betIds=bet_ids,
                                        side=side,
                                        settledDateRange=time_range,
                                        groupBy=group_by,
                                        includeItemDescription=include_item_description,
                                        locale=locale,
                                        fromRecord=from_record,
                                        recordCount=record_count)
        
        response = self.post(Endpoint.LIST_CLEARED_ORDERS.value, json_data=json_data)
        return ClearedOrderSummaryReport(response)

    def place_orders(self,
                     market_id: str,
                    order_type: OrderType,
                    selection_id: int,
                    handicap: float,
                    side: Side,
                    limit_order_size: float,
                    limit_order_price: float,
                    limit_order_persistence_type: PersistenceType,
                    limit_order_time_in_force: TimeInForce,
                    limit_order_min_fill_size: float,
                    limit_order_bet_target_type: BetTargetType,
                    limit_order_bet_target_size: float,
                    limit_on_close_order_liability: float,
                    limit_on_close_order_price: float,
                    market_on_close_order_liability: float,
                    customer_order_ref: str,
                    customer_ref: str,
                    market_version: int,
                    customer_strategy_ref: str,
                    async_: bool) -> PlaceExecutionReport:
        
        limit_order = LimitOrder(
            size=limit_order_size,
            price=limit_order_price,
            persistenceType=limit_order_persistence_type,
            timeInForce=limit_order_time_in_force,
            minFillSize=limit_order_min_fill_size,
            betTargetType=limit_order_bet_target_type,
            betTargetSize=limit_order_bet_target_size
        )
        
        limit_on_close_order = LimitOnCloseOrder(
            liability=limit_on_close_order_liability,
            price=limit_on_close_order_price
        )
        
        market_on_close_order = MarketOnCloseOrder(
            liability=market_on_close_order_liability
        )
        
        market_version_obj = MarketVersion(
            version=market_version
        )
        
        instruction = PlaceInstruction(
            orderType=order_type,
            selectionId=selection_id,
            handicap=handicap,
            side=side,
            limitOrder=limit_order,
            limitOnCloseOrder=limit_on_close_order,
            marketOnCloseOrder=market_on_close_order,
            customerOrderRef=customer_order_ref
        )
        
        instructions = [instruction]

        json_data = PlaceOrders(marketId=market_id,
                                instructions=instructions,
                                customerRef=customer_ref,
                                marketVersion=market_version,
                                customerStrategyRef=customer_strategy_ref,
                                async_=None)#TODO

    def cancel_orders(self,
                      market_id: str,
                    bet_ids: List[str],
                    size_reductions: List[float],
                    customer_ref: str) -> CancelExecutionReport:
        
        instructions = [CancelInstruction(betId=bet_id, sizeReduction=size_reduction)
                        for bet_id, size_reduction in zip(bet_ids, size_reductions)]

    def replace_orders(self,
                       market_id: str,
                    bet_ids: List[str],
                    new_prices: List[float],
                    customer_ref: str,
                    market_version: int,
                    async_: bool) -> ReplaceExecutionReport:
        
        instructions = [ReplaceInstruction(betId=bet_id, newPrice=new_price)
                        for bet_id, new_price in zip(bet_ids, new_prices)]
        
        market_version_obj = MarketVersion(version=market_version)

    def update_orders(self,
                      market_id: str,
                    bet_ids: List[str],
                    new_persistence_types: List[PersistenceType],
                    customer_ref: str) -> UpdateExecutionReport:
        
        instructions = [UpdateInstruction(betId=bet_id, newPersistenceType=new_persistence_type)
                        for bet_id, new_persistence_type in zip(bet_ids, new_persistence_types)]
        
    def _request(self, method: str, endpoint: str, json_data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=json_data, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except requests.ConnectionError:
            raise Exception("A connection error occurred")
        except requests.Timeout:
            raise Exception("The request timed out")
        except requests.RequestException as e:
            raise Exception(f"An error occurred: {e}")

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", endpoint, json_data=json_data)

    def put(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("PUT", endpoint, json_data=json_data)

    def delete(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("DELETE", endpoint, json_data=json_data)

    def _handle_response(self, response: requests.Response) -> Any:
        if response.status_code >= 400:
            self._handle_api_specific_errors(response)
            raise Exception(f"HTTP {response.status_code}: {response.text}")
        try:
            return response.json()
        except ValueError:
            raise Exception("Invalid JSON response")