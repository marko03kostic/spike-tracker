from PySide6.QtWidgets import QDialog, QMainWindow, QToolBar, QTabWidget, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
from src.tracker_window import TrackerWindow
from src.add_market_dialog.add_market_by_id_dialog.dialog import AddMarketDialog

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.init_gui()

    def init_gui(self) -> None:
        self.setWindowTitle("SpikeTracker")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 900)
        self.resize(800, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.toolbar = QToolBar()
        self.add_market = self.toolbar.addAction('Add market', self.add_market_dialog_slot)
        self.remove_market = self.toolbar.addAction('Remove market', self.remove_market_slot)

        self.tab_widget = QTabWidget()

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.tab_widget)

    @Slot()
    def add_market_dialog_slot(self) -> None:
        dialog = AddMarketDialog(self)
        if dialog.exec() == QDialog.Accepted:
            event_name = dialog.market_catalogue.get('event', {}).get('name', None)
            market_name = dialog.market_catalogue.get('marketName', None)
            tab_title = f'{event_name} \n {market_name}'

            self.tab_widget.addTab(TrackerWindow(dialog.market_catalogue), tab_title)

    @Slot()
    def remove_market_slot(self) -> None:
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            widget = self.tab_widget.widget(current_index)
            self.tab_widget.removeTab(current_index)
            widget.deleteLater()