import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.client import BettingAPIClient
from src.backend.exchange_stream_api.stream import ExchangeStream

if __name__=='__main__':

    app = MainApplication(sys.argv)    
    
    app.ssoid = 'SD4M3RXML4T/4aekVPsqeh9wmz2qJyfBKNNDxg25Wns='
    app.app_key = 'UyNmNpCtpFF8RELo'
    
    app.betting_api_client = BettingAPIClient()
    app.exchange_stream = ExchangeStream()

    main_window = MainWindow()
    main_window.show()

    app.exec()