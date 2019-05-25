from channels.generic.websocket import AsyncWebsocketConsumer
import json

# A consumer accepts WebSocket connections.
# Receives messages from its client
# and echos those messages back to the same client.

# Every consumer instance has an automatically generated unique channel name
# and so can be communicated with via a channel layer.

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtain the 'room_name' parameter from the URL route
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Constructs a Channels group name
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accepts the WebSocket connection.
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Send an event to a group.

        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))