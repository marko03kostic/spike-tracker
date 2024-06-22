from pytestqt.qtbot import QtBot
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from PySide6.QtTest import QTest

from src.error_message import show_error_message

def test_show_error_message(qtbot: QtBot):
    test_message = "This is a test error message."
    
    msg_box = show_error_message(test_message)
    
    assert msg_box.windowTitle() == "Error"
    assert msg_box.text() == "Error"
    assert msg_box.informativeText() == test_message
    assert msg_box.icon() == QMessageBox.Critical

    ok_button = msg_box.button(QMessageBox.Ok)
    QTest.mouseClick(ok_button, Qt.MouseButton.LeftButton)
