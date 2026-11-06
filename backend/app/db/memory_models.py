from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from app.db.database import Base


class ConversationMemory(Base):
    __tablename__ = "conversation_memory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(
        Text,
        nullable=False
    )

    answer = Column(
        Text,
        nullable=False
    )

    agents = Column(
        String,
        nullable=True
    )