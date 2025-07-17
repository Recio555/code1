from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from datetime import datetime
import json
import uuid

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, websocket: WebSocket, room_id: str):
        if room_id in self.active_connections:
            self.active_connections[room_id].remove(websocket)

    async def broadcast(self, message: dict, room_id: str):
        if room_id in self.active_connections:
            for connection in self.active_connections[room_id]:
                await connection.send_json(message)

manager = ConnectionManager()

@router.websocket("/ws/class/{room_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, user_id: str):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            message['timestamp'] = str(datetime.now())
            message['user_id'] = user_id
            
            if message['type'] == 'whiteboard':
                # Guardar estado del pizarrón en MongoDB
                pass
            
            await manager.broadcast(message, room_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room_id)
        await manager.broadcast({
            "type": "notification",
            "message": f"User {user_id} left the class",
            "timestamp": str(datetime.now())
        }, room_id)

@router.get("/sessions/upcoming", response_model=list[dict])
async def get_upcoming_sessions(user_id: str):
    # Implementar lógica para obtener sesiones próximas
    return []