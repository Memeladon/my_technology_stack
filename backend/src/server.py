import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import PROJECT_NAME, PROJECT_VERSION
from src.routers import users, auth

app = FastAPI(title=PROJECT_NAME, version=PROJECT_VERSION, root_path="/api")

# ---------- Middleware ---------- #
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ Routing ------------ #
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def home():
    # health check
    return {"msg": "ok"}
