from okx import SubAccount, Account
import const

okx_subaccount_api = SubAccount.SubAccountAPI(const.OKX_API_KEY, const.OKX_SECRET_KEY, const.OKX_PASSPHRASE, flag="0", debug=False)
okx_account_api = Account.AccountAPI(const.OKX_API_KEY, const.OKX_SECRET_KEY, const.OKX_PASSPHRASE, flag="0", debug=False)

def get_risk_percentage():
    risk_list = {}
    subaccounts = ["evan196511", "evan196512", "evan196513"]
    usdMarginList = ["USDT", "USDC"]

    accountData = okx_account_api.get_account_balance()
    accountData = accountData["data"][0]["details"]

    for asset in accountData:
        if asset['ccy'] in usdMarginList:
            risk_list[f"OkMU_{asset['ccy']}"] = float(asset["mgnRatio"])
        else:
            risk_list[f"OkMC_{asset['ccy']}"] = float(asset["mgnRatio"])

    for i, sub_acct in enumerate(subaccounts):
        sub_data = okx_subaccount_api.get_account_balance(subAcct=sub_acct)
        sub_data = sub_data["data"][0]["details"]

        for asset in sub_data:
            if asset['ccy'] in usdMarginList:
                risk_list[f"Ok{i + 1}U_{asset['ccy']}"] = float(asset["mgnRatio"])
            else:
                risk_list[f"Ok{i + 1}C_{asset['ccy']}"] = float(asset["mgnRatio"])

    return risk_list