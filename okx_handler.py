from okx import SubAccount, Account

class OKXHandler:
    def __init__(self, apiKey, secretKey, password):
        self.okx_subaccount_api = SubAccount.SubAccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)
        self.okx_account_api = Account.AccountAPI(api_key=apiKey, api_secret_key=secretKey, passphrase=password, flag="0", debug=False)

    def get_risk_percentage(self) -> bool:
        risk_list = {}
        subaccounts = ["evan196511", "evan196512", "evan196513"]
        usdMarginList = ["USDT", "USDC"]

        # Todo: Check
        try:
            accountData = self.okx_account_api.get_account_balance()
            if accountData.get("code") == "0":
                accountData = accountData.get("data")[0]["details"]

                # Todo: Do not assump len(details[] > 0)

                for asset in accountData:
                    if asset['ccy'] in usdMarginList:
                        risk_list[f"OkMU_{asset['ccy']}"] = float(asset["mgnRatio"])
                    else:
                        risk_list[f"OkMC_{asset['ccy']}"] = float(asset["mgnRatio"])

                for i, sub_acct in enumerate(subaccounts):
                    sub_data = self.okx_subaccount_api.get_account_balance(subAcct=sub_acct)
                    sub_data = sub_data["data"][0]["details"]

                    for asset in sub_data:
                        if asset['ccy'] in usdMarginList:
                            risk_list[f"Ok{i + 1}U_{asset['ccy']}"] = float(asset["mgnRatio"])
                        else:
                            risk_list[f"Ok{i + 1}C_{asset['ccy']}"] = float(asset["mgnRatio"])
            else:
                raise Exception("?")
        except Exception as error:
            # Todo
            pass

        return risk_list