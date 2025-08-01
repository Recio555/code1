from contextlib import asynccontextmanager
from datetime import datetime
import os
import sys
from uuid import uuid4

from bson import ObjectId
from fastapi import FastAPI, status
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import uvicorn
from bson.json_util import dumps
from fastapi.responses import JSONResponse
from dal import ToDoDAL, ListSummary, ToDoList
from fastapi.middleware.cors import CORSMiddleware

COLLECTION_NAME = "nombre"
DB_NAME = "personadb"
MONGODB_URI = os.environ["MONGODB_URI"]
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, database, collection
    # Startup:
    client = AsyncIOMotorClient(MONGODB_URI)
    #database = client.get_default_database()
    database = client[DB_NAME]

    # Ensure the database is available:
    pong = await database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")

    #todo_lists = database.get_collection(COLLECTION_NAME)
    todo_lists = database[COLLECTION_NAME]
    app.todo_dal = ToDoDAL(todo_lists)

    # Yield back to FastAPI Application:
    yield

    # Shutdown:
    client.close()



app = FastAPI(lifespan=lifespan, debug=DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para desarrollo, luego restringe esto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class Persona(BaseModel):
    nombre: str
    apellido: str

# Endpoint para agregar una persona
# Ruta para guardar persona en MongoDB
@app.post("/api/lists/")
async def agregar_persona(persona: Persona):
    nueva_persona = {
        "_id": str(uuid4()),
        "nombre": persona.nombre,
        "apellido": persona.apellido
    }
    print(nueva_persona)
    todo_lists = database[COLLECTION_NAME]
    result = await todo_lists.insert_one(nueva_persona)
    return nueva_persona


@app.get("/api/lists")
async def get_all_lists() -> list[ListSummary]:
    return [i async for i in app.todo_dal.list_todo_lists()]



class NewList(BaseModel):
    name: str


class NewListResponse(BaseModel):
    id: str
    name: str


@app.post("/api/lists", status_code=status.HTTP_201_CREATED)
async def create_todo_list(new_list: NewList) -> NewListResponse:
    return NewListResponse(
        id=await app.todo_dal.create_todo_list(new_list.name),
        name=new_list.name,
    )


@app.get("/api/lists/{list_id}")
async def get_list(list_id: str) -> ToDoList:
    """Get a single to-do list"""
    return await app.todo_dal.get_todo_list(list_id)


@app.delete("/api/lists/{list_id}")
async def delete_list(list_id: str) -> bool:
    return await app.todo_dal.delete_todo_list(list_id)


class NewItem(BaseModel):
    label: str


class NewItemResponse(BaseModel):
    id: str
    label: str


@app.post(
    "/api/lists/{list_id}/items/",
    status_code=status.HTTP_201_CREATED,
)
async def create_item(list_id: str, new_item: NewItem) -> ToDoList:
    return await app.todo_dal.create_item(list_id, new_item.label)


@app.delete("/api/lists/{list_id}/items/{item_id}")
async def delete_item(list_id: str, item_id: str) -> ToDoList:
    return await app.todo_dal.delete_item(list_id, item_id)


class ToDoItemUpdate(BaseModel):
    item_id: str
    checked_state: bool


@app.patch("/api/lists/{list_id}/checked_state")
async def set_checked_state(list_id: str, update: ToDoItemUpdate) -> ToDoList:
    return await app.todo_dal.set_checked_state(
        list_id, update.item_id, update.checked_state
    )


class DummyResponse(BaseModel):
    id: str
    when: datetime


@app.get("/api/dummy")
async def get_dummy() -> DummyResponse:
    return DummyResponse(
        id=str(ObjectId()),
        when=datetime.now(),
    )


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()





def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
