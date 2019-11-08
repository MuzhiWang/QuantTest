import unittest
from Core.Provider import StockProvider
from Config import StockConfig
import time


class TestProvider(unittest.TestCase):

    provider = StockProvider.StockProvider()

    @unittest.skip
    def test_provider_tushare(self):
        start = time.time()
        self.provider.query_and_store_1min_stock(StockConfig.StockDataSource.TUSHARE, "000001", "2019-04-02",
                                                 "2019-07-05")
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")


    # @unittest.skip
    def test_provider_tdx(self):
        start = time.time()
        self.provider.query_and_store_1min_stock(StockConfig.StockDataSource.TDX, "000001", "2019-04-02",
                                                 "2019-07-05")
        print(f"test_provider spend time: {(time.time() - start) * 1000} ms")

