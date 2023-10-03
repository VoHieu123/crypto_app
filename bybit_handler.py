from pybit.unified_trading import HTTP
import const
import telegram_send
import time

class BybitHandler:

    def __init__(self, sleepTime):
        self.session = HTTP(
            testnet=False,
            api_key=const.BYBIT_API_KEY,
            api_secret=const.BYBIT_SECRET_KEY,
        )

        self.sleep_time = sleepTime
        self.risk = 0
        self.marginBalance = 0
        self.availableAmount = 0

    def update_account_balance(self) -> bool:
        retriesCount = 0
        while True:
            retriesCount += 1
            try:
                data = self.session.get_wallet_balance(accountType="UNIFIED")
                if data.get("retCode") == 0 and len(data["result"]["list"]) > 0:
                    for item in data["result"]["list"]:
                        if item["accountType"] == "UNIFIED":
                            self.risk = float(item["accountMMRate"])
                            self.smarginBalance = float(item["totalMarginBalance"])
                            for coin in item["coin"]:
                                if coin["coin"] == "USDT":
                                    self.availableAmount = float(coin["availableToWithdraw"])
                                    return True
                else:
                    raise Exception(message=f"Corrupted received data: {data['msg']}. Length: {len(data['data'])}.")
            except Exception as error:
                if retriesCount <= const.MAX_RETRIES:
                    message = [f"Bybit Error: {error}. Retries number: {retriesCount}"]
                    print(message[0])
                    time.sleep(self.sleepTime)
                    try:
                        telegram_send.send(messages=message)
                    except:
                        pass
                else:
                    print(error)
                    break

        return False

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