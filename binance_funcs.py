from binance import Client
import pandas as pd
from datetime import datetime
import numpy as np
import const

binance_client = Client(const.BIN_API_KEY, const.BIN_SECRET_KEY)

# def get_trades_data_history(input_symbol_array, input_limit=100):
#     data = pd.DataFrame()

#     for input_symbol in input_symbol_array:
#         temp = binance_client.futures_aggregate_trades(symbol="BTCUSDT_231229")
#         temp = pd.DataFrame(temp)
#         temp["T"] = pd.to_datetime(temp['T'].astype(dtype=np.int64), unit="ms")
#         temp.drop(["a", "q", "f", "l", "m"], axis=1, inplace=True)
#         temp2 = binance_client.futures_aggregate_trades(symbol="BTCUSDT_230929")
#         temp2 = pd.DataFrame(temp2)
#         temp2["T"] = pd.to_datetime(temp2['T'].astype(dtype=np.int64), unit="ms")
#         temp2.drop(["a", "q", "f", "l", "m"], axis=1, inplace=True)
#         temp = temp.join(temp2, lsuffix="left_", rsuffix="right_")
#         temp.to_csv("temp.csv")

def get_prices(input_symbol_array, num_of_rounds=10):
    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        print(input_symbol)

        send_symbol = input_symbol
        if input_symbol == "PEPEUSDT":
            send_symbol = "1000PEPEUSDT"
        if input_symbol == "LUNAUSDT":
            send_symbol = "LUNA2USDT"

        current_end_time = datetime.now()
        for i in range(num_of_rounds):
            print(i)
            try:
                # Todo: recent trades?
                temp = binance_client.futures_aggregate_trades(symbol=send_symbol, endTime=current_end_time, limit=1000)
            except:
                try:
                    temp = binance_client.futures_coin_aggregate_trades(symbol=send_symbol, endTime=current_end_time, limit=1000)
                except:
                    print(f"{input_symbol}: Failed to get prices!")
                    exit()

            temp = pd.DataFrame(temp)

            if len(temp) != 0:
                # Todo....
                current_end_time = temp["T"][0]
                print(current_end_time)

                temp.drop(["m", "f", "q", "l", "a"], axis=1, inplace=True)

                # Todo: Round to hour
                temp["T"] = pd.to_datetime(temp['T'].apply(lambda x: int((x/100000))*100000), unit="ms")
                temp.set_index("T", inplace=True)
                temp = temp[~temp.index.duplicated(keep='first')]

                temp.rename(columns = {"p" : input_symbol}, inplace = True)

                data = pd.concat([data, temp], axis=1)

            else:
                break
    data.to_excel("test.xlsx")
    return data

def get_most_recent_bid_ask(input_symbol_array):
    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        if "USDT" in input_symbol:
            # Todo: Try until get it?
            temp = binance_client.futures_orderbook_ticker(symbol=input_symbol)
            temp = pd.DataFrame([temp])
        elif "USD" in input_symbol:
            temp = binance_client.futures_coin_orderbook_ticker(symbol=input_symbol)
            temp = pd.DataFrame(temp)
        else:
            # Todo: Throw error
            print("Error!")

        if len(temp) != 0:
            temp = temp[["askPrice", "bidPrice"]]
            temp.rename(columns = {"bidPrice" : "bid_" + input_symbol}, inplace = True)
            temp.rename(columns = {"askPrice" : "ask_" + input_symbol}, inplace = True)
            if data.empty:
                data = temp
            else:
                data = data.join(temp)
        else:
            print("No response from symbol: ", input_symbol)
            data[input_symbol] = ''

    return data

def get_funding_rate(input_symbol_array, input_limit=1000):

    data = pd.DataFrame()

    for input_symbol in input_symbol_array:
        print(input_symbol)
        send_symbol = input_symbol
        if input_symbol == "PEPEUSDT":
            send_symbol = "1000PEPEUSDT"
        if input_symbol == "LUNAUSDT":
            send_symbol = "LUNA2USDT"

        try:
            temp = binance_client.futures_coin_funding_rate(symbol=send_symbol, limit=input_limit)
        except:
            try:
                temp = binance_client.futures_funding_rate(symbol=send_symbol, limit=input_limit)
            except:
                print(f"{input_symbol}: Failed to get funding rate!")
                exit()

        if "_PERP" in input_symbol:
            input_symbol = input_symbol.replace("_PERP", "")

        temp = pd.DataFrame(temp)
        temp.drop(["symbol"], axis=1, inplace=True)
        temp["fundingTime"] = pd.to_datetime(temp['fundingTime'].apply(lambda x: int((x/100000))*100000), unit="ms")
        temp["fundingRate"] = temp["fundingRate"].astype(np.float64)
        temp.sort_values('fundingTime', ascending=True, inplace=True)
        temp.set_index("fundingTime", inplace=True)

        # Rename columns
        temp.rename(columns = {"fundingRate" : input_symbol + "_BIN"}, inplace = True)

        # Append to data
        if data.empty:
            data = temp
        else:
            data = pd.concat([data, temp], axis=1)

    return data

def get_risk_percentage():
    risk_list = {}
    sub_accounts = ["evan1965.11@proton.me", "evan1965.12@proton.me", "evan1965.13@proton.me"]
    for i, sub_account in enumerate(sub_accounts):
        usdm = binance_client.get_subaccount_futures_details(email=sub_account, futuresType = 1)
        usdm = usdm["futureAccountResp"]["assets"]
        for usd in usdm:
            if int(float(usd["walletBalance"])) == 0 or int(float(usd["maintenanceMargin"])) == 0:
                continue
            risk_list[f"Bi{i + 1}U_{usd['asset']}"] = float(usd["maintenanceMargin"])/float(usd["marginBalance"])

        coinm = binance_client.get_subaccount_futures_details(email=sub_account, futuresType = 2)
        coinm = coinm["deliveryAccountResp"]["assets"]
        for coin in coinm:
            if int(float(coin["walletBalance"])) == 0 or int(float(coin["maintenanceMargin"])) == 0:
                continue
            risk_list[f"Bi{i + 1}C_{coin['asset']}"] = float(coin["maintenanceMargin"])/float(coin["marginBalance"])

    return risk_list