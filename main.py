import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.client import BettingAPIClient

if __name__=='__main__':

    app = MainApplication(sys.argv)
    app.betting_api_client = BettingAPIClient()
    
    app.ssoid = '2u+6HBu7gp4vse4DclmxqufZcZu6W1OzMnrbNjUKOLE='
    app.app_key = 'UyNmNpCtpFF8RELo'

    main_window = MainWindow()
    main_window.show()

    app.exec()