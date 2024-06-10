import sys
from src.main_application import MainApplication

from src.main_window import MainWindow
                                                                                                                                                                                                    
if __name__=='__main__':
    app = MainApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()