from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from models.models import SessionCreate, SessionInDB

class SessionService:
    def __init__(self, db=None):
        self.db = db
        self.collection = self.db["sessions"] if db else None
    
    async def get_session(self, session_id: str) -> Optional[dict]:
        """
        Get a session by ID
        """
        if not ObjectId.is_valid(session_id):
            return None
        return await self.collection.find_one({"_id": ObjectId(session_id)})
    
    async def get_user_sessions(self, user_id: str, skip: int = 0, limit: int = 100) -> List[dict]:
        """
        Get all sessions for a specific user
        """
        if not ObjectId.is_valid(user_id):
            return []
        cursor = self.collection.find({"user_id": ObjectId(user_id)}).skip(skip).limit(limit)
        return await cursor.to_list(length=limit)
    
    async def create_session(self, session: SessionCreate, user_id: str) -> dict:
        """
        Create a new session for a user
        """
        now = datetime.utcnow()
        session_dict = session.dict()
        new_session = {
            **session_dict,
            "user_id": ObjectId(user_id),
            "created_at": now,
            "updated_at": now,
            "is_active": True
        }
        
        result = await self.collection.insert_one(new_session)
        new_session["_id"] = result.inserted_id
        return new_session
    
    async def delete_session(self, session_id: str) -> bool:
        """
        Delete a session
        """
        if not ObjectId.is_valid(session_id):
            return False
        result = await self.collection.delete_one({"_id": ObjectId(session_id)})
        return result.deleted_count > 0