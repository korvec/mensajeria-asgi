import json
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#
#         self.group_name = 'test'
#
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name,
#             self.channel_name
#         )
#         self.accept()
#
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     def chat_message(self, event):
#         message = event['message']
#         self.send(text_data = json.dumps({
#             'type': 'chat',
#             'message': message
#         }))


# Otra forma con async y await:
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'test'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        content = {
            'type': 'acknowledge',
            'message': 'ACK'
        }
        await self.send(text_data = json.dumps(content))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        content = {
            'type': 'chat_message',
            'message': message
        }
        await self.channel_layer.group_send(self.group_name, content)

    async def chat_message(self, event):
        message = event['message']
        content = {
            'type': 'chat',
            'message': message
        }
        await self.send(text_data = json.dumps(content))
