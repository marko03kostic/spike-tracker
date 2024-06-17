from threading import Thread, Event
from typing import List, Union
import socket
import ssl
import json
import time

from src.main_application import MainApplication
from src.backend.exchange_stream.enums import (BettingType,
                                               Field,
                                               OP)
from src.backend.exchange_stream.definitions import (BetfairRequestMessage,
                                                     BetfairMarketSubscriptionMessage,
                                                     BetfairMarketFilter,
                                                     BetfairMarketDataFilter,
                                                     BetfairAuthenticationMessage)


class ExchangeStream(Thread):
    
    def __init__(self) -> None:
        super().__init__(daemon=True)
        self.main_app: MainApplication = MainApplication.instance()
        self._stop_event = Event()
        self._running = True
        self.HOST = 'stream-api.betfair.com'
        self.PORT = 443
        self.sock = None

    def connect(self) -> None:
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.sock = socket.create_connection((self.HOST, self.PORT))
        self.sock = context.wrap_socket(self.sock, server_hostname=self.HOST)

    def run(self) -> None:
        self.connect()
        try:
            recv_buffer = ""
            while not self._stop_event.is_set():
                received_data = self.sock.recv(10000)
                if not received_data:
                    break
                recv_buffer += received_data.decode('utf-8')
                while "\r\n" in recv_buffer:
                    message, recv_buffer = recv_buffer.split("\r\n", 1)
                    if message:
                        print(message)

        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            self.close()

    def close(self) -> None:
        if self.sock:
            self.sock.close()
            print('Connection closed')

    def send(self, data: BetfairRequestMessage) -> None:
        if not self._stop_event.is_set():
            while not self.sock:
                time.sleep(1)
            json_data = json.dumps(data)
            message = json_data + "\r\n"
            try:
                self.sock.sendall(message.encode('utf-8'))
            except socket.error as e:
                print(f"Failed to send data: {e}")

    def stop(self) -> None:
        self._stop_event.set()

    def send_market_subscription_message(self,
                                         id: str = None,
                                        segmentation_enabled: bool = None,
                                        conflate_ms: int = None,
                                        heartbeat_ms: int = None,
                                        initial_clk: str = None,
                                        clk: str = None,
                                        country_codes: List[str] = None,
                                        betting_types: List[BettingType] = None,
                                        turn_in_play_enabled: bool = None,
                                        market_types: List[str] = None,
                                        venues: List[str] = None,
                                        market_ids: List[str] = None,
                                        event_type_ids: List[str] = None,
                                        event_ids: List[str] = None,
                                        bsp_market: bool = None,
                                        race_types: List[str] = None,
                                        ladder_levels: int = None,
                                        fields: List[Field] = None) -> None:
        
        market_filter = BetfairMarketFilter(countryCodes=country_codes,
                                            bettingTypes=betting_types,
                                            turnInPlayEnabled=turn_in_play_enabled,
                                            marketTypes=market_types,
                                            venues=venues,
                                            marketIds=market_ids,
                                            eventTypeIds=event_type_ids,
                                            eventIds=event_ids,
                                            bspMarket=bsp_market,
                                            raceTypes=race_types)
        
        market_data_filter = BetfairMarketDataFilter(ladderLevels=ladder_levels,
                                                    fields=fields)

        message = BetfairMarketSubscriptionMessage(op=OP.marketSubscription.value,
                                                id=id,
                                                segmentationEnabled=segmentation_enabled,
                                                conflateMs=conflate_ms,
                                                heartbeatMs=heartbeat_ms,
                                                initialClk=initial_clk,
                                                clk=clk,
                                                marketFilter=market_filter,
                                                marketDataFilter=market_data_filter)
        self.send(data=message)

    def send_authentication_message(self, id: str = None) -> None:
        
        message = BetfairAuthenticationMessage(op=OP.authentication.value,
                                                id=id,
                                                appKey=self.main_app.app_key,
                                                session=self.main_app.ssoid)
        self.send(data=message)