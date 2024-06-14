from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
import re

from src.main_application import MainApplication
from src.error_message import show_error_message

class AddMarketDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_app: MainApplication = MainApplication.instance()
        self.setWindowTitle("Add Market by Id")
        self.setMinimumSize(300, 200)
        self.init_ui()

    def init_ui(self) -> None:
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

    def add_clicked(self) -> None:
        if self.is_input_valid():
            self.accept()

    def is_market_id_valid(self, market_id) -> bool:
        if self.main_app.betting_api_client.list_market_book(market_ids=[market_id,]):
            return True
        show_error_message("MarketId not found")
        return False
        
    def is_input_correct_format(self, input) -> bool:
        pattern = r'^\d\.\d+$'
        if re.match(pattern, input):
            return True
        show_error_message("Invalid format")
        return False
        
    def is_input_valid(self) -> bool:
        input = self.input_field.text()
        if self.is_input_correct_format(input):
            return self.is_market_id_valid(input)
        return False