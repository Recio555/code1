from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum
from bson import ObjectId

class SessionStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class MathTopic(str, Enum):
    ALGEBRA = "algebra"
    GEOMETRY = "geometry"
    CALCULUS = "calculus"
    STATISTICS = "statistics"
    TRIGONOMETRY = "trigonometry"
    ARITHMETIC = "arithmetic"
    OTHER = "other"

class SessionBase(BaseModel):
    title: str
    description: Optional[str] = None
    topic: MathTopic
    start_time: datetime
    end_time: datetime
    tutor_id: str
    student_id: str
    price: Optional[float] = None

class SessionCreate(SessionBase):
    pass

class SessionInDB(SessionBase):
    id: str = Field(alias="_id")
    status: SessionStatus = SessionStatus.SCHEDULED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    notes: Optional[str] = None
    
    class Config:
        populate_by_name = True

class Session(SessionBase):
    id: str
    status: SessionStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    notes: Optional[str] = None
    
    class Config:
        populate_by_name = True

class SessionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    topic: Optional[MathTopic] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[SessionStatus] = None
    notes: Optional[str] = None
    price: Optional[float] = None