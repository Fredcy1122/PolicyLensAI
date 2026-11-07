from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.db.memory_models import (
    ConversationMemory
)


class AgentMetrics:

    def get_metrics(self):

        db: Session = SessionLocal()

        try:

            records = (
                db.query(
                    ConversationMemory
                ).all()
            )

            total_questions = len(records)

            finance = 0
            customs = 0
            legal = 0
            trade = 0

            for item in records:

                agents = (
                    item.agents or ""
                ).lower()

                if "finance" in agents:
                    finance += 1

                if "customs" in agents:
                    customs += 1

                if "legal" in agents:
                    legal += 1

                if "trade" in agents:
                    trade += 1

            return {
                "total_questions":
                    total_questions,
                "finance":
                    finance,
                "customs":
                    customs,
                "legal":
                    legal,
                "trade":
                    trade,
            }

        finally:

            db.close()