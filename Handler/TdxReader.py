from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection

from Common.Log.Logger import Logger
from IDL import TdxReader_pb2
from IDL import TdxReader_pb2_grpc
from Gateway import Tdx
from Config.StockConfig import StockDataType

class TdxReader(TdxReader_pb2_grpc.TdxReaderServicer):

    __tdx_gw = None
    logger = None

    def __init__(self):
        self.__tdx_gw = Tdx.TDX_GW()
        self.logger = Logger.get_logger(__name__)

    def Hello(self, request, context):
        return TdxReader_pb2.HelloReply(message='Hello %s!' % request.name)

    def ReadTdxFile(self, request, context):
        if request.filePath is None or request.metric is None:
            return Exception("none file path or metric")

        stock_data_type = StockDataType.UNDEFINED
        if request.metric == TdxReader_pb2.ONE_MIN or request.metric == TdxReader_pb2.FIVE_MIN:
            stock_data_type = StockDataType.ONE_MIN
        elif request.metric == TdxReader_pb2.ONE_DAY:
            stock_data_type = StockDataType.DAILY

        data =  self.__tdx_gw.get_local_stock_bars_raw_data(
            file_path=request.filePath, stock_date_type=stock_data_type)

        stock_data = []
        for d in data:
            stock_data.append(TdxReader_pb2.StockData(
                dateTime=d['date'],
                open=d['open'],
                close=d['close'],
                high=d['high'],
                low=d['low'],
                amount=d['amount'],
                volume=d['volume']))

        return TdxReader_pb2.TdxFileData(data=stock_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tdx_reader = TdxReader()
    TdxReader_pb2_grpc.add_TdxReaderServicer_to_server(tdx_reader, server)

    SERVICE_NAMES = (
        TdxReader_pb2.DESCRIPTOR.services_by_name['TdxReader'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    tdx_reader.logger.debug("TdxReader gRPC server launched")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print("start gRPC service: TdxReader")
    serve()