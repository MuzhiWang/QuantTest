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
        industry_eight_diagrams_score = {}
        stocks_with_ma_map = {}
        stocks_with_eight_diagrams_map = {}
        if industry_code is not None:
            industry_name_df = self.__stock_provider.get_industries(industry_code)['name']
            # industry_name_map = {}
            for index, row in industry_name_df.iterrows():
                # industry_name = row['name'].split()[0]
                # {id: title}
                # industry_name_map[index] = industry_name_map[industry_name]
                industry_ids.append(index)

            # for ind_id, ind_title in industry_name_map.items():
            #     industry_stocks_with_ma_map[ind_id] = {}
            #     stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
            #     self.__logger.debug(f"start to query {len(stock_ids)} stocks of industry: {ind_id} - {ind_title}")
            #     for s_id in stock_ids:
            #         stock_id = self.__stock_provider.normalize_stock_id(s_id)
            #         stock_with_ma = stocks_with_ma_map[stock_id] if stock_id in stocks_with_ma_map else \
            #             self.__stock_controller.get_stock_with_ma(stock_id, start_date, end_date, ma_list)
            #         industry_stocks_with_ma_map[ind_id][stock_id] = stock_with_ma

        for ind_id in industry_ids:
            # Duplicated ind_id, skip
            if ind_id in industry_stocks_with_ma_map:
                pass

            ind_ed_df = pd.DataFrame()

            industry_stocks_with_ma_map[ind_id] = {}
            stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
            self.__logger.debug(f"start to query {len(stock_ids)} stocks of industry: {ind_id}")
            valid_stock_count = 0

            for s_id in stock_ids:
                stock_id = self.__stock_provider.normalize_stock_id(StockDataSource.JQDATA, s_id)

                if stock_id in stocks_with_ma_map:
                    stock_with_ma = stocks_with_ma_map[stock_id]
                    ind_ed_df[stock_id] = stocks_with_eight_diagrams_map[stock_id][EIGHT_DIAGRAMS_COL]
                    valid_stock_count += 1
                else:
                    stock_with_ma = \
                        self.__stock_controller.get_stock_with_ma(stock_id, start_date, end_date, ma_list).dropna()

                    # generate eight diagram scores
                    new_df = pd.DataFrame()

                    if stock_with_ma is None or stock_with_ma.empty:
                        self.__logger.warn(f"get NONE stock with ma for stock {stock_id}")
                    else:
                        new_df['date'] = stock_with_ma['date']
                        # new_df['eight_diagrams'] = stock_with_ma.apply(
                        #     (lambda row: EightDiagrams.get_eight_diagrams_score(row, ma_list)), axis=0)
                        ed_arr = []
                        for _, row in stock_with_ma.iterrows():
                            ed_arr.append(EightDiagrams.get_eight_diagrams_score(row, ma_list))

                        new_df[EIGHT_DIAGRAMS_COL] = ed_arr
                        ind_ed_df[stock_id] = new_df[EIGHT_DIAGRAMS_COL]
                        valid_stock_count += 1

                    stocks_with_eight_diagrams_map[ind_id] = new_df

                ret_df = pd.DataFrame()
                # ret_df['date'] =
                ret_df[EIGHT_DIAGRAMS_COL] = ind_ed_df.iloc[:, :].sum(axis=1) / valid_stock_count
                # industry_stocks_with_ma_map[ind_id][stock_id] = stocks_with_eight_diagrams_map[ind_id]
                industry_stocks_with_ma_map[ind_id] = ret_df

        return industry_stocks_with_ma_map

    @staticmethod
    def get_eight_diagrams_score(row, ma_list:[]):
        if row.isnull().values.any():
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




