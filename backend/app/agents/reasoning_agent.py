from app.services.rag_service import (
    answer_question
)


class ReasoningAgent:

    def execute(
        self,
        question: str,
        analyses: list
    ):
        context = []

        for item in analyses:

            context.append(
                f"""
Agent:
{item['agent']}

Focus:
{item['focus']}
"""
            )

        enhanced_question = f"""
Question:
{question}

Agent Guidance:

{' '.join(context)}

Answer the question carefully
using the above agent
guidance.
"""

        return answer_question(
            enhanced_question
        )