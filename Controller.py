from collections import ChainMap
import time, alarm

class Controller(object):
    labelDict = {}
    save_frequency_m = 10
    retrieveFrequencyS = 20
    currentTime = 0

    def __init__ (self, uiMainWindow, model, binanceHandler, okxHandler, bybitHandler):
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
                    for coinType in coinTypes:
                        label_key = f"{market}{subaccount}{coinType}"
                        label_name = f"label_{market}{subaccount}{coinType}"
                        self.labelDict[label_key] = getattr(self.uiMainWindow_, label_name)
                else:
                    label_key = f"{market}{subaccount}U"
                    label_name = f"label_{market}{subaccount}U"
                    self.labelDict[label_key] = getattr(self.uiMainWindow_, label_name)

    @staticmethod
    def change_last_letter(word, new_letter):
        if len(word) < 1:
            return word

        word_list = list(word)
        word_list[-1] = new_letter
        modified_word = ''.join(word_list)

        return modified_word

    @staticmethod
    def substring_after(s, delim):
        return s.partition(delim)[2]

    @staticmethod
    def substring_before(s, delim):
        return s.partition(delim)[0]

    # Todo: Update data everytime the combo boxes are clicked

    def transfer_button_clicked(self):
        print("Clicked")
        self.update_data()
        self.upload_data()
        print("Finished")
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
            alarm = float(self.uiMainWindow_.lineEdit_threshold.text())
        except:
            return
        asset = self.uiMainWindow_.lineEdit_assetName.text().upper()
        market = self.uiMainWindow_.comboBox_market.currentText()
        coinType = self.uiMainWindow_.comboBox_coinType.currentText()
        alarmType = self.uiMainWindow_.comboBox_alarmType.currentText()
        subAcc = self.uiMainWindow_.comboBox_subAcc.currentText()

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

        symbol = "".join(symbol_mappings.get(item, "") for item in [market, subAcc, coinType])

        if "By" in symbol:
            symbol = self.change_last_letter(symbol, "U")

        if alarmType == "Risk":
            self.model_.set_data(symbol=symbol, asset_name=asset, alarm=alarm)
        elif alarmType == "Equity":
            self.model_.set_data(symbol=symbol, asset_name=asset, equity_alarm=alarm)
        self.upload_data()

    @staticmethod
    def list_to_label(list):
        returnStr = ""
        for dict in list:
            returnStr += dict["asset"] + ": " + str(round(dict["risk"], 4)) + "/" + str(round(dict["alarm"], 4)) + "\n"
            returnStr += "EQUITY: " + str(round(dict["equity"], 4)) + "/" + str(round(dict["equity_alarm"], 4)) + "\n"

        return returnStr[:-1]

    def update_data(self):
        bin_risk = self.BinanceHandler_.get_account_status()
        okx_risk = self.OKXHandler_.get_account_status()
        bybit_risk = self.BybitHandler_.get_account_status()
        risk_dict = ChainMap(bin_risk, okx_risk, bybit_risk)
        for key, value in risk_dict.items():
            self.model_.set_data(symbol=self.substring_before(key, "_"),
                                 asset_name=self.substring_after(key, "_"),
                                 risk=value[0], equity=value[1], withdrawable=value[2])

    def upload_data(self):
        self.upload_withdrawable()
        self.upload_status()

    def upload_withdrawable(self):
        marketFrom = self.uiMainWindow_.comboBox_exchangeFrom.currentText()
        accountFrom = self.uiMainWindow_.comboBox_accountFrom.currentText()
        targetSymbol = f"{marketFrom[:2]}{'M' if accountFrom == 'Main' else accountFrom[-1:]}U"

        for dict in self.model_.get_data(symbol=targetSymbol):
            if dict["asset"] == "USDT":
                self.uiMainWindow_.label_withdrawable.setText(f"{round(dict.get('withdrawable'), 1)}")
                return
            
        self.uiMainWindow_.label_withdrawable.setText("0")

    def upload_status(self):
        for symbol, qtLabel in self.labelDict.items():
            currentListOfDict = self.model_.get_data(symbol=symbol)
            qtLabel.setText(self.list_to_label(currentListOfDict))

    def alarm_if(self):
        for symbol in self.labelDict.keys():
            currentListOfDict = self.model_.get_data(symbol=symbol)
            for dict in currentListOfDict:
                if dict["risk"] != 0:
                    if dict["risk"] > dict["alarm"] and "Bi" in symbol:
                        alarm.activate(message=f"Binance Sub{symbol[2]} {dict['asset']}: {dict['risk']}")
                    if dict["risk"] < dict["alarm"] and "Ok" in symbol:
                        alarm.activate(message=f"OKX Sub{symbol[2]} {dict['asset']}: {dict['risk']}")
                    if dict["risk"] > dict["alarm"] and "By" in symbol:
                        alarm.activate(message=f"Byb Sub{symbol[2]} {dict['asset']}: {dict['risk']}")

                    if dict["equity"] < dict["equity_alarm"] and "Bi" in symbol:
                        alarm.activate(message=f"Binance Sub{symbol[2]} {dict['asset']}: {dict['equity']}")
                    if dict["equity"] < dict["equity_alarm"] and "Ok" in symbol:
                        alarm.activate(message=f"OKX Sub{symbol[2]} {dict['asset']}: {dict['equity']}")
                    if dict["equity"] < dict["equity_alarm"] and "By" in symbol:
                        alarm.activate(message=f"Byb Sub{symbol[2]} {dict['asset']}: {dict['equity']}")

    def loop(self):
        if int(self.currentTime/(self.save_frequency_m*60)) < int(time.time()/(self.save_frequency_m*60)):
            pass

        if int(self.currentTime/self.retrieveFrequencyS) < int(time.time()/self.retrieveFrequencyS):
            self.update_data()
            self.upload_data()
            self.alarm_if()
            self.currentTime = time.time()