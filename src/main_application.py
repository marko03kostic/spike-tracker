from PySide6.QtWidgets import QApplication
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.backend.betting_api.client import BettingAPIClient

class MainApplication(QApplication):
    _instance = None

    def __init__(self, argv) -> None:
        if MainApplication._instance:
            raise RuntimeError("MainApplication is a singleton class and has already been initialized.")
        super().__init__(argv)
        MainApplication._instance = self
        self._betting_api_client: Optional[BettingAPIClient] = None
        self._ssoid: Optional[str] = None
        self._app_key: Optional[str] = None

    @staticmethod
    def instance() -> 'MainApplication':
        if not MainApplication._instance:
            raise RuntimeError("MainApplication instance not initialized yet")
        return MainApplication._instance
    
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