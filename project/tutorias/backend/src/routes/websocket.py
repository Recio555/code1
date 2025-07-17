import socketio
from fastapi.middleware.cors import CORSMiddleware
from socketio import ASGIApp
import jwt

SECRET_KEY = "tu_clave_secreta_segura"
ALGORITHM = "HS256"

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

# Guarda usuarios por sala para poder emitir mensajes solo a los miembros
rooms = {}

@sio.event
async def connect(sid, environ):
    print(f"✅ Cliente conectado: {sid}")

@sio.event
async def disconnect(sid):
    print(f"❌ Cliente desconectado: {sid}")
    # Elimina el usuario de las salas que esté y avisa a otros
    for room_id, members in list(rooms.items()):
        if sid in members:
            members.remove(sid)
            await sio.emit("user-left", {"sid": sid}, room=room_id)
            if not members:
                del rooms[room_id]

@sio.event
async def join(sid, data):
    room_id = data.get("room")
    if not room_id:
        await sio.disconnect(sid)
        return
    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(sid)
    await sio.enter_room(sid, room_id)
    print(f"Cliente {sid} se unió a la sala {room_id}")
    await sio.emit("user-joined", {"sid": sid}, room=room_id, skip_sid=sid)

@sio.event
async def offer(sid, data):
    to_sid = data.get("to")
    print(f"📡 Oferta recibida de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("offer", data, to=to_sid)

@sio.event
async def answer(sid, data):
    to_sid = data.get("to")
    print(f"🔁 Respuesta recibida de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("answer", data, to=to_sid)

@sio.event
async def ice_candidate(sid, data):
    to_sid = data.get("to")
    print(f"🧊 ICE candidate de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("ice-candidate", data, to=to_sid)


def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("❌ Token expirado")
    except jwt.InvalidTokenError:
        print("❌ Token inválido")
    return None

@sio.event
async def connect(sid, environ):
    query_string = environ.get('QUERY_STRING', '')
    session_token = None

    # Extraer sessionId (JWT)
    for param in query_string.split("&"):
        if param.startswith("sessionId="):
            session_token = param.split("=")[1]

    if not session_token:
        print(f"❌ Conexión rechazada (sin token) para SID: {sid}")
        return False

    user_data = decode_jwt(session_token)
    if not user_data:
        print(f"❌ Token JWT inválido. Rechazando conexión para SID: {sid}")
        return False

    print(f"✅ Cliente conectado: {sid}, usuario: {user_data}")
    await sio.save_session(sid, {"user": user_data})
    return True  # Aceptar conexión

@sio.event
async def disconnect(sid):
    print(f"❌ Cliente desconectado: {sid}")
    for room_id, members in list(rooms.items()):
        if sid in members:
            members.remove(sid)
            await sio.emit("user-left", {"sid": sid}, room=room_id)
            if not members:
                del rooms[room_id]

@sio.event
async def join(sid, data):
    room_id = data.get("room")
    if not room_id:
        await sio.disconnect(sid)
        return
    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(sid)
    await sio.enter_room(sid, room_id)
    print(f"📥 Cliente {sid} se unió a la sala {room_id}")
    await sio.emit("user-joined", {"sid": sid}, room=room_id, skip_sid=sid)

@sio.event
async def offer(sid, data):
    to_sid = data.get("to")
    print(f"📡 Oferta recibida de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("offer", data, to=to_sid)

@sio.event
async def answer(sid, data):
    to_sid = data.get("to")
    print(f"🔁 Respuesta recibida de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("answer", data, to=to_sid)

@sio.event
async def ice_candidate(sid, data):
    to_sid = data.get("to")
    print(f"🧊 ICE candidate de {sid} para {to_sid}")
    if to_sid:
        await sio.emit("ice-candidate", data, to=to_sid)

