from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List
import json
from app.models.schemas import WhiteboardState

router = APIRouter()

class WhiteboardManager:
    def __init__(self):
        self.boards: Dict[str, Dict[int, WhiteboardState]] = {}  # {room_id: {tab_id: state}}

    async def update_whiteboard(self, room_id: str, tab_id: int, data: dict):
        if room_id not in self.boards:
            self.boards[room_id] = {}
        
        self.boards[room_id][tab_id] = WhiteboardState(**data)
        
    def get_whiteboard(self, room_id: str, tab_id: int):
        return self.boards.get(room_id, {}).get(tab_id)

manager = WhiteboardManager()

@router.websocket("/ws/whiteboard/{room_id}/{user_id}")
async def whiteboard_websocket(
    websocket: WebSocket, 
    room_id: str, 
    user_id: str
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "get_state":
                tab_id = data["tab_id"]
                state = manager.get_whiteboard(room_id, tab_id)
                await websocket.send_json({
                    "type": "state_update",
                    "tab_id": tab_id,
                    "data": state.dict() if state else None
                })
            elif data["type"] == "state_update":
                tab_id = data["tab_id"]
                await manager.update_whiteboard(room_id, tab_id, data["state"])
                # Broadcast to other users in room
                
    except WebSocketDisconnect:
        pass