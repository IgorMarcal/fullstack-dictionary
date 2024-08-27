from fastapi import FastAPI
from .routes import api_router
from app.routers import auth

app = FastAPI()

app.include_router(api_router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Fullstack Challenge 🏅 - Dictionary"}
