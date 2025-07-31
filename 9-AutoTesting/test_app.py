import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.get_json() == {"message": "pong"}

def test_post_task_valid(client):
    payload = {
        "title": "Estudar para a entrevista",
        "done": False
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Estudar para a entrevista"
    assert data["done"] is False
    assert "id" in data