import os
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.database import Database

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "personadb"

def get_database():
    MONGODB_URI = os.getenv("MONGODB_URI")
    client = MongoClient(MONGODB_URI)
    #db = client["personadb"]

    return client["personadb"]