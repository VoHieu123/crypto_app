from okx import SubAccount, Account
import time, alarm, const

class OKXHandler:
    def __init__(self, apiKey, secretKey, password, sleepTime=3):
        self.okx_subaccount_api = SubAccount.SubAccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.okx_account_api = Account.AccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.sleep_time = sleepTime
        self.subaccount_list = []
        data = self.send_http_request(self=self, func=self.okx_subaccount_api.get_subaccount_list)
        for subaccount_data in data:
            self.subaccount_list.append(subaccount_data["subAcct"])

    @staticmethod
    def send_http_request(self, func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                data = func(**kwargs)
                if data.get("code") == "0":
                    return data["data"]
                else:
                    raise Exception(message=f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                alarm.activate(message=f"OKX error: {error}. Retries number: {retries_count}.")
                if retries_count >= const.MAX_RETRIES:
                    break
                time.sleep(self.sleep_time)

    def get_risk(self) -> bool:
        risk_list = {}
        usd_margin_list = ["USDT", "USDC"]

        account_data = self.send_http_request(self=self, func=self.okx_account_api.get_account_balance)
        for asset in account_data[0]["details"]:
            if asset['ccy'] in usd_margin_list:
                risk_list[f"OkMU_{asset['ccy']}"] = float(asset["mgnRatio"])
            else:
                risk_list[f"OkMC_{asset['ccy']}"] = float(asset["mgnRatio"])

        for i, sub_acct in enumerate(self.subaccount_list):
            sub_data = self.send_http_request(self=self, func=self.okx_subaccount_api.get_account_balance, subAcct=sub_acct)
            for asset in sub_data[0]["details"]:
                if asset['ccy'] in usd_margin_list:
                    risk_list[f"Ok{i + 1}U_{asset['ccy']}"] = float(asset["mgnRatio"])
                else:
                    risk_list[f"Ok{i + 1}C_{asset['ccy']}"] = float(asset["mgnRatio"])

        return risk_list