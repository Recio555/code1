import os
from fastapi import WebSocket
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCIceServer
from dotenv import load_dotenv

load_dotenv()

class WebRTCManager:
    def __init__(self):
        self.ice_servers = [
            RTCIceServer(urls="stun:stun.l.google.com:19302"),
            RTCIceServer(
                urls=os.getenv("TURN_SERVER_URL"),
                username=os.getenv("TURN_USERNAME"),
                credential=os.getenv("TURN_CREDENTIAL")
            )
        ]
        self.active_connections = {}

    async def handle_offer(self, websocket: WebSocket, offer: dict, room_id: str):
        pc = RTCPeerConnection()
        self.active_connections[room_id] = pc

        @pc.on("icecandidate")
        async def on_icecandidate(candidate):
            await websocket.send_json({
                "type": "ice_candidate",
                "candidate": candidate.to_json()
            })

        await pc.setRemoteDescription(
            RTCSessionDescription(sdp=offer["sdp"], type=offer["type"])
        )
        
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)

        return {
            "sdp": pc.localDescription.sdp,
            "type": pc.localDescription.type
        }

    async def add_ice_candidate(self, room_id: str, candidate: dict):
        if room_id in self.active_connections:
            pc = self.active_connections[room_id]
            await pc.addIceCandidate(candidate)