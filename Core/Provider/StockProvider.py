from Gateway import TuShare, JQData, Tdx
from Gateway import Config as gw_cfg
from Database.MongoDB import Client
from Common import DatetimeUtils, StringUtils, FileUtils
from Config import StockConfig
import pandas as pd
from .ConfigProvider import ConfigProvider
import re
import Gateway.Config as cfg


class StockProvider(object):
    DATE_INDEX = "date_index"

    __mongodb_client = None
    __jqdata_gw = None
    __tushare_gw = None
    __tdx_gw = None
    __config_provider = None

    def __init__(self):
        self.__mongodb_client = Client.Client()
        self.__jqdata_gw = JQData.JQData_GW()
        self.__tushare_gw = TuShare.TuShare_GW()
        self.__tdx_gw = Tdx.TDX_GW()
        self.__config_provider = ConfigProvider()

    def query_and_store_1min_stock(self, data_source: StockConfig.StockDataSource, stock_id: str, start_date: str,
                                   end_date: str, force_upsert=False):
        date_index = gw_cfg.Constant.DATE_INDEX[data_source]
        if date_index is None:
            raise Exception("date index is not found")

        df = None
        if data_source == StockConfig.StockDataSource.JQDATA:
            days = DatetimeUtils.get_days_between_dates(start_date, end_date)
            counts = days * StockConfig.Constant.MINUTES_IN_DAY
            raise Exception(f"JQDATA 's source data unimplemented")
        elif data_source == StockConfig.StockDataSource.TUSHARE:
            df = self.__tushare_gw.get_1min_stock_price(stock_id, start_date, end_date)
            # csv_path = "./test111.csv"
            # df.to_csv(csv_path, index=False)
            # df = pd.read_csv(csv_path)
        elif data_source == StockConfig.StockDataSource.TDX:
            raise Exception(f"tdx 's source data is in local. Please call local api")
        else:
            raise Exception(f"no data source matched for {data_source.name}")

        if df is None:
            return None

        self.__store_stock_df_data(data_source, df, stock_id, force_upsert)
        return df

    def get_and_store_local_1min_stock(
            self, data_source: StockConfig.StockDataSource, stock_id: str = None, force_upsert=False):
        if data_source is not StockConfig.StockDataSource.TDX:
            raise Exception("only support for TDX in local")

        if stock_id is not None:
            raise Exception("unimplemented")
        tdx_dir = self.__config_provider.get_tdx_directory_path()
        for exchange, path in tdx_dir.items():
            print(f"start to get and store local 1min stock data for exchange {exchange} ...")
            self.__get_local_files_and_store_stock(
                StockConfig.StockDataSource.TDX, FileUtils.convert_file_path_based_on_system(path), force_upsert)

    def get_stock_1min_df(self, data_source: StockConfig.StockDataSource, stock_id: str,
                          start_date: str, end_date: str):
        if data_source == StockConfig.StockDataSource.TDX:
            df = self.__mongodb_client.get_stock_price_df(data_source, StockConfig.StockDataType.DAILY,
                                                 stock_id, start_date, end_date)
            return df
        else:
            raise Exception("unimplemented get stock 1 min df for other data source except for TDX")

    def get_industries(self, industry_code: cfg.IndustryCode):
        return self.__jqdata_gw.get_industries(name=industry_code.name)

    def get_industry_stocks(self, industry_id: str):
        return self.__jqdata_gw.get_industry_stocks(industry_id)

    def normalize_stock_id(
            self, stock_data_source: StockConfig.StockDataSource, stock_id: str):
        if stock_data_source == StockConfig.StockDataSource.JQDATA:
            return self.__jqdata_gw.normalize_stock_id(stock_id)
        elif stock_data_source == StockConfig.StockDataSource.TUSHARE:
            raise Exception("unimplemented")
        # Tdx code like 'sz000001', 'sh600001'
        elif stock_data_source == StockConfig.StockDataSource.TDX:
            return re.sub('[a-zA-Z]', '', stock_id)
            

    def __get_local_files_and_store_stock(
            self, data_source: StockConfig.StockDataSource, dir_path: str, force_upsert: bool = False):
        if data_source is not StockConfig.StockDataSource.TDX:
            raise Exception("only support for TDX in local")

        all_files = FileUtils.get_all_files(dir_path)
        for file in all_files:
            stock_name = self.normalize_stock_id(data_source, file.split(".")[0])
            file_path = FileUtils.convert_file_path_based_on_system(f"{dir_path}/{file}")
            df = self.__tdx_gw.get_local_1min_bars(file_path)
            self.__store_stock_df_data(StockConfig.StockDataSource.TDX, df, stock_name, force_upsert)

    def __store_stock_df_data(
            self, data_source: StockConfig.StockDataSource, df: pd.DataFrame, stock_id: str, force_upsert: bool):
        date_index = gw_cfg.Constant.DATE_INDEX[data_source]
        df[self.DATE_INDEX] = pd.to_datetime(df[date_index]).dt.strftime(DatetimeUtils.DATE_FORMAT)
        stored_dates = self.__mongodb_client.get_stored_dates(data_source, StockConfig.StockDataType.DAILY,
                                                              stock_id) if not force_upsert else {}

        existed_date = []
        succeeded_date = []
        print(f"trying to store {stock_id}")
        for date_index, df_group in df.groupby([df[self.DATE_INDEX]]):
            if date_index in stored_dates and stored_dates[date_index]:
                existed_date.append(date_index)
            else:
                try:
                    self.__mongodb_client.upsert_stock_price_df(data_source,
                                                                StockConfig.StockDataType.DAILY, stock_id, df_group,
                                                                date_index)
                    self.__mongodb_client.save_dates(data_source, StockConfig.StockDataType.DAILY, stock_id,
                                                     date_index)
                    succeeded_date.append(date_index)
                except Exception as e:
                    print(
                        f"FAILED to upsert data for data for source {data_source.name} - stock {stock_id} - date {date_index}, with exception: {e} \n")

        # print(f"\nthe data EXISTS for source {data_source.name} - stock {stock_id} - dates: {existed_date}")
        print(f"SUCCEEDED to upsert data for source {data_source.name} - stock {stock_id} - dates: {succeeded_date} \n")
