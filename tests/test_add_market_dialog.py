import pytest
from unittest import mock
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QDialog
from src.main_application import MainApplication
from src.backend.betting_api.enums import MarketStatus, MarketProjection

from src.add_market_dialog.add_market_by_id_dialog.dialog import AddMarketDialog

@pytest.fixture
def dialog(qtbot):
    dialog = AddMarketDialog()

    with mock.patch.object(MainApplication, 'betting_api_client'):
        yield dialog 
    dialog.close()

@pytest.fixture
def mock_show_error_message():
    mock_show_error_message = mock.Mock()

    with mock.patch('src.add_market_dialog.add_market_by_id_dialog.dialog.show_error_message', mock_show_error_message):
        yield mock_show_error_message
    
    mock_show_error_message.reset_mock()

def test_is_market_id_valid_open(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = [{'marketId': '1.1234567', 'status': MarketStatus.OPEN.value}]
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is True
    assert dialog.market_id == '1.1234567'
    assert not mock_show_error_message.called

def test_is_market_id_valid_inactive(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = [{'marketId': '1.1234567', 'status': MarketStatus.INACTIVE.value}]
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is False
    mock_show_error_message.assert_called_once_with("Market is inactive")

def test_is_market_id_valid_suspended(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = [{'marketId': '1.1234567', 'status': MarketStatus.SUSPENDED.value}]
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is False
    mock_show_error_message.assert_called_once_with("Market is suspended")

def test_is_market_id_valid_closed(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = [{'marketId': '1.1234567', 'status': MarketStatus.CLOSED.value}]
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is False
    mock_show_error_message.assert_called_once_with("Market is closed")

def test_is_market_id_valid_not_found_empty_list(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = []
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is False
    mock_show_error_message.assert_called_once_with("Market not found")

def test_is_market_id_valid_not_found_not_matched_id(dialog, mock_show_error_message):
    dialog._main_app.betting_api_client.list_market_book.return_value = [{'marketId': '1.7654321', 'status': MarketStatus.OPEN.value}]
    
    result = dialog.is_market_id_valid('1.1234567')
    
    assert result is False
    mock_show_error_message.assert_called_once_with("Market not found")

def test_dialog_setup(dialog):
    assert isinstance(dialog, QDialog)
    assert dialog.windowTitle() == "Add Market by Id"
    assert dialog.minimumSize() == QSize(300, 200)

def test_is_input_correct_format_correct_format(dialog):
    dialog.input_field.setText("1.1234567")
    assert dialog.is_input_correct_format(dialog.input_field.text()) == True

def test_is_input_correct_format_incorrect_format(dialog):
    dialog.input_field.setText("abc")
    assert dialog.is_input_correct_format(dialog.input_field.text()) == False

def test_set_valid_market_catalogue_success(dialog):
    dialog._main_app.betting_api_client.list_market_catalogue.return_value = [{'marketId': '1.1234567'}]

    dialog.market_id = '1.1234567'

    result = dialog.set_valid_market_catalogue()

    assert result is True
    assert dialog.market_catalogue == {'marketId': '1.1234567'}
    dialog._main_app.betting_api_client.list_market_catalogue.assert_called_once_with(
        market_ids=['1.1234567'],
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

def test_set_valid_market_catalogue_no_market_catalogues(dialog):
    dialog._main_app.betting_api_client.list_market_catalogue.return_value = []

    dialog.market_id = '1.1234567'

    result = dialog.set_valid_market_catalogue()

    assert result is False
    assert dialog.market_catalogue is None
    dialog._main_app.betting_api_client.list_market_catalogue.assert_called_once_with(
        market_ids=['1.1234567'],
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

def test_set_valid_market_catalogue_market_id_not_matched(dialog):
    dialog._main_app.betting_api_client.list_market_catalogue.return_value = [{'marketId': '2.1234567'}]

    dialog.market_id = '1.1234567'

    result = dialog.set_valid_market_catalogue()

    assert result is False
    assert dialog.market_catalogue is None
    dialog._main_app.betting_api_client.list_market_catalogue.assert_called_once_with(
        market_ids=['1.1234567'],
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

def test_is_input_valid_correct_format_valid_market_id(dialog):
    dialog.is_input_correct_format = mock.Mock(return_value=True)
    
    dialog.is_market_id_valid = mock.Mock(return_value=True)

    dialog.input_field.setText("1.1234567")

    result = dialog.is_input_valid()

    assert result is True
    dialog.is_input_correct_format.assert_called_once_with("1.1234567")
    dialog.is_market_id_valid.assert_called_once_with("1.1234567")

def test_is_input_valid_correct_format_invalid_market_id(dialog):
    dialog.is_input_correct_format = mock.Mock(return_value=True)
    
    dialog.is_market_id_valid = mock.Mock(return_value=False)

    dialog.input_field.setText("1.1234567")

    result = dialog.is_input_valid()

    assert result is False
    dialog.is_input_correct_format.assert_called_once_with("1.1234567")
    dialog.is_market_id_valid.assert_called_once_with("1.1234567")

def test_is_input_valid_incorrect_format(dialog):

    dialog.is_input_correct_format = mock.Mock(return_value=False)

    dialog.input_field.setText("abc")

    result = dialog.is_input_valid()

    assert result is False
    dialog.is_input_correct_format.assert_called_once_with("abc")

def test_add_clicked_valid_input_valid_market_catalogue(dialog, mock_show_error_message):
    dialog.is_input_valid = mock.Mock(return_value=True)
    
    dialog.set_valid_market_catalogue = mock.Mock(return_value=True)

    dialog.accept = mock.Mock()

    dialog.add_clicked()

    dialog.is_input_valid.assert_called_once()
    dialog.set_valid_market_catalogue.assert_called_once()
    dialog.accept.assert_called_once()
    assert not mock_show_error_message.called

def test_add_clicked_valid_input_invalid_market_catalogue(dialog, mock_show_error_message):

    dialog.is_input_valid = mock.Mock(return_value=True)

    dialog.set_valid_market_catalogue = mock.Mock(return_value=False)

    dialog.accept = mock.Mock()

    dialog.add_clicked()

    dialog.is_input_valid.assert_called_once()
    dialog.set_valid_market_catalogue.assert_called_once()
    assert not dialog.accept.called
    mock_show_error_message.assert_called_once_with('An unexpected error occurred')

def test_add_clicked_invalid_input(dialog, mock_show_error_message):
    dialog.is_input_valid = mock.Mock(return_value=False)

    dialog.set_valid_market_catalogue = mock.Mock()

    dialog.accept = mock.Mock()

    dialog.add_clicked()

    dialog.is_input_valid.assert_called_once()
    assert not dialog.set_valid_market_catalogue.called
    assert not dialog.accept.called
    assert not mock_show_error_message.called

def test_market_catalogue_setter_and_getter(dialog):
    dialog.market_catalogue = '1234'
    assert dialog._market_catalogue == '1234'
    assert dialog.market_catalogue == '1234'

def test_market_id_setter_and_getter(dialog):
    dialog.market_id = '1234'
    assert dialog._market_id == '1234'
    assert dialog.market_id == '1234'