# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 684)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_29.addWidget(self.label_3)
        self.comboBox_exchangeFrom = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_exchangeFrom.setObjectName("comboBox_exchangeFrom")
        self.comboBox_exchangeFrom.addItem("")
        self.comboBox_exchangeFrom.addItem("")
        self.comboBox_exchangeFrom.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_exchangeFrom)
        self.comboBox_accountFrom = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_accountFrom.setObjectName("comboBox_accountFrom")
        self.comboBox_accountFrom.addItem("")
        self.comboBox_accountFrom.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_accountFrom)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_29.addWidget(self.label_4)
        self.comboBox_exchangeTo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_exchangeTo.setObjectName("comboBox_exchangeTo")
        self.comboBox_exchangeTo.addItem("")
        self.comboBox_exchangeTo.addItem("")
        self.comboBox_exchangeTo.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_exchangeTo)
        self.comboBox_accountTo = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_accountTo.setObjectName("comboBox_accountTo")
        self.comboBox_accountTo.addItem("")
        self.comboBox_accountTo.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_accountTo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_29.addWidget(self.lineEdit)
        self.button_transfer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_transfer.setIconSize(QtCore.QSize(16, 16))
        self.button_transfer.setObjectName("button_transfer")
        self.horizontalLayout_29.addWidget(self.button_transfer)
        self.horizontalLayout_29.setStretch(7, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_29)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_export = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_export.setObjectName("button_export")
        self.horizontalLayout_5.addWidget(self.button_export)
        self.label_totalValue = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_totalValue.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_totalValue.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_totalValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_totalValue.setObjectName("label_totalValue")
        self.horizontalLayout_5.addWidget(self.label_totalValue)
        self.label_infinity = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_infinity.setEnabled(True)
        self.label_infinity.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_infinity.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_infinity.setLineWidth(1)
        self.label_infinity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_infinity.setObjectName("label_infinity")
        self.horizontalLayout_5.addWidget(self.label_infinity)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_market = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_market.setObjectName("comboBox_market")
        self.comboBox_market.addItem("")
        self.comboBox_market.addItem("")
        self.comboBox_market.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_market)
        self.comboBox_subAcc = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_subAcc.setObjectName("comboBox_subAcc")
        self.comboBox_subAcc.addItem("")
        self.comboBox_subAcc.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_subAcc)
        self.comboBox_alarmType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_alarmType.setObjectName("comboBox_alarmType")
        self.comboBox_alarmType.addItem("")
        self.comboBox_alarmType.addItem("")
        self.comboBox_alarmType.addItem("")
        self.comboBox_alarmType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_alarmType)
        self.lineEdit_lowerThreshold = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_lowerThreshold.setObjectName("lineEdit_lowerThreshold")
        self.horizontalLayout.addWidget(self.lineEdit_lowerThreshold)
        self.lineEdit_upperThreshold = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_upperThreshold.setObjectName("lineEdit_upperThreshold")
        self.horizontalLayout.addWidget(self.lineEdit_upperThreshold)
        self.button_changeThreshold = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_changeThreshold.setObjectName("button_changeThreshold")
        self.horizontalLayout.addWidget(self.button_changeThreshold)
        self.button_positionsPnL = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_positionsPnL.setObjectName("button_positionsPnL")
        self.horizontalLayout.addWidget(self.button_positionsPnL)
        self.horizontalLayout.setStretch(3, 3)
        self.horizontalLayout.setStretch(4, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 917, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_mainAccount = QtWidgets.QLabel(parent=self.frame_8)
        self.label_mainAccount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mainAccount.setObjectName("label_mainAccount")
        self.horizontalLayout_41.addWidget(self.label_mainAccount)
        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)
        self.frame_9 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.label_BiMU = QtWidgets.QLabel(parent=self.frame_9)
        self.label_BiMU.setText("")
        self.label_BiMU.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_BiMU.setObjectName("label_BiMU")
        self.horizontalLayout_49.addWidget(self.label_BiMU)
        self.gridLayout.addWidget(self.frame_9, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_binance = QtWidgets.QLabel(parent=self.frame_3)
        self.label_binance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_binance.setObjectName("label_binance")
        self.horizontalLayout_4.addWidget(self.label_binance)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_subAccount1 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_subAccount1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_subAccount1.setObjectName("label_subAccount1")
        self.horizontalLayout_9.addWidget(self.label_subAccount1)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_Bi1U = QtWidgets.QLabel(parent=self.frame_4)
        self.label_Bi1U.setText("")
        self.label_Bi1U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi1U.setObjectName("label_Bi1U")
        self.horizontalLayout_7.addWidget(self.label_Bi1U)
        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 917, 164))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_13 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_ByMU = QtWidgets.QLabel(parent=self.frame_13)
        self.label_ByMU.setText("")
        self.label_ByMU.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_ByMU.setObjectName("label_ByMU")
        self.horizontalLayout_43.addWidget(self.label_ByMU)
        self.gridLayout_4.addWidget(self.frame_13, 0, 1, 1, 1)
        self.frame_36 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_36.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_bybit = QtWidgets.QLabel(parent=self.frame_36)
        self.label_bybit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bybit.setObjectName("label_bybit")
        self.horizontalLayout_32.addWidget(self.label_bybit)
        self.gridLayout_4.addWidget(self.frame_36, 0, 0, 1, 1)
        self.frame_32 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_32.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_By1U = QtWidgets.QLabel(parent=self.frame_32)
        self.label_By1U.setText("")
        self.label_By1U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_By1U.setObjectName("label_By1U")
        self.horizontalLayout_28.addWidget(self.label_By1U)
        self.gridLayout_4.addWidget(self.frame_32, 0, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setColumnStretch(2, 4)
        self.horizontalLayout_40.addLayout(self.gridLayout_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 917, 164))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_45 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_45.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_45)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_OkMU = QtWidgets.QLabel(parent=self.frame_45)
        self.label_OkMU.setText("")
        self.label_OkMU.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_OkMU.setObjectName("label_OkMU")
        self.horizontalLayout_46.addWidget(self.label_OkMU)
        self.gridLayout_3.addWidget(self.frame_45, 0, 1, 1, 1)
        self.frame_20 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_Ok1U = QtWidgets.QLabel(parent=self.frame_20)
        self.label_Ok1U.setText("")
        self.label_Ok1U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok1U.setObjectName("label_Ok1U")
        self.horizontalLayout_15.addWidget(self.label_Ok1U)
        self.gridLayout_3.addWidget(self.frame_20, 0, 2, 1, 1)
        self.frame_24 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_okx = QtWidgets.QLabel(parent=self.frame_24)
        self.label_okx.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_okx.setObjectName("label_okx")
        self.horizontalLayout_19.addWidget(self.label_okx)
        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(2, 4)
        self.horizontalLayout_27.addLayout(self.gridLayout_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 3)
        self.verticalLayout_3.setStretch(3, 3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crypto Alarm"))
        self.label_3.setText(_translate("MainWindow", "From:"))
        self.comboBox_exchangeFrom.setItemText(0, _translate("MainWindow", "Binance"))
        self.comboBox_exchangeFrom.setItemText(1, _translate("MainWindow", "Okx"))
        self.comboBox_exchangeFrom.setItemText(2, _translate("MainWindow", "Bybit"))
        self.comboBox_accountFrom.setItemText(0, _translate("MainWindow", "Main"))
        self.comboBox_accountFrom.setItemText(1, _translate("MainWindow", "Sub1"))
        self.label_4.setText(_translate("MainWindow", "To:"))
        self.comboBox_exchangeTo.setItemText(0, _translate("MainWindow", "Binance"))
        self.comboBox_exchangeTo.setItemText(1, _translate("MainWindow", "Okx"))
        self.comboBox_exchangeTo.setItemText(2, _translate("MainWindow", "Bybit"))
        self.comboBox_accountTo.setItemText(0, _translate("MainWindow", "Main"))
        self.comboBox_accountTo.setItemText(1, _translate("MainWindow", "Sub1"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter amount"))
        self.button_transfer.setText(_translate("MainWindow", "Transfer"))
        self.button_export.setText(_translate("MainWindow", "Export"))
        self.label_totalValue.setText(_translate("MainWindow", "Total"))
        self.label_infinity.setText(_translate("MainWindow", "Update"))
        self.comboBox_market.setItemText(0, _translate("MainWindow", "Binance"))
        self.comboBox_market.setItemText(1, _translate("MainWindow", "Bybit"))
        self.comboBox_market.setItemText(2, _translate("MainWindow", "OKX"))
        self.comboBox_subAcc.setItemText(0, _translate("MainWindow", "Main"))
        self.comboBox_subAcc.setItemText(1, _translate("MainWindow", "Sub1"))
        self.comboBox_alarmType.setItemText(0, _translate("MainWindow", "Risk"))
        self.comboBox_alarmType.setItemText(1, _translate("MainWindow", "Asset"))
        self.comboBox_alarmType.setItemText(2, _translate("MainWindow", "Position"))
        self.comboBox_alarmType.setItemText(3, _translate("MainWindow", "Size"))
        self.lineEdit_lowerThreshold.setPlaceholderText(_translate("MainWindow", "Enter alarm lower bound"))
        self.lineEdit_upperThreshold.setPlaceholderText(_translate("MainWindow", "Enter alarm upper bound"))
        self.button_changeThreshold.setText(_translate("MainWindow", "Change"))
        self.button_positionsPnL.setText(_translate("MainWindow", "PnLs"))
        self.label_mainAccount.setText(_translate("MainWindow", "Main account"))
        self.label_binance.setText(_translate("MainWindow", "Binance"))
        self.label_subAccount1.setText(_translate("MainWindow", "Sub-account 1"))
        self.label_bybit.setText(_translate("MainWindow", "Bybit"))
        self.label_okx.setText(_translate("MainWindow", "OKX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())