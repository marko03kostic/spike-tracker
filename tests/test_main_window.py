
from PySide6.QtCore import Qt, QSize
from pytestqt.qtbot import QtBot
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QTabWidget, QWidget, QPushButton
from unittest.mock import patch, Mock
import pytest

from src.backend.betting_api.definitions import MarketCatalogue
from src.main_window import MainWindow

@pytest.fixture
def main_window(qtbot):
    main_window = MainWindow()
    main_window.show()
    qtbot.add_widget(main_window)

    yield main_window

    main_window.close()

def test_main_window_initialization(main_window):
    """Test MainWindow initialization."""

    assert main_window.windowTitle() == "SpikeTracker"
    assert main_window.minimumSize() == QSize(400, 300)
    assert main_window.maximumSize() == QSize(1920, 1080)
    assert main_window.size() == QSize(800, 600)
    assert main_window.add_market == QPushButton('Add market')
    assert main_window.remove_market == QPushButton('Remove market')
    assert main_window.tab_widget == QTabWidget()

def test_add_market_dialog_slot(main_window):
    """Test add_market_dialog_slot method."""

    QTest.mouseClick(main_window.add_market, Qt.MouseButton.LeftButton)
    QTest.qWaitForWindowFocused(main_window.add_market_dialog)
    main_window.add_market_dialog.close()

    assert not main_window.add_market_dialog

def test_reset_add_market_dialog(main_window):

    main_window.add_market_dialog = '1234'

    main_window.reset_add_market_dialog()

    assert not main_window.add_market_dialog


class MockMarketTab(QWidget):
    def __init__(self, market_catalogue: MarketCatalogue, parent=None) -> None:
        super().__init__(parent)
        self.market_catalogue: MarketCatalogue = market_catalogue   

@patch('src.main_window.MarketTab', MockMarketTab)
def test_add_market_dialog_accepted(main_window):
    main_window.add_market_dialog = Mock()

    main_window.add_market_dialog.market_catalogue = {
        'event': {'name': 'Test Event'},
        'marketName': 'Test Market'
    }

    main_window.add_market_dialog_accepted_slot()

    assert main_window.tab_widget.count() == 1

    current_tab_index = main_window.tab_widget.currentIndex()
    current_tab_title = main_window.tab_widget.tabText(current_tab_index)

    assert current_tab_title == 'Test Event \n Test Market'


def test_remove_market_slot(main_window):

    main_window.tab_widget.addTab(QTabWidget(), 'Test tab')

    QTest.mouseClick(main_window.remove_market, Qt.MouseButton.LeftButton)

    assert main_window.tab_widget.count() == 0

def test_remove_one_market_slot(main_window):

    first_tab = QWidget()
    main_window.tab_widget.addTab(first_tab, 'First Tab')

    second_tab = QWidget()
    main_window.tab_widget.addTab(second_tab, 'Second Tab')

    assert main_window.tab_widget.count() == 2

    main_window.tab_widget.setCurrentIndex(0)

    QTest.mouseClick(main_window.remove_market, Qt.MouseButton.LeftButton)

    assert main_window.tab_widget.count() == 1
    assert main_window.tab_widget.widget(0) == second_tab

    current_tab_index = main_window.tab_widget.currentIndex()
    current_tab_title = main_window.tab_widget.tabText(current_tab_index)
    assert current_tab_title == 'Second Tab'