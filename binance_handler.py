from binance import Client
import time, alarm, const, utils
import pandas as pd

class BinanceHandler:
    def __init__(self, apiKey, secretKey):
        self.binance_client = Client(api_key=apiKey, api_secret=secretKey)
        self.subaccount_list = []
        subaccount_data = self.send_http_request(func=self.binance_client.get_sub_account_list)

        # Todo: Subaccount naming convention and sorting (also for Bybit)
        for sub_account in subaccount_data["subAccounts"]:
            self.subaccount_list.append(sub_account["email"])

    def get_sub_usdm_open_positions(self, sub_account):
        long_pos, short_pos = 0, 0
        usd = self.send_http_request(func=self.binance_client.get_subaccount_futures_positionrisk, email=sub_account, futuresType=1)
        usd = pd.DataFrame(usd["futurePositionRiskVOS"])
        usd = usd[usd["positionAmount"] != 0]
        if not usd.empty:
            usd = usd[["positionAmount", "markPrice"]]
            usd_long = usd[usd["positionAmount"] > 0]
            usd_short = usd[usd["positionAmount"] < 0]
            long_pos = (usd_long["positionAmount"]*usd_long["markPrice"]).sum()
            short_pos = (usd_short["positionAmount"]*usd_short["markPrice"]).sum()

        return long_pos, short_pos

    def get_sub_coinm_open_positions(self, sub_account):
        long_pos, short_pos = 0, 0
        coin = self.send_http_request(func=self.binance_client.get_subaccount_futures_positionrisk, email=sub_account, futuresType=2)
        coin = pd.DataFrame(coin["deliveryPositionRiskVOS"])
        coin = coin[coin["positionAmount"] != 0]
        if not coin.empty:
            coin = coin[["positionAmount", "markPrice"]]
            coin_long = coin[coin["positionAmount"] > 0]
            coin_short = coin[coin["positionAmount"] < 0]
            long_pos = (coin_long["positionAmount"]*coin_long["markPrice"]).sum()
            short_pos = (coin_short["positionAmount"]*coin_short["markPrice"]).sum()

        return long_pos, short_pos

    @staticmethod
    def send_http_request(func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                return utils.convert_to_float(func(**kwargs))
            except Exception as error:
                if retries_count < const.MAX_RETRIES:
                    alarm.activate(message=f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.", alarm=False)
                    time.sleep(const.SLEEP_TIME)
                else:
                    alarm.activate(message=f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.")
                    exit()

    def get_account_status(self) -> {}:
        status_list = {}
        mainAccountData = self.send_http_request(func=self.binance_client.futures_account)
        long_pos, short_pos = 0, 0
        usd = pd.DataFrame(mainAccountData["positions"])
        long_pos = usd[usd["positionAmt"] > 0]["notional"].sum()
        short_pos = usd[usd["positionAmt"] < 0]["notional"].sum()

        for asset in mainAccountData["assets"]:
            if asset["maintMargin"] != 0 or asset["maxWithdrawAmount"] != 0:
                status_list[f"BiMU_{asset['asset']}"] = {"risk": (asset["maintMargin"]/asset["marginBalance"]) if asset["marginBalance"] != 0 else 0,
                                                         "equity": asset["marginBalance"], "withdrawable": asset["maxWithdrawAmount"],
                                                         "long_pos": long_pos, "short_pos": short_pos}

        mainAccountData = self.send_http_request(func=self.binance_client.futures_coin_account)
        long_pos, short_pos = 0, 0
        coin = pd.DataFrame(mainAccountData["positions"])
        long_pos = coin[coin["positionAmt"] > 0]["notionalValue"].sum()
        short_pos = coin[coin["positionAmt"] < 0]["notionalValue"].sum()
        for asset in mainAccountData["assets"]:
            if asset["maintMargin"] != 0 or asset["maxWithdrawAmount"] != 0:
                status_list[f"BiMC_{asset['asset']}"] = {"risk": (asset["maintMargin"]/asset["marginBalance"]) if asset["marginBalance"] != 0 else 0,
                                                         "equity": asset["marginBalance"], "withdrawable": asset["maxWithdrawAmount"],
                                                         "long_pos": long_pos, "short_pos": short_pos}

        for i, sub_account in enumerate(self.subaccount_list):
            usdm = self.send_http_request(func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=1)
            for usd in usdm["futureAccountResp"]["assets"]:
                if usd["asset"] == "USDT":
                    long_pos, short_pos = self.get_sub_usdm_open_positions(sub_account)
                else:
                    long_pos, short_pos = 0, 0
                if usd["maintenanceMargin"] != 0 or usd["maxWithdrawAmount"] != 0:
                    status_list[f"Bi{i + 1}U_{usd['asset']}"] = {"risk": (usd["maintenanceMargin"]/usd["marginBalance"]) if usd["marginBalance"] != 0 else 0,
                                                                 "equity": usd["marginBalance"], "withdrawable": usd["maxWithdrawAmount"],
                                                                 "long_pos": long_pos, "short_pos": short_pos}

            long_pos, short_pos = self.get_sub_coinm_open_positions(sub_account)
            coinm = self.send_http_request(func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=2)
            for coin in coinm["deliveryAccountResp"]["assets"]:
                if coin["maintenanceMargin"] != 0 or coin["maxWithdrawAmount"] != 0:
                    status_list[f"Bi{i + 1}C_{coin['asset']}"] = {"risk": (coin["maintenanceMargin"]/coin["marginBalance"]) if coin["marginBalance"] != 0 else 0,
                                                                 "equity": coin["marginBalance"], "withdrawable": coin["maxWithdrawAmount"],
                                                                 "long_pos": long_pos, "short_pos": short_pos}

        return status_list

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