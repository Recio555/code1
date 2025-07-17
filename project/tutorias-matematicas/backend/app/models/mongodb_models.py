from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from app.core.config import settings

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserRole(str, Enum):
    STUDENT = "student"
    TUTOR = "tutor"
    ADMIN = "admin"

class Language(str, Enum):
    SPANISH = "es"
    ENGLISH = "en"
    FRENCH = "fr"
    GERMAN = "de"
    PORTUGUESE = "pt"

class MathTopic(str, Enum):
    ALGEBRA = "algebra"
    CALCULUS = "calculus"
    GEOMETRY = "geometry"
    STATISTICS = "statistics"
    TRIGONOMETRY = "trigonometry"
    LINEAR_ALGEBRA = "linear_algebra"
    DIFFERENTIAL_EQUATIONS = "differential_equations"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    preferred_language: Language = Language.SPANISH
    timezone: str = "UTC"

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    role: UserRole = UserRole.STUDENT

class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    role: UserRole
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    disabled: bool = False
    email_verified: bool = False

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class TutorProfile(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId = Field(...)
    bio: str = Field(..., min_length=50, max_length=1000)
    qualifications: List[str] = Field(..., min_items=1)
    languages_spoken: List[Language] = Field(..., min_items=1)
    math_topics: List[MathTopic] = Field(..., min_items=1)
    hourly_rate: float = Field(..., gt=0)
    availability: Dict[str, List[str]]  # {"day": ["time_slots"]}
    rating: Optional[float] = Field(None, ge=0, le=5)
    reviews_count: int = 0
    profile_picture: Optional[str] = None
    teaching_style: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class SessionStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Session(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    tutor_id: PyObjectId = Field(...)
    student_id: PyObjectId = Field(...)
    start_time: datetime
    end_time: datetime
    math_topic: MathTopic
    language: Language
    status: SessionStatus = SessionStatus.SCHEDULED
    notes: Optional[str] = None
    whiteboard_data: Optional[Dict] = None
    recording_url: Optional[str] = None
    files_shared: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class Review(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    session_id: PyObjectId = Field(...)
    tutor_id: PyObjectId = Field(...)
    student_id: PyObjectId = Field(...)
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=500)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class WhiteboardSession(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    session_id: PyObjectId = Field(...)
    tab_id: int = Field(..., ge=1)
    canvas_data: Dict
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class Recording(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    session_id: PyObjectId = Field(...)
    file_path: str
    duration: float  # in minutes
    recording_type: str  # video, whiteboard, combined
    created_at: datetime = Field(default_factory=datetime.utcnow)
    size: float  # in MB

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class SharedFile(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    session_id: PyObjectId = Field(...)
    uploader_id: PyObjectId = Field(...)
    file_name: str
    file_type: str
    file_size: float  # in MB
    s3_key: str  # or equivalent storage reference
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True

class StudentProgress(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    student_id: PyObjectId = Field(...)
    math_topic: MathTopic
    proficiency_level: float = Field(0, ge=0, le=1)
    last_session: Optional[datetime] = None
    sessions_count: int = 0
    improvement_areas: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True