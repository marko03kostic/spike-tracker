from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QScrollArea
from PySide6.QtCore import Slot
import json

from src.main_application import MainApplication
from src.market_tab.selection_widget.graph import RunnerChart
from src.backend.exchange_stream_api.definitions import BetfairMarketDefinition
from src.market_tab.selection_widget.ladder import BetfairLadderWidget
from src.backend.graphs_api.client import GraphsAPIClient

class SelectionWidget(QWidget):

    def __init__(self,
                 market_id: str,
                 selection_id: int,
                 handicap: int,
                 runner_name: str,
                 parent=None) -> None:
        
        super().__init__(parent)
        self._main_app: MainApplication = MainApplication.instance()
        self.market_id = market_id
        self.selection_id = selection_id
        self.handicap = handicap
        self.runner_name = runner_name

        self.chart = RunnerChart(GraphsAPIClient().load_runner_chart(market_id, selection_id, handicap), title=runner_name)
        self.ladder = BetfairLadderWidget(selection_id)
        self.init_gui()
        
        self._main_app.exchange_stream.market_cache.markets[self.market_id].full_price_ladder_updated.connect(self.update_full_price_ladder)
        
    @Slot(str)
    def update_full_price_ladder(self, full_price_ladder):
        if full_price_ladder:
            full_price_ladder = eval(full_price_ladder)
            self.ladder.updateData(full_price_ladder)
            
    def init_gui(self):
        layout = QHBoxLayout()
        layout.addWidget(self.chart)
        layout.addWidget(self.ladder)
        
        self.setLayout(layout)