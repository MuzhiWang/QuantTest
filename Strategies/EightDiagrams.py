from __future__ import division
from Core.Provider import StockProvider
from Config.StockConfig import StockDataSource
import pandas as pd
from Controller.Entities import DF_MA
import Gateway.Config as cfg
from Controller import StockController
from Common.Log.Logger import Logger
from Common import CommonUtils

EIGHT_DIAGRAMS_COL = 'eight_diagrams'

class EightDiagrams(object):

    __eight_diagrams_score_map = {
        1: 8.0,
        2: 7.0,
        3: 6.0,
        4: 5.0,
        5: 4.0,
        6: 3.0,
        7: 2.0,
        8: 1.0
    }

    def __init__(self):
        self.__stock_controller = StockController.StockController()
        self.__stock_provider = StockProvider.StockProvider()
        self.__logger = Logger.get_logger(__name__)

    def get_industry_stocks_with_eight_diagrams(self, start_date: str, end_date: str, ma_list: [],
                                                industry_code: cfg.IndustryCode = None, industry_ids: [] = None):
        if industry_ids is None and industry_code is None:
            raise Exception("industry code or id must exist one")

        if len(ma_list) != 3:
            raise Exception("ma list must contains 3 ma categories")

        ma_list = CommonUtils.sort_enum(ma_list)

        industry_stocks_with_ma_map = {}
        stocks_ed_df_map = {}
        if industry_code is not None:
            industry_name_df = self.__stock_provider.get_industries(industry_code)['name']
            # industry_name_map = {}
            for index, row in industry_name_df.iterrows():
                industry_ids.append(index)

        for ind_id in industry_ids:
            # Duplicated ind_id, skip
            if ind_id in industry_stocks_with_ma_map:
                pass

            ind_ed_df = pd.DataFrame()

            industry_stocks_with_ma_map[ind_id] = {}
            stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
            self.__logger.debug(f"start to query {len(stock_ids)} stocks of industry: {ind_id}")

            for s_id in stock_ids:
                # generate eight diagram scores
                stock_ed_df = pd.DataFrame()
                stock_id = self.__stock_provider.normalize_stock_id(StockDataSource.JQDATA, s_id)

                if stock_id in stocks_ed_df_map:
                    stock_ed_df = stocks_ed_df_map[stock_id]
                else:
                    # stock_with_ma = \
                    #     self.__stock_controller.get_stock_with_ma(stock_id, start_date, end_date, ma_list).dropna()
                    stock_with_ma = pd.read_csv("/Users/muzwang/gocode/src/github.com/QuantTest/Tests/stock_with_ma.csv")

                    # if there is no valid stock ma df generated. Ignore the stock and continue
                    if CommonUtils.is_df_none_or_empty(stock_with_ma):
                        self.__logger.warn(f"get NONE stock with ma for stock {stock_id}")
                        continue
                    else:
                        stock_ed_df['date'] = stock_with_ma['date']
                        # ed_arr = []
                        # for _, row in stock_with_ma.iterrows():
                        #     ed_arr.append(EightDiagrams.get_eight_diagrams_score(row, ma_list))

                        # stock_ed_df[stock_id] = ed_arr
                        stock_ed_df[stock_id] = stock_with_ma.apply(
                            (lambda row: EightDiagrams.get_eight_diagrams_score(row, ma_list)), axis=1)
                        stock_ed_df = stock_ed_df.set_index('date')
                        stocks_ed_df_map[stock_id] = stock_ed_df

                if ind_ed_df.empty or len(ind_ed_df.index) < len(stock_ed_df.index):
                    ind_ed_df = stock_ed_df.merge(ind_ed_df, how='left', left_index=True, right_index=True)
                else:
                    ind_ed_df = ind_ed_df.merge(stock_ed_df, how='left', left_index=True, right_index=True)

                # self.__logger.info(ind_ed_df.to_string())

            if ind_ed_df.empty:
                self.__logger.warn(f"the index ed df is null for index {ind_id}")
                continue

            self.__logger.debug(ind_ed_df.to_string())

            ind_ed_score_df = pd.DataFrame()
            ind_ed_df = ind_ed_df.reset_index('date')
            ind_ed_score_df['date'] = ind_ed_df['date']
            ind_ed_df = ind_ed_df.drop('date', axis=1)
            ind_ed_score_df[EIGHT_DIAGRAMS_COL] = ind_ed_df.apply(lambda row: EightDiagrams.__get_ed_score(row), axis=1).round(2)
            # ind_ed_score_df = ind_ed_score_df.set_index('date')
            self.__logger.debug(ind_ed_score_df.to_string())
            industry_stocks_with_ma_map[ind_id] = ind_ed_score_df

        return industry_stocks_with_ma_map

    @staticmethod
    def get_eight_diagrams_score(row, ma_list:[]):
        if row.isnull().sum() > 0:
            return -1
        long_ma = row[ma_list[0].name]
        middle_ma = row[ma_list[1].name]
        short_ma = row[ma_list[2].name]

        close_val = row['close']

        ed_score = -1
        if close_val >= long_ma:
            if close_val >= middle_ma:
                if close_val >= short_ma:
                    ed_score = 1
                else:
                    ed_score = 5
            else:
                if close_val >= short_ma:
                    ed_score = 3
                else:
                    ed_score = 7
        else:
            if close_val >= middle_ma:
                if close_val >= short_ma:
                    ed_score = 2
                else:
                    ed_score = 6
            else:
                if close_val >= short_ma:
                    ed_score = 4
                else:
                    ed_score = 8

        return ed_score

    @staticmethod
    def __get_ed_score(row):
        count = len(row) - row.isnull().sum()
        return row.sum() / count




