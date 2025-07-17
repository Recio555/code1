from fastapi import APIRouter, Depends
from pymongo.database import Database
from db.connection import get_database
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
from pymongo import MongoClient
from pymongo.collection import Collection
import os
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from schemas import UserCreate

from models import user_helper
from auth import hash_password, verify_password, create_access_token
from bson.objectid import ObjectId
import os


router = APIRouter()


db = get_database()
user_collection = db["users"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

# Función para obtener el usuario autenticado desde el token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = user_collection.find_one({"email": email})
    if user is None:
        raise credentials_exception
    return user_helper(user)

@router.post("/register")
def register(user: UserCreate):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    hashed = hash_password(user.password)
    user_doc = {"email": user.email, "password": hashed}
    res = user_collection.insert_one(user_doc)
    return {"id": str(res.inserted_id), "email": user.email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_collection.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me") # type: ignore
def read_me(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}

@router.get("/")
def root():
    return {"message": "API de login, registro y usuario autenticado"}


# __________________________________________________________________________
@router.get("/users/{username}")
async def get_user(username: str):
    db = get_database()
    collection = db["users"]
    user = collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Convertir el _id de ObjectId a string para devolverlo correctamente
    user["_id"] = str(user["_id"])
    return user
    


@router.get("/app/{persona}")
def get_tutors(persona: str, db: Database = Depends(get_database)):
    print("Base de datos activa:", db.name)
    collection = db["users"]
    lis = db.list_collection_names()
    print("Colecciones existentes:", lis)
    return {"colecciones": lis}
    
 
@router.get("/debug")
def debug(db: Database = Depends(get_database)):
    print("Colecciones:", db.list_collection_names())
    usuarios = db["users"] 
    print(usuarios)
    return {"colecciones": db.list_collection_names()}
 
 
@router.post("/users/{username}")
async def register_user(username: str):
    MONGODB_URI = os.getenv("MONGODB_URI")
    client = MongoClient(MONGODB_URI)
    db = client["personadb"]
    collection = db["users"]
    user_data = {
        "username": username,
        "email": "Salvador@gmail.com",
        "role": "user"
    }
    result = collection.insert_one(user_data)
    return {"message": "Usuario insertado", "id": str(result.inserted_id)}