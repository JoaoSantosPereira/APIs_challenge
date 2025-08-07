import pytest # type: ignore
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
        "title": "Learning Python APIs",
        "done": False
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == payload["title"]
    assert data["done"] is False
    assert "id" in data

def test_post_task_missing_title(client):
    payload = {"done": True} # missing "title" key
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert "title" in response.get_json()["error"].lower()

def test_post_task_short_title(client):
    payload = {"title": "aa", "done": True} # title too short
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert "title" in response.get_json()["error"].lower()

def test_post_task_missing_done(client):
    payload = {"title": "Study Flask"} # missing "done" key
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert "done" in response.get_json()["error"].lower()

def test_post_task_invalid_done_type(client):
    payload = {"title": "Learning Docker", "done": "yes"} # done wrong type
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert "done" in response.get_json()["error"].lower()