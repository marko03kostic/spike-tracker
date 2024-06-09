from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout

class TrackerWindow(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
