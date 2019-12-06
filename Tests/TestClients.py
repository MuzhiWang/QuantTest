from Config.StockConfig import StockCode, StockDataType, StockDataSource
from Gateway.TuShare import TuShare_GW
from Database.MongoDB import Client
import Common.StringUtils as str_utils
from Common import DatetimeUtils, FileUtils, CommonUtils
import unittest
import bson
from Gateway.JQData import JQData_GW
from Gateway.Tdx import TDX_GW
import pandas as pd
from Core.Provider import ConfigProvider
import re
import time
import Gateway.Config as cfg
from Common.Log.Logger import Logger
from Common.RunningTimeDecorator import running_time


class TestClients(unittest.TestCase):
    csv_path = FileUtils.convert_file_path_based_on_system(".\\test1.csv")
    mongodb_client = Client.Client()
    jqdate_client = JQData_GW()
    tushare_client = TuShare_GW()
    tdx_client = TDX_GW()
    cfg_provider = ConfigProvider.ConfigProvider()
    logger = Logger.get_logger(__name__)

    def setUp(self):
        self.time = time.time()

    def tearDown(self):
        self.logger.debug(f"{self.__str__()} spend time: {(time.time() - self.time) * 1000} ms")

    @unittest.skip
    def test_mongodb_client(self):
        start_date = "2019-09-01"
        end_date = "2019-09-04"

        ttt = str_utils.date_to_object_id(start_date)
        print(ttt)

        for stock in StockCode.Test:
            df = self.tushare_client.get_stock_price(StockDataType.DAILY, stock, start_date, end_date)
            # df = pd.read_csv(csv_path)
            print(df.head(10))
            # df.to_csv(csv_path, index=False)
            # t_df = pd.read_csv(csv_path)
            # print(t_df.head(10))
            # print(t_df.to_json())

            self.mongodb_client.upsert_stock_price_df(StockDataSource.JQDATA, StockDataType.DAILY, stock, df,
                                                      start_date)
            print("success to insert stock %s . with df: %s" % (stock, df.to_json()))

            get_rec = self.mongodb_client.get_stock_price_df(StockDataSource.JQDATA, StockDataType.DAILY, stock,
                                                             start_date)
            if get_rec is not None:
                print(get_rec.head(10))
            # break

    @unittest.skip
    def test_mongodb_client_get_record_no_record(self):
        start_date = "2019-09-03"
        stock = "000001"
        res = self.mongodb_client.get_stock_record_by_id(StockDataSource.TUSHARE, StockDataType.DAILY, stock,
                                                         str_utils.date_to_object_id(start_date))
        print(res)

    # @unittest.skip
    def test_mongodb_client_get_stock_price_df(self):

        start_date = "2019-09-02"
        end_date = "2019-10-03"
        stock = "000001"
        # res = self.mongodb_client.get_stock_price_df(StockDataSource.TUSHARE, StockDataType.DAILY, stock, start_date,
        #                                              end_date)
        # print(res.to_string())
        #
        # r1 = self.mongodb_client.get_stock_price_df(StockDataSource.TUSHARE, StockDataType.DAILY, stock, start_date,
        #                                             start_date)
        # r2 = self.mongodb_client.get_stock_price_df(StockDataSource.TUSHARE, StockDataType.DAILY, stock, end_date,
        #                                             end_date)
        r3 = self.mongodb_client.get_stock_price_df(StockDataSource.TDX, StockDataType.DAILY, stock, start_date,
                                                    end_date)
        # print(r1.head(10))
        # print(r2.head(10))
        # print(r1.append(r2))
        print(r3.to_string())

    @unittest.skip
    def test_datetime_utils(self):
        start_date = "2018-10-01"
        end_date = "2018-10-11"
        print(DatetimeUtils.get_interval_dates(start_date, end_date))

    # @unittest.skip
    def test_test_test(self):
        print(bson.ObjectId())
        print(bson.ObjectId("5dc5166437b0ee6779f63918"))
        print(DatetimeUtils.get_days_between_dates("2019-10-01", "2019-10-03"))
        aa = "testestet"
        a = f"hahah {aa}"
        print(a)

    @unittest.skip
    @running_time
    def test_mongodb_get_and_store_dates_status(self):
        self.mongodb_client.save_dates(StockDataSource.TDX, StockDataType.DAILY, "000003", "2012-01-11",
                                       "2019-02-01")
        res = self.mongodb_client.get_stored_dates(StockDataSource.TDX, StockDataType.DAILY, "000003")
        print(res)

    @unittest.skip
    def test_jqdata_client_get_1min(self):
        df = self.jqdate_client.get_1min_bars("000001", 250, "2019-09-03")
        df.to_csv(FileUtils.convert_file_path_based_on_system("./CSV/jqdata001.csv"), index=False)
        print(df)

    # @unittest.skip
    def test_jqdata_client_get_industries(self):
        str = 'sw_l1'
        str_enum = cfg.IndustryCode[str]
        print(str_enum.name)


        res = self.jqdate_client.get_industries(cfg.IndustryCode.sw_l1)
        print(res['name'])

        for index, row in res.iterrows():
            industry_info = row['name'].split()
            stocks_in_industries = self.jqdate_client.get_industry_stocks(index)
            print(f"start to query {len(stocks_in_industries)} stocks of industry: {index} "
                  f"- {industry_info[0]}")

        # res2 = self.jqdate_client.get_industry_stocks('HY005')
        # print(len(res2))
        # print(res2)

    # @unittest.skip
    def test_jqdata_client_normalize_stock_id(self):
        res = self.jqdate_client.normalize_stock_id("000019.XSHE")
        print(res)
        print(self.jqdate_client.normalize_stock_id("000001.XSHG"))
        print(self.jqdate_client.normalize_stock_id(self.jqdate_client.normalize_code("sz000001")))

    def test_jqdata_client_normalize_code(self):
        print(self.jqdate_client.normalize_code("sz000001"))

    # @unittest.skip
    def test_tushare_client(self):
        df = self.tushare_client.get_stock_price(StockDataType.ONE_HOUR, "000001", "2019-09-02", "2019-09-05")
        print(df)
        # df.to_csv(FileUtils.convert_file_path_based_on_system("./CSV/tushare001.csv"))

    @unittest.skip
    def test_tdx_client_get_local_1min_bars(self):
        df = self.tdx_client.get_local_stock_bars(
            FileUtils.convert_file_path_based_on_system(".\\LC1\\SZ\\sz000001.lc1"), StockDataType.ONE_MIN)
        print(df)
        df.to_csv(FileUtils.convert_file_path_based_on_system(".\\CSV\\tdx001.csv"))
        print(df.columns.values)

        df['date_index'] = pd.to_datetime(df['date']).dt.strftime(DatetimeUtils.DATE_FORMAT)
        print(df)

    def test_tdx_client_get_local_block(self):
        df = self.tdx_client.get_local_block()
        df = df.set_index('blockname')
        print(df.loc[cfg.TDX_BLOCK_NAME.HUSHENG_300][cfg.Constant.TDX_BLOCK_CODE_LIST].strip().split(','))

    # @unittest.skip
    def test_tdx_client_get_realtime_stock(self):
        df = self.tdx_client.get_realtime_stock_1min_bars('sh', "002807")
        self.logger.debug(df.to_string())


    @unittest.skip
    def test_tdx_client_get_realtime_stocks_quotas(self):
        res = self.tdx_client.get_realtime_stocks_quotes(["000001", '000002'])
        print(res)

    # @unittest.skip
    def test_tdx_client_get_history_minute_time_data(self):
        res = self.tdx_client.get_history_minute_time_data('sh', '000001', 20160607)
        print(res)

    # @unittest.skip
    def test_tdx_client_get_xdxr_info(self):
        res = self.tdx_client.get_xdxr_info('sh', '600381')
        print(res.to_string())

    # @unittest.skip
    def test_file_utils(self):
        path = self.cfg_provider.get_tdx_stock_directory_path(StockDataType.ONE_MIN, 'sh')
        print(path)
        path = FileUtils.convert_file_path_based_on_system(path)
        self.logger.debug(FileUtils.get_all_files(path))

    def test_file_utils_get_same_code_files(self):
        path = self.cfg_provider.get_tdx_stock_directory_path(StockDataType.ONE_MIN, 'sh')
        print(path)
        path1 = FileUtils.convert_file_path_based_on_system(path)
        sh_files = FileUtils.get_all_files(path1)
        path = self.cfg_provider.get_tdx_stock_directory_path(StockDataType.ONE_MIN, 'sz')
        path2 = FileUtils.convert_file_path_based_on_system(path)
        sz_files = FileUtils.get_all_files(path2)

        sh_file_codes = {}
        sz_file_codes = {}
        for f in sh_files:
            f_code = f.split(".lc1")[0].split("sh")[1]
            sh_file_codes[f_code] = True
        for f in sz_files:
            f_code = f.split(".lc1")[0].split("sz")[1]
            sz_file_codes[f_code] = True

        for key, _ in sh_file_codes.items():
            if key in sz_file_codes:
                print(f'both exist: {key}')

    @unittest.skip
    def test_common_utils(self):
        print(CommonUtils.get_os_system())
        t = "sz000001"
        self.logger.debug(f"after replace:" + re.sub('[a-zA-Z]', '', t))


if __name__ == '__main__':
    unittest.main()
