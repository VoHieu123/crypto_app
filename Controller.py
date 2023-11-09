from utils import auto_format as fmt
from utils import substring_after, substring_before
from utils import Range
import time, alarm
from utils import Communication
from PyQt6.QtGui import QFont
import datetime
import computer_specific
import pandas as pd

class Controller():
    def __init__ (self, identity, uiMainWindow, model, communication: Communication, binanceHandler, okxHandler, bybitHandler):
        self.labelDict = {}
        self.save_frequency_m = 10*60
        self.update_time = 0
        self.alarm_error_duration = 60*25
        self.retrieve_frequency = 30
        self.current_time = 0
        self.identity_ = identity
        self.communication_ = communication
        self.BinanceHandler_ = binanceHandler
        self.BybitHandler_ = bybitHandler
        self.OKXHandler_ = okxHandler
        self.uiMainWindow_ = uiMainWindow
        self.model_ = model
        self.uiMainWindow_.ui.button_changeThreshold.clicked.connect(self.change_threshold_button_clicked)
        self.uiMainWindow_.ui.button_transfer.clicked.connect(self.transfer_button_clicked)
        self.uiMainWindow_.ui.button_export.clicked.connect(self.export_button_clicked)
        self.uiMainWindow_.ui.button_positionsPnL.clicked.connect(self.positions_pnl_button_clicked)

        markets = ["Bi", "Ok", "By"]
        subaccounts = ["M", "1"]

        self.labelDict = {}

        font = QFont()
        font.setPointSize(13)

        for market in markets:
            for subaccount in subaccounts:
                label_key = f"{market}{subaccount}U"
                label_name = f"label_{market}{subaccount}U"
                try:
                    ui_label = getattr(self.uiMainWindow_.ui, label_name)
                    ui_label.setFont(font)
                    self.labelDict[label_key] = ui_label
                except Exception as e:
                    print(f"Controller error: {e}")
                    pass

        label_const_list = [f"label_{name}" for name in ["totalValue", "infinity", "binance", "okx", "bybit", "mainAccount", "subAccount1"]]
        for label in label_const_list:
            ui_label = getattr(self.uiMainWindow_.ui, label)
            ui_label.setFont(font)

        self.uiMainWindow_.ui.label_infinity.setStyleSheet("QLabel { border: 1px solid black;}")
        self.uiMainWindow_.ui.label_totalValue.setStyleSheet("QLabel { border: 1px solid black;}")

    def positions_pnl_button_clicked(self):
        data = pd.DataFrame()
        pnls_1 = self.OKXHandler_.get_positions_pnl()
        pnls_2 = self.OKXHandler_.get_positions_pnl(1)
        pnls_3 = self.BinanceHandler_.get_positions_pnl()
        pnls_4 = self.BinanceHandler_.get_positions_pnl(1)
        data = pd.concat([data, pnls_1, pnls_2, pnls_3, pnls_4], axis=1)

        data.to_excel(f"{computer_specific.PNL_PATH}pnls_{self.model_.identity.lower()}.xlsx", index=False)

    def transfer_button_clicked(self):
        self.update_data()
        try:
            withdrawAmount = float(self.uiMainWindow_.ui.lineEdit_withdrawAmount.text())
        except:
            return
        moduleDict = {"Binance": self.BinanceHandler_,
                      "Bybit": self.BybitHandler_,
                      "Okx": self.OKXHandler_}
        exchangeFrom = self.uiMainWindow_.ui.comboBox_exchangeFrom.currentText()
        accountFrom = self.uiMainWindow_.ui.comboBox_accountFrom.currentText()
        exchangeTo = self.uiMainWindow_.ui.comboBox_exchangeTo.currentText()
        accountTo = self.uiMainWindow_.ui.comboBox_accountTo.currentText()

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
        lower_alarm = self.uiMainWindow_.ui.lineEdit_lowerThreshold.text()
        upper_alarm = self.uiMainWindow_.ui.lineEdit_upperThreshold.text()
        self.uiMainWindow_.ui.lineEdit_lowerThreshold.setText("")
        self.uiMainWindow_.ui.lineEdit_upperThreshold.setText("")
        market = self.uiMainWindow_.ui.comboBox_market.currentText()
        alarm_type = self.uiMainWindow_.ui.comboBox_alarmType.currentText()
        sub_acc = self.uiMainWindow_.ui.comboBox_subAcc.currentText()

        try:
            if alarm_type == "Risk" or alarm_type == "Position":
                alarm = Range(-1 if lower_alarm == "" else float(lower_alarm)/100,
                              -1 if upper_alarm == "" else float(upper_alarm)/100)
            else:
                alarm = Range(-1 if lower_alarm == "" else float(lower_alarm),
                              -1 if upper_alarm == "" else float(upper_alarm))
        except:
            return

        symbol_mappings = {
            "Binance": "Bi",
            "OKX": "Ok",
            "Bybit": "By",
            "Main": "M",
            "Sub1": "1",
            "Sub2": "2",
            "Sub3": "3",
        }

        symbol = "".join(symbol_mappings.get(item, "") for item in [market, sub_acc])
        symbol += "U"

        if alarm_type == "Risk":
            self.model_.set_data(symbol=symbol, asset_name="USDT", risk_alarm=alarm)
        elif alarm_type == "Asset":
            self.model_.set_data(symbol=symbol, asset_name="USDT", equity_alarm=alarm)
        elif alarm_type == "Position":
            self.model_.set_data(symbol=symbol, asset_name="USDT", position_alarm=alarm)
        elif alarm_type == "Size":
            self.model_.set_data(symbol=symbol, asset_name="USDT", size_alarm=alarm)
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
                pnls = value.get("pnls")
                self.model_.set_data(symbol=symbol, asset_name=asset_name, pnls=pnls,
                                     risk=risk, equity=equity, withdrawable=withdrawable,
                                     long_pos=long_pos, short_pos=short_pos, initial=initial, maintenance=maintenance)

        self.update_time = time.time()

    def upload_risk(self):
        def handle_frontend_data(list):
            save_data_flag = False
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
                    size_background_color = None

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
                            save_data_flag = True
                            risk_background_color = "yellow"
                            alarm.activate(message=f"{send_symbol}risk alarm {dict['name']}: {dict['risk']}", alarm=True)

                        if dict["equity_alarm"].out_of_range(dict["equity"]):
                            save_data_flag = True
                            equity_background_color = "yellow"
                            alarm.activate(message=f" {send_symbol}equity alarm {dict['name']}: {dict['equity']}", alarm=True)

                        if position != 0:
                            if dict["position_alarm"].out_of_range(position):
                                save_data_flag = True
                                position_background_color = "yellow"
                                alarm.activate(risk_sound=False, message=f"{send_symbol}position alarm {dict['name']}: {position}", alarm=True)
                            if dict["size_alarm"].out_of_range((dict["long_pos"] - dict["short_pos"])/2):
                                save_data_flag = True
                                size_background_color = "yellow"
                                alarm.activate(risk_sound=False, message=f"{send_symbol}size alarm {dict['name']}: {(dict['long_pos'] - dict['short_pos'])/2}", alarm=True)

                    if dict["withdrawable"] > 0:
                        returnStr += "Free: " + fmt(dict["pnls"]) + " / " + fmt(dict["withdrawable"], color="blue") + "<br>"
                    if dict["initial"] > 0:
                        returnStr += "Margin: " + fmt(dict["initial"]) + " / " + fmt(dict["maintenance"], color="red") + "<br>"
                    if dict["risk"] > 0:
                        if "Ok" in symbol:
                            returnStr += "Risk: " + fmt(dict["risk_alarm"].start, font_size=20, background_color="yellow", color="red", format_number=".0%") + " / " + fmt(dict["risk"], background_color=risk_background_color, format_number=".2%", font_weight="bold") + " / " + fmt(dict["risk_alarm"].end, color="blue", format_number=".0%") + "<br>"
                        else:
                            returnStr += "Risk: " + fmt(dict["risk_alarm"].start, color="red", format_number=".0%") + " / " + fmt(dict["risk"], background_color=risk_background_color, format_number=".2%", font_weight="bold") + " / " + fmt(dict["risk_alarm"].end, color="blue", format_number=".0%", font_size=20, background_color="yellow") + "<br>"
                    if dict["equity"] > 0:
                        returnStr += "Asset: " + fmt(dict["equity_alarm"].start, color="red", font_size=20, background_color="yellow") + " / " + fmt(dict["equity"], background_color=equity_background_color, font_weight="bold") + " / " + fmt(dict["equity_alarm"].end, color="blue") + "<br>"
                    if position != 0:
                        returnStr += "Position: " + fmt(dict["long_pos"]) + " / " + fmt(dict["short_pos"], color="red") + "<br>"
                        returnStr += "Rate: " + fmt(dict["position_alarm"].start, color="red", format_number=".0%") + " / " + fmt(position, background_color=position_background_color, format_number=".2%", font_weight="bold") + " / " + fmt(dict["position_alarm"].end, color="blue", format_number=".0%", font_size=20, background_color="yellow") + "<br>"
                        returnStr += "Size: " + fmt(dict["size_alarm"].start, color="red") + " / " + fmt((dict["long_pos"] - dict["short_pos"])/2, background_color=size_background_color) + " / " + fmt(dict["size_alarm"].end, color="blue") + "<br>"

            return save_data_flag, total_value, returnStr[:-4]

        total_value = 0
        should_save_data_flag = False
        for symbol, qtLabel in self.labelDict.items():
            symbol_list = self.model_.get_data(symbol=symbol)
            if symbol_list:
                should_save_data, value, stringText = handle_frontend_data(symbol_list)
                if should_save_data:
                    should_save_data_flag = True
                total_value += value
                qtLabel.setText(stringText)

        if should_save_data_flag:
            self.model_.save_data()
        self.uiMainWindow_.ui.label_totalValue.setText(f"Total: {fmt(total_value, color='red')}")

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
            print("Program can't connect with servers.")
            print(self.current_time - self.update_time)
            self.update_time += 15

    # These loops must not modify the Model objects
    def ui_update(self):
        self.upload_risk()
        self.uiMainWindow_.ui.label_infinity.setText(f"Total: {fmt(datetime.datetime.now().strftime('%H:%M:%S'), color='red')}")