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
    def convert_to_float(self, data):
        if isinstance(data, dict):
            return {key: self.convert_to_float(self=self, data=value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.convert_to_float(self=self, data=item) for item in data]
        elif isinstance(data, str):
            try:
                return 0 if data == "" else float(data)
            except ValueError:
                return data
        else:
            return data

    @staticmethod
    def send_http_request(self, func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                return self.convert_to_float(self=self, data=func(**kwargs))
            except Exception as error:
                alarm.activate(message=f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.")
                if retries_count >= const.MAX_RETRIES:
                    break
                time.sleep(self.sleep_time)

    def get_account_status(self) -> {}:
        # Format: {"symbol_1": [risk_1, equity_1, withdrawable_1], "symbol_2": [risk_2, equity_2, withdrawable_2]}
        risk_list = {}
        mainAccountData = self.send_http_request(self=self, func=self.binance_client.futures_account)
        for asset in mainAccountData["assets"]:
            # Todo: Consider also the balance that doesn't have open position
            # Todo: Get the available balance
            if int(asset["walletBalance"]) == 0 or int(asset["maintMargin"]) == 0:
                continue
            risk_list[f"BiMU_{asset['asset']}"] = [asset["maintMargin"]/asset["marginBalance"], asset["marginBalance"], 0]

        mainAccountData = self.send_http_request(self=self, func=self.binance_client.futures_coin_account)
        for asset in mainAccountData["assets"]:
            if int(asset["walletBalance"]) == 0 or int(asset["maintMargin"]) == 0:
                continue
            risk_list[f"BiMC_{asset['asset']}"] = [asset["maintMargin"]/asset["marginBalance"], asset["marginBalance"], 0]

        for i, sub_account in enumerate(self.subaccount_list):
            usdm = self.send_http_request(self=self, func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=1)
            for usd in usdm["futureAccountResp"]["assets"]:
                if int(usd["walletBalance"]) == 0 or int(usd["maintenanceMargin"]) == 0:
                    continue
                risk_list[f"Bi{i + 1}U_{usd['asset']}"] = [usd["maintenanceMargin"]/usd["marginBalance"], usd["marginBalance"], 0]

            coinm = self.send_http_request(self=self, func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=2)
            for coin in coinm["deliveryAccountResp"]["assets"]:
                if int(coin["walletBalance"]) == 0 or int(coin["maintenanceMargin"]) == 0:
                    continue
                risk_list[f"Bi{i + 1}C_{coin['asset']}"] = [coin["maintenanceMargin"]/coin["marginBalance"], coin["marginBalance"], 0]

        return risk_list

    def transfer_money(self, to, amount, subAccount=None):
        # coins_data = self.binance_client.get_all_coins_info()
        # for coin_data in coins_data:
        #     if coin_data["coin"] == "USDT":
        #         available = coin_data["free"]
        #         for network in coin_data["networkList"]:
        #             if network['network'] == "BSC":
        #                 pass
        # # self.binance_client.withdraw(coin="USDT", network="BSC", amount=amount, walletType=0,
        # #                              address="0xba1e35b0f3392af3b423409876d0773c9fc3ed36")
        # if to == "Bybit":
        #     pass
        # elif to == "OKX":
        #     pass
        pass


# handler = BinanceHandler(apiKey="P9Z0jtiqSvr9cKMnsgHmjpBNpOZAaoAs7O5uVu0ScscQHReq9fMxsb1gTxtm2AsY", secretKey="bOVuS18DGDXlHpw94EwqnV2cH6EDC8v3v96LykSFLzUpsLRXHpWmhgrEQvBWFGzy")
# handler.transfer_money(to="Bybit", amount=4488.71)