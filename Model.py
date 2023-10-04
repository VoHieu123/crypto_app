BIN_DEFAULT_ALARM = 0.7
OKX_DEFAULT_ALARM = 9
BYBIT_DEFAULT_ALARM = 0.7

class Model(object):
    DEFAULT_ALARM = {"Bi": BIN_DEFAULT_ALARM, "Ok": OKX_DEFAULT_ALARM, "Byb": BYBIT_DEFAULT_ALARM}

    def __init__(self):
        # Todo: Persistent storage
        self.data = {
            "BiMU": [], "Bi1U": [], "Bi2U": [], "Bi3U": [], "BiMC": [], "Bi1C": [], "Bi2C": [], "Bi3C": [],
            "OkMU": [], "Ok1U": [], "Ok2U": [], "Ok3U": [], "Ok1C": [], "OkMC": [], "Ok2C": [], "Ok3C": [],
            "ByMU": [], "By1U": [], "By2U": [], "By3U": [], "By1C": [], "ByMC": [], "By2C": [], "By3C": []
        }

    def set_data(self, symbol, asset, risk=-1, alarm=-1) -> bool:
        if symbol in self.data:
            for sub_dict in self.data[symbol]:
                if isinstance(sub_dict, dict) and sub_dict.get("asset") == asset:
                    sub_dict["risk"] = risk if risk != -1 else sub_dict["risk"]
                    sub_dict["alarm"] = alarm if alarm != -1 else sub_dict["alarm"]
                    return True

            if alarm == -1:
                if "Bi" in symbol:
                    alarm = BIN_DEFAULT_ALARM
                elif "Ok" in symbol:
                    alarm = OKX_DEFAULT_ALARM
                elif "By" in symbol:
                    alarm = BYBIT_DEFAULT_ALARM

                # if alarm == -1:
                #     exchange_prefix = next((prefix for prefix in ["Bi", "Ok", "By"] if prefix in symbol), "")
                #     alarm = self.DEFAULT_ALARM.get(exchange_prefix, 0)
            self.data[symbol].append({"asset": asset, "risk": risk, "alarm": alarm})
            return True

        return False

    def get_data(self, symbol):
        if symbol in self.data:
            return [sub_dict for sub_dict in self.data[symbol] if isinstance(sub_dict, dict) and all(key in sub_dict for key in ("asset", "risk", "alarm"))]

        return []
