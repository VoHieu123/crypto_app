from pybit.unified_trading import HTTP
import const, time, utils
import pandas as pd

class BybitHandler:
    def __init__(self, model, apiKey, secretKey):
        self.model_ = model
        self.session = HTTP(
            testnet=False,
            api_key=apiKey,
            api_secret=secretKey,
        )
        self.account_uid_dict = {}
        subaccount_data = self.send_http_request(func=self.session.get_sub_uid)
        main_uid = self.send_http_request(func=self.session.get_uid_wallet_type)
        self.account_uid_dict["Main"] = int(main_uid["accounts"][0]["uid"])
        if subaccount_data['subMemberIds'] != subaccount_data['transferableSubMemberIds']:
            exit("Bybit error: subMemberIds and transferableSubMemberIds are different.")
        for i, uid in enumerate(subaccount_data['transferableSubMemberIds']):
            self.account_uid_dict[f"Sub{i + 1}"] = int(uid)

    def get_open_position(self):
        cursor = None
        data = pd.DataFrame()
        while True:
            currentData = self.send_http_request(func=self.session.get_positions,
                                          category="linear", settleCoin="USDT",
                                          limit=200, cursor=cursor)
            cursor = currentData["nextPageCursor"]
            if len(currentData["list"]) == 0:
                break
            currentData = pd.DataFrame(currentData["list"])
            currentData = currentData[["symbol", "markPrice", "side", "size"]]
            data = pd.concat([data, currentData])
        long_pos, short_pos = 0, 0
        for _, row in data.iterrows():
            coin = row["symbol"]
            price = self.model_.get_universal_mark_price(coin)
            if row["side"] == "Buy":
                long_pos += row["size"]*price
            elif row["side"] == "Sell":
                short_pos += row["size"]*price

        return long_pos, short_pos*(-1)

    @staticmethod
    def send_http_request(func, **kwargs):
        retries_count = -1
        while True:
            retries_count += 1
            try:
                data = func(**kwargs)
                if data.get("retCode") == 0:
                    return utils.convert_to_float(data["result"])
                else:
                    raise Exception(f"Received corrupted data: {data['msg']}.")
            except Exception as error:
                utils.resynch()
                if retries_count < const.MAX_RETRIES:
                    # print(f"Bybit error in {func.__name__}: {error}. Retries number: {retries_count}.")
                    time.sleep(const.SLEEP_TIME)
                else:
                    raise Exception(f"Error: {error}.")

    # Todo: Haven't done it for subaccount
    def get_account_status(self) -> {}:
        status_list = {}
        mmr, equity, withdrawable, long_pos, short_pos = None, None, None, None, None
        data = self.send_http_request(func=self.session.get_wallet_balance, accountType="UNIFIED")
        for item in data["list"]:
            if item["accountType"] == "UNIFIED":
                mmr = item["accountMMRate"]
                equity = item["totalEquity"]
                im = item["totalInitialMargin"]
                mm = item["totalMaintenanceMargin"]
                break

        # Account asset should always be moved to Unified Trading Account before hand
        data = self.send_http_request(func=self.session.get_coin_balance,
                                      accountType="UNIFIED", coin="USDT",
                                      withTransferSafeAmount=1)

        withdrawable = data["balance"]["transferSafeAmount"]

        long_pos, short_pos = self.get_open_position()

        # Todo: Currently assuming USDT is the only currency
        if all(item is not None for item in [mmr, equity, withdrawable, long_pos, short_pos]):
            status_list[f"ByMU_USDT"] = {"risk": mmr, "equity": equity, "withdrawable": withdrawable,
                                         "long_pos": long_pos, "short_pos": short_pos,
                                         "initial": im, "maintenance": mm}

        return status_list

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