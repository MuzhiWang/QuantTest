from Gateway import TuShare, JQData, Config
from Database.MongoDB import Client
from Common import DatetimeUtils, StringUtils
from Config import StockConfig
import pandas as pd

class StockProvider(object):

    __mongodb_client = None
    __jqdata_gw = None
    __tushare_gw = None

    def __init__(self):
        self.__mongodb_client = Client.Client()
        self.__jqdata_gw = JQData.JQData_GW()
        self.__tushare_gw = TuShare.TuShare_GW()

    def query_and_store_1min_stock(self, stock_id: str, start_date: str, end_date: str):
        days = DatetimeUtils.get_days_between_dates(start_date, end_date)
        counts = days * StockConfig.Constant.MINUTES_IN_DAY

        df = self.__tushare_gw.get_1min_stock_price(stock_id, start_date, end_date)
        df['date'] = pd.to_datetime(df['trade_time'])
        print(df)

        for group_name, df_group in df.groupby([df['date'].dt.date]):
            print("\n\n\n")
            print(group_name)
            print(df_group)
