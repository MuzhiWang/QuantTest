from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection

from IDL import TdxReader_pb2
from IDL import TdxReader_pb2_grpc

class TdxReader(TdxReader_pb2_grpc.TdxReaderServicer):

    def Hello(self, request, context):
        return TdxReader_pb2.HelloReply(message='Hello %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TdxReader_pb2_grpc.add_TdxReaderServicer_to_server(TdxReader(), server)

    SERVICE_NAMES = (
        TdxReader_pb2.DESCRIPTOR.services_by_name['TdxReader'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print("start gRPC service: TdxReader")
    serve()