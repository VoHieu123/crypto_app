from okx import SubAccount, Account
import time, alarm, const, utils
import pandas as pd

class OKXHandler:
    def __init__(self, model, apiKey, secretKey, password):
        self.model_ = model
        self.okx_subaccount_api = SubAccount.SubAccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.okx_account_api = Account.AccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.subaccount_list = []
        self.sub_api_list = []
        data = self.send_http_request(func=self.okx_subaccount_api.get_subaccount_list)
        for subaccount_data in data:
            self.subaccount_list.append(subaccount_data["subAcct"])
            # Todo: self.sub_api_list.append()

        self.subaccount_list = sorted(self.subaccount_list, key=lambda x: x[-1])

    def get_open_positions(self, sub_account=None):

        def handle_position(positions):
            long_pos_usdm, short_pos_usdm, long_pos_coinm, short_pos_coinm = 0, 0, 0, 0
            for position in positions:
                if "USDT" in position["instId"]:
                    coin = position["instId"].replace("-", "")
                    coin = coin.replace("SWAP", "")
                    price = self.model_.get_universal_mark_price(coin)
                    if position["pos"] > 0:
                        long_pos_usdm += position["notionalCcy"]*price
                    elif position["pos"] < 0:
                        short_pos_usdm += position["notionalCcy"]*price
                # else:
                #     if position["pos"] > 0:
                #         long_pos_coinm += position["notionalUsd"]
                #     else:
                #         short_pos_coinm += position["notionalUsd"]

            return long_pos_usdm, short_pos_usdm*(-1), long_pos_coinm, short_pos_coinm*(-1)

        positions = 0, 0, 0, 0
        if sub_account != None:
            if sub_account in self.subaccount_list:
                # Todo: later
                sub_account_index = self.subaccount_list.index(sub_account)
                sub_api = Account.AccountAPI(api_key=const.TA_OKX_API_KEY_SUB1, flag="0", debug=False,
                                            api_secret_key=const.TA_OKX_SECRET_KEY_SUB1,
                                            passphrase=const.TA_OKX_PASSPHRASE_SUB1)
                positions = self.send_http_request(func=sub_api.get_position_risk, instType="SWAP")
        else:
            positions = self.send_http_request(func=self.okx_account_api.get_position_risk, instType="SWAP")

        return handle_position(positions[0]["posData"])

    @staticmethod
    def send_http_request(func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                data = func(**kwargs)
                if data.get("code") == "0":
                    return utils.convert_to_float(data["data"])
                else:
                    raise Exception(message=f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                message = f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}."
                if retries_count < const.MAX_RETRIES:
                    print(message)
                    time.sleep(const.SLEEP_TIME)
                else:
                    alarm.activate(message=message)
                    exit()

    def get_account_status(self) -> bool:
        status_list = {}
        usd_margin_list = ["USDT", "USDC"]

        long_pos_usdm, short_pos_usdm, long_pos_coinm, short_pos_coinm = self.get_open_positions()

        account_data = self.send_http_request(func=self.okx_account_api.get_account_balance)
        for asset in account_data[0]["details"]:
            if asset['ccy'] in usd_margin_list:
                status_list[f"OkMU_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                       "long_pos": long_pos_usdm, "short_pos": short_pos_usdm}
            else:
                status_list[f"OkMC_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                       "long_pos": long_pos_coinm, "short_pos": short_pos_coinm}

        for i, sub_acct in enumerate(self.subaccount_list):
            sub_data = self.send_http_request(func=self.okx_subaccount_api.get_account_balance, subAcct=sub_acct)
            for asset in sub_data[0]["details"]:
                long_pos_usdm, short_pos_usdm, long_pos_coinm, short_pos_coinm = self.get_open_positions(sub_acct)
                if asset['ccy'] in usd_margin_list:
                    status_list[f"Ok{i + 1}U_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                                 "long_pos": long_pos_usdm, "short_pos": short_pos_usdm}
                else:
                    status_list[f"Ok{i + 1}C_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                                 "long_pos": long_pos_coinm, "short_pos": short_pos_coinm}

        return status_list