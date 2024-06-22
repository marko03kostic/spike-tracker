import sys
import pytest
from unittest import mock
from src.main_application import MainApplication

def test_singleton_init(qapp):
    assert MainApplication.instance()

def test_singleton_double_init(qapp):
    with pytest.raises(RuntimeError):
        MainApplication(sys.argv)

def test_ssoid_setter_and_getter(qapp):
    qapp.ssoid = '1234'
    assert qapp._ssoid == '1234'
    assert qapp.ssoid == '1234'

def test_qapp_key_setter_and_getter(qapp):
    qapp.app_key = '1234'
    assert qapp._app_key == '1234'
    assert qapp.app_key == '1234'

def test_betting_api_client_setter_and_getter(qapp):
    qapp.betting_api_client = '1234'
    assert qapp._betting_api_client == '1234'
    assert qapp.betting_api_client == '1234'

