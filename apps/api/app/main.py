from fastapi import FastAPI

app = FastAPI(
    title="CommonGround API",
    description="Backend API for the CommonGround project",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "CommonGround API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }