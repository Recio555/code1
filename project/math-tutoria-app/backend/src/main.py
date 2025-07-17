from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os
from datetime import datetime, timedelta
from typing import Optional

from app.routes import users, auth, sessions

app = FastAPI(title="Math Tutoring API")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambiar a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variables globales para la conexión a MongoDB
mongo_client = None
db = None

@app.on_event("startup")
async def startup_db_client():
    global mongo_client, db
    mongo_uri = os.environ.get("MONGODB_URI")
    if not mongo_uri:
        raise Exception("MONGODB_URI environment variable not set")
    mongo_client = AsyncIOMotorClient(mongo_uri)
    db = mongo_client.get_database()
    print("Connected to MongoDB Atlas")

@app.on_event("shutdown")
async def shutdown_db_client():
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("MongoDB connection closed")

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de Tutoría de Matemáticas"}

# Ejemplo de modelo de usuario
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: Optional[bool] = None

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

# Incluir routers
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(sessions.router)