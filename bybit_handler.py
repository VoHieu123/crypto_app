from pybit.unified_trading import HTTP
import const
import time, alarm

class BybitHandler:
    def __init__(self, apiKey, secretKey, sleepTime=3):
        self.session = HTTP(
            testnet=False,
            api_key=apiKey,
            api_secret=secretKey,
        )

        self.sleep_time = sleepTime

    @staticmethod
    def send_http_request(self, func, **kwargs):
        if func == self.session.get_risk:
            if kwargs.get('accountType') == None:
                raise Exception("Invalid arguments")
            # coin = kwargs.get('coin')
        elif func == self.session.get_coin_info:
            pass

        retriesCount = -1
        while True:
            retriesCount += 1
            try:
                data = func(**kwargs)
                if data.get("retCode") == 0:
                    return data["result"]
                else:
                    raise Exception(message=f"Received corrupted data: {data['msg']}. Length: {len(data['data'])}.")
            except Exception as error:
                alarm.activate(message=f"Bybit Error: {error}. Retries number: {retriesCount}")
                if retriesCount >= const.MAX_RETRIES:
                    break
                time.sleep(self.sleep_time)

    def get_risk(self) -> {}:
        risk_list = {}
        data = self.send_http_request(self=self, func=self.session.get_risk, accountType="UNIFIED")
        for item in data["list"]:
            if item["accountType"] == "UNIFIED":
                risk_list[f"ByMU_ALL"] = float(item["accountMMRate"])
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