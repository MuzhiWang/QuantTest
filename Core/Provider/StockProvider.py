from Gateway import TuShare, JQData, Tdx
from Gateway import Config as gw_cfg
from Database.MongoDB import Client
from Common import DatetimeUtils, StringUtils
from Config import StockConfig
import pandas as pd

class StockProvider(object):

    DATE_INDEX = "date_index"

    __mongodb_client = None
    __jqdata_gw = None
    __tushare_gw = None
    __tdx_gw = None

    def __init__(self):
        self.__mongodb_client = Client.Client()
        self.__jqdata_gw = JQData.JQData_GW()
        self.__tushare_gw = TuShare.TuShare_GW()
        self.__tdx_gw = Tdx.TDX_GW()

    def query_and_store_1min_stock(self, data_source: StockConfig.StockDataSource, stock_id: str, start_date: str,
                                   end_date: str, force_upsert=False):
        date_index = gw_cfg.Constant.DATE_INDEX[data_source]
        if date_index is None:
            raise Exception("date index is not found")

        if data_source == StockConfig.StockDataSource.JQDATA:
            days = DatetimeUtils.get_days_between_dates(start_date, end_date)
            counts = days * StockConfig.Constant.MINUTES_IN_DAY
        elif data_source == StockConfig.StockDataSource.TUSHARE:
            df = self.__tushare_gw.get_1min_stock_price(stock_id, start_date, end_date)
            # csv_path = "./test111.csv"
            # df.to_csv(csv_path, index=False)
            # df = pd.read_csv(csv_path)
        elif data_source == StockConfig.StockDataSource.TDX:
            df = self.__tdx_gw.get_1min_bar("/Users/muzwang/gocode/src/github.com/QuantTest/Tests/LC1/sz000001.lc1")
        else:
            raise Exception(f"no data source matched for {data_source.name}")

        if df is None:
            return None

        df[self.DATE_INDEX] = pd.to_datetime(df[date_index]).dt.strftime(DatetimeUtils.DATE_FORMAT)
        print(df)

        stored_dates = self.__mongodb_client.get_stored_dates(data_source, StockConfig.StockDataType.DAILY,
                                                              stock_id) if not force_upsert else {}
        for date_index, df_group in df.groupby([df[self.DATE_INDEX]]):
            print(f"trying to store {date_index}")
            if date_index in stored_dates and stored_dates[date_index]:
                print(f"the data EXISTS for source {data_source.name} - stock {stock_id} - date {date_index} \n")
            else:
                try:
                    self.__mongodb_client.upsert_stock_price_df(data_source,
                                                                StockConfig.StockDataType.DAILY, stock_id, df_group,
                                                                date_index)
                    self.__mongodb_client.save_dates(data_source, StockConfig.StockDataType.DAILY, stock_id,
                                                     date_index)
                    print(f"SUCCEEDED to upsert data for source {data_source.name} - stock {stock_id} - date {date_index} \n")
                except Exception as e:
                    print(f"FAILED to upsert data for data for source {data_source.name} - stock {stock_id} - date {date_index}, with exception: {e} \n")


