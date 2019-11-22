import unittest
from Core.Provider import StockProvider, ConfigProvider
from Config import StockConfig
import time
import os
from Common import FileUtils
import pandas as pd
import matplotlib.pyplot as plt
from Gateway.Config import TDX_BLOCK_NAME
from Common.RunningTimeDecorator import running_time


class TestProvider(unittest.TestCase):

    provider = StockProvider.StockProvider()
    cfg_provider = ConfigProvider.ConfigProvider()

    def setUp(self):
        self.time = time.time()

    def tearDown(self):
        print(f"{self.__str__()} spend time: {(time.time() - self.time) * 1000} ms")

    # @unittest.skip
    def test_provider_tushare(self):
        start = time.time()
        self.provider.query_and_store_stock(StockConfig.StockDataSource.TUSHARE, StockConfig.StockDataType.ONE_MIN,
                                                 "000002", "2019-04-02", "2019-07-05", force_upsert=True)
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")


    @unittest.skip
    def test_provider_tdx(self):
        start = time.time()
        df = self.provider.query_and_store_stock(StockConfig.StockDataSource.JQDATA,
                                                 StockConfig.StockDataType.DAILY, "000001", "2019-04-02",
                                                      "2019-07-05")
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")
        print(df.to_string())

    # @unittest.skip
    def test_config_provider(self):
        current_file = os.path.abspath(os.path.dirname(__file__))
        parent_of_parent_dir = os.path.join(current_file, FileUtils.convert_file_path_based_on_system('../'))
        print(parent_of_parent_dir)

        print(self.cfg_provider.get_tdx_stock_directory_path(StockConfig.StockDataType.DAILY, 'sz'))

    @unittest.skip
    def test_provider_tdx_store_local(self):
        start = time.time()
        self.provider.get_and_store_local_stock(StockConfig.StockDataSource.TDX, StockConfig.StockDataType.ONE_MIN)
        print(f"test_provider tdx store local spend time: {(time.time() - start) * 1000} ms")

    @unittest.skip
    def test_provider_get_1min_stock(self):
        df = self.provider.get_stock_df(StockConfig.StockDataSource.TDX, StockConfig.StockDataType.ONE_MIN, "000001",
                                        "2019-07-23", "2019-11-01")
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = [int(t.value / (10 ** 9)) for t in df.date]
        df = df[['date', 'close']]

        # print(df.info())
        # print(df.to_string())

        r = df.rolling(window=3600).mean()
        rr = r.plot(x = 'date', y = 'close', color = 'red')
        plt.show()

        # x = range(1, 5)
        # y = range(1,5)
        # plt.plot(x, y)
        # plt.show()
        print(r)
        # print(r.info())
        # print(r.to_string())

    # @unittest.skip
    def test_normalize_stock_id(self):
        res = self.provider.normalize_stock_id(StockConfig.StockDataSource.JQDATA, "000019.XSHE")
        print(res)
        print(self.provider.normalize_stock_id(StockConfig.StockDataSource.TDX, "sz000001"))

    @running_time
    def test_get_block_stocks(self):
        res = self.provider.get_block_stocks(StockConfig.StockDataSource.TDX, TDX_BLOCK_NAME.ZHONGZHENG_200)
        print(res)





