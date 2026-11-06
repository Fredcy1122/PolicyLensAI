from app.core.logger import logger

from app.agents.router_agent import (
    RouterAgent
)
from app.agents.persistent_memory import (
    PersistentMemory
)
from app.agents.collaboration import (
    AgentCollaboration
)
from app.agents.synthesis_agent import (
    SynthesisAgent
)

from app.agents.intents import (
    Intent
)

from app.agents.legal_agent import (
    LegalAgent
)

from app.agents.customs_agent import (
    CustomsAgent
)

from app.agents.trade_agent import (
    TradeAgent
)

from app.agents.finance_agent import (
    FinanceAgent
)

from app.services.rag_service import (
    answer_question
)


memory = PersistentMemory()

def execute_question(
    question: str
):
    router = RouterAgent()

    routing = router.score_agents(
        question
    )

    rankings = routing["rankings"]

    matches = routing["matches"]

    logger.info(
        f"Rankings: {rankings}"
    )

    selected = [
        item
        for item in rankings
        if item[1] > 0
    ][:1]

    results = []

    collaboration = (
        AgentCollaboration()
    )

    shared_context = ""

    for intent, score in selected:

        if intent == Intent.LEGAL:

            agent = LegalAgent()

        elif intent == Intent.CUSTOMS:

            agent = CustomsAgent()

        elif intent == Intent.TRADE:

            agent = TradeAgent()

        elif intent == Intent.FINANCE:

            agent = FinanceAgent()

        else:
            continue

        agent.memory = memory

        agent.shared_context = (
            shared_context
        )

        result = agent.run(
            question
        )

        results.append(
            result
        )

        shared_context = (
            collaboration
            .build_shared_context(
            results
            )
        )
    if not results:

        result = answer_question(
            question
        )

        result["agent"] = (
            "Policy Agent"
        )

        return result

    synthesis = (
        SynthesisAgent()
    )

    combined = (
        synthesis.combine(
            results
        )
    )
    memory.add(
        question,
        combined["answer"],
        ",".join(
            combined.get(
                "agents",
                []
            )
        )
    )

    
    combined["agents"] = [
        str(intent.value)
        for intent, score
        in selected
    ]

    combined["routing"] = {
        "matched_keywords": matches,
        "selected_agents":
            combined["agents"]
    }

    combined["confidence"] = (
        max(
            [
                score
                for intent, score
                in selected
            ],
            default=0
        )
        * 10
    )

    return combined