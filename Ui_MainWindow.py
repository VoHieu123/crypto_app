# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
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
        self.comboBox_accountTo.addItem("")
        self.comboBox_accountTo.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_accountTo)
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_29.addWidget(self.label_10)
        self.comboBox_withdrawCoin = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_withdrawCoin.setObjectName("comboBox_withdrawCoin")
        self.comboBox_withdrawCoin.addItem("")
        self.horizontalLayout_29.addWidget(self.comboBox_withdrawCoin)
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_29.addWidget(self.label_23)
        self.label_withdrawable = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_withdrawable.setObjectName("label_withdrawable")
        self.horizontalLayout_29.addWidget(self.label_withdrawable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_29.addWidget(self.lineEdit)
        self.button_transfer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_transfer.setIconSize(QtCore.QSize(16, 16))
        self.button_transfer.setObjectName("button_transfer")
        self.horizontalLayout_29.addWidget(self.button_transfer)
        self.horizontalLayout_29.setStretch(11, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_29)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
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
        self.comboBox_subAcc.addItem("")
        self.comboBox_subAcc.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_subAcc)
        self.comboBox_coinType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_coinType.setObjectName("comboBox_coinType")
        self.comboBox_coinType.addItem("")
        self.comboBox_coinType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_coinType)
        self.comboBox_alarmType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_alarmType.setObjectName("comboBox_alarmType")
        self.comboBox_alarmType.addItem("")
        self.comboBox_alarmType.addItem("")
        self.comboBox_alarmType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_alarmType)
        self.lineEdit_assetName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_assetName.setObjectName("lineEdit_assetName")
        self.horizontalLayout.addWidget(self.lineEdit_assetName)
        self.lineEdit_threshold = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.horizontalLayout.addWidget(self.lineEdit_threshold)
        self.button_changeThreshold = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_changeThreshold.setObjectName("button_changeThreshold")
        self.horizontalLayout.addWidget(self.button_changeThreshold)
        self.label_infinity = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_infinity.setEnabled(True)
        self.label_infinity.setText("")
        self.label_infinity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_infinity.setObjectName("label_infinity")
        self.horizontalLayout.addWidget(self.label_infinity)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(4, 3)
        self.horizontalLayout.setStretch(5, 3)
        self.horizontalLayout.setStretch(7, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 917, 260))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_10 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.label_BiMC = QtWidgets.QLabel(parent=self.frame_10)
        self.label_BiMC.setText("")
        self.label_BiMC.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_BiMC.setObjectName("label_BiMC")
        self.horizontalLayout_48.addWidget(self.label_BiMC)
        self.gridLayout.addWidget(self.frame_10, 2, 1, 1, 1)
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
        self.frame_5 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_Bi1C = QtWidgets.QLabel(parent=self.frame_15)
        self.label_Bi1C.setText("")
        self.label_Bi1C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi1C.setObjectName("label_Bi1C")
        self.horizontalLayout_6.addWidget(self.label_Bi1C)
        self.gridLayout.addWidget(self.frame_15, 2, 2, 1, 1)
        self.frame_19 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_Bi3U = QtWidgets.QLabel(parent=self.frame_19)
        self.label_Bi3U.setText("")
        self.label_Bi3U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi3U.setObjectName("label_Bi3U")
        self.horizontalLayout_12.addWidget(self.label_Bi3U)
        self.gridLayout.addWidget(self.frame_19, 1, 4, 1, 1)
        self.frame_7 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.gridLayout.addWidget(self.frame_7, 0, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        self.frame_17 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Bi2C = QtWidgets.QLabel(parent=self.frame_17)
        self.label_Bi2C.setText("")
        self.label_Bi2C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi2C.setObjectName("label_Bi2C")
        self.horizontalLayout_10.addWidget(self.label_Bi2C)
        self.gridLayout.addWidget(self.frame_17, 2, 3, 1, 1)
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
        self.frame_18 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_Bi3C = QtWidgets.QLabel(parent=self.frame_18)
        self.label_Bi3C.setText("")
        self.label_Bi3C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi3C.setObjectName("label_Bi3C")
        self.horizontalLayout_11.addWidget(self.label_Bi3C)
        self.gridLayout.addWidget(self.frame_18, 2, 4, 1, 1)
        self.frame_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.gridLayout.addWidget(self.frame_6, 0, 3, 1, 1)
        self.frame_16 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_Bi2U = QtWidgets.QLabel(parent=self.frame_16)
        self.label_Bi2U.setText("")
        self.label_Bi2U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Bi2U.setObjectName("label_Bi2U")
        self.horizontalLayout_14.addWidget(self.label_Bi2U)
        self.gridLayout.addWidget(self.frame_16, 1, 3, 1, 1)
        self.frame_8 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_41.addWidget(self.label_15)
        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 5)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout.setColumnStretch(4, 5)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 4)
        self.gridLayout.setRowStretch(2, 4)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 917, 105))
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
        self.label_31 = QtWidgets.QLabel(parent=self.frame_36)
        self.label_31.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_32.addWidget(self.label_31)
        self.gridLayout_4.addWidget(self.frame_36, 0, 0, 1, 1)
        self.frame_40 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_40.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_By2U = QtWidgets.QLabel(parent=self.frame_40)
        self.label_By2U.setText("")
        self.label_By2U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_By2U.setObjectName("label_By2U")
        self.horizontalLayout_36.addWidget(self.label_By2U)
        self.gridLayout_4.addWidget(self.frame_40, 0, 3, 1, 1)
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
        self.frame_43 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_3)
        self.frame_43.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_By3U = QtWidgets.QLabel(parent=self.frame_43)
        self.label_By3U.setText("")
        self.label_By3U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_By3U.setObjectName("label_By3U")
        self.horizontalLayout_39.addWidget(self.label_By3U)
        self.gridLayout_4.addWidget(self.frame_43, 0, 4, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 5)
        self.gridLayout_4.setColumnStretch(2, 5)
        self.gridLayout_4.setColumnStretch(3, 5)
        self.gridLayout_4.setColumnStretch(4, 5)
        self.horizontalLayout_40.addLayout(self.gridLayout_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 917, 208))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.frame_28 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_Ok2U = QtWidgets.QLabel(parent=self.frame_28)
        self.label_Ok2U.setText("")
        self.label_Ok2U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok2U.setObjectName("label_Ok2U")
        self.horizontalLayout_23.addWidget(self.label_Ok2U)
        self.gridLayout_3.addWidget(self.frame_28, 0, 3, 1, 1)
        self.frame_24 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(parent=self.frame_24)
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)
        self.frame_44 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_44.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_OkMC = QtWidgets.QLabel(parent=self.frame_44)
        self.label_OkMC.setText("")
        self.label_OkMC.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_OkMC.setObjectName("label_OkMC")
        self.horizontalLayout_45.addWidget(self.label_OkMC)
        self.gridLayout_3.addWidget(self.frame_44, 1, 1, 1, 1)
        self.frame_30 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_30.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_Ok3C = QtWidgets.QLabel(parent=self.frame_30)
        self.label_Ok3C.setText("")
        self.label_Ok3C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok3C.setObjectName("label_Ok3C")
        self.horizontalLayout_25.addWidget(self.label_Ok3C)
        self.gridLayout_3.addWidget(self.frame_30, 1, 4, 1, 1)
        self.frame_21 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_21)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.gridLayout_3.addWidget(self.frame_21, 1, 0, 1, 1)
        self.frame_29 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_Ok2C = QtWidgets.QLabel(parent=self.frame_29)
        self.label_Ok2C.setText("")
        self.label_Ok2C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok2C.setObjectName("label_Ok2C")
        self.horizontalLayout_24.addWidget(self.label_Ok2C)
        self.gridLayout_3.addWidget(self.frame_29, 1, 3, 1, 1)
        self.frame_27 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_Ok1C = QtWidgets.QLabel(parent=self.frame_27)
        self.label_Ok1C.setText("")
        self.label_Ok1C.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok1C.setObjectName("label_Ok1C")
        self.horizontalLayout_22.addWidget(self.label_Ok1C)
        self.gridLayout_3.addWidget(self.frame_27, 1, 2, 1, 1)
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
        self.frame_31 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_4)
        self.frame_31.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_Ok3U = QtWidgets.QLabel(parent=self.frame_31)
        self.label_Ok3U.setText("")
        self.label_Ok3U.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Ok3U.setObjectName("label_Ok3U")
        self.horizontalLayout_26.addWidget(self.label_Ok3U)
        self.gridLayout_3.addWidget(self.frame_31, 0, 4, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout_3.setColumnStretch(2, 5)
        self.gridLayout_3.setColumnStretch(3, 5)
        self.gridLayout_3.setColumnStretch(4, 5)
        self.horizontalLayout_27.addLayout(self.gridLayout_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 4)
        self.verticalLayout_3.setStretch(3, 8)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(2, 1)
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
        self.comboBox_accountFrom.setItemText(2, _translate("MainWindow", "Sub2"))
        self.comboBox_accountFrom.setItemText(3, _translate("MainWindow", "Sub3"))
        self.label_4.setText(_translate("MainWindow", "To:"))
        self.comboBox_exchangeTo.setItemText(0, _translate("MainWindow", "Binance"))
        self.comboBox_exchangeTo.setItemText(1, _translate("MainWindow", "Okx"))
        self.comboBox_exchangeTo.setItemText(2, _translate("MainWindow", "Bybit"))
        self.comboBox_accountTo.setItemText(0, _translate("MainWindow", "Main"))
        self.comboBox_accountTo.setItemText(1, _translate("MainWindow", "Sub1"))
        self.comboBox_accountTo.setItemText(2, _translate("MainWindow", "Sub2"))
        self.comboBox_accountTo.setItemText(3, _translate("MainWindow", "Sub3"))
        self.label_10.setText(_translate("MainWindow", "Coin:"))
        self.comboBox_withdrawCoin.setItemText(0, _translate("MainWindow", "USDT"))
        self.label_23.setText(_translate("MainWindow", "Available:"))
        self.label_withdrawable.setText(_translate("MainWindow", "0"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter amount"))
        self.button_transfer.setText(_translate("MainWindow", "Transfer"))
        self.comboBox_market.setItemText(0, _translate("MainWindow", "Binance"))
        self.comboBox_market.setItemText(1, _translate("MainWindow", "Bybit"))
        self.comboBox_market.setItemText(2, _translate("MainWindow", "OKX"))
        self.comboBox_subAcc.setItemText(0, _translate("MainWindow", "Main"))
        self.comboBox_subAcc.setItemText(1, _translate("MainWindow", "Sub1"))
        self.comboBox_subAcc.setItemText(2, _translate("MainWindow", "Sub2"))
        self.comboBox_subAcc.setItemText(3, _translate("MainWindow", "Sub3"))
        self.comboBox_coinType.setItemText(0, _translate("MainWindow", "USDM"))
        self.comboBox_coinType.setItemText(1, _translate("MainWindow", "COINM"))
        self.comboBox_alarmType.setItemText(0, _translate("MainWindow", "Risk"))
        self.comboBox_alarmType.setItemText(1, _translate("MainWindow", "Equity"))
        self.comboBox_alarmType.setItemText(2, _translate("MainWindow", "Position"))
        self.lineEdit_assetName.setPlaceholderText(_translate("MainWindow", "Enter asset name. Default: \"USDT\"."))
        self.lineEdit_threshold.setPlaceholderText(_translate("MainWindow", "Enter alarm range. E.x: (1 - 20)"))
        self.button_changeThreshold.setText(_translate("MainWindow", "Change"))
        self.label_5.setText(_translate("MainWindow", "Coin-M"))
        self.label.setText(_translate("MainWindow", "BIN > BYB > OKX"))
        self.label_2.setText(_translate("MainWindow", "USD-M"))
        self.label_14.setText(_translate("MainWindow", "Sub-account 3"))
        self.label_7.setText(_translate("MainWindow", "Sub-account 1"))
        self.label_9.setText(_translate("MainWindow", "Sub-account 2"))
        self.label_15.setText(_translate("MainWindow", "Main account"))
        self.label_31.setText(_translate("MainWindow", "Unified"))
        self.label_19.setText(_translate("MainWindow", "USD-M"))
        self.label_16.setText(_translate("MainWindow", "Coin-M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
