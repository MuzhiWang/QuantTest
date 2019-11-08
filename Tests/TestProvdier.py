import unittest
from Core.Provider import StockProvider


class TestProvider(unittest.TestCase):

    provider = StockProvider.StockProvider()

    # @unittest.skip
    def test_provider(self):
        self.provider.query_and_store_1min_stock("000001", "2019-09-02", "2019-09-05")
