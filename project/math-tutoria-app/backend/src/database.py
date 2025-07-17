import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# MongoDB connection string
# In production, use environment variables for sensitive information
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://your-username:your-password@your-cluster.mongodb.net/your-database?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "Personadb")

# Asynchronous client for FastAPI
async def get_async_db():
    client = AsyncIOMotorClient(MONGODB_URI)
    try:
        yield client[DB_NAME]
    finally:
        client.close()

# Synchronous client for some operations
def get_sync_db():
    client = MongoClient(MONGODB_URI)
    try:
        return client[DB_NAME]
    finally:
        client.close()

# Get synchronous database instance
db = get_sync_db()