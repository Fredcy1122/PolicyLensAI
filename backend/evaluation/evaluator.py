import json
import time
from pathlib import Path

from evaluation.retrieval_metrics import (
    evaluate_retrieval
)

from app.services.rag_service import (
    answer_question
)

BASE_DIR = Path(__file__).resolve().parent

BENCHMARK_FILE = (
    BASE_DIR / "benchmark_questions.json"
)
def run_evaluation():

    with open(
    BENCHMARK_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        benchmark = json.load(f)

    retrieval_correct = 0
    retrieval_total = 0

    abstention_correct = 0
    abstention_total = 0

    latencies = []

    for item in benchmark:

        question = item["question"]

        expected_document = item.get(
            "expected_document"
        )

        should_abstain = item.get(
            "should_abstain",
            False
        )

        # Retrieval Evaluation
        if expected_document:

            retrieval_total += 1

            if evaluate_retrieval(
                question,
                expected_document
            ):
                retrieval_correct += 1

        # Latency Evaluation
        start = time.time()

        response = answer_question(
            question
        )

        duration = time.time() - start

        latencies.append(duration)

        # Abstention Evaluation
        abstention_total += 1

        if response.get(
            "abstained",
            False
        ) == should_abstain:

            abstention_correct += 1

    retrieval_accuracy = (
        retrieval_correct / retrieval_total * 100
        if retrieval_total > 0
        else 0
    )

    abstention_accuracy = (
        abstention_correct / abstention_total * 100
        if abstention_total > 0
        else 0
    )

    average_latency = (
        sum(latencies) / len(latencies)
        if latencies
        else 0
    )

    return {
        "retrieval_accuracy":
            retrieval_accuracy,

        "abstention_accuracy":
            abstention_accuracy,

        "average_latency":
            average_latency,

        "total_questions":
            len(benchmark)
    }