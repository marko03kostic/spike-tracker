from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

from src.backend.requests.betting_api_requests import get_list_event_types_request

from src.error_message import show_error_message

class AddMarketDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Market by Id")
        self.setMinimumSize(300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        
        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)
        
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)
        
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_clicked)
        button_layout.addWidget(self.add_button)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

    def add_clicked(self):
        get_list_event_types_request()
        if self.is_market_id_valid():
            self.accept()
        else:
            show_error_message("Invalid MarketId")

    def is_market_id_valid(self):
        input_text = self.input_field.text()
        return len(input_text) > 0 