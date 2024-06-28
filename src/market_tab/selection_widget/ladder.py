from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QScrollArea

class BetfairLadderWidget(QWidget):
    def __init__(self, selection_id: int, data=None, parent=None):
        super(BetfairLadderWidget, self).__init__(parent)
        self.selection_id = selection_id

        # Default data if none is provided
        if data is None:
            data = {
                'atb': {},
                'atl': {},
                'trd': {}
            }

        self.data = data
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.scrollArea = QScrollArea()
        self.tableWidget = QTableWidget()
        
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.tableWidget)
        
        self.layout.addWidget(self.scrollArea)
        self.setLayout(self.layout)

        self.populateTable()

    def populateTable(self):
        self.tableWidget.clear()

        # Fill the table
        all_prices = set(self.data['atb'].keys()).union(self.data['atl'].keys()).union(self.data['trd'].keys())
        sorted_prices = sorted(all_prices)

        self.tableWidget.setRowCount(len(sorted_prices))
        self.tableWidget.setColumnCount(4)
        
        self.tableWidget.setHorizontalHeaderLabels(["Price", "ATB", "ATL", "TRD"])

        for row, price in enumerate(sorted_prices):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(self.data['atb'].get(price, ''))))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.data['atl'].get(price, ''))))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(self.data['trd'].get(price, ''))))
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setSortingEnabled(True)

    def updateData(self, new_data):
        self.data = new_data.get(self.selection_id, {'atb': {}, 'atl': {}, 'trd': {}})
        self.populateTable()