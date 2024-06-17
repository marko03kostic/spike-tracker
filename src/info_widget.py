from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit

from src.backend.betting_api.definitions import MarketCatalogue

class InfoWidget(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._market_catalogue: MarketCatalogue = market_catalogue
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        top_label = QLabel("Market Info")
        layout.addWidget(top_label)

        form_layout = QFormLayout()

        market_id_label = QLabel(f"Event name: {self._market_catalogue.get('event').get('name')}")
        form_layout.addRow(market_id_label)

        market_name_label = QLabel(f"Market Name: {self._market_catalogue.get('marketName')}")
        form_layout.addRow(market_name_label)

        market_id_label = QLabel(f"Event Type: {self._market_catalogue.get('eventType').get('name')}")
        form_layout.addRow(market_id_label)

        event_id_label = QLabel(f"Competition: {self._market_catalogue.get('competition').get('name')}")
        form_layout.addRow(event_id_label)

        market_id_label = QLabel(f"Event ID: {self._market_catalogue.get('event').get('id')}")
        form_layout.addRow(market_id_label)
        
        market_id_label = QLabel(f"Market ID: {self._market_catalogue.get('marketId')}")
        form_layout.addRow(market_id_label)
        
        layout.addLayout(form_layout)
        self.setLayout(layout)