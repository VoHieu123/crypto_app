from utils import Range
from utils import substring_before, substring_after
import pickle, os
import computer_specific as cs
import pandas as pd
import const, openpyxl, datetime

BIN_DEFAULT_RISK_ALARM = Range(0.0, 0.5)
OKX_DEFAULT_RISK_ALARM = Range(0.0, 12.0)
BYBIT_DEFAULT_RISK_ALARM = Range(0.0, 0.5)

BIN_DEFAULT_EQUITY_ALARM = Range(2000, 15000)
OKX_DEFAULT_EQUITY_ALARM = Range(2000, 15000)
BYBIT_DEFAULT_EQUITY_ALARM = Range(2000, 15000)

BIN_DEFAULT_POSITION_ALARM = Range(0.00, 0.2)
OKX_DEFAULT_POSITION_ALARM = Range(0.00, 0.2)
BYBIT_DEFAULT_POSITION_ALARM = Range(0.00, 0.2)

BIN_DEFAULT_SIZE_ALARM = Range(0.00, 5000)
OKX_DEFAULT_SIZE_ALARM = Range(0.00, 5000)
BYBIT_DEFAULT_SIZE_ALARM = Range(0.00, 5000)

class Asset:
    def __init__(self, symbol, asset_name, pnls=-1, size_alarm=Range(-1, -1),
                 risk=-1, risk_alarm=Range(-1, -1), equity=-1, equity_alarm=Range(-1, -1),
                 withdrawable=-1, long_pos=-1, short_pos=-1, position_alarm=Range(-1, -1),
                 initial=-1, maintenance=-1):

        self.size_alarm = size_alarm
        self.pnls = pnls
        self.name = asset_name
        self.risk = risk
        self.equity = equity
        self.equity_alarm = equity_alarm
        self.risk_alarm = risk_alarm
        self.withdrawable = withdrawable
        self.long_pos = long_pos
        self.short_pos = short_pos
        self.position_alarm = position_alarm
        self.symbol = symbol
        self.initial = initial
        self.maintenance = maintenance

        if size_alarm == Range(-1, -1):
            if "Bi" in symbol:
                self.size_alarm = BIN_DEFAULT_SIZE_ALARM
            elif "Ok" in symbol:
                self.size_alarm = OKX_DEFAULT_SIZE_ALARM
            elif "By" in symbol:
                self.size_alarm = BYBIT_DEFAULT_SIZE_ALARM

        if position_alarm == Range(-1, -1):
            if "Bi" in symbol:
                self.position_alarm = BIN_DEFAULT_POSITION_ALARM
            elif "Ok" in symbol:
                self.position_alarm = OKX_DEFAULT_POSITION_ALARM
            elif "By" in symbol:
                self.position_alarm = BYBIT_DEFAULT_POSITION_ALARM

        if equity_alarm == Range(-1, -1):
            if "Bi" in symbol:
                self.equity_alarm = BIN_DEFAULT_EQUITY_ALARM
            elif "Ok" in symbol:
                self.equity_alarm = OKX_DEFAULT_EQUITY_ALARM
            elif "By" in symbol:
                self.equity_alarm = BYBIT_DEFAULT_EQUITY_ALARM

        if risk_alarm == Range(-1, -1):
            if "Bi" in symbol:
                self.risk_alarm = BIN_DEFAULT_RISK_ALARM
            elif "Ok" in symbol:
                self.risk_alarm = OKX_DEFAULT_RISK_ALARM
            elif "By" in symbol:
                self.risk_alarm = BYBIT_DEFAULT_RISK_ALARM

    def is_valid_instance(self) -> bool:
        if any(attribute == -1 for attribute in \
               [self.risk, self.equity, self.long_pos, self.short_pos, self.initial, self.maintenance]):
            return False
        return True

    def get_data_copy(self):
        return Asset(symbol=self.symbol, asset_name=self.name, risk=self.risk, equity=self.equity,
                     withdrawable=self.withdrawable, long_pos=self.long_pos, pnls=self.pnls,
                     short_pos=self.short_pos, initial=self.initial, maintenance=self.maintenance)

    def get_settings_copy(self):
        return Asset(symbol=self.symbol, asset_name=self.name,
                     risk_alarm=self.risk_alarm,
                     size_alarm=self.size_alarm,
                     equity_alarm=self.equity_alarm,
                     position_alarm=self.position_alarm)

    def set_free(self, pnls):
        self.pnls = pnls if pnls!= -1 else self.pnls
    def set_withdrawable(self, withdrawable):
        self.withdrawable = withdrawable if withdrawable != -1 else self.withdrawable
    def set_long_pos(self, long_pos):
        self.long_pos = long_pos if long_pos != -1 else self.long_pos
    def set_short_pos(self, short_pos):
        self.short_pos = short_pos if short_pos != -1 else self.short_pos
    def set_risk(self, risk):
        self.risk = risk if risk != -1 else self.risk
    def set_initial(self, initial):
        self.initial = initial if initial != -1 else self.initial
    def set_maintenance(self, maintenance):
        self.maintenance = maintenance if maintenance != -1 else self.maintenance
    def set_equity(self, equity):
        self.equity = equity if equity != -1 else self.equity
    def set_size_alarm(self, size_alarm: Range):
        if size_alarm.start != -1:
            self.size_alarm.start = size_alarm.start
        if size_alarm.end != -1:
            self.size_alarm.end = size_alarm.end
    def set_risk_alarm(self, risk_alarm: Range):
        if risk_alarm.start != -1:
            self.risk_alarm.start = risk_alarm.start
        if risk_alarm.end != -1:
            self.risk_alarm.end = risk_alarm.end
    def set_equity_alarm(self, equity_alarm: Range):
        if equity_alarm.start!= -1:
            self.equity_alarm.start = equity_alarm.start
        if equity_alarm.end!= -1:
            self.equity_alarm.end = equity_alarm.end
    def set_position_alarm(self, position_alarm: Range):
        if position_alarm.start!= -1:
            self.position_alarm.start = position_alarm.start
        if position_alarm.end!= -1:
            self.position_alarm.end = position_alarm.end

class Model(object):
    def __init__(self, identity):
        self.account_history = pd.DataFrame()
        self.identity = identity
        if identity == "TA":
            self.settings_path = cs.SETTINGS_PATH + "_ta" + ".pkl"
            self.data_path = cs.DATA_PATH + "_ta" + ".pkl"
        elif identity == "ST":
            self.settings_path = cs.SETTINGS_PATH + "_st" + ".pkl"
            self.data_path = cs.DATA_PATH + "_st" + ".pkl"

        if os.path.exists(self.data_path):
            with open(self.data_path, "rb") as pkl_file:
                self.account_history = pickle.load(pkl_file)

        if os.path.exists(self.settings_path):
            with open(self.settings_path, "rb") as pkl_file:
                self.data = pickle.load(pkl_file)
        else:
            self.data = {
                "BiMU": [], "Bi1U": [], "Bi2U": [], "Bi3U": [], "BiMC": [], "Bi1C": [], "Bi2C": [], "Bi3C": [],
                "OkMU": [], "Ok1U": [], "Ok2U": [], "Ok3U": [], "Ok1C": [], "OkMC": [], "Ok2C": [], "Ok3C": [],
                "ByMU": [], "By1U": [], "By2U": [], "By3U": [], "By1C": [], "ByMC": [], "By2C": [], "By3C": []
            }

        self.universal_mark_prices = {}

    def set_universal_mark_prices(self, usdm, market: str):
        self.universal_mark_prices[market] = usdm

    def get_universal_mark_price(self, coin):
        coin = "1000PEPEUSDT" if coin == "PEPEUSDT" else coin
        price = 0
        for df in self.universal_mark_prices.values():
            if coin in df['symbol'].values:
                price += df[df['symbol'] == coin]['markPrice'].values[0]
            else:
                print(f"No {coin}")

        return price/len(self.universal_mark_prices)

    def __del__(self):
        data = {"BiMU": [], "Bi1U": [], "Bi2U": [], "Bi3U": [], "BiMC": [], "Bi1C": [], "Bi2C": [], "Bi3C": [],
                "OkMU": [], "Ok1U": [], "Ok2U": [], "Ok3U": [], "Ok1C": [], "OkMC": [], "Ok2C": [], "Ok3C": [],
                "ByMU": [], "By1U": [], "By2U": [], "By3U": [], "By1C": [], "ByMC": [], "By2C": [], "By3C": []}

        for symbol, list in self.data.items():
            for asset in list:
                data[symbol].append(asset.get_settings_copy())

        with open(self.settings_path, "wb") as pkl_file:
            pickle.dump(data, pkl_file)

        with open(self.data_path, "wb") as pkl_file:
            pickle.dump(self.account_history, pkl_file)

    def save_data(self):
        current_data = pd.DataFrame()
        for assets in self.data.values():
            for asset in assets:
                attribute_names = ["symbol", "name", "risk", "equity", "withdrawable", "pnls",
                                   "long_pos", "short_pos", "initial", "maintenance"]
                data = {key: getattr(asset.get_data_copy(), key) for key in attribute_names}
                if any(value  == -1 for value in data.values()):
                    continue

                name = data["name"]
                symbol = data["symbol"]
                if name == "USDT":
                    data = pd.DataFrame([data])
                    data.drop(["name", "symbol"], axis=1, inplace=True)
                    data.rename(columns={"risk": "Risk", "equity": "Asset", "pnls": "PnLs",
                                         "withdrawable": "Free", "long_pos": "Long",
                                         "short_pos": "Short", "initial": "IM", "maintenance": "MM"}, inplace=True)
                    data = data.add_prefix(f"{symbol}_")
                    current_data = pd.concat([current_data, data], axis=1)

        data_type = ["Risk", "Asset", "PnLs", "Free", "Long", "Short", "IM", "MM"]

        for type in data_type:
            cols = [col for col in current_data.columns if col.endswith(type)]
            current_data[f"Total_{type}"] = current_data[cols].sum(axis=1)

        total_columns = [col for col in current_data.columns if col.startswith("Total_")]

        # Reorder the DataFrame columns with "Total_" prefix at the beginning
        new_column_order = total_columns + [col for col in current_data.columns if col not in total_columns]
        current_data = current_data[new_column_order]

        current_data.insert(0, "TIME", pd.Timestamp.now())
        current_data['TAB'] = ""
        self.account_history = pd.concat([self.account_history, current_data])

    def export_data(self):
        # Todo: Check data integrity
        name = f"{cs.DESKTOP_PATH}{self.identity.lower()}_data_{datetime.datetime.now().strftime('%H_%M')}{const.OUTPUT_DATA_EXT}"
        try:
            self.account_history.to_excel(name, index=False)
            workbook = openpyxl.load_workbook(name)
            worksheet = workbook.active

            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                if column_letter == "A":
                    worksheet.column_dimensions[column_letter].width = (max_length + 2) * 3
                else:
                    worksheet.column_dimensions[column_letter].width = (max_length + 2) * 1.1

            worksheet.insert_rows(1)
            current_symbol = ""
            cell_to_merge = 0
            for cell in worksheet[2]:
                if cell.value and cell.value != "TIME":
                    symbol = substring_before(cell.value, "_")
                    cell.value = substring_after(cell.value, "_")

                    if symbol == current_symbol:
                        cell_to_merge += 1
                    else:
                        if current_symbol != "":
                            worksheet.merge_cells(start_row=1, end_row=1,
                                                start_column=cell.column - 1 - cell_to_merge,
                                                end_column=cell.column - 1)
                            worksheet.cell(row=1, column=cell.column - 1 - cell_to_merge,
                                            value=current_symbol)
                        cell_to_merge = 0
                        current_symbol = symbol

            workbook.save(name)
            workbook.close()
        except Exception as e:
            print(f"Model error: {e}")
            pass


    def set_data(self, symbol, asset_name, pnls=-1, size_alarm=Range(-1, -1),
                 risk=-1, risk_alarm=Range(-1, -1), equity=-1, equity_alarm=Range(-1, -1),
                 withdrawable=-1, long_pos=-1, short_pos=-1, position_alarm=Range(-1, -1),
                 initial=-1, maintenance=-1) -> bool:
        if symbol in self.data:
            for asset in self.data[symbol]:
                if asset.name == asset_name:
                    asset.set_free(pnls)
                    asset.set_risk(risk)
                    asset.set_size_alarm(size_alarm)
                    asset.set_risk_alarm(risk_alarm)
                    asset.set_equity(equity)
                    asset.set_equity_alarm(equity_alarm)
                    asset.set_position_alarm(position_alarm)
                    asset.set_long_pos(long_pos)
                    asset.set_short_pos(short_pos)
                    asset.set_initial(initial)
                    asset.set_maintenance(maintenance)
                    asset.set_withdrawable(withdrawable)
                    return True

            if all(attr != -1 for attr in [risk, equity, withdrawable, long_pos, short_pos, maintenance, initial]):
                new_asset = Asset(symbol=symbol, asset_name=asset_name, risk=risk, risk_alarm=risk_alarm, pnls=pnls,
                                  equity=equity, equity_alarm=equity_alarm, withdrawable=withdrawable, size_alarm=size_alarm,
                                  long_pos=long_pos, short_pos=short_pos, position_alarm=position_alarm,
                                  initial=initial, maintenance=maintenance)
                self.data[symbol].append(new_asset)
                return True

        return False

    def get_data(self, symbol):
        returnDict = []
        if symbol in self.data:
            for asset in self.data[symbol]:
                if asset.is_valid_instance():
                    attribute_names = ["name", "risk", "equity", "withdrawable", "pnls",
                                       "risk_alarm", "equity_alarm", "position_alarm", "size_alarm",
                                       "long_pos", "short_pos", "initial", "maintenance"]

                    returnDict.append({key: getattr(asset, key) for key in attribute_names})

        return returnDict
