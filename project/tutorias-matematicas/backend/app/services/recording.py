import os
import uuid
from datetime import datetime
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from app.core.config import settings
from app.utils.database import get_database

class RecordingMetadata(BaseModel):
    session_id: str
    recording_type: str  # 'video', 'whiteboard', 'combined'
    file_path: str
    duration: float
    created_at: datetime = datetime.now()

async def save_recording(file_data: bytes, metadata: RecordingMetadata):
    db = get_database()
    fs = AsyncIOMotorGridFSBucket(db)
    
    filename = f"{metadata.session_id}_{metadata.recording_type}_{uuid.uuid4()}.mp4"
    file_id = await fs.upload_from_stream(
        filename, 
        file_data, 
        metadata=metadata.dict()
    )
    
    return str(file_id)

async def get_recording(recording_id: str):
    db = get_database()
    fs = AsyncIOMotorGridFSBucket(db)
    
    file = await fs.open_download_stream(recording_id)
    metadata = file.metadata
    content = await file.read()
    
    return content, metadata