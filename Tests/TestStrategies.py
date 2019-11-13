import unittest
import time
from Controller import StockController
from Controller.Entities import DF_MA
import pandas as pd
from Strategies.EightDiagrams import EightDiagrams


class MyTestCase(unittest.TestCase):

    __strategy = EightDiagrams()

    @unittest.skip
    def test_something(self):
        self.assertEqual(True, False)

    # @unittest.skip
    def test_stock_controller_get_industry_stocks_with_ma(self):
        dic = self.__strategy.get_industry_stocks_with_ma(
            start_date="2019-09-09",
            end_date="2019-11-01",
            ma_list=[DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.TEN_DAYS, DF_MA.MACatogary.FIVE_DAYS],
            industry_ids=["801770"]
        )

        # print(dic)

if __name__ == '__main__':
    unittest.main()
