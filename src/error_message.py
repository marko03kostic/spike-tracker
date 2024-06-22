from PySide6.QtWidgets import QMessageBox

def show_error_message(message: str) -> QMessageBox:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.show()
    return msg