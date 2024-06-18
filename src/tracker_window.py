from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout

from src.info_widget import InfoWidget
from src.backend.betting_api.definitions import MarketCatalogue
from src.backend.exchange_stream.stream import ExchangeStream

class TrackerWindow(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._market_catalogue: MarketCatalogue = market_catalogue
        self.init_gui()
        self._exchange_stream: ExchangeStream = ExchangeStream()
        self._exchange_stream.start()
        self._exchange_stream.send_authentication_message()
        self._exchange_stream.send_market_subscription_message(market_ids=[self._market_catalogue.get('marketId')])

    def init_gui(self):
        self.edit = QLineEdit("Market tracking window")
        self.info_widget = InfoWidget(self._market_catalogue)

        layout = QVBoxLayout()
        layout.addWidget(self.info_widget)
        layout.addWidget(self.edit)

        self.setLayout(layout)

    def __del__(self):
        self._exchange_stream.stop()
