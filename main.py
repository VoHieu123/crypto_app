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

app = QApplication(sys.argv)
MainWindow = MyWindow()
ui = Ui_MainWindow.Ui_MainWindow()
ui.setupUi(MainWindow)
model = Model.Model()
controller = Controller.Controller(ui, model)

def backgroundTask():
    while not exitFlag:
        controller.loop()

def main():
    choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))
    while(choice != 1 and choice != 2):
        if choice == 1:
            binance_funcs.init(apiKey=const.TA_BIN_API_KEY, secretKey=const.TA_BIN_SECRET_KEY)
            okx_funcs.init(apiKey=const.TA_OKX_API_KEY, secretKey=const.TA_OKX_SECRET_KEY, password=const.TA_OKX_PASSPHRASE)
        elif choice == 2:
            binance_funcs.init(apiKey=const.ST_BIN_API_KEY, secretKey=const.ST_BIN_SECRET_KEY)
            okx_funcs.init(apiKey=const.ST_OKX_API_KEY, secretKey=const.ST_OKX_SECRET_KEY, password=const.ST_OKX_PASSPHRASE)
        else:
            choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    backgroudThread = threading.Thread(target=backgroundTask)
    backgroudThread.start()
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
