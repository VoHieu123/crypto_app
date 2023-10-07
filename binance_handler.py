from binance import Client
import time, alarm, const

class BinanceHandler:
    def __init__(self, apiKey, secretKey, sleepTime=3):
        self.binance_client = Client(api_key=apiKey, api_secret=secretKey)
        self.sleep_time = sleepTime
        self.subaccount_list = []
        subaccount_data = self.send_http_request(self=self, func=self.binance_client.get_sub_account_list)
        for sub_account in subaccount_data["subAccounts"]:
            self.subaccount_list.append(sub_account["email"])

    @staticmethod
    def send_http_request(self, func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                return func(**kwargs)
            except Exception as error:
                alarm.activate(message=f"Binance error: {error}. Retries number: {retries_count}.")
                if retries_count >= const.MAX_RETRIES:
                    break
                time.sleep(self.sleep_time)

    def get_risk(self) -> {}:
        risk_list = {}
        mainAccountData = self.send_http_request(self=self, func=self.binance_client.futures_account)
        for asset in mainAccountData["assets"]:
            if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
                continue
            risk_list[f"BiMU_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

        mainAccountData = self.send_http_request(self=self, func=self.binance_client.futures_coin_account)
        for asset in mainAccountData["assets"]:
            if int(float(asset["walletBalance"])) == 0 or int(float(asset["maintMargin"])) == 0:
                continue
            risk_list[f"BiMC_{asset['asset']}"] = float(asset["maintMargin"])/float(asset["marginBalance"])

        for i, sub_account in enumerate(self.subaccount_list):
            usdm = self.send_http_request(self=self, func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=1)
            for usd in usdm["futureAccountResp"]["assets"]:
                if int(float(usd["walletBalance"])) == 0 or int(float(usd["maintenanceMargin"])) == 0:
                    continue
                risk_list[f"Bi{i + 1}U_{usd['asset']}"] = float(usd["maintenanceMargin"])/float(usd["marginBalance"])

            coinm = self.send_http_request(self=self, func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=2)
            for coin in coinm["deliveryAccountResp"]["assets"]:
                if int(float(coin["walletBalance"])) == 0 or int(float(coin["maintenanceMargin"])) == 0:
                    continue
                risk_list[f"Bi{i + 1}C_{coin['asset']}"] = float(coin["maintenanceMargin"])/float(coin["marginBalance"])

        return risk_list