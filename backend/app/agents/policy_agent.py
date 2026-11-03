from app.agents.intents import Intent


class PolicyAgent:

    def classify_intent(
        self,
        question: str
    ) -> Intent:

        question = question.lower()

        if "summary" in question:
            return Intent.SUMMARY

        if "summarize" in question:
            return Intent.SUMMARY

        if "compare" in question:
            return Intent.COMPARISON

        if "effective date" in question:
            return Intent.METADATA

        if "publication date" in question:
            return Intent.METADATA

        return Intent.RETRIEVAL