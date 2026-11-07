from fastapi import APIRouter

from app.agents.agent_metrics import (
    AgentMetrics
)

router = APIRouter()


@router.get("/agents/metrics")
def get_agent_metrics():

    metrics = AgentMetrics()

    return metrics.get_metrics()