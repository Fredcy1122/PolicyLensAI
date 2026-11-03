from fastapi import APIRouter
from app.api.routes import chat
from app.api.routes import health
from app.api.routes import documents


api_router = APIRouter()

api_router.include_router(
    health.router,
    tags=["Health"]
)

api_router.include_router(
    documents.router,
    prefix="/api",
    tags=["Documents"]
)

api_router.include_router(
    chat.router,
    prefix="/api",
    tags=["Chat"]
)