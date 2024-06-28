from PySide6.QtWidgets import QApplication
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.backend.betting_api.client import BettingAPIClient
    from src.backend.exchange_stream_api.stream import ExchangeStream

class MainApplication(QApplication):
    
    def __init__(self, argv) -> None:
        super().__init__(argv)
        self._betting_api_client: Optional[BettingAPIClient] = None
        self._exchange_stream: Optional[ExchangeStream] = None
        self._ssoid: Optional[str] = None
        self._app_key: Optional[str] = None

    @property
    def ssoid(self) -> Optional[str]:
        return self._ssoid

    @ssoid.setter
    def ssoid(self, value: Optional[str]) -> None:
        self._ssoid = value

    @property
    def app_key(self) -> Optional[str]:
        return self._app_key

    @app_key.setter
    def app_key(self, value: Optional[str]) -> None:
        self._app_key = value

    @property
    def betting_api_client(self) -> Optional['BettingAPIClient']:
        return self._betting_api_client

    @betting_api_client.setter
    def betting_api_client(self, value: Optional['BettingAPIClient']) -> None:
        self._betting_api_client = value
        
    @property
    def exchange_stream(self) -> Optional['ExchangeStream']:
        return self._exchange_stream

    @exchange_stream.setter
    def exchange_stream(self, value: Optional['ExchangeStream']) -> None:
        self._exchange_stream = value