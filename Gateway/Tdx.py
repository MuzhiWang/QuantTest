from pytdx.reader import lc_min_bar_reader
import time
import pandas as pd

class TDX_GW(object):

    __lc_min_bar_reader = None

    def __init__(self):
        self.__lc_min_bar_reader = lc_min_bar_reader.TdxLCMinBarReader()

    def get_1min_bar(self, file_path: str):
        start = time.time()
        # df = self.__lc_min_bar_reader.get_df(file_path)
        data = self.__lc_min_bar_reader.parse_data_by_file(file_path)
        df = pd.DataFrame(data=data)
        # df = df['date', 'open', 'high', 'low', 'close', 'amount', 'volume']
        print(f"TDX get 1min bar time spent: {(time.time() - start) * 1000} ms")

        return df[['date', 'open', 'high', 'low', 'close', 'amount', 'volume']]