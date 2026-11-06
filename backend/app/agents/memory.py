class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(
        self,
        question: str,
        answer: str
    ):
        self.history.append(
            {
                "question": question,
                "answer": answer,
            }
        )

    def get_context(self):
        if not self.history:
            return ""

        context = []

        for item in self.history[-5:]:

            context.append(
                f"Question: {item['question']}"
            )

            context.append(
                f"Answer: {item['answer']}"
            )

        return "\n".join(context)