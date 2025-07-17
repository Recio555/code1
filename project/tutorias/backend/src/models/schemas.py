from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
#from models.mongodb_models import PyObjectId

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    #id: PyObjectId
    role: str
    created_at: datetime

    class Config:
        #json_encoders = {PyObjectId: str}
        pass