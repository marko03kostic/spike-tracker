from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

from add_market_dialog.add_market_select_dialog.events_markets_tree import EventsMarketsTree

class AddMarketDialog(QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("SpikeTracker")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 900)
        self.resize(400, 400)
        self.init_gui()

    def init_gui(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Would you like to start tracking a new market?")
        layout.addWidget(self.label)

        self.market_events_tree_widget = EventsMarketsTree()
        layout.addWidget(self.market_events_tree_widget)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Add")
        self.cancel_button = QPushButton("Cancel")

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)