import pytest
from PySide6.QtWidgets import QLabel

from src.market_tab.info_widget import InfoWidget

@pytest.fixture
def market_catalogue():
    return {
        'event': {
            'name': 'Sample Event',
            'id': '1'
        },
        'marketName': 'Sample Market',
        'eventType': {
            'name': 'Sample EventType'
        },
        'competition': {
            'name': 'Sample Competition'
        },
        'marketId': '123'
    }

def test_info_widget(qtbot, market_catalogue):
    
    widget = InfoWidget(market_catalogue)
    qtbot.addWidget(widget)

    # Check the widget has the correct labels
    assert widget.top_label.text() == "Market Info"
    assert widget.event_name_label.text() == "Event name: Sample Event"
    assert widget.market_name_label.text() == "Market Name: Sample Market"
    assert widget.event_type_label.text() == "Event Type: Sample EventType"
    assert widget.competition_label.text() == "Competition: Sample Competition"
    assert widget.event_id_label.text() == "Event ID: 1"
    assert widget.market_id_label.text() == "Market ID: 123"

    widget.close()