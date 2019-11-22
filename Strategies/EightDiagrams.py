from __future__ import division
from Core.Provider import StockProvider
from Config.StockConfig import StockDataSource, StockDataType
import pandas as pd
from Controller.Entities import DF_MA
import Gateway.Config as cfg
from Controller import StockController
from Common.Log.Logger import Logger
from Common import CommonUtils
from Core.Provider.ConfigProvider import ConfigProvider

from multiprocessing import Pool

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

    stock_controller = StockController.StockController()
    stock_provider = StockProvider.StockProvider()
    logger = Logger.get_logger(__name__)
    cfg_provider = ConfigProvider()

    def __init__(self):
        self.stock_controller = EightDiagrams.stock_controller
        self.stock_provider = EightDiagrams.stock_provider
        self.logger = EightDiagrams.logger
        self.cfg_provider = EightDiagrams.cfg_provider

    def get_industry_stocks_with_eight_diagrams(self, stock_date_type: StockDataType, start_date: str, end_date: str, ma_list: [],
                                                industry_code: cfg.IndustryCode = None, industry_ids: [] = None):
        if industry_ids is None and industry_code is None:
            raise Exception("industry code or id must exist one")

        if len(ma_list) != 3:
            raise Exception("ma list must contains 3 ma categories")

        ma_list = CommonUtils.sort_enum(ma_list)

        industry_stocks_with_ma_map = {}
        stocks_ed_df_map = {}
        if industry_code is not None:
            industry_name_df = self.stock_provider.get_industries(industry_code)['name']
            # industry_name_map = {}
            for index, row in industry_name_df.iterrows():
                industry_ids.append(index)

        for ind_id in industry_ids:
            # Duplicated ind_id, skip
            if ind_id in industry_stocks_with_ma_map:
                pass


            industry_stocks_with_ma_map[ind_id] = {}
            # stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
            stock_ids = ['000001', '000002', '000004', '000005', '000006',
                         '000007', '000008', '000009', '000010', '000011']
            self.logger.debug(f"start to query {len(stock_ids)} stocks of industry: {ind_id}")

            ind_ed_df = self.__get_batch_stocks_ed_df(
                stock_ids, stocks_ed_df_map, stock_date_type, start_date, end_date, ma_list)

            if ind_ed_df.empty:
                self.logger.warning(f"the index ed df is null for index {ind_id}")
                continue

            # self.__logger.debug(ind_ed_df.to_string())

            ind_ed_score_df = pd.DataFrame()
            ind_ed_df = ind_ed_df.reset_index('date')
            ind_ed_score_df['date'] = ind_ed_df['date']
            ind_ed_df = ind_ed_df.drop('date', axis=1)
            ind_ed_score_df[EIGHT_DIAGRAMS_COL] = ind_ed_df.apply(lambda row: EightDiagrams.__get_ed_score(row), axis=1).round(2)
            # ind_ed_score_df = ind_ed_score_df.set_index('date')
            self.logger.debug(ind_ed_score_df.to_string())
            industry_stocks_with_ma_map[ind_id] = ind_ed_score_df

        return industry_stocks_with_ma_map


    def get_block_stocks_with_eight_diagrams(self, stock_date_type: StockDataType, start_date: str, end_date: str, ma_list: [],
                                                block_names: []):
        if block_names is None or len(block_names) == 0:
            raise Exception("block must exist")

        if len(ma_list) != 3:
            raise Exception("ma list must contains 3 ma categories")

        ma_list = CommonUtils.sort_enum(ma_list)

        block_stocks_with_ma_map = {}
        stocks_ed_df_map = {}

        for block_name in block_names:
            # Duplicated ind_id, skip
            if block_name in block_stocks_with_ma_map:
                pass

            block_stocks_with_ma_map[block_name] = {}
            stock_ids = EightDiagrams.stock_provider.get_block_stocks(StockDataSource.TDX, block_name)
            EightDiagrams.logger.debug(f"start to query {len(stock_ids)} stocks of block: {block_name}")

            block_ed_df = self.__get_batch_stocks_ed_df(
                stock_ids, stocks_ed_df_map, stock_date_type, start_date, end_date, ma_list)

            if block_ed_df.empty:
                EightDiagrams.logger.warning(f"the index ed df is null for index {block_name}")
                continue

            # EightDiagrams.__logger.debug(ind_ed_df.to_string())

            ind_ed_score_df = pd.DataFrame()
            block_ed_df = block_ed_df.reset_index('date')
            ind_ed_score_df['date'] = block_ed_df['date']
            block_ed_df = block_ed_df.drop('date', axis=1)
            ind_ed_score_df[EIGHT_DIAGRAMS_COL] = block_ed_df.apply(lambda row: EightDiagrams.__get_ed_score(row), axis=1).round(2)
            # ind_ed_score_df = ind_ed_score_df.set_index('date')
            EightDiagrams.logger.debug(ind_ed_score_df.to_string())
            block_stocks_with_ma_map[block_name] = ind_ed_score_df

        return block_stocks_with_ma_map

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

    def __get_batch_stocks_ed_df(self, stock_ids: [], stocks_ed_df_map: {},
                                 stock_date_type: StockDataType, start_date: str, end_date: str, ma_list: []):
        processes_number = self.cfg_provider.get_multi_processes_number('eight_diagram')
        prev_idx = 0
        cur_idx = 0
        slot_count = int(len(stock_ids) / processes_number) + 1

        pool = Pool(processes=processes_number)
        ret_df = pd.DataFrame()
        batch_dfs = []

        for i in range(processes_number):
            cur_idx += slot_count
            async_res = pool.apply_async(func=get_limited_batch_stocks_ed_df, args=(stock_ids[prev_idx:cur_idx], stocks_ed_df_map, stock_date_type,
                                                                        start_date, end_date, ma_list,))
            batch_dfs.append(async_res)
            prev_idx = cur_idx

            if cur_idx >= len(stock_ids):
                break

        pool.close()
        pool.join()

        for async_batch_df in batch_dfs:
            cur_df = async_batch_df.get()
            if CommonUtils.is_df_none_or_empty(ret_df) or \
                    len(ret_df.index) < len(cur_df.index):
                ret_df = cur_df.merge(ret_df, how='left', left_index=True, right_index=True)
            else:
                ret_df = ret_df.merge(cur_df, how='left', left_index=True, right_index=True)

        self.logger.debug(f'multiple processes with {processes_number} processes done!')

        return ret_df



def get_limited_batch_stocks_ed_df(stock_ids: [], stocks_ed_df_map: {},
                                   stock_date_type: StockDataType, start_date: str,
                                   end_date: str, ma_list: []):
    batch_stocks_ed_df = pd.DataFrame()
    for s_id in stock_ids:
        # generate eight diagram scores
        stock_ed_df = pd.DataFrame()
        stock_id = EightDiagrams.stock_provider.normalize_stock_id(StockDataSource.JQDATA, s_id)

        if stock_id in stocks_ed_df_map:
            stock_ed_df = stocks_ed_df_map[stock_id]
        else:
            stock_with_ma = \
                EightDiagrams.stock_controller.get_stock_with_ma(stock_date_type, stock_id, start_date, end_date,
                                                          ma_list).dropna()
            # stock_with_ma = pd.read_csv("/Users/muzwang/gocode/src/github.com/QuantTest/Tests/stock_with_ma.csv").dropna()

            # if there is no valid stock ma df generated. Ignore the stock and continue
            if CommonUtils.is_df_none_or_empty(stock_with_ma):
                EightDiagrams.logger.warning(f"get NONE stock with ma for stock {stock_id}")
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

        if CommonUtils.is_df_none_or_empty(batch_stocks_ed_df) or \
                len(batch_stocks_ed_df.index) < len(stock_ed_df.index):
            batch_stocks_ed_df = stock_ed_df.merge(batch_stocks_ed_df, how='left', left_index=True, right_index=True)
        else:
            batch_stocks_ed_df = batch_stocks_ed_df.merge(stock_ed_df, how='left', left_index=True, right_index=True)

        # EightDiagrams.__logger.debug(batch_stocks_ed_df.to_string())

    # print(f'batch stock df: {batch_stocks_ed_df.head()}')
    return batch_stocks_ed_df
