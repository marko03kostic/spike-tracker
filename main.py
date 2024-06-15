import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.client import BettingAPIClient

if __name__=='__main__':
    app = MainApplication(sys.argv)
    app.betting_api_client = BettingAPIClient()
    
    app.ssoid = 'cMF7sYZod/3hnYYjFdMLdaxkNAtDdh8OuBpeLsoaIGQ='
    app.app_key = 'WWuV5iOZ92ilM16t'

    main_window = MainWindow()
    main_window.show()

    app.exec()