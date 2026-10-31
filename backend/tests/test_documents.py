from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_documents():
    response = client.get("/api/documents")

    assert response.status_code == 200
    assert len(response.json()) > 0