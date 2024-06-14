from typing import List

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout

class EventsMarketsTree(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.populate_tree()

    def init_ui(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tree_widget = QTreeWidget()
        layout.addWidget(self.tree_widget)

    def populate_tree(self) -> None:
        # Send request to fetch items (replace this with your actual request)
        items = self.fetch_items()

        # Populate the tree widget with received items
        self.populate_tree_widget(items)

    def fetch_items(self) -> List[str]:
        # Dummy implementation of fetching items (replace this with your actual request logic)
        return ['Item 1', 'Item 2', 'Item 3']

    def populate_tree_widget(self, items: List[str]) -> None:
        self.tree_widget.clear()
        for item in items:
            tree_item = QTreeWidgetItem([item])
            self.tree_widget.addTopLevelItem(tree_item)