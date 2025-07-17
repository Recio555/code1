from fastapi import WebSocket
from typing import Dict, List
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {}
        self.rooms_data: Dict[str, Dict] = {}

    async def connect(self, websocket: WebSocket, room_id: str, user_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = {}
            self.rooms_data[room_id] = {"participants": [], "chat": []}
        
        self.active_connections[room_id][user_id] = websocket
        self.rooms_data[room_id]["participants"].append(user_id)
        await self._broadcast_room_update(room_id)

    async def disconnect(self, room_id: str, user_id: str):
        if room_id in self.active_connections and user_id in self.active_connections[room_id]:
            del self.active_connections[room_id][user_id]
            self.rooms_data[room_id]["participants"].remove(user_id)
            await self._broadcast_room_update(room_id)

    async def _broadcast_room_update(self, room_id: str):
        if room_id in self.active_connections:
            for connection in self.active_connections[room_id].values():
                await connection.send_json({
                    "type": "room_update",
                    "participants": self.rooms_data[room_id]["participants"]
                })

    async def broadcast_chat_message(self, room_id: str, message: dict):
        if room_id in self.rooms_data:
            self.rooms_data[room_id]["chat"].append(message)
            for connection in self.active_connections[room_id].values():
                await connection.send_json({
                    "type": "chat_message",
                    "data": message
                })

manager = ConnectionManager()