BIN_DEFAULT_ALARM = 0.7
OKX_DEFAULT_ALARM = 9

class Model(object):
    # Todo: Persistent storage
    data = {"BiMU": [], "Bi1U": [], "Bi2U": [], "Bi3U": [], "BiMC": [], "Bi1C": [], "Bi2C": [], "Bi3C": [],
            "OkMU": [], "Ok1U": [], "Ok2U": [], "Ok3U": [], "Ok1C": [], "OkMC": [], "Ok2C": [], "Ok3C": [],
            "ByMU": [], "By1U": [], "By2U": [], "By3U": [], "By1C": [], "ByMC": [], "By2C": [], "By3C": []}

    def __init__(self):
        pass

    def setData(self, symbol, asset, risk=-1, alarm=-1) -> bool:
        if symbol in self.data:
            for subDict in self.data[symbol]:
                if isinstance(subDict, dict) and "asset" in subDict and "risk" in subDict and "alarm" in subDict and subDict["asset"] == asset:
                    subDict["risk"] = risk if risk != -1 else subDict["risk"]
                    subDict["alarm"] = alarm if alarm != -1 else subDict["alarm"]
                    return True

            if alarm == -1:
                if "Bi" in symbol:
                    alarm = BIN_DEFAULT_ALARM
                elif "Ok" in symbol:
                    alarm = OKX_DEFAULT_ALARM
            self.data[symbol].append({"asset": asset, "risk": risk, "alarm": alarm})
            return True

        return False

    def getData(self, symbol):
        if symbol in self.data and len(self.data[symbol]) > 0:
            for subDict in self.data[symbol]:
                if isinstance(subDict, dict) and "asset" in subDict and "risk" in subDict and "alarm" in subDict:
                    return self.data[symbol]
        return []
