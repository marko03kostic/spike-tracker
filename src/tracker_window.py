from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout

from src.backend.betting_api.definitions import MarketCatalogue

class TrackerWindow(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._market_catalogue: MarketCatalogue = market_catalogue
        self.edit = QLineEdit("Market tracking window")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
