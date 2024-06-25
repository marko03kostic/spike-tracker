from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QScrollArea

from src.market_tab.selection_widget.graph import RunnerChart
from src.backend.graphs_api.client import GraphsAPIClient

class SelectionWidget(QWidget):

    def __init__(self,
                 market_id: str,
                 selection_id: int,
                 handicap: int,
                 runner_name: str,
                 parent=None) -> None:
        
        super().__init__(parent)
        self.market_id = market_id
        self.selection_id = selection_id
        self.handicap = handicap
        self.runner_name = runner_name

        self.chart = RunnerChart(GraphsAPIClient().load_runner_chart(market_id, selection_id, handicap), title=runner_name)
        self.ladder = None
        self.init_gui()

    def init_gui(self):
        layout = QHBoxLayout()
        layout.addWidget(self.chart)
        
        self.setLayout(layout)