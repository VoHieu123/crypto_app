import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import Ui_MainWindow
import Controller
import threading
import Model
import const
import binance_handler, bybit_handler, okx_handler
from utils import Communication
import alarm

class MyWindow(QMainWindow):
    def __init__(self, communication: Communication):
        super().__init__()
        self.communication_ = communication
        self.communication_.ui_signal.connect(self.update_ui)
        self.controller_ = None
        self.exit_flag = False

    def set_up(self, controller):
        self.controller_ = controller

    def update_ui(self):
        if self.controller_ is not None:
            self.controller_.ui_update()

    def closeEvent(self, event):
        self.exit_flag = True

def data_task(controller, window: MyWindow):
    while not window.exit_flag:
        try:
            controller.data_loop()
        except Exception as e:
            # print(f"Error: {e}")
            alarm.activate(message=f"Program runs again because of error: {e}", to=["Hieu"])

def main():
    choice = int(input("Type: 1 - Tuan Anh, 2 - Steve: "))

    while True:
        if choice == 1:
            identity = "TA"
            chosenBinAPIKey = const.TA_BIN_API_KEY
            chosenBinSecretKey = const.TA_BIN_SECRET_KEY
            chosenOKXAPIKey = const.TA_OKX_API_KEY
            chosenOKXSecretKey = const.TA_OKX_SECRET_KEY
            chosenPassword = const.TA_OKX_PASSPHRASE
            chosenBybAPIKey = const.TA_BYB_API_KEY
            chosenBybSecretKey = const.TA_BYB_SECRET_KEY
            break
        elif choice == 2:
            identity = "ST"
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

    model = Model.Model(identity)
    BybitHandler = bybit_handler.BybitHandler(model=model, apiKey=chosenBybAPIKey, secretKey=chosenBybSecretKey)
    BinanceHandler = binance_handler.BinanceHandler(model=model, apiKey=chosenBinAPIKey, secretKey=chosenBinSecretKey)
    OKXHandler = okx_handler.OKXHandler(model=model, apiKey=chosenOKXAPIKey, secretKey=chosenOKXSecretKey, password=chosenPassword)
    app = QApplication(sys.argv)
    communication = Communication()
    MainWindow = MyWindow(communication)
    ui = Ui_MainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    controller = Controller.Controller(identity, ui, model, communication, binanceHandler=BinanceHandler,
                                       okxHandler=OKXHandler, bybitHandler=BybitHandler)
    MainWindow.set_up(controller=controller)
    MainWindow.setWindowTitle("Steve" if choice == 2 else "Tuan Anh")

    MainWindow.show()
    data_thread = threading.Thread(target=data_task, args=(controller, MainWindow))
    data_thread.start()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
