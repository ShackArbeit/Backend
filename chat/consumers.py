import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room,Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()
