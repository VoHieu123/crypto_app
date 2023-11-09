from binance import Client
import time, const, utils
import pandas as pd

class BinanceHandler:
    def __init__(self, model, apiKey, secretKey):
        self.model_ = model
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

    def get_positions_pnl(self, sub_account_index=None):
        pnls = pd.DataFrame()
        if sub_account_index:
            for i, sub_account in enumerate(self.subaccount_list):
                if i + 1 == sub_account_index:
                    pnls = self.send_http_request(func=self.binance_client.get_subaccount_futures_positionrisk, email=sub_account, futuresType=1)
                    pnls = pd.DataFrame(pnls["futurePositionRiskVOS"])
                    pnls = pnls[pnls["positionAmount"] != 0]
                    break
        else:
            pnls = self.send_http_request(func=self.binance_client.futures_account)
            pnls = pd.DataFrame(pnls["positions"])
            pnls = pnls[pnls["positionAmt"] != 0]

        if not pnls.empty:
            pnls = pnls[["symbol", "unrealizedProfit"]]
            pnls.sort_values(by='symbol', inplace=True, ignore_index=True, ascending=True)
            pnls.rename(columns = {"unrealizedProfit" : "uPnLs_" + (f"sub{sub_account_index}" if sub_account_index else "main")}, inplace = True)
            pnls.rename(columns = {"symbol" : "Binance_" + (f"sub{sub_account_index}" if sub_account_index else "main")}, inplace = True)
        else:
            pnls = pd.DataFrame()

        return pnls

    @staticmethod
    def send_http_request(func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                return utils.convert_to_float(func(**kwargs))
            except Exception as error:
                utils.resynch()
                if retries_count < const.MAX_RETRIES:
                    print(f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.")
                    time.sleep(const.SLEEP_TIME)
                else:
                    raise Exception(f"Error: {error}.")

    def get_account_status(self) -> {}:
        status_list = {}
        mainAccountData = self.send_http_request(func=self.binance_client.futures_account)
        usd = pd.DataFrame(mainAccountData["positions"])
        long_pos = usd[usd["positionAmt"] > 0]["notional"].sum()
        short_pos = usd[usd["positionAmt"] < 0]["notional"].sum()

        for asset in mainAccountData["assets"]:
            if (asset["maintMargin"] != 0 or asset["maxWithdrawAmount"] != 0) and asset['asset'] == "USDT":
                pnls = self.get_positions_pnl()
                pnls = pnls["uPnLs_main"].sum() if not pnls.empty else 0
                status_list[f"BiMU_USDT"] = {"risk": (asset["maintMargin"]/asset["marginBalance"]) if asset["marginBalance"] != 0 else 0,
                                                         "equity": asset["marginBalance"], "withdrawable": asset["maxWithdrawAmount"], "pnls": pnls,
                                                         "long_pos": long_pos, "short_pos": short_pos, "initial": asset["initialMargin"], "maintenance": asset["maintMargin"]}

        for i, sub_account in enumerate(self.subaccount_list):
            usdm = self.send_http_request(func=self.binance_client.get_subaccount_futures_details, email=sub_account, futuresType=1)
            for usd in usdm["futureAccountResp"]["assets"]:
                if usd["asset"] == "USDT":
                    pnls = self.get_positions_pnl(sub_account_index=i + 1)
                    pnls = pnls[f"uPnLs_sub{i + 1}"].sum() if not pnls.empty else 0
                    long_pos, short_pos = self.get_sub_usdm_open_positions(sub_account)
                    if usd["maintenanceMargin"] != 0 or usd["maxWithdrawAmount"] != 0:
                        status_list[f"Bi{i + 1}U_USDT"] = {"risk": (usd["maintenanceMargin"]/usd["marginBalance"]) if usd["marginBalance"] != 0 else 0,
                                                                    "equity": usd["marginBalance"], "withdrawable": usd["maxWithdrawAmount"],
                                                                    "long_pos": long_pos, "short_pos": short_pos, "initial": usd["initialMargin"],
                                                                    "maintenance": usd["maintenanceMargin"], "pnls": pnls}

        return status_list

    def get_universal_mark_prices(self):
        usdm = self.send_http_request(func=self.binance_client.futures_mark_price)
        usdm = pd.DataFrame(usdm)
        usdm = usdm[["markPrice", "symbol"]]
        return usdm

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