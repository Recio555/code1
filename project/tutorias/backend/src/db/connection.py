import os
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.database import Database

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "personadb"
client = MongoClient(MONGODB_URI)
db = client["personadb"]


def get_database():
    MONGODB_URI = os.getenv("MONGODB_URI")
    client = MongoClient(MONGODB_URI)
    #db = client["personadb"]

    return client["personadb"]


#def get_database():
 #   return db

async def get_user_collection():
    return db["users"]

async def get_sessions_collection():
    return db["sessions"]

async def get_collection():
    client = MongoClient(MONGODB_URI)
    return client["users"]
