# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.ProphetModel_pb2 as ProphetModel__pb2


class ProphetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.forecast = channel.unary_unary(
                '/net.livemood.bdc.prophet.proto.ProphetService/forecast',
                request_serializer=ProphetModel__pb2.ProphetRequest.SerializeToString,
                response_deserializer=ProphetModel__pb2.Response.FromString,
                )


class ProphetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def forecast(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProphetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'forecast': grpc.unary_unary_rpc_method_handler(
                    servicer.forecast,
                    request_deserializer=ProphetModel__pb2.ProphetRequest.FromString,
                    response_serializer=ProphetModel__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'net.livemood.bdc.prophet.proto.ProphetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProphetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def forecast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.livemood.bdc.prophet.proto.ProphetService/forecast',
            ProphetModel__pb2.ProphetRequest.SerializeToString,
            ProphetModel__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
