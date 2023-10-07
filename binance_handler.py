from binance import Client

class BinanceHandler:
    def __init__(self, apiKey, secretKey):
        self.binanceClient = Client(api_key=apiKey, api_secret=secretKey)

    def get_risk(self) -> {}:
        risk_list = {}
        mainAccountData = self.binanceClient.futures_account()
        for asset in mainAccountData["assets"]:
            if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
                continue
            risk_list[f"BiMU_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

        mainAccountData = self.binanceClient.futures_coin_account()
        for asset in mainAccountData["assets"]:
            if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
                continue
            risk_list[f"BiMC_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

        try:
            sub_accounts_raw = self.binanceClient.get_sub_account_list()
            sub_accounts = []
            for sub_account in sub_accounts_raw["subAccounts"]:
                sub_accounts.append(sub_account["email"])
            for i, sub_account in enumerate(sub_accounts):
                usdm = self.binanceClient.get_subaccount_futures_details(email=sub_account, futuresType = 1)
                usdm = usdm["futureAccountResp"]["assets"]
                for usd in usdm:
                    if int(float(usd["walletBalance"])) == 0 or int(float(usd["maintenanceMargin"])) == 0:
                        continue
                    risk_list[f"Bi{i + 1}U_{usd['asset']}"] = float(usd["maintenanceMargin"])/float(usd["marginBalance"])

                coinm = self.binanceClient.get_subaccount_futures_details(email=sub_account, futuresType = 2)
                coinm = coinm["deliveryAccountResp"]["assets"]
                for coin in coinm:
                    if int(float(coin["walletBalance"])) == 0 or int(float(coin["maintenanceMargin"])) == 0:
                        continue
                    risk_list[f"Bi{i + 1}C_{coin['asset']}"] = float(coin["maintenanceMargin"])/float(coin["marginBalance"])
        except:
            pass

        return risk_list