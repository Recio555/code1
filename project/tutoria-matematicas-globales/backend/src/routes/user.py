from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from bson import ObjectId

from database import get_async_db
from models.models import User, UserCreate, UserInDB
from services.auth_service import get_password_hash, get_current_active_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_tutors():
    return {"message": "Lista de tutores"}

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db=Depends(get_async_db)):
    """
    Create a new user
    """
    # Check if username exists
    if await db["users"].find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Check if email exists
    if await db["users"].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    now = datetime.utcnow()
    hashed_password = get_password_hash(user.password)
    
    user_dict = user.dict()
    del user_dict["password"]
    new_user = {
        **user_dict,
        "hashed_password": hashed_password,
        "created_at": now,
        "updated_at": now
    }
    
    result = await db["users"].insert_one(new_user)
    new_user["_id"] = result.inserted_id
    
    return new_user

@router.get("/me", response_model=User)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    """
    Get current user
    """
    return current_user

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str, db=Depends(get_async_db)):
    """
    Get a user by ID
    """
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user