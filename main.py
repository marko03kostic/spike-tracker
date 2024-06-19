import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.client import BettingAPIClient
from src.backend.graphs_api.client import GraphsAPIClient

if __name__=='__main__':
    app = MainApplication(sys.argv)
    app.betting_api_client = BettingAPIClient()
    app.graphs_api_client = GraphsAPIClient()
    
    app.ssoid = 'EqJKQvwYcbOuVFyQW/M7uJOX3hdxg99ExZZN5c++0Vg='
    app.app_key = 'UyNmNpCtpFF8RELo'

    main_window = MainWindow()
    main_window.show()

    app.exec()