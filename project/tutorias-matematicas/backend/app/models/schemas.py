from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field, EmailStr, validator
from bson import ObjectId
from app.models.mongodb_models import PyObjectId, MathTopic, Language

# --------------------------
# COMMON SCHEMAS
# --------------------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    scopes: List[str] = []

# --------------------------
# USER SCHEMAS
# --------------------------

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    preferred_language: Language = Language.SPANISH
    timezone: str = "UTC"

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    role: str = "student"

    @validator('role')
    def validate_role(cls, v):
        if v not in ["student", "tutor", "admin"]:
            raise ValueError("Invalid role")
        return v

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    preferred_language: Optional[Language] = None
    timezone: Optional[str] = None
    profile_picture: Optional[str] = None

class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    role: str
    hashed_password: str
    created_at: datetime
    disabled: bool = False
    email_verified: bool = False
    profile_picture: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class UserPublic(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    role: str
    profile_picture: Optional[str] = None

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# TUTOR SCHEMAS
# --------------------------

class TutorProfileBase(BaseModel):
    bio: str = Field(..., min_length=50, max_length=1000)
    qualifications: List[str] = Field(..., min_items=1)
    languages_spoken: List[Language] = Field(..., min_items=1)
    math_topics: List[MathTopic] = Field(..., min_items=1)
    hourly_rate: float = Field(..., gt=0)
    teaching_style: Optional[str] = None

class TutorProfileCreate(TutorProfileBase):
    availability: Dict[str, List[str]] = Field(..., example={"Monday": ["09:00", "10:00"]})

class TutorProfileUpdate(BaseModel):
    bio: Optional[str] = None
    qualifications: Optional[List[str]] = None
    languages_spoken: Optional[List[Language]] = None
    math_topics: Optional[List[MathTopic]] = None
    hourly_rate: Optional[float] = None
    teaching_style: Optional[str] = None
    availability: Optional[Dict[str, List[str]]] = None

class TutorProfilePublic(TutorProfileBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    rating: Optional[float] = None
    reviews_count: int = 0
    profile_picture: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# SESSION SCHEMAS
# --------------------------

class SessionBase(BaseModel):
    tutor_id: PyObjectId
    student_id: PyObjectId
    start_time: datetime
    end_time: datetime
    math_topic: MathTopic
    language: Language
    notes: Optional[str] = None

class SessionCreate(SessionBase):
    pass

class SessionUpdate(BaseModel):
    notes: Optional[str] = None
    status: Optional[str] = None

    @validator('status')
    def validate_status(cls, v):
        if v and v not in ["scheduled", "in_progress", "completed", "cancelled"]:
            raise ValueError("Invalid session status")
        return v

class SessionPublic(SessionBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    status: str
    whiteboard_data: Optional[Dict] = None
    recording_url: Optional[str] = None
    files_shared: List[str] = []
    created_at: datetime
    tutor_details: Optional[Dict] = None
    student_details: Optional[Dict] = None

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# WHITEBOARD SCHEMAS
# --------------------------

class WhiteboardUpdate(BaseModel):
    canvas_data: Dict
    tab_id: int = Field(1, ge=1)

class WhiteboardPublic(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    session_id: PyObjectId
    tab_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# REVIEW SCHEMAS
# --------------------------

class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=500)

class ReviewCreate(ReviewBase):
    session_id: PyObjectId
    tutor_id: PyObjectId

class ReviewPublic(ReviewBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    student_id: PyObjectId
    student_name: str
    created_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# FILE SCHEMAS
# --------------------------

class FileUpload(BaseModel):
    session_id: PyObjectId
    file_type: str

class FilePublic(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    file_name: str
    file_type: str
    file_size: float
    uploader_name: str
    created_at: datetime

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# PROGRESS SCHEMAS
# --------------------------

class ProgressUpdate(BaseModel):
    math_topic: MathTopic
    proficiency_level: float = Field(..., ge=0, le=1)
    improvement_areas: Optional[List[str]] = None

class ProgressPublic(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    math_topic: MathTopic
    proficiency_level: float
    sessions_count: int
    last_session: Optional[datetime] = None
    improvement_areas: List[str] = []

    class Config:
        json_encoders = {ObjectId: str}

# --------------------------
# WEBRTC SCHEMAS
# --------------------------

class WebRTCOffer(BaseModel):
    sdp: str
    type: str

class WebRTCAnswer(BaseModel):
    sdp: str
    type: str

class WebRTCIceCandidate(BaseModel):
    candidate: str
    sdpMid: str
    sdpMLineIndex: int

# --------------------------
# SEARCH & FILTER SCHEMAS
# --------------------------

class TutorSearchFilters(BaseModel):
    languages: Optional[List[Language]] = None
    math_topics: Optional[List[MathTopic]] = None
    min_rating: Optional[float] = Field(None, ge=0, le=5)
    max_rate: Optional[float] = Field(None, gt=0)
    availability: Optional[Dict[str, List[str]]] = None

class SessionFilters(BaseModel):
    status: Optional[str] = None
    math_topic: Optional[MathTopic] = None
    language: Optional[Language] = None
    date_range: Optional[Dict[str, datetime]] = None