# scripts/test_agent.py

from app.agents.agent_executor import (
    execute_question
)

print(
    execute_question(
        "Compare two policy documents"
    )
)

print(
    execute_question(
        "Summarize this regulation"
    )
)

print(
    execute_question(
        "What is the publication date?"
    )
)
