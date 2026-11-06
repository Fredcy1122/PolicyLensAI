class AgentCollaboration:

    def build_shared_context(
        self,
        results: list
    ):
        observations = []

        for result in results:

            if (
                isinstance(result, dict)
                and "answer" in result
            ):
                observations.append(
                    result["answer"]
                )

        return "\n\n".join(
            observations
        )