from PySide6.QtWidgets import QApplication

class MainApplication(QApplication):
    _instance = None

    def __init__(self, argv):
        super().__init__(argv)
        if not MainApplication._instance:
            MainApplication._instance = self
        self._SSOID = None
        self._app_key = None

    @staticmethod
    def instance() -> 'MainApplication':
        if not MainApplication._instance:
            raise RuntimeError("MainApplication instance not initialized yet")
        return MainApplication._instance

    @property
    def SSOID(self):
        return self._SSOID

    @SSOID.setter
    def SSOID(self, value):
        self._SSOID = value

    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value