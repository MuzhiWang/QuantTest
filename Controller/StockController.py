from Core.Provider import StockProvider
from Config.StockConfig import StockDataSource
import pandas as pd
from Controller.Entities import DF_MA

class StockController(object):

    def __init__(self):
        self.__stock_provider = StockProvider.StockProvider()


    def get_stock_ma(self, stock_id: str, start_date: str, end_date: str, ma_list: []):
        if ma_list is None:
            raise Exception("must define ma list")

        df = self.__stock_provider.get_stock_1min_df(
            StockDataSource.TDX, stock_id, start_date, end_date)
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = [int(t.value / (10 ** 9)) for t in df.date]
        # df = df.drop(columns=['date_index'])
        df = df[['date', 'close']]

        df_ma = DF_MA.DF_MA(df, start_date, end_date, ma_list)
        for ma in ma_list:
            r_df = df.rolling(window=DF_MA.Constant.ma_category_mins_map[ma]).mean()
            df_ma.ma_dict[ma] = r_df

        return df_ma

    def get_index_ma(self, index_id: str, ma_list: []):
        pass
