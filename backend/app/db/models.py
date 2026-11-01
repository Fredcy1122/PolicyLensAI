from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    document_id = Column(String, unique=True)

    title = Column(String)
    category = Column(String)

    issuing_authority = Column(String)

    status = Column(String)

    source_url = Column(String)