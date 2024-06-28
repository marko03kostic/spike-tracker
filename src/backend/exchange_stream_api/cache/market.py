from typing import List, Union, Dict
from dataclasses import dataclass, field
from PySide6.QtCore import QObject, Signal

from src.backend.exchange_stream_api.definitions import BetfairRunnerChange, BetfairMarketDefinition

class Market(QObject):
    full_price_ladder_updated = Signal(str)
    level_based_ladder_updated = Signal(dict)
    single_values_updated = Signal(dict)
    total_volume_updated = Signal(int)
    market_definition_updated = Signal(BetfairMarketDefinition)

    def __init__(self, market_id: str):
        super().__init__()
        self.market_id = market_id
        self.full_price_ladder: Dict[int, Dict[str, Dict[float, float]]] = {}
        self.level_based_ladder: Dict[int, Dict[str, List[List[Union[float, int]]]]] = {}
        self.single_values: Dict[int, Dict[str, Union[int, float]]] = {}
        self.total_volume: int = 0
        self.market_definition: BetfairMarketDefinition = BetfairMarketDefinition()

    def update(self, runner_changes: List[BetfairRunnerChange]) -> None:
        for runner_change in runner_changes:

            tv = runner_change.get('tv', None)
            ltp = runner_change.get('ltp', None)
            spn = runner_change.get('spn', None)
            spf =  runner_change.get('spf', None)
            batb = runner_change.get('batb', [])
            batl = runner_change.get('batl', [])
            bdatb = runner_change.get('bdatb', [])
            bdatl = runner_change.get('bdatl', [])
            atb = runner_change.get('atb', [])
            atl = runner_change.get('atl', [])
            spb = runner_change.get('spb', [])
            spl = runner_change.get('spl', [])
            trd = runner_change.get('trd', [])

            hc = runner_change.get('hc', None)

            runner_id = runner_change.get('id')
            runner_id = runner_id if not hc else f'{runner_id}_{hc}'

            self.update_single_values(tv, 'tv', runner_id)
            self.update_single_values(ltp, 'ltp', runner_id)
            self.update_single_values(spn, 'spn', runner_id)
            self.update_single_values(spf, 'spf', runner_id)

            self.update_level_based_ladder(batb, 'batb', runner_id)
            self.update_level_based_ladder(batl, 'batl', runner_id)
            self.update_level_based_ladder(bdatb, 'bdatb', runner_id)
            self.update_level_based_ladder(bdatl, 'bdatl', runner_id)

            self.update_full_price_ladder(atb, 'atb', runner_id)
            self.update_full_price_ladder(atl, 'atl', runner_id)
            self.update_full_price_ladder(trd, 'trd', runner_id)
            self.update_full_price_ladder(spb, 'spb', runner_id)
            self.update_full_price_ladder(spl, 'spl', runner_id)
            
            self.full_price_ladder_updated.emit(str(self.full_price_ladder))

    def update_full_price_ladder(self, updates: List[List[float]], selection_name: str, runner_id: int) -> None:
        if updates:
            for price_size in updates:
                price = price_size[0]
                size = price_size[1]

                if size != 0:
                    self.full_price_ladder.setdefault(runner_id, {}).setdefault(selection_name, {})[price] = size
                else:
                    self.full_price_ladder.setdefault(runner_id, {}).setdefault(selection_name, {}).pop(price, None)
            
    def update_level_based_ladder(self, updates: List[List[Union[float, int]]], selection_name: str, runner_id: int) -> None:
        ladder_dict = {}
        for i in range(10):
            ladder_dict[i] = [i, 0, 0]
        for position in self.level_based_ladder.setdefault(runner_id, {}).setdefault(selection_name, []):
            ladder_dict[position[0]] = position
        for update in updates:
            position, back_price, lay_price = update
            ladder_dict[position] = update
        self.level_based_ladder.setdefault(runner_id, {})[selection_name] = sorted(list(ladder_dict.values()), key=lambda x: x[0])
        self.level_based_ladder_updated.emit(self.level_based_ladder)
        
    def update_single_values(self, update: Union[int, float], name: str, runner_id: int) -> None:
        if update:
            self.single_values.setdefault(runner_id, {})[name] = update
            self.single_values_updated.emit(self.single_values)
            
    def update_total_volume(self, total_volume: float) -> None:
        if total_volume:
            self.total_volume = total_volume
            self.total_volume_updated.emit(self.total_volume)

    def update_market_definition(self, market_definition: BetfairMarketDefinition) -> None:
        if market_definition:
            self.market_definition = market_definition
            self.market_definition_updated.emit(self.market_definition)