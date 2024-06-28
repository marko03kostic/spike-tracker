from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout
from PySide6.QtCore import Slot

from src.backend.betting_api.definitions import MarketCatalogue
from src.main_application import MainApplication

class InfoWidget(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._main_app: MainApplication = MainApplication.instance()
        self._market_catalogue: MarketCatalogue = market_catalogue
        
        self.initUI()
        
        self._main_app.exchange_stream.market_cache.markets[self._market_catalogue.get('marketId')].total_volume_updated.connect(self.update_total_volume)

    @Slot(int)
    def update_total_volume(self, total_volume: int):
        self.tv_label.setText(f"Total volume: {total_volume}")

    def initUI(self):
        layout = QVBoxLayout()
        
        self.top_label = QLabel("Market Info")
        layout.addWidget(self.top_label)

        form_layout = QFormLayout()
        
        self.tv_label = QLabel()
        form_layout.addRow(self.tv_label)

        self.event_name_label = QLabel(f"Event name: {self._market_catalogue.get('event').get('name')}")
        form_layout.addRow(self.event_name_label)

        self.market_name_label = QLabel(f"Market Name: {self._market_catalogue.get('marketName')}")
        form_layout.addRow(self.market_name_label)

        self.event_type_label = QLabel(f"Event Type: {self._market_catalogue.get('eventType').get('name')}")
        form_layout.addRow(self.event_type_label)

        self.competition_label = QLabel(f"Competition: {self._market_catalogue.get('competition').get('name')}")
        form_layout.addRow(self.competition_label)

        self.event_id_label = QLabel(f"Event ID: {self._market_catalogue.get('event').get('id')}")
        form_layout.addRow(self.event_id_label)
        
        self.market_id_label = QLabel(f"Market ID: {self._market_catalogue.get('marketId')}")
        form_layout.addRow(self.market_id_label)
        
        layout.addLayout(form_layout)
        self.setLayout(layout)