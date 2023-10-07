from collections import ChainMap
import time, alarm

class Controller(object):
    labelDict = {}
    save_frequency_m = 10
    retrieveFrequencyS = 20
    currentTime = 0

    def __init__ (self, uiMainWindow, Model, binanceHandler, okxHandler, bybitHandler):
        self.BinanceHandler_ = binanceHandler
        self.BybitHandler_ = bybitHandler
        self.OKXHandler_ = okxHandler
        self.uiMainWindow_ = uiMainWindow
        self.model_ = Model
        self.uiMainWindow_.button_changeThreshold.clicked.connect(self.change_threshold_button_clicked)

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

    def change_threshold_button_clicked(self):
        # Todo: Check if user type correctly
        alarm = float(self.uiMainWindow_.lineEdit_threshold.text())
        asset = self.uiMainWindow_.lineEdit_assetName.text().upper()
        market = self.uiMainWindow_.comboBox_market.currentText()
        coinType = self.uiMainWindow_.comboBox_coinType.currentText()
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

        self.model_.set_data(symbol=symbol, asset=asset, alarm=alarm)
        self.uploadData()

    def listToLabel(self, list):
        returnStr = ""
        for dict in list:
            returnStr += dict["asset"] + ": " + str(round(dict["risk"], 4)) + "/" + str(round(dict["alarm"], 4)) + "\n"

        return returnStr[:-1]

    def updateData(self):
            bin_risk = self.BinanceHandler_.get_risk()
            okx_risk = self.OKXHandler_.get_risk()
            bybit_risk = self.BybitHandler_.get_risk()
            risk_dict = ChainMap(bin_risk, okx_risk, bybit_risk)
            for key, value in risk_dict.items():
                self.model_.set_data(symbol=self.substring_before(key, "_"), asset=self.substring_after(key, "_"), risk=value)

    def uploadData(self):
        for symbol, qtLabel in self.labelDict.items():
            currentListOfDict = self.model_.get_data(symbol=symbol)
            qtLabel.setText(self.listToLabel(currentListOfDict))

    def alarmIf(self):
        for symbol in self.labelDict.keys():
            currentListOfDict = self.model_.get_data(symbol=symbol)
            for dict in currentListOfDict:
                if dict["risk"] > dict["alarm"] and "Bi" in symbol:
                    alarm.activate(message=f"Binance Sub{symbol[2]} {dict['asset']}: {dict['risk']}")
                elif dict["risk"] < dict["alarm"] and "Ok" in symbol:
                    alarm.activate(message=f"OKX Sub{symbol[2]} {dict['asset']}: {dict['risk']}")
                elif dict["risk"] > dict["alarm"] and "By" in symbol:
                    alarm.activate(message=f"Byb Sub{symbol[2]} {dict['asset']}: {dict['risk']}")

    def loop(self):
        if int(self.currentTime/(self.save_frequency_m*60)) < int(time.time()/(self.save_frequency_m*60)):
            pass

        if int(self.currentTime/self.retrieveFrequencyS) < int(time.time()/self.retrieveFrequencyS):
            self.updateData()
            self.uploadData()
            self.alarmIf()
            self.currentTime = time.time()

