import json

from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "ok"

def test_balance():
    client = app.test_client()
    response = client.get("/balance")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["balance"] == 1000.0

def test_deposit():
    client = app.test_client()
    response = client.post("/deposit", json={"amount": 200})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["balance"] == 1200.0