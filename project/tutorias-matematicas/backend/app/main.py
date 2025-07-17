from fastapi import FastAPI
from app.routes import auth, users, sessions, virtual_class, whiteboard
from app.utils.database import connect_to_mongo

app = FastAPI(title="Tutorías Matemáticas API")

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

# Registrar rutas
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(sessions.router, prefix="/sessions", tags=["Sessions"])
app.include_router(virtual_class.router, prefix="/virtual-class", tags=["Virtual Class"])
app.include_router(whiteboard.router, prefix="/whiteboard", tags=["Whiteboard"])
