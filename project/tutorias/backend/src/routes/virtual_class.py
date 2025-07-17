from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends,  HTTPException
from services.websocket_manager import manager
from utils.dependencies import get_current_user
from models.schemas import UserPublic
from datetime import datetime, timezone
import logging
from db.connection import get_collection
from uuid import uuid4
from pydantic import BaseModel
from db.connection import get_database



def get_collection():
    db = get_database()
    return db["users"]

logger = logging.getLogger(__name__)

router = APIRouter()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    room_id: str,
    current_user: UserPublic = Depends(get_current_user)
):
    await manager.connect(websocket, room_id, str(current_user.id))
    logger.info(f"User {current_user.full_name} connected to room {room_id}")

    try:
        while True:
            try:
                data = await websocket.receive_json()
            except Exception:
                await websocket.send_json({"type": "error", "message": "Invalid JSON"})
                continue

            if data["type"] == "chat_message":
                message = {
                    "user_id": str(current_user.id),
                    "user_name": current_user.full_name,
                    "content": data["content"],
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                await manager.broadcast_chat_message(room_id, message)
                logger.info(f"[{room_id}] {current_user.full_name}: {data['content']}")
            else:
                await websocket.send_json({
                    "type": "error",
                    "message": f"Unknown message type: {data['type']}"
                })

    except WebSocketDisconnect:
        await manager.disconnect(room_id, str(current_user.id))
        logger.info(f"User {current_user.full_name} disconnected from room {room_id}")

# Datos simulados
fake_sessions = {
    "abc123": {"title": "Sesión de Matemáticas", "tutor": "Juan"},
    "xyz789": {"title": "Sesión de Física", "tutor": "Ana"},
}

@router.get("/sessions/{session_id}")
def get_session(session_id: str):
    session = fake_sessions.get(session_id)
    print(session)
    if not session:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return session

class Session(BaseModel):
    session_id: str

@router.post("/create-session")
def create_session():
    session_id = str(uuid4())[:8]  # ejemplo: 8 caracteres únicos
    #return {"session_id": session_id}
    user_collection = get_collection()
    #user_collection.insert_one({"session_id": session_id})
    return {"session_id": session_id}

