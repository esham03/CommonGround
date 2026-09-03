from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.routers.auth import router as auth_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CommonGround API",
    version="0.1.0",
)


# Authentication routes
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "CommonGround API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }