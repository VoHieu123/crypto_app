from okx import SubAccount, Account
import time, alarm, const, utils

class OKXHandler:
    def __init__(self, apiKey, secretKey, password):
        self.okx_subaccount_api = SubAccount.SubAccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.okx_account_api = Account.AccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.subaccount_list = []
        data = self.send_http_request(func=self.okx_subaccount_api.get_subaccount_list)
        for subaccount_data in data:
            self.subaccount_list.append(subaccount_data["subAcct"])

        self.subaccount_list = sorted(self.subaccount_list, key=lambda x: x[-1])

    # Todo: Later
    def get_usdm_open_positions(self, sub_account):
        pass

    def get_coinm_open_positions(self, sub_account):
        pass

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
                if retries_count < const.MAX_RETRIES:
                    alarm.activate(message=f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.", alarm=False)
                    utils.synchronize_time()
                    time.sleep(const.SLEEP_TIME)
                else:
                    alarm.activate(message=f"Binance error in {func.__name__}: {error}. Retries number: {retries_count}.", alarm=True)
                    exit()

    def get_account_status(self) -> bool:
        # Format: {"symbol_1": [risk_1, equity_1, withdrawable_1], "symbol_2": [risk_2, equity_2, withdrawable_2]}
        status_list = {}
        usd_margin_list = ["USDT", "USDC"]

        account_data = self.send_http_request(func=self.okx_account_api.get_account_balance)
        for asset in account_data[0]["details"]:
            if asset['ccy'] in usd_margin_list:
                status_list[f"OkMU_{asset['ccy']}"] = [asset["mgnRatio"], asset["eq"], asset["availBal"]]
            else:
                status_list[f"OkMC_{asset['ccy']}"] = [asset["mgnRatio"], asset["eq"], asset["availBal"]]

        for i, sub_acct in enumerate(self.subaccount_list):
            sub_data = self.send_http_request(func=self.okx_subaccount_api.get_account_balance, subAcct=sub_acct)
            for asset in sub_data[0]["details"]:
                if asset['ccy'] in usd_margin_list:
                    status_list[f"Ok{i + 1}U_{asset['ccy']}"] = [asset["mgnRatio"], asset["eq"], asset["availBal"]]
                else:
                    status_list[f"Ok{i + 1}C_{asset['ccy']}"] = [asset["mgnRatio"], asset["eq"],  asset["availBal"]]

        return status_list