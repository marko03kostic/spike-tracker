# conftest.py
import pytest
from src.main_application import MainApplication

@pytest.fixture(scope="session")
def qapp_cls():
    return MainApplication
