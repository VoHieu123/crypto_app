BIN_DEFAULT_ALARM = [0.5, 0.6]
OKX_DEFAULT_ALARM = [3, 3]
BYBIT_DEFAULT_ALARM = 0.5

BIN_DEFAULT_EQUITY_ALARM = [8000, 600]
OKX_DEFAULT_EQUITY_ALARM = [8000, 600]
BYBIT_DEFAULT_EQUITY_ALARM = 8000

BIN_DEFAULT_POSITION_ALARM = [0.05, 0.05]
OKX_DEFAULT_POSITION_ALARM = [0.05, 0.05]
BYBIT_DEFAULT_POSITION_ALARM = 0.05

class Asset:
    def __init__(self, symbol, asset_name,
                 risk=-1, alarm=-1, equity=-1, equity_alarm=-1,
                 withdrawable=-1, long_pos=-1, short_pos=-1, position_alarm=-1):
        self.name = asset_name
        self.risk = risk
        self.equity = equity
        self.equity_alarm = equity_alarm
        self.alarm = alarm
        self.withdrawable = withdrawable
        self.long_pos = long_pos
        self.short_pos = short_pos
        self.position_alarm = position_alarm

        if position_alarm == -1:
            if "Bi" in symbol:
                self.position_alarm = BIN_DEFAULT_POSITION_ALARM[0] if "U" in symbol else BIN_DEFAULT_POSITION_ALARM[1]
            elif "Ok" in symbol:
                self.position_alarm = OKX_DEFAULT_POSITION_ALARM[0] if "U" in symbol else OKX_DEFAULT_POSITION_ALARM[1]
            elif "By" in symbol:
                self.position_alarm = BYBIT_DEFAULT_POSITION_ALARM

        if equity_alarm == -1:
            if "Bi" in symbol:
                self.equity_alarm = BIN_DEFAULT_EQUITY_ALARM[0] if "U" in symbol else BIN_DEFAULT_EQUITY_ALARM[1]
            elif "Ok" in symbol:
                self.equity_alarm = OKX_DEFAULT_EQUITY_ALARM[0] if "U" in symbol else OKX_DEFAULT_EQUITY_ALARM[1]
            elif "By" in symbol:
                self.equity_alarm = BYBIT_DEFAULT_EQUITY_ALARM

        if alarm == -1:
            if "Bi" in symbol:
                self.alarm = BIN_DEFAULT_ALARM[0] if "U" in symbol else BIN_DEFAULT_ALARM[1]
            elif "Ok" in symbol:
                self.alarm = OKX_DEFAULT_ALARM[0] if "U" in symbol else OKX_DEFAULT_ALARM[1]
            elif "By" in symbol:
                self.alarm = BYBIT_DEFAULT_ALARM

    def is_valid_instance(self) -> bool:
        if any(attribute == -1 for attribute in [self.risk, self.alarm, self.equity, self.equity_alarm, self.long_pos, self.short_pos]):
            return False
        return True

    def set_long_pos(self, long_pos):
        self.long_pos = long_pos if long_pos != -1 else self.long_pos
    def set_short_pos(self, short_pos):
        self.short_pos = short_pos if short_pos != -1 else self.short_pos
    def set_risk(self, risk):
        self.risk = risk if risk != -1 else self.risk
    def set_alarm(self, alarm):
        self.alarm = alarm if alarm != -1 else self.alarm
    def set_equity(self, equity):
        self.equity = equity if equity != -1 else self.equity
    def set_equity_alarm(self, equity_alarm):
        self.equity_alarm = equity_alarm if equity_alarm != -1 else self.equity_alarm
    def set_position_alarm(self, position_alarm):
        self.position_alarm = position_alarm if position_alarm != -1 else self.position_alarm

class Model(object):
    def __init__(self):
        self.risk_data = {
            "BiMU": [], "Bi1U": [], "Bi2U": [], "Bi3U": [], "BiMC": [], "Bi1C": [], "Bi2C": [], "Bi3C": [],
            "OkMU": [], "Ok1U": [], "Ok2U": [], "Ok3U": [], "Ok1C": [], "OkMC": [], "Ok2C": [], "Ok3C": [],
            "ByMU": [], "By1U": [], "By2U": [], "By3U": [], "By1C": [], "ByMC": [], "By2C": [], "By3C": []
        }

    def set_data(self, symbol, asset_name,
                 risk=-1, alarm=-1, equity=-1, equity_alarm=-1,
                 withdrawable=-1, long_pos=-1, short_pos=-1, position_alarm=-1) -> bool:
        if symbol in self.risk_data:
            for asset in self.risk_data[symbol]:
                if asset.name == asset_name:
                    asset.set_risk(risk)
                    asset.set_alarm(alarm)
                    asset.set_equity(equity)
                    asset.set_equity_alarm(equity_alarm)
                    asset.set_position_alarm(position_alarm)
                    asset.set_long_pos(long_pos)
                    asset.set_short_pos(short_pos)
                    return True

            if all(attr != -1 for attr in [risk, equity, withdrawable, long_pos, short_pos]):
                new_asset = Asset(symbol=symbol, asset_name=asset_name, risk=risk, alarm=alarm,
                                equity=equity, equity_alarm=equity_alarm, withdrawable=withdrawable,
                                long_pos=long_pos, short_pos=short_pos, position_alarm=position_alarm)
                self.risk_data[symbol].append(new_asset)
                return True

        return False

    def get_data(self, symbol):
        returnDict = []
        if symbol in self.risk_data:
            for asset in self.risk_data[symbol]:
                if asset.is_valid_instance():
                    returnDict.append({"asset": asset.name, "risk": asset.risk, "alarm": asset.alarm,
                                       "equity": asset.equity, "equity_alarm": asset.equity_alarm,
                                       "withdrawable": asset.withdrawable, "long_pos": asset.long_pos,
                                       "short_pos": asset.short_pos, "position_alarm": asset.position_alarm})

        return returnDict
