from app.services.rag_service import (
    answer_question
)


class BaseAgent:
    
    shared_context = ""


    SYSTEM_CONTEXT = ""

    def run(
        self,
        question: str
    ):
        context = ""

        if hasattr(self, "memory"):

            recent_items = (
                self.memory.recent()
            )

            memory_context = []

            for item in recent_items:

                memory_context.append(
                    f"Question: {item.question}"
                )

                memory_context.append(
                    f"Answer: {item.answer}"
                )

            context = "\n".join(
                memory_context
            )

        enhanced_question = (
            f"{self.SYSTEM_CONTEXT}\n\n"
            f"Agent Collaboration Context:\n"
            f"{self.shared_context}\n\n"
            f"Conversation Context:\n"
            f"{context}\n\n"
            f"Question: {question}"
        )

        result = answer_question(
            enhanced_question
        )

        return result