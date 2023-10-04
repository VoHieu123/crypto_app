from pybit.unified_trading import HTTP
import const
import telegram_send
import time

class BybitHandler:

    def __init__(self, apiKey, secretKey, sleepTime=3):
        self.session = HTTP(
            testnet=False,
            api_key=apiKey,
            api_secret=secretKey,
        )

        self.sleep_time = sleepTime

    def get_risk_percentage(self) -> {}:
        risk_list = {}
        retriesCount = 0
        while True:
            retriesCount += 1
            try:
                data = self.session.get_wallet_balance(accountType="UNIFIED")
                if data.get("retCode") == 0 and len(data["result"]["list"]) > 0:
                    for item in data["result"]["list"]:
                        if item["accountType"] == "UNIFIED":
                            risk_list[f"ByMU_ALL"] = float(item["accountMMRate"])
                            return risk_list
                else:
                    raise Exception(message=f"Corrupted received data: {data['msg']}. Length: {len(data['data'])}.")
            except Exception as error:
                if retriesCount <= const.MAX_RETRIES:
                    message = [f"Bybit Error: {error}. Retries number: {retriesCount}"]
                    print(message[0])
                    time.sleep(self.sleep_time)
                    try:
                        telegram_send.send(messages=message)
                    except:
                        pass
                else:
                    print(error)
                    break

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

# byb = BybitHandler(apiKey=const.TA_BYB_API_KEY, secretKey=const.TA_BYB_SECRET_KEY)
# byb.get_risk_percentage()