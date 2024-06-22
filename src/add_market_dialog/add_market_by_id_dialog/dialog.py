from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Slot
import re

from src.main_application import MainApplication
from src.error_message import show_error_message
from src.backend.betting_api.enums import MarketStatus, MarketProjection
from src.backend.betting_api.definitions import MarketCatalogue

class AddMarketDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._main_app: MainApplication = MainApplication.instance()
        self._market_id: str = None
        self._market_catalogue: MarketCatalogue = None

        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle("Add Market by Id")
        self.setMinimumSize(300, 200)

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

    @Slot()
    def add_clicked(self) -> None:
        if self.is_input_valid():
            if self.set_valid_market_catalogue():
                self.accept()
            else:
                show_error_message('An unexpected error occurred')

    def is_input_valid(self) -> bool:
        input = self.input_field.text()
        if self.is_input_correct_format(input):
            return self.is_market_id_valid(input)
        return False

    def is_market_id_valid(self, market_id: str) -> bool:
        market_books = self._main_app.betting_api_client.list_market_book(market_ids=[market_id,])
        if market_books:
            market_book = market_books[0]
            if market_book.get('marketId') == market_id:
                market_status = market_book.get('status', None)
                if market_status == MarketStatus.OPEN.value:
                    self.market_id = market_id
                    return True
                elif market_status == MarketStatus.INACTIVE.value:
                    show_error_message("Market is inactive")
                    return False
                elif market_status == MarketStatus.SUSPENDED.value:
                    show_error_message("Market is suspended")
                    return False
                elif market_status == MarketStatus.CLOSED.value:
                    show_error_message("Market is closed")
                    return False
        show_error_message("Market not found")
        return False
        
    def is_input_correct_format(self, input: str) -> bool:
        pattern = r'^\d\.\d+$'
        if re.match(pattern, input):
            return True
        show_error_message("Invalid format")
        return False

    def set_valid_market_catalogue(self) -> bool:
        market_catalogues = self._main_app.betting_api_client.list_market_catalogue(
            market_ids=[self.market_id],
            max_results=1,
            market_projection=[
                MarketProjection.COMPETITION.value,
                MarketProjection.EVENT.value,
                MarketProjection.EVENT_TYPE.value,
                MarketProjection.MARKET_DESCRIPTION.value,
                MarketProjection.MARKET_START_TIME.value,
                MarketProjection.RUNNER_DESCRIPTION.value,
                MarketProjection.RUNNER_METADATA.value
            ]
        )
        if market_catalogues:
            market_catalogue = market_catalogues[0]
            if market_catalogue.get('marketId') == self.market_id:
                self.market_catalogue = market_catalogue
                return True
        return False

    @property
    def market_id(self) -> str:
        return self._market_id

    @market_id.setter
    def market_id(self, value: str) -> None:
        self._market_id = value

    @property
    def market_catalogue(self) -> MarketCatalogue:
        return self._market_catalogue

    @market_catalogue.setter
    def market_catalogue(self, value: MarketCatalogue) -> None:
        self._market_catalogue = value