import unittest
import time
from Controller import StockController
from Controller.Entities import DF_MA
import pandas as pd
from Strategies.EightDiagrams import EightDiagrams
from Common.Log.Logger import Logger
from Common.RunningTimeDecorator import running_time

from Controller.StockController import StockController
from Config.StockConfig import StockDataType
from Gateway.Config import TDX_BLOCK_NAME


class TestStrategies(unittest.TestCase):

    __strategy = EightDiagrams()
    __stock_controller = StockController()
    __logger = Logger.get_logger(__name__)

    # @unittest.skip
    @running_time
    def test_eight_diagrams_get_industry_stocks_with_ma(self):
        dic = self.__strategy.get_industry_stocks_with_eight_diagrams(StockDataType.ONE_MIN,
                                                                      start_date="2019-07-27", end_date="2019-11-02",
                                                                      ma_list=[DF_MA.MACatogary.TWNTY_DAYS,
                                                                               DF_MA.MACatogary.TEN_DAYS,
                                                                               DF_MA.MACatogary.FIVE_DAYS],
                                                                      industry_ids=["852121"])

        TestStrategies.__logger.info(dic)\

    @running_time
    def test_eight_diagrams_get_block_stocks_with_ma(self):
        dic = self.__strategy.get_block_stocks_with_eight_diagrams(StockDataType.FIVE_MINS,
                                                                      start_date="2019-07-27", end_date="2019-11-07",
                                                                      ma_list=[DF_MA.MACatogary.TWNTY_DAYS,
                                                                               DF_MA.MACatogary.TEN_DAYS,
                                                                               DF_MA.MACatogary.FIVE_DAYS],
                                                                      block_names=[TDX_BLOCK_NAME.ZHONGZHENG_100, TDX_BLOCK_NAME.HUSHENG_300])

        TestStrategies.__logger.info(dic)

    @running_time
    def test_eight_diagrams_get_ed_score(self):
        ma_list = [DF_MA.MACatogary.TWNTY_DAYS, DF_MA.MACatogary.TEN_DAYS, DF_MA.MACatogary.FIVE_DAYS]
        stock_with_ma = self.__stock_controller.get_stock_with_ma(StockDataType.ONE_MIN, "000001", "2019-07-25",
                                                                  "2019-11-01", ma_list)
        # stock_with_ma.to_csv("./stock_with_ma.csv")
        # stock_with_ma = pd.read_csv("./stock_with_ma.csv")

        new_df = stock_with_ma.dropna().iloc[:, 1:].sum(axis=1)
        print(new_df.to_string())

        # res = stock_with_ma.apply(
        #     (lambda row: EightDiagrams.get_eight_diagrams_score(row, ma_list)))

        res = pd.DataFrame()
        ed_arr = []
        for _, row in stock_with_ma.iterrows():
            ed_arr.append(EightDiagrams.get_eight_diagrams_score(row, ma_list))
        res['eight_diagrams'] = ed_arr

        print(res.to_string())



if __name__ == '__main__':
    unittest.main()
