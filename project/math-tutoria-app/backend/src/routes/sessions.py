from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from database import get_async_db
from models.models import Session, SessionCreate, UserInDB
from services.auth_service import get_current_active_user
from services.session_service import SessionService

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
    responses={404: {"description": "Not found"}}
)

async def get_session_service(db=Depends(get_async_db)):
    return SessionService(db=db)

@router.get("/", response_model=List[Session])
async def get_sessions(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_user),
    session_service: SessionService = Depends(get_session_service)
):
    """
    Get all sessions for the current user
    """
    sessions = await session_service.get_user_sessions(
        user_id=str(current_user.id), 
        skip=skip, 
        limit=limit
    )
    return sessions

@router.post("/", response_model=Session, status_code=status.HTTP_201_CREATED)
async def create_session(
    session: SessionCreate,
    current_user: UserInDB = Depends(get_current_active_user),
    session_service: SessionService = Depends(get_session_service)
):
    """
    Create a new session for the current user
    """
    created_session = await session_service.create_session(
        session=session, 
        user_id=str(current_user.id)
    )
    return created_session

@router.get("/{session_id}", response_model=Session)
async def get_session(
    session_id: str,
    current_user: UserInDB = Depends(get_current_active_user),
    session_service: SessionService = Depends(get_session_service)
):
    """
    Get a specific session by ID
    """
    session = await session_service.get_session(session_id=session_id)
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Check if session belongs to current user
    if str(session["user_id"]) != str(current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to access this session")
    
    return session

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_session(
    session_id: str,
    current_user: UserInDB = Depends(get_current_active_user),
    session_service: SessionService = Depends(get_session_service)
):
    """
    Delete a specific session by ID
    """
    # First check if session exists and belongs to user
    session = await session_service.get_session(session_id=session_id)
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Check if session belongs to current user
    if str(session["user_id"]) != str(current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to delete this session")
    
    # Delete the session
    deleted = await session_service.delete_session(session_id=session_id)
    
    if not deleted:
        raise HTTPException(status_code=500, detail="Failed to delete session")
    
    return None

