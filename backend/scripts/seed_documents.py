from app.db.database import SessionLocal
from app.db.models import Document

db = SessionLocal()

documents = [
    {
        "document_id": "DOC001",
        "title": "Nigeria Customs Act",
        "category": "Legislation",
        "issuing_authority": "Nigeria Customs Service",
        "status": "Active",
        "source_url": "https://customs.gov.ng"
    },
    {
        "document_id": "DOC002",
        "title": "Import Procedures Guide",
        "category": "Guidance",
        "issuing_authority": "Nigeria Customs Service",
        "status": "Active",
        "source_url": "https://customs.gov.ng"
    }
]

for item in documents:

    exists = (
        db.query(Document)
        .filter(
            Document.document_id == item["document_id"]
        )
        .first()
    )

    if not exists:
        db.add(Document(**item))

db.commit()

print("Documents seeded")