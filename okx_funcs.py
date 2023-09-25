from okx import PublicData, SubAccount, MarketData
import pandas as pd
import numpy as np
from datetime import datetime
import time
import const

okx_public_api = PublicData.PublicAPI(const.OKX_API_KEY, const.OKX_SECRET_KEY, const.OKX_PASSPHRASE, flag="0", debug=False)
okx_market_api = MarketData.MarketAPI(const.OKX_API_KEY, const.OKX_SECRET_KEY, const.OKX_PASSPHRASE, flag="0", debug=False)
okx_subaccount_api = SubAccount.SubAccountAPI(const.OKX_API_KEY, const.OKX_SECRET_KEY, const.OKX_PASSPHRASE, flag="0", debug=False)

def get_prices(input_symbol_array):
    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        temp = okx_market_api.get_trades(instId=input_symbol, limit=1)
        if len(temp["data"]) != 0:
            temp = pd.DataFrame(temp["data"])

            temp.rename(columns = {"px" : temp["instId"][0]}, inplace = True)
            temp.drop(["tradeId", "sz", "side", "instId", "ts"], axis=1, inplace=True)

            if data.empty:
                data = temp
            else:
                data = data.join(temp)
        else:
            print("No response from symbol: ", input_symbol)
            data[input_symbol] = ''

    return data

def get_most_recent_bid_ask(input_symbol_array):
    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        temp = okx_market_api.get_ticker(instId=input_symbol)
        time.sleep(0.1)

        if len(temp["data"]) != 0:
            temp = pd.DataFrame(temp["data"])
            temp = temp[["askPx", "bidPx"]]
            temp.rename(columns = {"bidPx" : "bid_" + input_symbol}, inplace = True)
            temp.rename(columns = {"askPx" : "ask_" + input_symbol}, inplace = True)

            if data.empty:
                data = temp
            else:
                data = data.join(temp)
        else:
            print("No response from symbol: ", input_symbol)
            data[input_symbol] = ''

    return data

def get_risk_percentage():
    risk_list = {}
    subaccounts = ["evan196511", "evan196512", "evan196513"]

    for i, sub_acct in enumerate(subaccounts):
        sub_data = okx_subaccount_api.get_account_balance(subAcct=sub_acct)
        sub_data = sub_data["data"][0]["details"]

        for asset in sub_data:
            risk_list[f"Ok{i + 1}U_{asset['ccy']}"] = float(asset["mgnRatio"])

    return risk_list

def get_funding_rate(input_symbol_array):

    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        print(input_symbol)
        data_flag = False
        time_to_get = int(time.time() *1000)
        current_data = pd.DataFrame()
        start_again_flag = False

        temp = okx_public_api.funding_rate_history(input_symbol, after=time_to_get, limit=100)
        # time.sleep(0.2)

        while len(temp["data"]) != 0 or start_again_flag:
            data_flag = True if start_again_flag == False else data_flag
            start_again_flag = False if start_again_flag else start_again_flag
            temp = pd.DataFrame(temp["data"])

            temp.drop(["instType", "instId", "fundingRate"], axis=1, inplace=True)
            time_to_get = int(temp["fundingTime"].iloc[-1]) - 1000
            temp["fundingTime"] = pd.to_datetime(temp['fundingTime'].astype(dtype=np.int64).apply(lambda x: int((int(x)/100000))*100000), unit="ms")
            temp.set_index("fundingTime", inplace=True)
            temp = temp[~temp.index.duplicated(keep='first')]
            current_data = pd.concat([temp, current_data])
            temp = okx_public_api.funding_rate_history(input_symbol, after=time_to_get, limit=100)
            # time.sleep(0.2)

            if len(temp["data"]) == 0 and len(current_data) < 293:
                print(temp)
                temp = okx_public_api.funding_rate_history(input_symbol, after=time_to_get, limit=100)
                # time.sleep(0.2)

        if data_flag:
            input_symbol = input_symbol[:-5].replace("-", "")
            current_data["realizedRate"] = current_data["realizedRate"].astype(np.float64)
            if input_symbol == "PEPE-USDT-SWAP":
                current_data["realizedRate"] = current_data["realizedRate"].apply(lambda i: i*1000)
            current_data.rename(columns = {"realizedRate" : input_symbol + "_OKX"}, inplace = True)
            data = pd.concat([data, current_data], axis=1)
        else:
            print("No response from symbol: ", input_symbol)
            data[input_symbol + "_OKX"] = ''

    return data