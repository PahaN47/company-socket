import json
import grpc

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .grpc import message_grpc_pb2_grpc, message_grpc_pb2


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json["type"]
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = message_grpc_pb2_grpc.MessageControllerStub(channel)

            if type == "send":
                response = stub.Create(
                    message_grpc_pb2.MessageRequest(
                        chat=text_data_json["chat"], user=text_data_json["user"], message=text_data_json["message"]
                    )
                )
                data = {
                    "id": response.id,
                    "chat": response.chat,
                    "user": response.user,
                    "message": response.message,
                    "date": response.date,
                    "type": "send",
                }

                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name, {"type": "send_message", "data": data}
                )
            elif type == "delete":
                response = stub.Destroy(message_grpc_pb2.MessageDestroyRequest(id=text_data_json["id"]))

                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {"type": "delete_message", "data": {"id": text_data_json["id"], "type": "delete"}},
                )

    def send_message(self, event):
        data = event["data"]

        self.send(text_data=json.dumps(data))

    def delete_message(self, event):
        data = event["data"]

        self.send(text_data=json.dumps(data))
