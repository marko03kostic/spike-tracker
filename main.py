import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.client import BettingAPIClient
from src.backend.graphs_api.client import GraphsAPIClient

if __name__=='__main__':
    app = MainApplication(sys.argv)
    app.betting_api_client = BettingAPIClient()
    app._graphs_api_client = GraphsAPIClient()
    
    app.ssoid = '+zumf1NVPeHCI+fK3inuFvMj0ukkx/HtkKQT5ahZt0I='
    app.app_key = 'UyNmNpCtpFF8RELo'

    print(app._graphs_api_client.load_runner_chart('1.226741615', 15294, 0))

    main_window = MainWindow()
    main_window.show()

    app.exec()