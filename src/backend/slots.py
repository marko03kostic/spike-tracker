from PySide6.QtCore import Slot
from src.gui.tracker_window import TrackerWindow

@Slot()
def add_market_slot(main_window) -> None:
    main_window.tab_widget.addTab(TrackerWindow(), "Market")

@Slot()
def remove_market_slot(main_window) -> None:
    current_index = main_window.tab_widget.currentIndex()
    if current_index != -1:  # Make sure there is a tab to remove
        main_window.tab_widget.removeTab(current_index)
