import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QTabWidget, QVBoxLayout, QWidget
from src.backend.slots import add_market_slot, remove_market_slot

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SpikeTracker")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 900)
        self.resize(800, 600)
        self.init_gui()

    def init_gui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.toolbar = QToolBar()
        self.toolbar.addAction('Add market', lambda: add_market_slot(self))
        self.toolbar.addAction('Remove market', lambda: remove_market_slot(self))

        self.tab_widget = QTabWidget()

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.tab_widget)
