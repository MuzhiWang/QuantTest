import unittest
import time
from Controller import StockController
from Controller.Entities import DF_MA
import pandas as pd

class TestController(unittest.TestCase):

    __stock_controller = StockController.StockController()

    def setUp(self):
        self.time = time.time()

    def tearDown(self):
        print(f"{self.__str__()} spend time: {(time.time() - self.time) * 1000} ms")


    # @unittest.skip
    def test_DF_MA_entity(self):
        ma_list = [DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.EIGHT_DAYS]
        print(DF_MA.Constant.ma_category_mins_map[ma_list[0]])

    # @unittest.skip
    def test_stock_controller_get_stock_ma(self):
        ma_list = [DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.FIFTEEN_DAYS, DF_MA.MACatogary.EIGHT_DAYS]
        df_ma = self.__stock_controller.get_stock_with_ma("000001", "2019-07-25", "2019-11-08", ma_list)
        # print(df_ma.df)
        print(df_ma.columns.values)

        df_ma['date'] = pd.to_datetime(df_ma['date'], unit='s')
        print(df_ma.to_string())

    # @unittest.skip
    def test_stock_controller_get_industry_stocks_with_ma(self):
        dic = self.__stock_controller.get_industry_stocks_with_ma(
            start_date="2019-09-09",
            end_date="2019-11-01",
            ma_list=[DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.TEN_DAYS, DF_MA.MACatogary.FIVE_DAYS],
            industry_id="850941"
        )

        print(dic)