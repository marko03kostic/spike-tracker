from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFormLayout

from src.backend.betting_api.definitions import MarketCatalogue

class InfoWidget(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._market_catalogue: MarketCatalogue = market_catalogue
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.top_label = QLabel("Market Info")
        layout.addWidget(self.top_label)

        form_layout = QFormLayout()

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