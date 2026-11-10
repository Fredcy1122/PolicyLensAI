from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings

from app.db.database import Base
from app.db.database import engine
from app.db import models
from app.db import memory_models

Base.metadata.create_all(bind=engine)

print("=== POLICYLENS STARTING ===")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://policy-lens-ai-six.vercel.app",
        "https://policy-lens-3oc25vbm2-fredrick6.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

print("=== POLICYLENS READY ===")

@app.get("/")
def root():
    return {
        "message": "PolicyLens AI API running"
    }