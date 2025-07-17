from fastapi import FastAPI, status, HTTPException
from contextlib import asynccontextmanager
from pymongo.mongo_client import MongoClient
from datetime import datetime
import os
import sys

from bson import ObjectId


from pydantic import BaseModel
import uvicorn
from bson import ObjectId
from bson.json_util import dumps



#COLLECTION_NAME = "todo_lists"
#MONGODB_URI = os.environ["MONGODB_URI"]
MONGODB_URI = os.environ.get("MONGODB_URI")
DEBUG = os.environ.get("DEBUG", "").strip().lower() in {"1", "true", "on", "yes"}



# Initialize FastAPI app
uri = "mongodb+srv://hnorecio:Filipenses48@cluster0.xiwaxdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, database, collection
    
    client = MongoClient(uri)
    # Ensure the database is available:
    database = client["sample_mflix"]
    pong = database.command("ping")
    if int(pong["ok"]) != 1:
        raise Exception("Cluster connection is not okay!")

    todo_lists = database.get_collection('comments')
    
    #app.todo_dal = ToDoDAL(todo_lists)

    # Yield back to FastAPI Application:
    yield

    # Shutdown:
    client.close()

    

app = FastAPI(lifespan=lifespan, debug=DEBUG)

def serializar_documento(documento):
    documento["_id"] = str(documento["_id"])
    return documento



@app.get("/")
async def get_all_lists():
    coleccion =  database["comments"]
    documentos = coleccion.find()
    json_string = dumps(documentos)
    return json_string 
  
















def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001, reload=DEBUG)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
