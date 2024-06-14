from PySide6.QtWidgets import QApplication
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.backend.betting_api.client import BaseAPIClient 



class MainApplication(QApplication):
    _instance = None

    def __init__(self, argv):
        if MainApplication._instance:
            raise RuntimeError("MainApplication is a singleton class and has already been initialized.")
        super().__init__(argv)
        MainApplication._instance = self
        self._betting_api_client: BaseAPIClient = None
        self._ssoid = None
        self._app_key = None

    @staticmethod
    def instance() -> 'MainApplication':
        if not MainApplication._instance:
            raise RuntimeError("MainApplication instance not initialized yet")
        return MainApplication._instance
    
    @property
    def ssoid(self):
        return self._ssoid

    @ssoid.setter
    def ssoid(self, value):
        self._ssoid = value

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value

    @property
    def betting_api_client(self):
        return self._betting_api_client
    
    @betting_api_client.setter
    def betting_api_client(self, value):
        self._betting_api_client = value