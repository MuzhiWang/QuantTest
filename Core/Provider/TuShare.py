import tushare as ts

class TuShare(object):
    __token = "2fe3395cd410fb8ef0c467b5f5c5e871a69050f7d1ba434299d7ceab"
    __stock_id_suffix = ".sz"

    def __init__(self):
        ts.set_token(self.__token)

    def get_1min_stock_price(self, stock_id, start_date, end_date):
        stock_id = stock_id + self.__stock_id_suffix
        return ts.pro_bar(ts_code=stock_id, start_date=start_date, end_date=end_date, freq='1min')