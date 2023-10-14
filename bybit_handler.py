from pybit.unified_trading import HTTP
import const, time, alarm
import utils

class BybitHandler:
    def __init__(self, apiKey, secretKey, sleepTime=3):
        self.session = HTTP(
            testnet=False,
            api_key=apiKey,
            api_secret=secretKey,
        )

        self.sleep_time = sleepTime
        self.account_uid_dict = {}
        subaccount_data = self.send_http_request(self=self, func=self.session.get_sub_uid)
        main_uid = self.send_http_request(self=self, func=self.session.get_uid_wallet_type)
        self.account_uid_dict["Main"] = int(main_uid["accounts"][0]["uid"])
        if subaccount_data['subMemberIds'] != subaccount_data['transferableSubMemberIds']:
            exit("Bybit error: subMemberIds and transferableSubMemberIds are different.")
        for i, uid in enumerate(subaccount_data['transferableSubMemberIds']):
            self.account_uid_dict[f"Sub{i + 1}"] = int(uid)

    @staticmethod
    def convert_to_float(self, data):
        if isinstance(data, dict):
            return {key: self.convert_to_float(self=self, data=value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.convert_to_float(self=self, data=item) for item in data]
        elif isinstance(data, str):
            try:
                return 0 if data == "" else float(data)
            except ValueError:
                return data
        else:
            return data

    @staticmethod
    def send_http_request(self, func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                data = func(**kwargs)
                if data.get("retCode") == 0:
                    return self.convert_to_float(self=self, data=data["result"])
                else:
                    raise Exception(message=f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                if retries_count >= const.MAX_RETRIES:
                    alarm.activate(message=f"Bybit error in {func.__name__}: {error}. Retries number: {retries_count}.", alarm=False)
                    utils.synchronize_time()
                    time.sleep(self.sleep_time)
                    break
                else:
                    alarm.activate(message=f"Bybit error in {func.__name__}: {error}. Retries number: {retries_count}.", alarm=True)
                    exit()

    def get_account_status(self) -> {}:
        # Format: {"symbol": [risk, equity, withdrawable]}
        risk_list = {}
        mmr, equity, withdrawable = None, None, None
        data = self.send_http_request(self=self, func=self.session.get_wallet_balance, accountType="UNIFIED")
        for item in data["list"]:
            mmr = item["accountMMRate"]
            equity = item["totalEquity"]

        # Account asset should always be moved to Unified Trading Account before hand
        data = self.send_http_request(self=self, func=self.session.get_coin_balance,
                                      accountType="UNIFIED", coin="USDT",
                                      withTransferSafeAmount=1)

        withdrawable = data["balance"]["transferSafeAmount"]

        if all(item is not None for item in [mmr, equity, withdrawable]):
            risk_list[f"ByMU_USDT"] = [mmr, equity, withdrawable]

        return risk_list

    def transfer_money_internal(amt, accountFrom, accountTo):
        pass

    def transfer_money_global(amt) -> bool:
        # data = session.get_coin_info(coin="USDT")
        # if data["retCode"] == 0:
        #     data = data["result"]["rows"][0]
        #     for chain in data["chains"]:
        #         if chain["chainType"] == const.BYBIT_WITHDRAWAL_CHAIN_NAME:
        #             minFee = chain["withdrawFee"]
        #             break
        #     res = session.withdraw(feeType=1, amount=amt, coin="USDT", chain="ARBI", address=const.OKX_ADDRESS)
        return True

## Transfer between different account types under the same uid
# self.session.create_internal_transfer(
#         transferId=self.generate_uuid(),
#         coin="USDT",
#         amount="5",
#         fromAccountType="UNIFIED",
#         toAccountType="FUND",
#     )
## Transfer between differnt accounts types under different uids
# self.session.create_universal_transfer(
#         transferId=self.generate_uuid(),
#         coin="USDT",
#         amount="5",
#         fromMemberId=106785119,
#         toMemberId=109067714,
#         fromAccountType="FUND",
#         toAccountType="FUND",
#     )