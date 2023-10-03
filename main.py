import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import Ui_MainWindow
import Controller
import threading
import Model
import const
import binance_funcs
import okx_funcs

exitFlag = False

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        global exitFlag
        exitFlag = True


def backgroundTask(controller):
    while not exitFlag:
        controller.loop()

def main():
    choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    while True:
        if choice == 1:
            chosenBinAPIKey = const.TA_BIN_API_KEY
            chosenBinSecretKey = const.TA_BIN_SECRET_KEY
            chosenOKXAPIKey = const.TA_OKX_API_KEY
            chosenOKXSecretKey = const.TA_OKX_SECRET_KEY
            chosenPassword = const.TA_OKX_PASSPHRASE
            break
        elif choice == 2:
            chosenBinAPIKey = const.ST_BIN_API_KEY
            chosenBinSecretKey = const.ST_BIN_SECRET_KEY
            chosenOKXAPIKey = const.ST_OKX_API_KEY
            chosenOKXSecretKey = const.ST_OKX_SECRET_KEY
            chosenPassword = const.ST_OKX_PASSPHRASE
            break
        else:
            choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    BinanceHandler = binance_funcs.BinanceHandler(apiKey=chosenBinAPIKey, secretKey=chosenBinSecretKey)
    OKXHandler = okx_funcs.OKXHandler(chosenOKXAPIKey, secretKey=chosenOKXSecretKey, password=chosenPassword)
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    model = Model.Model()
    controller = Controller.Controller(ui, model, BinanceHandler=BinanceHandler, OKXHandler=OKXHandler)
    backgroudThread = threading.Thread(target=backgroundTask, args=(controller, ))
    backgroudThread.start()
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
