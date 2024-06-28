from PySide6.QtWidgets import QDialog, QMainWindow, QToolBar, QTabWidget, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Slot
from src.market_tab.market_tab import MarketTab
from src.main_application import MainApplication
from src.add_market_dialog.add_market_by_id_dialog.dialog import AddMarketDialog

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self._main_app: MainApplication = MainApplication.instance()
        self.add_market_dialog = None
        self.init_gui()

    def init_gui(self) -> None:
        self.setWindowTitle("SpikeTracker")
        self.setMinimumSize(900, 500)
        self.setMaximumSize(1920, 1080)
        self.resize(900, 500)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.toolbar = QToolBar()

        self.add_market = QPushButton('Add market')
        self.toolbar.addWidget(self.add_market)
        self.add_market.clicked.connect(self.add_market_dialog_slot)

        self.remove_market = QPushButton('Remove market')
        self.toolbar.addWidget(self.remove_market)
        self.remove_market.clicked.connect(self.remove_market_slot)

        self.tab_widget = QTabWidget()

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.tab_widget)

    @Slot()
    def add_market_dialog_slot(self) -> None:
        self.add_market_dialog = AddMarketDialog()
        self.add_market_dialog.show()
        self.add_market_dialog.accepted.connect(self.add_market_dialog_accepted_slot)
        self.add_market_dialog.finished.connect(self.reset_add_market_dialog)

    @Slot()
    def add_market_dialog_accepted_slot(self) -> None:
        market_id = self.add_market_dialog.market_catalogue.get('marketId')
        self._main_app.exchange_stream.add_market(market_id)
        
        event_name = self.add_market_dialog.market_catalogue.get('event', {}).get('name', None)
        market_name = self.add_market_dialog.market_catalogue.get('marketName', None)
        tab_title = f'{event_name} \n {market_name}'

        market_tab = MarketTab(self.add_market_dialog.market_catalogue)
        self.tab_widget.addTab(market_tab, tab_title)

    @Slot()
    def remove_market_slot(self) -> None:
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            widget = self.tab_widget.widget(current_index)
            market_id = widget.market_catalogue.get('marketId')
            self._main_app.exchange_stream.remove_market(market_id)
            self.tab_widget.removeTab(current_index)
            widget.deleteLater()

    @Slot()
    def reset_add_market_dialog(self) -> None:
        self.add_market_dialog = None