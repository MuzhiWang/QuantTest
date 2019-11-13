from Core.Provider import StockProvider
from Config.StockConfig import StockDataSource
import pandas as pd
from Controller.Entities import DF_MA
import Gateway.Config as cfg


class StockController(object):

    def __init__(self):
        self.__stock_provider = StockProvider.StockProvider()

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
