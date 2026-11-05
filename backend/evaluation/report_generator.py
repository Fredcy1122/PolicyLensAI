from evaluation.evaluator import (
    run_evaluation
)


def generate_report():

    results = run_evaluation()

    print("\n")

    print("=" * 50)
    print("POLICYLENS EVALUATION REPORT")
    print("=" * 50)

    print(
        f"Questions Evaluated: "
        f"{results['total_questions']}"
    )

    print(
        f"Retrieval Accuracy: "
        f"{results['retrieval_accuracy']:.2f}%"
    )

    print(
        f"Abstention Accuracy: "
        f"{results['abstention_accuracy']:.2f}%"
    )

    print(
        f"Average Latency: "
        f"{results['average_latency']:.2f}s"
    )

    print("=" * 50)
