from okx import SubAccount, Account
import time, const, utils

class OKXHandler:
    def __init__(self, model, apiKey, secretKey, password):
        self.model_ = model
        self.okx_subaccount_api = SubAccount.SubAccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.okx_account_api = Account.AccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)

        self.subaccount_dict = {}
        subaccount_list = []
        data = self.send_http_request(func=self.okx_subaccount_api.get_subaccount_list)
        for subaccount_data in data:
            subaccount_list.append(subaccount_data["subAcct"])
        subaccount_list = sorted(subaccount_list, key=lambda x: x[-1])

        for i, subaccount in enumerate(subaccount_list):
            try:
                api_key = getattr(const, f"{self.model_.identity}_OKX_API_KEY_SUB{i + 1}")
                secret_key = getattr(const, f"{self.model_.identity}_OKX_SECRET_KEY_SUB{i + 1}")
                password = getattr(const, f"{self.model_.identity}_OKX_PASSPHRASE_SUB{i + 1}")
                self.subaccount_dict[subaccount] = Account.AccountAPI(api_key=api_key,api_secret_key=secret_key,
                                                passphrase=password, flag="0", debug=False)
            except:
                pass

    def get_margins(self, ccy="USDT", sub_account=None):
        im, mm = 0, 0
        if sub_account:
            margin_data = self.send_http_request(func=self.subaccount_dict[sub_account].get_positions, instType="SWAP")
        else:
            margin_data = self.send_http_request(func=self.okx_account_api.get_positions, instType="SWAP")
        for margin in margin_data:
            if margin["ccy"] == ccy and margin["mgnMode"] == "cross":
                im += margin["imr"]
                mm += margin["mmr"]
        return im, mm

    def get_long_short(self, ccy="USDT", sub_account=None):
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

        if sub_account in self.subaccount_dict:
            positions = self.send_http_request(func=self.subaccount_dict[sub_account].get_position_risk)
        else:
            positions = self.send_http_request(func=self.okx_account_api.get_position_risk)

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
                    raise Exception(f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                utils.resynch()
                if retries_count < const.MAX_RETRIES:
                    # print(f"OKX error in {func.__name__}: {error}. Retries number: {retries_count}.")
                    time.sleep(const.SLEEP_TIME)
                else:
                    raise Exception(f"Error: {error}.")

    def get_account_status(self) -> {}:
        status_list = {}
        usd_margin_list = ["USDT", "USDC"]

        long_pos_usdm, short_pos_usdm, long_pos_coinm, short_pos_coinm = self.get_long_short()

        account_data = self.send_http_request(func=self.okx_account_api.get_account_balance)
        for asset in account_data[0]["details"]:
            if asset['ccy'] in usd_margin_list:
                im, mm = self.get_margins(asset['ccy'])
                status_list[f"OkMU_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                       "long_pos": long_pos_usdm, "short_pos": short_pos_usdm,
                                                       "initial": im, "maintenance": mm}
            else:
                status_list[f"OkMC_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"], "withdrawable": asset["availBal"],
                                                       "long_pos": long_pos_coinm, "short_pos": short_pos_coinm,
                                                       "initial": 0, "maintenance": 0}

        for i, sub_acct in enumerate(self.subaccount_dict):
            sub_data = self.send_http_request(func=self.okx_subaccount_api.get_account_balance, subAcct=sub_acct)
            long_pos_usdm, short_pos_usdm, long_pos_coinm, short_pos_coinm = self.get_long_short(sub_account=sub_acct)
            for asset in sub_data[0]["details"]:
                im, mm = self.get_margins(ccy=asset['ccy'], sub_account=sub_acct)
                if asset['ccy'] in usd_margin_list:
                    status_list[f"Ok{i + 1}U_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"],
                                                                 "withdrawable": asset["availBal"],
                                                                 "long_pos": long_pos_usdm, "short_pos": short_pos_usdm,
                                                                 "initial": im, "maintenance": mm}
                else:
                    status_list[f"Ok{i + 1}C_{asset['ccy']}"] = {"risk": asset["mgnRatio"], "equity": asset["eq"],
                                                                 "withdrawable": asset["availBal"],
                                                                 "long_pos": long_pos_coinm, "short_pos": short_pos_coinm,
                                                                 "initial": im, "maintenance": mm}

        return status_list