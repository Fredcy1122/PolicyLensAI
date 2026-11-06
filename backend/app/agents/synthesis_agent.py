class SynthesisAgent:

    def combine(
        self,
        results: list
    ):
        answers = []

        agents = []

        for result in results:

            if (
                isinstance(result, dict)
                and "answer" in result
            ):
                answers.append(
                    result["answer"]
                )

            if (
                isinstance(result, dict)
                and "agent" in result
            ):
                agents.append(
                    result["agent"]
                )
        final_answer = "\n\n".join(
            answers
        )
        return {
            "answer": final_answer,


            "contributors":
                len(results),

            "participating_agents":
                agents,
            "collaboration": True
        }