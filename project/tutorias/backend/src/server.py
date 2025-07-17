from contextlib import asynccontextmanager
import os
import sys
from fastapi import FastAPI, status
from pydantic import BaseModel
import uvicorn
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from routes import test, user, websocket
from routes import  virtual_class
from core.config import settings




COLLECTION_NAME = "user"
DB_NAME = "personadb"
MONGODB_URI = os.environ["MONGODB_URI"]
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, database, collection
    client = MongoClient(MONGODB_URI)
    database = client[DB_NAME]
    pong =  database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")
    todo_lists = database.get_collection(COLLECTION_NAME)
    todo_lists = database[COLLECTION_NAME]
    yield
    client.close()

app = FastAPI(lifespan=lifespan, debug=DEBUG)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/session/{session_id}")
async def get_session(session_id: str):
    return {"message": f"Estás en la sesión {session_id}"}


# RUTAS
#app.include_router(test.router)
#app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
#app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(virtual_class.router, prefix="/api/v1/virtual-class", tags=["virtual-class"])
app.include_router(user.router,  prefix="/auth")




# ejecuta la aplicacion
def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
    