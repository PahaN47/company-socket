# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chat.grpc import message_grpc_pb2 as message__grpc_dot_grpc_dot_message__grpc__pb2


class MessageControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
            "/company_back.message_grpc.MessageController/Create",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.SerializeToString,
            response_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
        )
        self.Destroy = channel.unary_unary(
            "/company_back.message_grpc.MessageController/Destroy",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageDestroyRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
        self.List = channel.unary_unary(
            "/company_back.message_grpc.MessageController/List",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListRequest.SerializeToString,
            response_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListResponse.FromString,
        )
        self.PartialUpdate = channel.unary_unary(
            "/company_back.message_grpc.MessageController/PartialUpdate",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessagePartialUpdateRequest.SerializeToString,
            response_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
        )
        self.Retrieve = channel.unary_unary(
            "/company_back.message_grpc.MessageController/Retrieve",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRetrieveRequest.SerializeToString,
            response_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
        )
        self.Update = channel.unary_unary(
            "/company_back.message_grpc.MessageController/Update",
            request_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.SerializeToString,
            response_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
        )


class MessageControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MessageControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.FromString,
            response_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.SerializeToString,
        ),
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageDestroyRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListRequest.FromString,
            response_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListResponse.SerializeToString,
        ),
        "PartialUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.PartialUpdate,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessagePartialUpdateRequest.FromString,
            response_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.SerializeToString,
        ),
        "Retrieve": grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRetrieveRequest.FromString,
            response_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.FromString,
            response_serializer=message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "company_back.message_grpc.MessageController", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MessageController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/Create",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.SerializeToString,
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Destroy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/Destroy",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/List",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListRequest.SerializeToString,
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PartialUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/PartialUpdate",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessagePartialUpdateRequest.SerializeToString,
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Retrieve(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/Retrieve",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRetrieveRequest.SerializeToString,
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/company_back.message_grpc.MessageController/Update",
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageRequest.SerializeToString,
            message__grpc_dot_grpc_dot_message__grpc__pb2.MessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
