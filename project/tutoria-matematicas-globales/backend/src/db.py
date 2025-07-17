import motor.motor_asyncio
from .config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
database = client.tutoring_app

users_collection = database.users
tutors_collection = database.tutors
sessions_collection = database.sessions
resources_collection = database.resources