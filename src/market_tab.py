from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QScrollArea

from src.info_widget import InfoWidget
from src.backend.betting_api.definitions import MarketCatalogue
from src.backend.exchange_stream_api.stream import ExchangeStream
from src.graph import RunnerChartWidget
from src.backend.graphs_api.client import GraphsAPIClient

class MarketTab(QWidget):

    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self._market_catalogue: MarketCatalogue = market_catalogue
        self.charts = {}
        self.init_charts()
        self.init_gui()
        self._exchange_stream: ExchangeStream = ExchangeStream()
        self._exchange_stream.start()
        self._exchange_stream.send_authentication_message()
        self._exchange_stream.send_market_subscription_message(market_ids=[self._market_catalogue.get('marketId')])

    def init_gui(self):
        self.info_widget = InfoWidget(self._market_catalogue)

        # Left layout for charts
        left_layout = QVBoxLayout()
        for chart_widget in self.charts.values():
            left_layout.addWidget(chart_widget)
        
        # Scroll area for left layout
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(left_widget)

        # Right layout for info and bottom widget
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.info_widget)
        
        self.bottom_widget = QLineEdit("Bottom Widget")  # Replace with your actual bottom widget
        right_layout.addWidget(self.bottom_widget)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        right_layout.addItem(spacer)

        # Main layout
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(scroll_area, 2)  # Left layout takes 2/3 of the space
        main_layout.addLayout(right_layout, 1)  # Right layout takes 1/3 of the space

        self.setLayout(main_layout)


    def init_charts(self):
        market_id = self._market_catalogue.get('marketId')

        for runner in self._market_catalogue.get('runners'):
            selection_id = runner.get('selectionId')
            handicap = runner.get('handicap')

            self.charts[selection_id] = RunnerChartWidget(GraphsAPIClient().load_runner_chart(market_id, selection_id, handicap))


    def __del__(self):
        self._exchange_stream.stop()
