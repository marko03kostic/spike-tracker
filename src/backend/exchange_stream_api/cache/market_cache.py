from typing import List, Dict
from dataclasses import dataclass, field
from threading import Timer
import time

from src.backend.exchange_stream_api.cache.market import Market
from src.backend.exchange_stream_api.enums import (StatusCode,
                               ChangeType)
from src.backend.exchange_stream_api.definitions import (BetfairRunnerChange,
                                                    BetfairMarketDefinition,
                                                    BetfairMarketChangeMessage)

@dataclass
class MarketCache:
    markets: Dict[str, Market] = field(default_factory=dict)
    total_volumes: Dict[str, int | float] = field(default_factory=dict)
    market_definitions: Dict[str, Dict] = field(default_factory=dict)
    spike_tracker = None
    market_heartbeat_timer: Timer | None = None
    market_heartbeat_interval: int | None = None
    latency_threshold_ms: int = 5000

    def update(self, message: BetfairMarketChangeMessage) -> None:
        if self.market_heartbeat_timer:
            self.market_heartbeat_timer.cancel()

        heartbeat_ms = message.get('heartbeatMs', None)
        if heartbeat_ms:
            self.market_heartbeat_interval = (heartbeat_ms / 1000)*1.05

        if self.market_heartbeat_interval:
            self.market_heartbeat_timer = Timer(self.market_heartbeat_interval, self.handle_missing_heartbeat)
            self.market_heartbeat_timer.start()

        initial_clk = message.get('initialClk')
        clk = message.get('clk')
        change_type = message.get('ct')
        segment_type = message.get('segmentType')
        conflate_ms = message.get('conflateMs')
        status = message.get('status')
        publish_time = message.get('pt')
        market_changes = message.get('mc')

        if clk:
            self.clk = clk
        if initial_clk:
            self.initial_clk = initial_clk

        latency_ms = int(time.time() * 1000) - publish_time
        if latency_ms > self.latency_threshold_ms and latency_ms < 1000000:
            print('Market change latency high!!!')

        if status == StatusCode.FAILURE.value:
            print(StatusCode.FAILURE.value)

        if change_type == ChangeType.SUB_IMAGE.value:
            self.clear_cache()
        elif change_type == ChangeType.RESUB_DELTA.value:
            pass
        elif change_type == ChangeType.HEARTBEAT.value:
            pass

        #self.update_spike_tracker(message, self.markets, publish_time)
        
        if market_changes:
            for market_change in market_changes:
                market_id = market_change.get('id')
                runner_changes = market_change.get('rc')
                total_volume = market_change.get('tv', None)
                image = market_change.get('img', False)
                market_definition = market_change.get('marketDefinition', None)

                self.update_runners(runner_changes, image, market_id)
                self.update_total_volume(total_volume, market_id)
                self.update_market_definition(market_definition, market_id)

    def update_runners(self, runner_changes: List[BetfairRunnerChange], image: bool, market_id: str) -> None:
        if image:
            market = self.add_market(market_id)
            self.markets[market_id] = market
            self.markets.get(market_id).update(runner_changes)
        else:
            try:
                self.markets.get(market_id).update(runner_changes)
            except AttributeError:
                market = self.add_market(market_id)
                self.markets[market_id] = market
                self.markets.get(market_id).update(runner_changes)

    def update_total_volume(self, total_volume: float, market_id: str) -> None:
        if total_volume:
            self.total_volumes[market_id] = total_volume

    def update_market_definition(self, market_definition: BetfairMarketDefinition, market_id: str) -> None:
        if market_definition:
            self.market_definitions[market_id] = market_definition

    def update_spike_tracker(self, message: BetfairMarketChangeMessage, markets: Dict[str, Market], publish_time: str) -> None:
        self.spike_tracker.update(message, markets, publish_time)

    def add_market(self, market_id: str) -> Market:
        market = Market(market_id)
        self.markets[market_id] = market
        self.total_volumes[market_id] = None
        self.market_definitions[market_id] = None
        return market

    def clear_cache(self) -> None:
        self.markets.clear()
        self.total_volumes.clear()
        self.market_definitions.clear()

    def handle_missing_heartbeat(self) -> None:
        print('Market heartbeat missing!!!')