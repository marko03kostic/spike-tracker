import pytest
from unittest.mock import patch, Mock
from PySide6.QtWidgets import QWidget

from src.market_tab.market_tab import MarketTab

@pytest.fixture
def market_catalogue():
    return {
        'marketId': '1.23456789',
        'runners': [
            {'selectionId': '1', 'handicap': 0, 'runnerName': 'Runner 1'},
            {'selectionId': '2', 'handicap': 0, 'runnerName': 'Runner 2'}
        ]
    }

@pytest.fixture
def mock_exchange_stream():
    with patch('src.market_tab.market_tab.ExchangeStream') as MockExchangeStream:
        mock_stream = MockExchangeStream.return_value
        yield mock_stream

@pytest.fixture
def mock_selection_widget():
    mock_selection_widget = Mock()
    with patch('src.market_tab.market_tab.SelectionWidget', mock_selection_widget):
        yield mock_selection_widget
    mock_selection_widget.reset_mock()

@pytest.fixture
def mock_info_widget():
    mock_info_widget = Mock(spec=QWidget)
    with patch('src.market_tab.market_tab.InfoWidget', mock_info_widget):
        yield mock_info_widget
    mock_info_widget.reset_mock()

@pytest.fixture
def market_tab(qtbot, market_catalogue, mock_exchange_stream, mock_selection_widget, mock_info_widget):
    market_tab = MarketTab(market_catalogue=market_catalogue,
                           exchange_stream=mock_exchange_stream)
    market_tab.show()
    qtbot.add_widget(market_tab)

    yield market_tab

    market_tab.close()
