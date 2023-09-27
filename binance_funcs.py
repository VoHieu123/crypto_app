from binance import Client

binanceClient = 0

def init(apiKey, secretKey):
    global binanceClient
    binanceClient = Client(api_key=apiKey, api_secret=secretKey)

def get_risk_percentage():
    risk_list = {}
    mainAccountData = binanceClient.futures_account()
    for asset in mainAccountData["assets"]:
        if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
            continue
        risk_list[f"BiMU_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

    mainAccountData = binanceClient.futures_coin_account()
    for asset in mainAccountData["assets"]:
        if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
            continue
        risk_list[f"BiMC_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

    sub_accounts = ["evan1965.11@proton.me", "evan1965.12@proton.me", "evan1965.13@proton.me"]
    for i, sub_account in enumerate(sub_accounts):
        usdm = binanceClient.get_subaccount_futures_details(email=sub_account, futuresType = 1)
        usdm = usdm["futureAccountResp"]["assets"]
        for usd in usdm:
            if int(float(usd["walletBalance"])) == 0 or int(float(usd["maintenanceMargin"])) == 0:
                continue
            risk_list[f"Bi{i + 1}U_{usd['asset']}"] = float(usd["maintenanceMargin"])/float(usd["marginBalance"])

        coinm = binanceClient.get_subaccount_futures_details(email=sub_account, futuresType = 2)
        coinm = coinm["deliveryAccountResp"]["assets"]
        for coin in coinm:
            if int(float(coin["walletBalance"])) == 0 or int(float(coin["maintenanceMargin"])) == 0:
                continue
            risk_list[f"Bi{i + 1}C_{coin['asset']}"] = float(coin["maintenanceMargin"])/float(coin["marginBalance"])

    return risk_list