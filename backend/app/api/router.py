from fastapi import APIRouter
from app.api.routes import chat
from app.api.routes import health
from app.api.routes import documents
from app.api.routes import dashboard
from app.api.routes import summary
from app.api.routes import comparison
from app.api.routes import evaluation

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
    summary.router,
    prefix="/api",
    tags=["Summary"]
)
api_router.include_router(
    comparison.router,
    prefix="/api",
    tags=["Comparison"]
)
api_router.include_router(
    evaluation.router,
    prefix="/api",
    tags=["Evaluation"]
)

api_router.include_router(
    chat.router,
    prefix="/api",
    tags=["Chat"]
)
api_router.include_router(
    dashboard.router,
    prefix="/api",
    tags=["Dashboard"]
)