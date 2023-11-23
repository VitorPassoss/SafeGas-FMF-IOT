from channels.generic.websocket import AsyncWebsocketConsumer
import json




class IotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = f"iot"
        await self.accept()
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

    async def disconnect(self, _):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "iot_message",
                    "data": text_data_json,
                },
            )

    async def iot_message(self, event):
        await self.send(text_data=json.dumps(event))