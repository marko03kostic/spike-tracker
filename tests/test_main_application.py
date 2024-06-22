import sys
import pytest

from src.main_application import MainApplication

def test_singleton_init():
    app = MainApplication(sys.argv)
    assert MainApplication.instance()
    app.shutdown()

def test_singleton_double_init():
    app = MainApplication(sys.argv)
    with pytest.raises(RuntimeError):
        MainApplication(sys.argv)
    app.shutdown()

def test_ssoid_setter_and_getter():
    app = MainApplication(sys.argv)
    app.ssoid = '1234'
    assert app._ssoid == '1234'
    assert app.ssoid == '1234'
    app.shutdown()

def test_app_key_setter_and_getter():
    app = MainApplication(sys.argv)
    app.app_key = '1234'
    assert app._app_key == '1234'
    assert app.app_key == '1234'
    app.shutdown()

def test_betting_api_client_setter_and_getter():
    app = MainApplication(sys.argv)
    app.betting_api_client = '1234'
    assert app._betting_api_client == '1234'
    assert app.betting_api_client == '1234'
    app.shutdown()