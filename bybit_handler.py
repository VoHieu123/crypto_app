from pybit.unified_trading import HTTP
import const, time, alarm

class BybitHandler:
    def __init__(self, apiKey, secretKey, sleepTime=3):
        self.session = HTTP(
            testnet=False,
            api_key=apiKey,
            api_secret=secretKey,
        )

        self.sleep_time = sleepTime
        self.subaccount_list = []
        # Todo: Test connection?
        # Todo: Get subaccount list

    @staticmethod
    def send_http_request(self, func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                data = func(**kwargs)
                if data.get("retCode") == 0:
                    return data["result"]
                else:
                    raise Exception(message=f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                alarm.activate(message=f"Bybit error: {error}. Retries number: {retries_count}.")
                if retries_count >= const.MAX_RETRIES:
                    break
                time.sleep(self.sleep_time)

    def get_account_status(self) -> {}:
        risk_list = {}
        data = self.send_http_request(self=self, func=self.session.get_wallet_balance, accountType="UNIFIED")
        for item in data["list"]:
            if item["accountType"] == "UNIFIED":
                risk_list[f"ByMU_ALL"] = [float(item["accountMMRate"]), float(item["totalEquity"])]
                return risk_list

        return {}

    def transfer_money(amt) -> bool:
        # data = session.get_coin_info(coin="USDT")
        # if data["retCode"] == 0:
        #     data = data["result"]["rows"][0]
        #     for chain in data["chains"]:
        #         if chain["chainType"] == const.BYBIT_WITHDRAWAL_CHAIN_NAME:
        #             minFee = chain["withdrawFee"]
        #             break
        #     res = session.withdraw(feeType=1, amount=amt, coin="USDT", chain="ARBI", address=const.OKX_ADDRESS)
        return True