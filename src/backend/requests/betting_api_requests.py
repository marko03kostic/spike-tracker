from typing import List, Optional
import requests

from src.main_application import MainApplication
from src.backend.models.betting_api.request import RequestHeaders, ListEventTypesRequest, ENDPOINT
from src.backend.models.betting_api.methods import Method
from src.backend.models.betting_api.params import Params
from src.backend.models.betting_api.list_event_types import (ListEventTypesParams,
                                                             MarketFilter,
                                                             MarketBettingType,
                                                             TimeRange,
                                                             OrderStatus)

def get_list_event_types_request(text_query: Optional[str] = None,
                                    event_type_ids: Optional[List[str]] = None,
                                    event_ids: Optional[List[str]] = None,
                                    competition_ids: Optional[List[str]] = None,
                                    market_ids: Optional[List[str]] = None,
                                    venues: Optional[List[str]] = None,
                                    bsp_only: Optional[bool] = None,
                                    turn_in_play_enabled: Optional[bool] = None,
                                    in_play_only: Optional[bool] = None,
                                    market_betting_types: Optional[List[MarketBettingType]] = None,
                                    market_countries: Optional[List[str]] = None,
                                    market_type_codes: Optional[List[str]] = None,
                                    time_range_from: Optional[str] = None,
                                    time_range_to: Optional[str] = None,
                                    with_orders: Optional[List[OrderStatus]] = None,
                                    race_types: Optional[List[str]] = None,
                                    locale: Optional[str] = None) -> ListEventTypesRequest:

    market_start_time = TimeRange(from_=time_range_from,
                                  to=time_range_to)

    market_filter = MarketFilter(textQuery=text_query,
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

    list_event_types_params = ListEventTypesParams(filter=market_filter,
                                                   locale=locale)

    list_event_types_request = ListEventTypesRequest(params=list_event_types_params,
                                                     jsonrpc='2.0',
                                                     method=Method.LIST_EVENT_TYPES.value)

    get(params=list_event_types_request)

def create_request_headers(app_key: str, SSOID: str) -> RequestHeaders:
    return RequestHeaders(X_Application=app_key,
                          X_Authentication=SSOID,
                          content_type='application/json')

def get(params: Params) -> None:
    app = MainApplication.instance() 

    headers = create_request_headers(app_key=app.app_key,
                                     SSOID=app.SSOID)

    '''response = requests.get(url=f'{headers=headers,
                                      params=params)'''
    
    print(headers)
    print(params)