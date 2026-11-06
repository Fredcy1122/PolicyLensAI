from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.db.memory_models import (
    ConversationMemory
)


class PersistentMemory:

    def add(
        self,
        question: str,
        answer: str,
        agents: str = ""
    ):
        db: Session = SessionLocal()

        try:

            item = ConversationMemory(
                question=question,
                answer=answer,
                agents=agents
            )

            db.add(item)

            db.commit()

        finally:

            db.close()

    def recent(
        self,
        limit: int = 5
    ):
        db: Session = SessionLocal()

        try:

            items = (
                db.query(
                    ConversationMemory
                )
                .order_by(
                    ConversationMemory.id.desc()
                )
                .limit(limit)
                .all()
            )

            return list(
                reversed(items)
            )

        finally:

            db.close()