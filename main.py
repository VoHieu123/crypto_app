import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import Ui_MainWindow
import Controller
import threading
import Model

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
    backgroudThread = threading.Thread(target=backgroundTask)
    backgroudThread.start()
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
