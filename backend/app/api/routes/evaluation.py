from fastapi import APIRouter

from evaluation.evaluator import (
    run_evaluation
)

router = APIRouter()


@router.get("/evaluation")
def evaluation():
    return run_evaluation()