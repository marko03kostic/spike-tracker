from dataclasses import dataclass

from src.backend.exchange_stream_api.definitions import BetfairConnectionMessage

@dataclass
class ConnectionCache:
    connection_id: str = None

    def update(self, message: BetfairConnectionMessage) -> None:
        self.connection_id = message.get('connectionId')