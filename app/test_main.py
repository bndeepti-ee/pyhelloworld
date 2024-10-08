from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"

def test_read_from():
    response = client.get("/hello/java")
    assert response.status_code == 200
    assert response.json() == "Hello from Java World"