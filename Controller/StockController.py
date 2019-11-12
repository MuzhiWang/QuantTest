from Core.Provider import StockProvider
from Config.StockConfig import StockDataSource
import pandas as pd
from Controller.Entities import DF_MA
import Gateway.Config as cfg


class StockController(object):

    def __init__(self):
        self.__stock_provider = StockProvider.StockProvider()


    def get_industry_stocks_with_ma(self, start_date: str, end_date: str, ma_list: [],
                                    industry_code: cfg.IndustryCode = None, industry_ids: [] = None):
        industry_stocks_with_ma_map = {}
        stocks_with_ma_map = {}
        if industry_code is not None:
            industry_name_df = self.__stock_provider.get_industries(industry_code)['name']
            industry_name_map = {}
            for index, row in industry_name_df.iterrows():
                industry_name = row['name'].split()[0]
                # {id: title}
                industry_name_map[index] = industry_name_map[industry_name]

            for ind_id, ind_title in industry_name_map.items():
                industry_stocks_with_ma_map[ind_id] = {}
                stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
                print(f"start to query {len(stock_ids)} stocks of industry: {ind_id} - {ind_title}")
                for s_id in stock_ids:
                    stock_id = self.__stock_provider.normalize_stock_id(s_id)
                    stock_with_ma = stocks_with_ma_map[stock_id] if stock_id in stocks_with_ma_map else \
                        self.get_stock_with_ma(stock_id, start_date, end_date, ma_list)
                    industry_stocks_with_ma_map[ind_id][stock_id] = stock_with_ma
        elif industry_ids is not None:
            for ind_id in industry_ids:
                industry_stocks_with_ma_map[ind_id] = {}
                stock_ids = self.__stock_provider.get_industry_stocks(ind_id)
                print(f"start to query {len(stock_ids)} stocks of industry: {ind_id}")
                for s_id in stock_ids:
                    stock_id = self.__stock_provider.normalize_stock_id(StockDataSource.JQDATA, s_id)
                    stock_with_ma = stocks_with_ma_map[stock_id] if stock_id in stocks_with_ma_map else \
                        self.get_stock_with_ma(stock_id, start_date, end_date, ma_list)
                    industry_stocks_with_ma_map[ind_id][stock_id] = stock_with_ma
        else:
            raise Exception("industry code or id must exist one")

        return industry_stocks_with_ma_map


    def get_stock_with_ma(self, stock_id: str, start_date: str, end_date: str, ma_list: []):
        if ma_list is None:
            raise Exception("must define ma list")

        df = self.__stock_provider.get_stock_1min_df(
            StockDataSource.TDX, stock_id, start_date, end_date)

        if df is None:
            print(f"get stock '{stock_id}' with ma got NONE df")
            return pd.DataFrame()

        df['date'] = pd.to_datetime(df['date'])
        df['date'] = [int(t.value / (10 ** 9)) for t in df.date]
        # df = df.drop(columns=['date_index'])
        df = df[['date', 'close']]
        ret_df = df.copy(deep=True)

        for ma in ma_list:
            r_df = df.rolling(window=DF_MA.Constant.ma_category_mins_map[ma]).mean()
            ret_df[ma.name] = r_df['close']

        return ret_df

    def get_index_ma(self, index_id: str, ma_list: []):
        pass
