from fastapi import APIRouter

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt, JWTError
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import os
from db.connection import get_database


def get_collection():
    db = get_database()
    return db["users"]
# Configuración manual (puedes reemplazar con variables de entorno si quieres)
#MONGO_URI = "mongodb+srv://<usuario>:<clave>@<cluster>.mongodb.net/?retryWrites=true&w=majority"
JWT_SECRET = "supersecretkey"
JWT_ALGORITHM = "HS256"


router = APIRouter()


# Seguridad
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Modelos
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Utilidades
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"]
    }

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_collection().find_one({"email": email})
    if user is None:
        raise credentials_exception
    return user_helper(user)

# Endpoints
@router.post("/register")
def register(user: UserCreate):
    user_collection = get_collection()
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    hashed = hash_password(user.password)
    user_doc = {"email": user.email, "password": hashed}
    res = user_collection.insert_one(user_doc)
    return {"id": str(res.inserted_id), "email": user.email}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_collection().find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def read_me(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}

@router.get("/")
def root():
    return {"message": "API de login, registro y ruta protegida con FastAPI y MongoDB"}