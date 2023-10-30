from utils import auto_format as fmt
from utils import substring_after, substring_before, change_last_letter
from utils import Range
import time, alarm
from utils import Communication
from PyQt6.QtGui import QFont
import datetime

class Controller():
    def __init__ (self, identity, uiMainWindow, model, communication: Communication, binanceHandler, okxHandler, bybitHandler):
        self.labelDict = {}
        self.save_frequency_m = 10*60
        self.update_time = 0
        self.alarm_error_duration = 60*20
        self.retrieve_frequency = 30
        self.current_time = 0
        self.identity_ = identity
        self.communication_ = communication
        self.BinanceHandler_ = binanceHandler
        self.BybitHandler_ = bybitHandler
        self.OKXHandler_ = okxHandler
        self.uiMainWindow_ = uiMainWindow
        self.model_ = model
        self.uiMainWindow_.button_changeThreshold.clicked.connect(self.change_threshold_button_clicked)
        self.uiMainWindow_.button_transfer.clicked.connect(self.transfer_button_clicked)
        self.uiMainWindow_.button_export.clicked.connect(self.export_button_clicked)

        markets = ["Bi", "Ok", "By"]
        subaccounts = ["M", "1", "2", "3"]
        coinTypes = ["U", "C"]

        self.labelDict = {}

        font = QFont()
        font.setPointSize(16)

        for market in markets:
            for subaccount in subaccounts:
                for coin_type in coinTypes:
                    label_key = f"{market}{subaccount}{coin_type}"
                    label_name = f"label_{market}{subaccount}{coin_type}"
                    try:
                        ui_label = getattr(self.uiMainWindow_, label_name)
                        ui_label.setFont(font)
                        self.labelDict[label_key] = ui_label
                    except Exception as e:
                        # print(e)
                        pass

        self.uiMainWindow_.label_infinity.setStyleSheet("QLabel { border: 1px solid black;}")
        self.uiMainWindow_.label_totalValue.setStyleSheet("QLabel { border: 1px solid black;}")

    # Todo: Update data everytime the combo boxes are clicked
    def transfer_button_clicked(self):
        # Todo: What if error happens here?
        self.update_data()
        self.upload_withdrawable()
        try:
            withdrawAmount = float(self.uiMainWindow_.lineEdit_withdrawAmount.text())
        except:
            return
        moduleDict = {"Binance": self.BinanceHandler_,
                      "Bybit": self.BybitHandler_,
                      "Okx": self.OKXHandler_}
        exchangeFrom = self.uiMainWindow_.comboBox_exchangeFrom.currentText()
        accountFrom = self.uiMainWindow_.comboBox_accountFrom.currentText()
        exchangeTo = self.uiMainWindow_.comboBox_exchangeTo.currentText()
        accountTo = self.uiMainWindow_.comboBox_accountTo.currentText()
        coin = self.uiMainWindow_.comboBox_withdrawCoin.currentText()

        # Todo: Check if the withdrawal amount is enough
        # Then move to money to funding wallet
        # The money maybe less than the requested amount
        # If so => confirm from user
        # Execute the move,
        # constantly fetch data from server/subcribe to a socket to check withdrawal progress
        # Binance: cannot be cancelled, Bybit and Okx: can be cancelled
        # For auto-pilot situation, no confirmation and UI needed

        # Internal transfer: Only prompt a simple message
        if exchangeFrom == exchangeTo:
            moduleDict[exchangeFrom].transfer_money_internal()
        else:
            pass

    def export_button_clicked(self):
        self.model_.export_data()

    def change_threshold_button_clicked(self):
        alarm = self.uiMainWindow_.lineEdit_threshold.text().replace(" ", "")
        asset = self.uiMainWindow_.lineEdit_assetName.text().upper()
        if asset == "":
            asset = "USDT"
        self.uiMainWindow_.lineEdit_threshold.setText("")
        self.uiMainWindow_.lineEdit_assetName.setText("")
        try:
            alarm = Range(float(substring_before(alarm, "-")), float(substring_after(alarm, "-")))
        except:
            return
        market = self.uiMainWindow_.comboBox_market.currentText()
        coin_type = self.uiMainWindow_.comboBox_coinType.currentText()
        alarm_type = self.uiMainWindow_.comboBox_alarmType.currentText()
        sub_acc = self.uiMainWindow_.comboBox_subAcc.currentText()

        symbol_mappings = {
            "Binance": "Bi",
            "OKX": "Ok",
            "Bybit": "By",
            "Main": "M",
            "Sub1": "1",
            "Sub2": "2",
            "Sub3": "3",
            "USDM": "U",
            "COINM": "C"
        }

        symbol = "".join(symbol_mappings.get(item, "") for item in [market, sub_acc, coin_type])

        if "By" in symbol:
            symbol = change_last_letter(symbol, "U")

        if alarm_type == "Risk":
            self.model_.set_data(symbol=symbol, asset_name=asset, risk_alarm=alarm)
        elif alarm_type == "Equity":
            self.model_.set_data(symbol=symbol, asset_name=asset, equity_alarm=alarm)
        elif alarm_type == "Position":
            self.model_.set_data(symbol=symbol, asset_name=asset, position_alarm=alarm)
        self.upload_risk()

    def update_data(self):
        # Define a list or dictionary of handlers
        handlers = {
            "Binance": self.BinanceHandler_,
            "OKX": self.OKXHandler_,
            "Bybit": self.BybitHandler_
        }

        self.model_.set_universal_mark_prices(self.BinanceHandler_.get_universal_mark_prices())

        # Iterate through the handlers and set data in the model
        for handler in handlers.values():
            risk_data = handler.get_account_status()
            for key, value in risk_data.items():
                symbol = substring_before(key, "_")
                asset_name = substring_after(key, "_")
                risk, equity, withdrawable = value.get("risk"), value.get("equity"), value.get("withdrawable")
                long_pos, short_pos = value.get("long_pos"), value.get("short_pos")
                initial, maintenance = value.get("initial"), value.get("maintenance")
                self.model_.set_data(symbol=symbol, asset_name=asset_name,
                                     risk=risk, equity=equity, withdrawable=withdrawable,
                                     long_pos=long_pos, short_pos=short_pos, initial=initial, maintenance=maintenance)

        self.update_time = time.time()

    def upload_withdrawable(self):
        marketFrom = self.uiMainWindow_.comboBox_exchangeFrom.currentText()
        accountFrom = self.uiMainWindow_.comboBox_accountFrom.currentText()
        targetSymbol = f"{marketFrom[:2]}{'M' if accountFrom == 'Main' else accountFrom[-1:]}U"

        for dict in self.model_.get_data(symbol=targetSymbol):
            if dict["name"] == "USDT":
                self.uiMainWindow_.label_withdrawable.setText(f"{round(dict.get('withdrawable'), 1)}")
                return

        self.uiMainWindow_.label_withdrawable.setText("0")

    def upload_risk(self):
        def handle_frontend_data(list):
            total_value = 0
            def calculate_position_risk(long_pos, short_pos):
                    if long_pos == 0 or short_pos == 0:
                        return 0
                    a = long_pos/(long_pos+abs(short_pos))
                    b = abs(short_pos)/(long_pos+abs(short_pos))
                    return abs(a-b)

            returnStr = ""
            for dict in list:
                if dict["name"] == "USDT":
                    total_value += dict["equity"]
                    position_background_color = None
                    risk_background_color = None
                    equity_background_color = None

                    position = calculate_position_risk(dict["long_pos"], dict["short_pos"])

                    if dict["risk"] != 0:
                        send_symbol = "Tuan Anh " if self.identity_ == "TA" else "Steve "
                        if "Bi" in symbol:
                            send_symbol += "Binance "
                        elif "Ok" in symbol:
                            send_symbol += "OKX "
                        elif "By" in symbol:
                            send_symbol += "Bybit "

                        if symbol[2] != "M":
                            send_symbol += f"Sub{symbol[2]} "
                        else:
                            send_symbol += "Main "

                        if dict["risk_alarm"].out_of_range(dict["risk"]):
                            risk_background_color = "yellow"
                            alarm.activate(message=f"{send_symbol}risk alarm {dict['name']}: {dict['risk']}", alarm=True)

                        if dict["equity_alarm"].out_of_range(dict["equity"]):
                            equity_background_color = "yellow"
                            alarm.activate(message=f" {send_symbol}equity alarm {dict['name']}: {dict['equity']}", alarm=True)

                        if position != 0:
                            if dict["position_alarm"].out_of_range(position):
                                position_background_color = "yellow"
                                alarm.activate(message=f"{send_symbol}position alarm {dict['name']}: {position}", alarm=True)

                    returnStr += "Free: " + fmt(0) + " / " + fmt(dict["withdrawable"], color="blue") + "<br>"
                    if dict["initial"] > 0:
                        returnStr += "Margin: " + fmt(dict["initial"]) + " / " + fmt(dict["maintenance"], color="red") + "<br>"
                    if dict["risk"] > 0:
                        returnStr += "Risk: " + fmt(dict["risk_alarm"].start, color="red", formatStr=".0%") + " / " + fmt(dict["risk"], background_color=risk_background_color, formatStr=".2%", font_weight="bold") + " / " + fmt(dict["risk_alarm"].end, color="blue", formatStr=".0%") + "<br>"
                    if dict["equity"] > 0:
                        returnStr += "Asset: " + fmt(dict["equity_alarm"].start, color="red") + " / " + fmt(dict["equity"], background_color=equity_background_color, font_weight="bold") + " / " + fmt(dict["equity_alarm"].end, color="blue") + "<br>"
                    if position != 0:
                        returnStr += "Position: " + fmt(dict["long_pos"]) + " / " + fmt(dict["short_pos"], color="red") + "<br>"
                        returnStr += "Rate: " + fmt(dict["position_alarm"].start, color="red", formatStr=".0%") + " / " + fmt(position, background_color=position_background_color, formatStr=".2%", font_weight="bold") + " / " + fmt(dict["position_alarm"].end, color="blue", formatStr=".0%") + "<br>"

            return total_value, returnStr[:-4]

        total_value = 0
        for symbol, qtLabel in self.labelDict.items():
            symbol_list = self.model_.get_data(symbol=symbol)
            if symbol_list:
                value, stringText = handle_frontend_data(symbol_list)
                total_value += value
                qtLabel.setText(stringText)

        self.uiMainWindow_.label_totalValue.setText(f"Total: {fmt(total_value, color='red')}")

    def data_loop(self):
        # Todo: Stop this when transferring
        if int(self.current_time/self.retrieve_frequency) < int(time.time()/self.retrieve_frequency):
            self.update_data()
            self.communication_.ui_signal.emit()

        if int(self.current_time/self.save_frequency_m) < int(time.time()/self.save_frequency_m):
           self.model_.save_data()

        self.current_time = time.time()
        if self.current_time - self.update_time > self.alarm_error_duration:
            alarm.activate("Program can't connect with servers.", alarm=True)
            print(self.current_time - self.update_time)
            self.update_time += 15

    # These loops must not modify the Model objects
    def ui_update(self):
        self.upload_withdrawable()
        self.upload_risk()
        self.uiMainWindow_.label_infinity.setText(f"{datetime.datetime.now().strftime('%H:%M:%S')}")