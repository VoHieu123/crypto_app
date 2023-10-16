import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import Ui_MainWindow
import Controller
import threading
import Model
import const
import binance_handler,bybit_handler, okx_handler

exitFlag = False

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        global exitFlag
        exitFlag = True


def backgroundTask(controller, app):
    try:
        while not exitFlag:
            controller.loop()
    except SystemExit as e:
        app.exit()
    except Exception as e:
        pass

def main():
    choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    while True:
        if choice == 1:
            chosenBinAPIKey = const.TA_BIN_API_KEY
            chosenBinSecretKey = const.TA_BIN_SECRET_KEY
            chosenOKXAPIKey = const.TA_OKX_API_KEY
            chosenOKXSecretKey = const.TA_OKX_SECRET_KEY
            chosenPassword = const.TA_OKX_PASSPHRASE
            chosenBybAPIKey = const.TA_BYB_API_KEY
            chosenBybSecretKey = const.TA_BYB_SECRET_KEY
            break
        elif choice == 2:
            chosenBinAPIKey = const.ST_BIN_API_KEY
            chosenBinSecretKey = const.ST_BIN_SECRET_KEY
            chosenOKXAPIKey = const.ST_OKX_API_KEY
            chosenOKXSecretKey = const.ST_OKX_SECRET_KEY
            chosenPassword = const.ST_OKX_PASSPHRASE
            chosenBybAPIKey = const.ST_BYB_API_KEY
            chosenBybSecretKey = const.ST_BYB_SECRET_KEY
            break
        else:
            choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    BybitHandler = bybit_handler.BybitHandler(apiKey=chosenBybAPIKey, secretKey=chosenBybSecretKey)
    BinanceHandler = binance_handler.BinanceHandler(apiKey=chosenBinAPIKey, secretKey=chosenBinSecretKey)
    OKXHandler = okx_handler.OKXHandler(apiKey=chosenOKXAPIKey, secretKey=chosenOKXSecretKey, password=chosenPassword)
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    model = Model.Model()
    controller = Controller.Controller(ui, model, binanceHandler=BinanceHandler, okxHandler=OKXHandler, bybitHandler=BybitHandler)
    backgroudThread = threading.Thread(target=backgroundTask, args=(controller, app))
    backgroudThread.start()
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
