from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QScrollArea, QPushButton
from typing import Optional

from src.market_tab.info_widget import InfoWidget
from src.backend.betting_api.definitions import MarketCatalogue
from src.backend.exchange_stream_api.stream import ExchangeStream
from src.market_tab.selection_widget.selection_widget import SelectionWidget

class MarketTab(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self.market_catalogue: MarketCatalogue = market_catalogue
        self.selections = {}
        self.init_selections()
        self.init_gui()

    def init_gui(self):
        self.info_widget = InfoWidget(self.market_catalogue)

        left_layout = QVBoxLayout()
        for selection in self.selections.values():
            left_layout.addWidget(selection)
        
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(left_widget)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.info_widget)
        
        self.bottom_widget = QPushButton('kurac na biciklu')
        right_layout.addWidget(self.bottom_widget)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        right_layout.addItem(spacer)

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(scroll_area, 2)
        main_layout.addLayout(right_layout, 1)

        self.setLayout(main_layout)

    def init_selections(self):
        market_id = self.market_catalogue.get('marketId')

        for runner in self.market_catalogue.get('runners'):
            selection_id = runner.get('selectionId')
            handicap = runner.get('handicap')
            runner_name = runner.get('runnerName')

            self.selections[selection_id] = SelectionWidget(market_id, selection_id, handicap, runner_name, parent=self)

    @property
    def market_catalogue(self) -> Optional[MarketCatalogue]:
        return self._market_catalogue

    @market_catalogue.setter
    def market_catalogue(self, value: Optional[MarketCatalogue]) -> None:
        self._market_catalogue = value
