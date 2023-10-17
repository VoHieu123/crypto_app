from utils import auto_format as fmt
from utils import substring_after, substring_before, change_last_letter
from utils import Range
import time, alarm
from utils import Communication

class Controller():
    labelDict = {}
    save_frequency_m = 10
    retrieveFrequencyS = 20
    currentTime = 0

    def __init__ (self, uiMainWindow, model, communication: Communication, binanceHandler, okxHandler, bybitHandler):
        self.communication_ = communication
        self.BinanceHandler_ = binanceHandler
        self.BybitHandler_ = bybitHandler
        self.OKXHandler_ = okxHandler
        self.uiMainWindow_ = uiMainWindow
        self.model_ = model
        self.uiMainWindow_.button_changeThreshold.clicked.connect(self.change_threshold_button_clicked)
        self.uiMainWindow_.button_transfer.clicked.connect(self.transfer_button_clicked)

        markets = ["Bi", "Ok", "By"]
        subaccounts = ["M", "1", "2", "3"]
        coinTypes = ["U", "C"]

        self.labelDict = {}

        for market in markets:
            for subaccount in subaccounts:
                if market == "Bi" or market == "Ok":
                    for coin_type in coinTypes:
                        label_key = f"{market}{subaccount}{coin_type}"
                        label_name = f"label_{market}{subaccount}{coin_type}"
                        self.labelDict[label_key] = getattr(self.uiMainWindow_, label_name)
                else:
                    label_key = f"{market}{subaccount}U"
                    label_name = f"label_{market}{subaccount}U"
                    self.labelDict[label_key] = getattr(self.uiMainWindow_, label_name)

    # Todo: Update data everytime the combo boxes are clicked
    def transfer_button_clicked(self):
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

    def change_threshold_button_clicked(self):
        try:
            alarm = self.uiMainWindow_.lineEdit_threshold.text().replace(" ", "")
            alarm = Range(float(substring_before(alarm, "-")), float(substring_after(alarm, "-")))
        except:
            return
        asset = self.uiMainWindow_.lineEdit_assetName.text().upper()
        market = self.uiMainWindow_.comboBox_market.currentText()
        coin_type = self.uiMainWindow_.comboBox_coinType.currentText()
        alarm_type = self.uiMainWindow_.comboBox_alarmType.currentText()
        sub_acc = self.uiMainWindow_.comboBox_subAcc.currentText()

        self.uiMainWindow_.lineEdit_threshold.setText("")
        self.uiMainWindow_.lineEdit_assetName.setText("")

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
        self.upload_data()
        self.alarm_if()

    @staticmethod
    def list_to_label(list):
        returnStr = ""
        for dict in list:
            position = abs(dict["long_pos"] + dict["short_pos"])/dict["long_pos"] if dict["long_pos"] > 0 else 0
            returnStr += "(" + dict["asset"] + ") "
            if dict["risk"] > 0:
                returnStr += "RISK" + ": " + fmt(dict["risk_alarm"].start, color="red") + "/" + fmt(dict["risk"]) + "/" + fmt(dict["risk_alarm"].end, color="blue") + "<br>"
            if dict["equity"] > 0:
                returnStr += "EQUITY: " + fmt(dict["equity_alarm"].start, color="red") + "/" + fmt(dict["equity"]) + "/" + fmt(dict["equity_alarm"].end, color="blue") + "<br>"
            if dict["long_pos"] != 0 and dict["short_pos"] != 0:
                returnStr += "LONG/SHORT: " + fmt(dict["long_pos"]) + "/" + fmt(dict["short_pos"]) + "<br>"
                returnStr += "POSITION: " + fmt(dict["position_alarm"].start, color="red") + "/" + fmt(position) + "/" + fmt(dict["position_alarm"].end, color="blue") + "<br>"

        return returnStr[:-4]

    def update_data(self):
        # Define a list or dictionary of handlers
        handlers = {
            "Binance": self.BinanceHandler_,
            "OKX": self.OKXHandler_,
            "Bybit": self.BybitHandler_
        }

        # Iterate through the handlers and set data in the model
        for handler in handlers.values():
            risk_data = handler.get_account_status()
            for key, value in risk_data.items():
                symbol = substring_before(key, "_")
                asset_name = substring_after(key, "_")
                risk, equity, withdrawable, = value.get("risk"), value.get("equity"), value.get("withdrawable")
                long_pos, short_pos = value.get("long_pos"), value.get("short_pos")
                self.model_.set_data(symbol=symbol, asset_name=asset_name,
                                     risk=risk, equity=equity, withdrawable=withdrawable,
                                     long_pos=long_pos, short_pos=short_pos)


    def upload_data(self):
        self.upload_withdrawable()
        self.upload_risk()

    def upload_withdrawable(self):
        marketFrom = self.uiMainWindow_.comboBox_exchangeFrom.currentText()
        accountFrom = self.uiMainWindow_.comboBox_accountFrom.currentText()
        targetSymbol = f"{marketFrom[:2]}{'M' if accountFrom == 'Main' else accountFrom[-1:]}U"

        for dict in self.model_.get_data(symbol=targetSymbol):
            if dict["asset"] == "USDT":
                self.uiMainWindow_.label_withdrawable.setText(f"{round(dict.get('withdrawable'), 1)}")
                return

        self.uiMainWindow_.label_withdrawable.setText("0")

    def upload_risk(self):
        for symbol, qtLabel in self.labelDict.items():
            symbol_list = self.model_.get_data(symbol=symbol)
            qtLabel.setText(self.list_to_label(symbol_list))

    def alarm_if(self):
        for symbol in self.labelDict.keys():
            symbol_list = self.model_.get_data(symbol=symbol)
            for dict in symbol_list:
                if dict["risk"] != 0:
                    if dict["risk_alarm"].out_of_range(dict["risk"]) and "Bi" in symbol:
                        alarm.activate(message=f"Binance Sub{symbol[2]} risk alarm {dict['asset']}: {dict['risk']}")
                    if dict["risk_alarm"].out_of_range(dict["risk"]) and "Ok" in symbol:
                        alarm.activate(message=f"OKX Sub{symbol[2]} risk alarm {dict['asset']}: {dict['risk']}")
                    if dict["risk_alarm"].out_of_range(dict["risk"]) and "By" in symbol:
                        alarm.activate(message=f"Byb Sub{symbol[2]} risk alarm {dict['asset']}: {dict['risk']}")

                    if dict["equity_alarm"].out_of_range(dict["equity"]) and "Bi" in symbol:
                        alarm.activate(message=f"Binance Sub{symbol[2]} equity alarm {dict['asset']}: {dict['equity']}")
                    if dict["equity_alarm"].out_of_range(dict["equity"]) and "Ok" in symbol:
                        alarm.activate(message=f"OKX Sub{symbol[2]} equity alarm {dict['asset']}: {dict['equity']}")
                    if dict["equity_alarm"].out_of_range(dict["equity"]) and "By" in symbol:
                        alarm.activate(message=f"Byb Sub{symbol[2]} equity alarm {dict['asset']}: {dict['equity']}")

                    position = abs(dict["long_pos"] + dict["short_pos"])/dict["long_pos"] if dict["long_pos"] > 0 else 0
                    if position != 0:
                        if dict["position_alarm"].out_of_range(position) and "Bi" in symbol:
                            alarm.activate(message=f"Binance Sub{symbol[2]} position alarm {dict['asset']}: {position}")
                        if dict["position_alarm"].out_of_range(position) and "Ok" in symbol:
                            alarm.activate(message=f"OKX Sub{symbol[2]} position alarm {dict['asset']}: {position}")
                        if dict["position_alarm"].out_of_range(position) and "By" in symbol:
                            alarm.activate(message=f"Byb Sub{symbol[2]} position alarm {dict['asset']}: {position}")

    def data_loop(self):
        # Todo: Stop this when transferring
        if int(self.currentTime/(self.save_frequency_m*60)) < int(time.time()/(self.save_frequency_m*60)):
            pass

        if int(self.currentTime/self.retrieveFrequencyS) < int(time.time()/self.retrieveFrequencyS):
            self.update_data()
            self.alarm_if()
            self.communication_.ui_signal.emit()
            self.currentTime = time.time()

    # This loop must not modify the Model object
    def ui_update(self):
        self.upload_data()