from typing import List, Union
from dataclasses import dataclass, field

from src.backend.exchange_stream.definitions import BetfairRunnerChange

@dataclass
class Market:
    market_id: str
    full_price_ladder: dict = field(default_factory=dict)
    level_based_ladder: dict = field(default_factory=dict)
    single_values: dict = field(default_factory=dict)

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

    def update_single_values(self, update: Union[int, float], name: str, runner_id: int) -> None:
        if update:
            self.single_values.setdefault(runner_id, {})[name] = update