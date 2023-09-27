from binance import Client
import pandas as pd
from datetime import datetime
import numpy as np
import const

binance_client = Client(const.BIN_API_KEY, const.BIN_SECRET_KEY)

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