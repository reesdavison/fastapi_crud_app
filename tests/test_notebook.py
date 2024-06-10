from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_notebook():
    response = client.post("/notebooks/", json={"name": "Test Notebook"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Notebook"
    idx = response.json()["id"]
    assert idx is not None

    response = client.get(f"/notebooks/{idx}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Notebook"
    assert response.json()["id"] == idx


def test_get_notebook_bad_input():
    idx = "foo"
    response = client.get(f"/notebooks/{idx}")
    assert response.status_code == 422


def test_get_notebook_doesnt_exist():
    # hacky test for now, would clear the DB before doing this
    idx = "99999999999"
    response = client.get(f"/notebooks/{idx}")
    assert response.status_code == 404
