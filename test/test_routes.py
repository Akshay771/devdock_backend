# tests/test_routes.py

from app import app


def test_index_route():
    client = app.test_client()
    response = client.get('/health-check')
    assert response.status_code == 200
    assert b"Welcome to My Flask App" in response.data
