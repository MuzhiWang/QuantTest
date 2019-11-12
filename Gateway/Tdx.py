from pytdx.reader import lc_min_bar_reader
from pytdx.hq import TdxHq_API, TDXParams
import time
import pandas as pd

class TDX_GW(object):

    __lc_min_bar_reader = None
    __tdx_api = None
    __connected_ip = '119.147.212.81'
    __connected_port = 7709

    def __init__(self):
        self.__lc_min_bar_reader = lc_min_bar_reader.TdxLCMinBarReader()
        self.__tdx_api = TdxHq_API()


    def get_local_1min_bars(self, file_path: str):
        start = time.time()
        # df = self.__lc_min_bar_reader.get_df(file_path)
        data = self.__lc_min_bar_reader.parse_data_by_file(file_path)
        df = pd.DataFrame(data=data)
        # df = df['date', 'open', 'high', 'low', 'close', 'amount', 'volume']
        # print(f"TDX get 1min bar time spent: {(time.time() - start) * 1000} ms")

        return df[['date', 'open', 'high', 'low', 'close', 'amount', 'volume']]

    def get_realtime_stock_1min_bars(self, stock_id: str):
        with self.__tdx_api.connect(self.__connected_ip, self.__connected_port):
            df = self.__tdx_api.to_df(
                self.__tdx_api.get_security_bars(8, 0, stock_id, 0, 10))  # 返回DataFrame
            return df

    def test(self):
        with self.__tdx_api.connect(self.__connected_ip, self.__connected_port):
            return self.__tdx_api.to_df(
                # self.__tdx_api.get_history_minute_time_data(31, "00020", 20190808)
                # self.__tdx_api.get_instrument_bars(TDXParams.KLINE_TYPE_DAILY, 8, "10000843", 0, 100)
                # self.__tdx_api.get_block_info()
            )

