import sys
from src.main_application import MainApplication

from src.main_window import MainWindow

from src.backend.betting_api.api_client import BettingAPIClient
                                                                                                                                                                                                    
if __name__=='__main__':
    app = MainApplication(sys.argv)

    app.SSOID = '9OJHiR0k6yIgd0FHxNgIPQSBYbdAUJV/7V9wkYkfebU='
    app.app_key = 'WWuV5iOZ92ilM16t'

    bc = BettingAPIClient(app)
    print(bc.headers)
    print('')
    print(bc.list_cleared_orders(bet_status='SETTLED'))

    main_window = MainWindow()
    main_window.show()

    app.exec()