from app.rag.document_retriever import (
    get_document_content
)

from app.agents.classifier_agent import (
    ClassifierAgent
)

from app.agents.document_router import (
    select_agents
)

from app.agents.synthesis_agent import (
    SynthesisAgent
)

from app.services.llm_service import (
    generate_response
)


def analyze_document(
    document_id: str
):

    content = get_document_content(
        document_id
    )

    content = content[:5000]

    classifier = ClassifierAgent()

    document_type = classifier.classify(
        content
    )

    selected_agents = (
        select_agents(
            document_type
        )
    )

    agent_results = []

    for agent in selected_agents:

        if hasattr(
            agent,
            "review_document"
        ):
            result = (
                agent.review_document(
                    content
                )
            )

            agent_results.append(
                result
            )

    synthesis = (
        SynthesisAgent()
    )

    combined = (
        synthesis.combine(
            agent_results
        )
    )

    combined = (
        synthesis.combine(
            agent_results
        )
    )

    return {
        "analysis":
            combined["answer"],

        "document_type":
            document_type,

        "agents":
            combined[
                "participating_agents"
            ],

        "contributors":
            combined[
                "contributors"
            ]
    }