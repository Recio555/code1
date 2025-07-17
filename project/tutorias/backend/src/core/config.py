from pydantic_settings import BaseSettings
import secrets
from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

class Settings(BaseSettings):
    MONGODB_URI: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

# Acceder a la configuración
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = settings.ALGORITHM

# Ahora puedes usar: settings.MONGODB_URL, settings.SECRET_KEY, etc.
