import unittest
from Core.Provider import StockProvider, ConfigProvider
from Config import StockConfig
import time
import os
from Common import FileUtils


class TestProvider(unittest.TestCase):

    provider = StockProvider.StockProvider()
    cfg_provider = ConfigProvider.ConfigProvider()

    def setUp(self):
        self.time = time.time()

    def tearDown(self):
        print(f"{self.__str__()} spend time: {(time.time() - self.time) * 1000} ms")

    @unittest.skip
    def test_provider_tushare(self):
        start = time.time()
        self.provider.query_and_store_1min_stock(StockConfig.StockDataSource.TUSHARE, "000001", "2019-04-02",
                                                 "2019-07-05")
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")


    @unittest.skip
    def test_provider_tdx(self):
        start = time.time()
        self.provider.query_and_store_1min_stock(StockConfig.StockDataSource.TDX, "000001", "2019-04-02",
                                                 "2019-07-05")
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")

    # @unittest.skip
    def test_config_provider(self):
        current_file = os.path.abspath(os.path.dirname(__file__))
        parent_of_parent_dir = os.path.join(current_file, FileUtils.convert_file_path_based_on_system('../'))
        print(parent_of_parent_dir)

        print(self.cfg_provider.get_tdx_directory_path('sz'))

    @unittest.skip
    def test_provider_tdx_store_local(self):
        start = time.time()
        self.provider.get_and_store_local_1min_stock(StockConfig.StockDataSource.TDX)
        print(f"test_provider tdx store local spend time: {(time.time() - start) * 1000} ms")

    # @unittest.skip
    def test_provider_get_1min_stock(self):
        df = self.provider.get_stock_1min_df(
            StockConfig.StockDataSource.TDX, "000001", "2019-06-25", "2019-11-04")
        print(df)


