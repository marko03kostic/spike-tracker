from typing import TypedDict, Literal, Union
from enum import Enum

from src.backend.models.betting_api.params import Params
from src.backend.models.betting_api.methods import Method


ENDPOINT = 'https://api.betfair.com/exchange/betting/json-rpc/v1'


class RequestHeaders(TypedDict):
    X_Application: str
    X_Authentication: str
    content_type: Literal['application/json']

    
class Request(TypedDict):
    jsonrpc: Literal['2.0']
    method: Method
    params: Params


class ListEventTypesRequest(Request):
    method: Literal[Method.LIST_EVENT_TYPES]
    params: Params.LIST_EVENT_TYPES