from pytdx.reader import lc_min_bar_reader, block_reader
from pytdx.reader.block_reader import BlockReader_TYPE_GROUP
from pytdx.hq import TdxHq_API, TDXParams
import time
import pandas as pd
from Common.CommonUtils import *
from Core.Provider import ConfigProvider

class TDX_GW(object):

    __lc_min_bar_reader = None
    __tdx_api = None
    __connected_ip = '119.147.212.81'
    __connected_port = 7709

    def __init__(self):
        self.__lc_min_bar_reader = lc_min_bar_reader.TdxLCMinBarReader()
        self.__block_reader = block_reader.BlockReader()
        self.__tdx_api = TdxHq_API()
        self.__cfg_provider = ConfigProvider.ConfigProvider()


    def get_local_stock_bars(self, file_path: str):
        # start = time.time()
        # df = self.__lc_min_bar_reader.get_df(file_path)
        data = self.__lc_min_bar_reader.parse_data_by_file(file_path)
        df = pd.DataFrame(data=data)
        # df = df['date', 'open', 'high', 'low', 'close', 'amount', 'volume']
        # print(f"TDX get 1min bar time spent: {(time.time() - start) * 1000} ms")

        return df[['date', 'open', 'high', 'low', 'close', 'amount', 'volume']]

    def get_local_block(self):
        file_path = self.__cfg_provider.get_tdx_block_directory_path()
        return self.__block_reader.get_df(file_path, BlockReader_TYPE_GROUP)

    def get_realtime_stock_1min_bars(self, stock_id: str):
        with self.__tdx_api.connect(self.__connected_ip, self.__connected_port):
            df = self.__tdx_api.to_df(
                self.__tdx_api.get_security_bars(8, 0, stock_id, 0, 10))  # 返回DataFrame
            return df

    def get_realtime_stocks_quotes(self, stock_ids: []):
        stock_list = []
        for id in stock_ids:
            stock_list.append((get_stock_market(id), id))
        with self.__tdx_api.connect(self.__connected_ip, self.__connected_port):
            return self.__tdx_api.get_security_quotes(stock_list)

    def test(self):
        with self.__tdx_api.connect(self.__connected_ip, self.__connected_port):
            return self.__tdx_api.to_df(
                # self.__tdx_api.get_history_minute_time_data(31, "00020", 20190808)
                # self.__tdx_api.get_instrument_bars(TDXParams.KLINE_TYPE_DAILY, 8, "10000843", 0, 100)
                # self.__tdx_api.get_block_info()
            )

