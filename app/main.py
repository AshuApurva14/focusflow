from fastapi import FastAPI

app = FastAPI(
    title="FocusFlow API",
    version="1.0.0",
    description="Focus Training System"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FocusFlow"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }