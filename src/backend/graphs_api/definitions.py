from typing import TypedDict, Literal, Union, List

class LoadRunnerChart(TypedDict):
    marketId: str
    selectionId: int
    handicap: float
    alt: Literal['json']

class Point(TypedDict):
    value: Union[int, float]
    volume: Union[int, float]
    timestamp: int

class RunnerChartResult(TypedDict):
    points: List[Point]
    factor: int